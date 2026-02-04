"""User service tests."""

import pytest

from app.domain.user import UserCreate
from app.errors import ValidationError
from app.repositories.user_repository import UserRepository
from app.services.user_service import UserService


def test_create_user_success() -> None:
    """Service: create user success."""
    repo = UserRepository()
    service = UserService(repo)
    data = UserCreate(name="Alice", email="alice@example.com")
    user = service.create_user(data)
    assert user.name == "Alice"
    assert user.email == "alice@example.com"
    assert user.id


def test_create_user_duplicate_email_raises_validation_error() -> None:
    """Service: duplicate email raises ValidationError."""
    repo = UserRepository()
    service = UserService(repo)
    data = UserCreate(name="Alice", email="alice@example.com")
    service.create_user(data)
    with pytest.raises(ValidationError) as exc_info:
        service.create_user(data)
    assert "already registered" in exc_info.value.message
