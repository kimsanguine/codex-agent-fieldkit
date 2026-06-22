#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

PATTERN='(sk-[A-Za-z0-9_-]{20,}|ghp_[A-Za-z0-9_]{20,}|gho_[A-Za-z0-9_]{20,}|xox[baprs]-[A-Za-z0-9-]{20,}|AKIA[0-9A-Z]{16}|BEGIN (RSA|OPENSSH|EC|DSA) PRIVATE KEY|OPENAI_API_KEY=[A-Za-z0-9_-]+|ANTHROPIC_API_KEY=[A-Za-z0-9_-]+)'

if grep -RInE --exclude-dir=.git --exclude='.gitleaks.toml' --exclude='check_no_secrets.sh' "$PATTERN" "$ROOT"; then
  echo "Secret-like value found. Remove it or replace with a placeholder." >&2
  exit 1
fi

echo "secret scan: pass"
