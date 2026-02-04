"""User repository tests."""

import pytest

from app.domain.user import UserCreate
from app.errors import NotFoundError
from app.repositories.user_repository import UserRepository


def test_repository_create_and_get() -> None:
    """Repository: create and get user."""
    repo = UserRepository()
    data = UserCreate(name="Bob", email="bob@example.com")
    user = repo.create(data)
    assert user.id
    assert user.name == "Bob"
    got = repo.get_by_id(user.id)
    assert got.id == user.id
    assert got.email == user.email


def test_repository_get_not_found() -> None:
    """Repository: get by id raises NotFoundError when not found."""
    repo = UserRepository()
    with pytest.raises(NotFoundError):
        repo.get_by_id("nonexistent-id")
