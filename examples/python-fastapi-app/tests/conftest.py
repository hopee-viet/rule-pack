"""Pytest fixtures."""

from collections.abc import Generator

import pytest
from fastapi.testclient import TestClient

from app.deps import get_user_service
from app.main import app
from app.repositories.user_repository import UserRepository
from app.services.user_service import UserService


@pytest.fixture
def client() -> Generator[TestClient, None, None]:
    """FastAPI test client with shared in-memory repository."""
    repo = UserRepository()

    def override_get_user_service() -> UserService:
        return UserService(repo)

    app.dependency_overrides[get_user_service] = override_get_user_service
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()
