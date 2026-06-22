#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

PATTERN='(drive\.google\.com|docs\.google\.com|padlet\.com|vercel\.app|localhost:[0-9]+|127\.0\.0\.1:[0-9]+|file://|Users/sanguinekim)'

if grep -RInE --exclude-dir=.git --exclude='check_public_links.sh' "$PATTERN" "$ROOT"; then
  echo "Potentially unsafe public link or local path found." >&2
  exit 1
fi

echo "public link scan: pass"
