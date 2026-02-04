"""Dependency injection (composition root)."""

from app.repositories.user_repository import UserRepository
from app.services.user_service import UserService


def get_user_service() -> UserService:
    """Create UserService with repository."""
    repo = UserRepository()
    return UserService(repo)
