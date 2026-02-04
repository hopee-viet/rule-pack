# Python FastAPI Example — Rule Pack Demo

Sample app với layered architecture: api → services → repositories.

## Chạy

```bash
# Cài dependencies (dùng uv)
uv sync

# Chạy server
uv run uvicorn app.main:app --reload

# Chạy tests
uv run pytest

# Lint + format + typecheck + import-linter
uv run ruff format .
uv run ruff check .
uv run mypy app tests
uv run lint-imports

# Pre-commit (sau khi cài hook)
pre-commit install
pre-commit run --all-files
```

## API

- `POST /users` — Tạo user (body: `{ "name": "...", "email": "..." }`)
- `GET /users/{id}` — Lấy user theo ID

## Demo vi phạm boundary

Để test import-linter fail, thêm vào `app/api/users.py`:

```python
from app.repositories.user_repository import UserRepository  # ❌ vi phạm
```

Chạy `lint-imports` → sẽ fail với "API cannot import repositories directly".
