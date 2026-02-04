"""User service."""

from app.domain.user import UserCreate, UserResponse
from app.errors import ValidationError
from app.repositories.user_repository import UserRepository


class UserService:
    """User business logic."""

    def __init__(self, repository: UserRepository) -> None:
        self._repo = repository

    def create_user(self, data: UserCreate) -> UserResponse:
        """Create user, raise ValidationError if duplicate email."""
        existing = self._repo.get_by_email(data.email)
        if existing:
            raise ValidationError(
                "Email already registered",
                details={"email": data.email},
            )
        return self._repo.create(data)

    def get_user(self, user_id: str) -> UserResponse:
        """Get user by ID."""
        return self._repo.get_by_id(user_id)

    def list_users(self) -> list[UserResponse]:
        """List all users."""
        return self._repo.list_all()
