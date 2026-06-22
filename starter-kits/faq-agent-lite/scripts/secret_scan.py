from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SECRET_PATTERNS = [
    re.compile(r"sk-[A-Za-z0-9_-]{20,}"),
    re.compile(r"gh[pousr]_[A-Za-z0-9_]{20,}"),
    re.compile(r"OPENAI_API_KEY=[A-Za-z0-9_-]+"),
    re.compile(r"ANTHROPIC_API_KEY=[A-Za-z0-9_-]+"),
    re.compile(r"BEGIN (RSA|OPENSSH|EC|DSA) PRIVATE KEY"),
]
SKIP = {".git", "__pycache__", ".pytest_cache"}


def main() -> None:
    hits: list[str] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if any(part in SKIP for part in path.parts):
            continue
        if path.name == "secret_scan.py":
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                hits.append(str(path.relative_to(ROOT)))

    if hits:
        for hit in hits:
            print(f"secret-like value: {hit}")
        raise SystemExit("Secret scan failed.")

    print("starter secret scan: pass")


if __name__ == "__main__":
    main()
