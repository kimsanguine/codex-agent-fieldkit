from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote


MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
SKIP_PARTS = {".git", ".venv", "node_modules", "__pycache__"}
EXTERNAL_PREFIXES = ("http://", "https://", "mailto:", "tel:", "data:", "javascript:")


def local_target(raw_target: str) -> str | None:
    target = raw_target.strip().split(maxsplit=1)[0].strip("<>")
    if not target or target.startswith("#") or target.startswith(EXTERNAL_PREFIXES):
        return None
    return unquote(target.split("#", 1)[0])


def find_broken_links(root: Path) -> list[str]:
    broken: list[str] = []
    for source in root.rglob("*.md"):
        if any(part in SKIP_PARTS for part in source.relative_to(root).parts):
            continue
        text = source.read_text(encoding="utf-8")
        for raw_target in MARKDOWN_LINK.findall(text):
            target = local_target(raw_target)
            if target is None:
                continue
            resolved = (root / target.lstrip("/")) if target.startswith("/") else (source.parent / target)
            if not resolved.exists():
                broken.append(f"{source.relative_to(root)} -> {target}")
    return broken


def main() -> int:
    parser = argparse.ArgumentParser(description="Reject broken local Markdown links.")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    root = args.root.resolve()
    broken = find_broken_links(root)
    if broken:
        print("documentation links: fail", file=sys.stderr)
        print("\n".join(broken), file=sys.stderr)
        return 1
    print("documentation links: pass")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
