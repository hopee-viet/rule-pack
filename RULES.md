# RULES — Coding & Architecture Conventions

## 1. Layering (bắt buộc)

```
api/ (routers) → services/ → repositories/
                ↓
            domain/ (models, schemas)
            errors/
```

| Layer | Trách nhiệm | Import được |
|-------|-------------|-------------|
| **api/** | Nhận input, validate, gọi service, trả response | services, domain, errors |
| **services/** | Business logic | repositories, domain, errors |
| **repositories/** | Data access | domain, errors |
| **domain/** | Entities, Pydantic schemas | errors |
| **errors/** | AppError và subclasses | — |

### Ví dụ đúng

```python
# api/users.py
from app.services.user_service import UserService  # ✅

# services/user_service.py
from app.repositories.user_repository import UserRepository  # ✅
```

### Ví dụ sai (import-linter sẽ fail)

```python
# api/users.py
from app.repositories.user_repository import UserRepository  # ❌ api không import repo
```

## 2. Error Handling

### AppError base

```python
# app/errors/base.py
class AppError(Exception):
    def __init__(self, code: str, message: str, details: dict | None = None):
        self.code = code
        self.message = message
        self.details = details or {}
```

### Subclasses

- `ValidationError`: 400, input không hợp lệ
- `NotFoundError`: 404, resource không tồn tại
- `RepositoryError`: 500, lỗi data access

### Exception handler

Map `AppError` → HTTP response trong `app/main.py` (hoặc `app/api/handlers.py`). Không để exception tràn ra ngoài.

## 3. Logging

- **Tập trung**: Log ở repositories (hoặc module logger riêng)
- **Không log trùng**: Một lỗi chỉ log 1 lần, ở layer thấp nhất (repository)
- **Structured**: Dùng `logger.info("msg", extra={...})` khi cần context

## 4. Naming

- **Files**: `snake_case` (user_service.py)
- **Classes**: `PascalCase`
- **Functions/vars**: `snake_case`
- **Constants**: `UPPER_SNAKE_CASE`

## 5. Validation

- Dùng Pydantic cho request/response
- Validate: email format, name not empty
- ValidationError khi invalid

## 6. Tests

- pytest + FastAPI TestClient
- Test từng layer: service, repository, API
- Mock repository khi test service nếu cần
