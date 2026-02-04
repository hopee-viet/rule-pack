# Cursor System Prompt — Rule Pack

## Bắt buộc trước khi đề xuất thay đổi lớn

1. **Chạy toolchain**:
   - `ruff format --check` và `ruff check`
   - `mypy app tests`
   - `pytest`
   - `lint-imports` (import-linter)

2. Nếu có lỗi, **ưu tiên fix theo auto-fix của ruff** trước khi sửa thủ công.

## Boundary imports (bắt buộc)

- `app.api` **không** import `app.repositories` trực tiếp — chỉ import `app.services`
- `app.services` **không** import `app.api`
- `app.repositories` **không** import `app.api` hoặc `app.services`

Flow: `api` → `service` → `repository` → `domain` / `errors`

## Khi viết code mới

- Tuân thủ layering: router gọi service, service gọi repository
- Dùng `AppError` và subclasses cho error handling
- Log tập trung ở repository layer, không log trùng nhiều layer
