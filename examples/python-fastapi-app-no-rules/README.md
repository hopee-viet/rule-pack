# Python FastAPI Example — No Rules (Test)

Bản **không có Cursor rules** — dùng để so sánh với `python-fastapi-app` (có rules).

## Khác biệt

| | python-fastapi-app | python-fastapi-app-no-rules |
|---|-------------------|-----------------------------|
| `.cursor/rules/` | ✅ Có | ❌ Không |
| RULES.md | ✅ Có | ❌ Không |
| Machine config (ruff, mypy...) | ✅ Có | ✅ Có |

## Cách test

1. Mở `python-fastapi-app-no-rules` trong Cursor
2. Hỏi AI: "Thêm `from app.repositories.user_repository import UserRepository` vào `app/api/users.py`"
3. So sánh: AI có thể chấp nhận (vì không có rules)
4. Mở `python-fastapi-app` (có rules) → hỏi cùng câu → AI sẽ từ chối

## Chạy

```bash
uv sync
uv run pytest
uv run uvicorn app.main:app --reload
```
