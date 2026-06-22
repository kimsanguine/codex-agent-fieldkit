#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

if command -v gitleaks >/dev/null 2>&1; then
  gitleaks detect --no-git --source "$ROOT" --redact --verbose
  echo "gitleaks scan: pass"
else
  echo "gitleaks scan: skipped (gitleaks not installed locally; CI runs gitleaks/gitleaks-action)"
fi
