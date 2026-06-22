#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

if find "$ROOT" \
  \( -path '*/.git/*' -o -path '*/.venv/*' \) -prune -o \
  \( -name '__pycache__' -o -name '*.pyc' -o -name '.DS_Store' -o -name '.env' \) -print | grep .; then
  echo "Generated cache, local metadata, or env artifact found." >&2
  exit 1
fi

echo "generated artifact scan: pass"
