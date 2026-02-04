# Cursor System Prompt — Rule Pack

## Bắt buộc sau khi hoàn thành thay đổi code

1. **Chạy full check** trước khi kết thúc task:
   - `ruff format .` và `ruff check .`
   - `mypy app tests`
   - `pytest`
   - `lint-imports`

2. Nếu có lỗi, **fix ngay** (ưu tiên auto-fix của ruff).

## Boundary imports (bắt buộc)

- `app.api` **không** import `app.repositories` trực tiếp — chỉ import `app.services`
- `app.services` **không** import `app.api`
- `app.repositories` **không** import `app.api` hoặc `app.services`

Flow: `api` → `service` → `repository` → `domain` / `errors`

## Khi viết code mới

- Tuân thủ layering: router gọi service, service gọi repository
- Dùng `AppError` và subclasses cho error handling
- Log tập trung ở repository layer, không log trùng nhiều layer
