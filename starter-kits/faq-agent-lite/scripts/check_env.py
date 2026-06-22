from __future__ import annotations

import sys


def main() -> None:
    if sys.version_info < (3, 10):
        raise SystemExit("Python 3.10+ is required.")
    print(f"python: {sys.version.split()[0]}")
    print("env check: pass")


if __name__ == "__main__":
    main()
