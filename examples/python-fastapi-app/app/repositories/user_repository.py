"""In-memory user repository."""

import logging
import uuid

from app.domain.user import UserCreate, UserResponse
from app.errors import NotFoundError, RepositoryError

logger = logging.getLogger(__name__)


class UserRepository:
    """In-memory user storage."""

    def __init__(self) -> None:
        self._store: dict[str, UserResponse] = {}

    def create(self, data: UserCreate) -> UserResponse:
        """Create a new user."""
        try:
            user_id = str(uuid.uuid4())
            user = UserResponse(id=user_id, name=data.name, email=data.email)
            self._store[user_id] = user
            logger.info("User created", extra={"user_id": user_id})
            return user
        except Exception as e:
            logger.exception("Repository create failed")
            raise RepositoryError(str(e)) from e

    def get_by_id(self, user_id: str) -> UserResponse:
        """Get user by ID."""
        if user_id not in self._store:
            raise NotFoundError(f"User {user_id} not found")
        return self._store[user_id]

    def get_by_email(self, email: str) -> UserResponse | None:
        """Get user by email."""
        for user in self._store.values():
            if user.email == email:
                return user
        return None

    def list_all(self) -> list[UserResponse]:
        """List all users."""
        return list(self._store.values())
