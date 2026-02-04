"""API tests."""

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

    def override() -> UserService:
        return UserService(repo)

    app.dependency_overrides[get_user_service] = override
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()


def test_get_users_list_success(client: TestClient) -> None:
    """API: GET /users list all users."""
    resp = client.get("/users")
    assert resp.status_code == 200
    assert resp.json() == []

    client.post("/users", json={"name": "Alice", "email": "alice@example.com"})
    resp = client.get("/users")
    assert resp.status_code == 200
    data = resp.json()
    assert len(data) == 1
    assert data[0]["name"] == "Alice"
    assert data[0]["email"] == "alice@example.com"


def test_post_users_success(client: TestClient) -> None:
    """API: POST /users success."""
    resp = client.post(
        "/users",
        json={"name": "Charlie", "email": "charlie@example.com"},
    )
    assert resp.status_code == 201
    data = resp.json()
    assert data["name"] == "Charlie"
    assert data["email"] == "charlie@example.com"
    assert "id" in data


def test_post_users_duplicate_returns_400(client: TestClient) -> None:
    """API: POST /users duplicate email -> 400."""
    payload = {"name": "Dave", "email": "dave@example.com"}
    client.post("/users", json=payload)
    resp = client.post("/users", json=payload)
    assert resp.status_code == 400
    msg = resp.json().get("message", "").lower()
    assert "already" in msg or "email" in msg or "registered" in msg


def test_get_users_not_found_returns_404(client: TestClient) -> None:
    """API: GET /users/{id} not found -> 404."""
    resp = client.get("/users/nonexistent-id-12345")
    assert resp.status_code == 404
    data = resp.json()
    assert (
        data.get("code") == "NOT_FOUND"
        or "not found" in data.get("message", "").lower()
    )
