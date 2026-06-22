from __future__ import annotations

import sys


def main() -> None:
    if sys.version_info < (3, 10):
        raise SystemExit("Python 3.10+ is required.")
    print(f"Python {sys.version.split()[0]} OK")


if __name__ == "__main__":
    main()
