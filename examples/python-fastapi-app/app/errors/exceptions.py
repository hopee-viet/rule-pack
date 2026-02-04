"""Concrete error types."""

from app.errors.base import AppError


class ValidationError(AppError):
    """Input validation failed (400)."""

    def __init__(self, message: str, details: dict[str, object] | None = None) -> None:
        super().__init__(code="VALIDATION_ERROR", message=message, details=details)


class NotFoundError(AppError):
    """Resource not found (404)."""

    def __init__(self, message: str, details: dict[str, object] | None = None) -> None:
        super().__init__(code="NOT_FOUND", message=message, details=details)


class RepositoryError(AppError):
    """Data access error (500)."""

    def __init__(self, message: str, details: dict[str, object] | None = None) -> None:
        super().__init__(code="REPOSITORY_ERROR", message=message, details=details)
