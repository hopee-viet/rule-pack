# Rule Pack — Developer Platform MVP

Chuẩn hóa và enforce code conventions + architecture rules cho team khi dùng AI coding tools (Cursor/Claude).

## Mục tiêu

- **Giảm code "loạn"**: Quy tắc rõ ràng, AI và dev tuân thủ
- **Machine-enforced**: Lint/format/typecheck/pre-commit chặn vi phạm
- **AI context**: Prompts và rules để Cursor tuân thủ boundary + conventions

## Cài đặt

```bash
# Clone repo
git clone <repo-url> rule-pack && cd rule-pack

# Áp dụng vào project của bạn
./tooling/scripts/apply.sh /path/to/your/python-project
```

## Kiểm tra môi trường

```bash
./tooling/scripts/doctor.sh /path/to/your-project
```

## Cấu trúc

```
rule-pack/
├── README.md
├── RULES.md
├── prompts/cursor_system.md
├── .cursor/rules/           # symlink → rules/cursor
├── rules/python/
│   ├── ruff.toml
│   ├── mypy.ini
│   ├── pytest.ini
│   ├── .pre-commit-config.yaml
│   └── .importlinter
├── rules/cursor/
│   ├── core.mdc
│   └── python.mdc
├── tooling/scripts/
│   ├── apply.sh
│   └── doctor.sh
└── .editorconfig
```

## Sau khi apply

1. `cd /path/to/your-project`
2. `uv sync` — apply.sh đã thêm ruff, mypy, pytest, pre-commit, import-linter vào dev deps
3. `pre-commit install`
4. Mở project trong Cursor → AI tự load rules

**Lưu ý:** AI chạy check bằng `uv run ruff`, `uv run pytest`... (từ project venv). Cần `uv sync` trước.

### Cursor đang mở project — chưa nhận rules ngay?

Cursor chỉ load rules khi mở project. Nếu apply rules vào project **đang mở**, cần **reload**:

- **Cmd+Shift+P** (Mac) hoặc **Ctrl+Shift+P** (Win/Linux)
- Gõ: `Developer: Reload Window`
- Enter

Hoặc đóng project rồi mở lại.

## Enforce 3 lớp

| Lớp | Mô tả |
|-----|-------|
| **1. Human-readable** | RULES.md, prompts/cursor_system.md |
| **2. Machine-enforced** | ruff, mypy, pytest, pre-commit, import-linter |
| **3. AI context** | Cursor rules (.cursor/rules/*.mdc) |

## Troubleshooting

### Cursor chưa nhận rules sau khi apply

Project đang mở + vừa apply → Cursor chưa load rules. **Reload Window** (Cmd+Shift+P → Developer: Reload Window) hoặc đóng/mở lại project.

### import-linter fail

Kiểm tra boundary: `api` không import `repositories` trực tiếp. Chỉ `api` → `services` → `repositories`.

### ruff/mypy: command not found

Chạy `uv sync` trong project. AI dùng `uv run ruff` để chạy từ venv — cần dev deps đã cài.

### pre-commit fail

```bash
pre-commit run --all-files
```

Nếu ruff auto-fix được, chạy lại sẽ pass.
