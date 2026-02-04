#!/usr/bin/env bash
# Check environment: Python, uv/poetry, pre-commit, tools.
# Usage: ./doctor.sh [project_path]

set -e

PROJECT="${1:-.}"
cd "$PROJECT"

echo "=== Rule Pack Doctor ==="
echo "Project: $(pwd)"
echo ""

# Python
echo "Python:"
if command -v python3 &>/dev/null; then
  python3 --version
else
  echo "  ❌ python3 not found"
fi
echo ""

# Package manager
echo "Package manager:"
if command -v uv &>/dev/null; then
  echo "  uv: $(uv --version)"
elif command -v poetry &>/dev/null; then
  echo "  poetry: $(poetry --version)"
else
  echo "  ⚠️  uv or poetry not found (recommend: uv)"
fi
echo ""

# Pre-commit
echo "Pre-commit:"
if command -v pre-commit &>/dev/null; then
  pre-commit --version
  if [ -f .git/hooks/pre-commit ]; then
    echo "  ✅ pre-commit hook installed"
  else
    echo "  ⚠️  Run: pre-commit install"
  fi
else
  echo "  ❌ pre-commit not found"
fi
echo ""

# Tools (when in venv)
echo "Tools:"
for cmd in ruff mypy pytest lint-imports; do
  if command -v "$cmd" &>/dev/null; then
    echo "  ✅ $cmd"
  else
    echo "  ❌ $cmd (install deps: uv sync)"
  fi
done
echo ""
echo "Done."
