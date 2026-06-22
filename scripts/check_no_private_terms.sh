#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

TERMS=(
  "삼성생명"
  "Samsung Life"
  "BIZROUTER"
  "kimsanguine@gmail.com"
  "2606_삼성_바이브코딩"
)

FAILED=0
for term in "${TERMS[@]}"; do
  if grep -RIn \
    --exclude-dir=.git \
    --exclude='check_no_private_terms.sh' \
    --exclude='test_no_private_terms.py' \
    "$term" "$ROOT" >/tmp/codex_fieldkit_private_term_hits.txt; then
    cat /tmp/codex_fieldkit_private_term_hits.txt
    FAILED=1
  fi
done

if [[ "$FAILED" -ne 0 ]]; then
  echo "Private or client-specific term found." >&2
  exit 1
fi

echo "private term scan: pass"
