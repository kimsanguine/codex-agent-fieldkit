#!/usr/bin/env bash
set -euo pipefail

ROOT="${1:-$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)}"

while IFS= read -r forbidden; do
  printf 'forbidden public path: %s\n' "$forbidden" >&2
  exit 1
done < <(find "$ROOT" \
  \( -path '*/.git/*' -o -path '*/.worktrees/*' -o -path '*/worktrees/*' -o -path '*/.venv/*' \) -prune -o \
  \( -type d \( -name docs -o -name .archive \) \) -print)

echo "public surface: pass"
