#!/usr/bin/env bash
# Apply rule pack configs to a target project.
# Usage: ./apply.sh <target_project_path>
# Example: ./apply.sh examples/python-fastapi-app

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
RULE_PACK_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
RULES_PYTHON="$RULE_PACK_ROOT/rules/python"
RULES_CURSOR="$RULE_PACK_ROOT/rules/cursor"

if [ -z "$1" ]; then
  echo "Usage: $0 <target_project_path>"
  echo "Example: $0 examples/python-fastapi-app"
  exit 1
fi

if [ ! -d "$1" ]; then
  echo "Error: Target directory does not exist: $1"
  exit 1
fi

TARGET="$(cd "$1" && pwd)"

echo "Applying rule pack to: $TARGET"

# Copy configs
cp "$RULES_PYTHON/ruff.toml" "$TARGET/"
cp "$RULES_PYTHON/mypy.ini" "$TARGET/"
cp "$RULES_PYTHON/pytest.ini" "$TARGET/"
cp "$RULES_PYTHON/.pre-commit-config.yaml" "$TARGET/"
cp "$RULES_PYTHON/.importlinter" "$TARGET/"

# Copy editorconfig if not exists
if [ ! -f "$TARGET/.editorconfig" ]; then
  cp "$RULE_PACK_ROOT/.editorconfig" "$TARGET/"
fi

# Copy Cursor rules
mkdir -p "$TARGET/.cursor/rules"
cp "$RULES_CURSOR"/*.mdc "$TARGET/.cursor/rules/"
echo "Cursor rules applied to .cursor/rules/"

# Copy RULES.md if not exists
if [ ! -f "$TARGET/RULES.md" ]; then
  cp "$RULE_PACK_ROOT/RULES.md" "$TARGET/"
fi

echo "Configs applied. Next steps:"
echo "  1. cd $TARGET"
echo "  2. uv sync  # or poetry install"
echo "  3. pre-commit install"
echo "  4. pre-commit run --all-files"
