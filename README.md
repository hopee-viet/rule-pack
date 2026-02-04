# Rule Pack — Developer Platform MVP

Chuẩn hóa và enforce code conventions + architecture rules cho team khi dùng AI coding tools (Cursor/Claude).

## Mục tiêu

- **Giảm code "loạn"**: Quy tắc rõ ràng, AI và dev tuân thủ
- **Machine-enforced**: Lint/format/typecheck/test/CI chặn vi phạm
- **AI context**: Prompts và rules để Cursor/Claude tuân thủ boundary + conventions

## Cài đặt (one command)

```bash
# Clone repo
git clone <repo-url> dev-rule-pack && cd dev-rule-pack

# Áp dụng rule pack vào project (ví dụ: examples/python-fastapi-app)
./tooling/scripts/apply.sh examples/python-fastapi-app

# Hoặc áp dụng vào project bất kỳ
./tooling/scripts/apply.sh /path/to/your/python-project
```

## Kiểm tra môi trường

```bash
./tooling/scripts/doctor.sh
```

Kiểm tra: Python version, uv/poetry, pre-commit, các tool cần thiết.

## Cấu trúc

```
dev-rule-pack/
├── README.md
├── RULES.md                 # Quy tắc coding + kiến trúc
├── prompts/
│   └── cursor_system.md     # System prompt cho Cursor (global rules)
├── .cursor/rules/           # symlink → rules/cursor (1 nguồn)
├── rules/python/
│   ├── ruff.toml
│   ├── mypy.ini
│   ├── pytest.ini
│   ├── .pre-commit-config.yaml
│   └── .importlinter
├── rules/cursor/            # Nguồn rules (apply.sh copy, .cursor/rules symlink)
│   ├── core.mdc
│   └── python.mdc
├── tooling/
│   └── scripts/
│       ├── apply.sh
│       └── doctor.sh
├── examples/
│   ├── python-fastapi-app/      # Có Cursor rules
│   └── python-fastapi-app-no-rules/  # Không rules (để test so sánh)
└── .editorconfig
```

## Cấu hình Cursor để AI tuân thủ rules

Sau khi chạy `apply.sh`, project sẽ có `.cursor/rules/` với:
- **core.mdc** — `alwaysApply: true`, AI luôn thấy conventions cốt lõi
- **python.mdc** — áp dụng khi mở file `**/*.py`

Cursor tự động load rules khi bạn mở project. Không cần cấu hình thêm.

**Nếu muốn rules cho mọi project:** Cursor → Settings → Rules for AI → thêm nội dung từ `prompts/cursor_system.md`.

## Enforce 3 lớp

| Lớp | Mô tả |
|-----|-------|
| **1. Human-readable** | RULES.md, prompts/cursor_system.md |
| **2. Machine-enforced** | ruff, mypy, pytest, pre-commit, import-linter, CI |
| **3. AI context** | Cursor rules (.cursor/rules/*.mdc), cursor_system.md |

## Chạy example

```bash
cd examples/python-fastapi-app
uv sync
uv run pytest
uv run uvicorn app.main:app --reload
```

## Troubleshooting

### import-linter fail

Nếu CI fail với `ImportLinterError`:
- Kiểm tra boundary: `api` không import `repositories` trực tiếp
- Chỉ `api` → `services` → `repositories` (một chiều)

### pre-commit fail

```bash
pre-commit run --all-files
```

Nếu ruff auto-fix được, chạy lại sẽ pass.

### mypy strict

Đảm bảo type hints đầy đủ. Chạy `mypy app tests` để xem lỗi cụ thể.
