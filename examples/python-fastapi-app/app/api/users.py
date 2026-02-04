"""User API routes."""

from fastapi import APIRouter, Depends, status

from app.deps import get_user_service
from app.domain.user import UserCreate, UserResponse
from app.services.user_service import UserService

router = APIRouter()


@router.get("", response_model=list[UserResponse])
def list_users(
    service: UserService = Depends(get_user_service),
) -> list[UserResponse]:
    """List all users."""
    return service.list_users()


@router.post("", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(
    data: UserCreate,
    service: UserService = Depends(get_user_service),
) -> UserResponse:
    """Create a new user."""
    return service.create_user(data)


@router.get("/{user_id}", response_model=UserResponse)
def get_user(
    user_id: str,
    service: UserService = Depends(get_user_service),
) -> UserResponse:
    """Get user by ID."""
    return service.get_user(user_id)
