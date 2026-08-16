from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

from starter_registry import RegistryError, validate_registry


REQUIRED_ROOT_PATHS = (
    "AGENTS.md",
    "Makefile",
    "starter-kits/registry.json",
    ".agents/skills/codex-agent-fieldkit/SKILL.md",
)


def main() -> int:
    parser = argparse.ArgumentParser(description="Read-only setup check for Codex Agent Fieldkit.")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    root = args.root.resolve()
    failures: list[str] = []

    missing = [path for path in REQUIRED_ROOT_PATHS if not (root / path).exists()]
    if missing:
        failures.append("missing " + ", ".join(missing))
    else:
        try:
            _, kits = validate_registry(root)
        except RegistryError as exc:
            failures.append(str(exc))
        else:
            print(f"[PASS] repository contract ({len(kits)} registered starter kit(s))")

    if failures:
        print("[FAIL] repository contract: " + "; ".join(failures))
    for command in ("python3", "make", "git"):
        status = "PASS" if shutil.which(command) else "FAIL"
        print(f"[{status}] required command: {command}")
        if status == "FAIL":
            failures.append(f"missing required command {command}")

    if shutil.which("codex"):
        print("[PASS] optional command: codex")
    else:
        print("[WARN] optional command: codex (install/sign in before the skill-guided step)")

    if failures:
        print("Next action: open the repository root and resolve the failing checks above.")
        return 1
    print("Next action: make demo")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
