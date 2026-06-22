#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

PATTERN='([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}|01[016789]-?[0-9]{3,4}-?[0-9]{4}|\b[0-9]{3}-[0-9]{2}-[0-9]{4}\b)'

if grep -RInE \
  --exclude-dir=.git \
  --exclude='check_no_pii.sh' \
  --exclude='check_no_private_terms.sh' \
  --exclude='test_no_private_terms.py' \
  "$PATTERN" "$ROOT"; then
  echo "PII-like value found. Remove it or replace with synthetic placeholder text." >&2
  exit 1
fi

echo "pii scan: pass"
