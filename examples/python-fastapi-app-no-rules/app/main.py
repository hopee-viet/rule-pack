"""FastAPI application entry point."""

from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from app.api.users import router as users_router
from app.errors import AppError, NotFoundError, RepositoryError, ValidationError

app = FastAPI(title="Rule Pack Demo API")
app.include_router(users_router, prefix="/users", tags=["users"])


@app.exception_handler(AppError)
def app_error_handler(request: Request, exc: AppError) -> JSONResponse:
    """Map AppError to HTTP response."""
    if isinstance(exc, ValidationError):
        status_code = status.HTTP_400_BAD_REQUEST
    elif isinstance(exc, NotFoundError):
        status_code = status.HTTP_404_NOT_FOUND
    elif isinstance(exc, RepositoryError):
        status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    else:
        status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

    return JSONResponse(
        status_code=status_code,
        content={
            "code": exc.code,
            "message": exc.message,
            "details": exc.details,
        },
    )


@app.get("/health")
def health() -> dict[str, str]:
    """Health check."""
    return {"status": "ok"}
