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
2. `uv sync` (hoặc `pip install -e ".[dev]"`)
3. `pre-commit install`
4. Mở project trong Cursor → AI tự load rules

## Enforce 3 lớp

| Lớp | Mô tả |
|-----|-------|
| **1. Human-readable** | RULES.md, prompts/cursor_system.md |
| **2. Machine-enforced** | ruff, mypy, pytest, pre-commit, import-linter |
| **3. AI context** | Cursor rules (.cursor/rules/*.mdc) |

## Troubleshooting

### import-linter fail

Kiểm tra boundary: `api` không import `repositories` trực tiếp. Chỉ `api` → `services` → `repositories`.

### pre-commit fail

```bash
pre-commit run --all-files
```

Nếu ruff auto-fix được, chạy lại sẽ pass.
