from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run(command: list[str]) -> None:
    print(f"$ {' '.join(command)}")
    subprocess.run(command, cwd=ROOT, check=True)


def main() -> None:
    run([sys.executable, "scripts/check_env.py"])
    run([sys.executable, "-m", "unittest", "discover", "-s", "tests"])
    run([sys.executable, "scripts/eval.py"])
    run([sys.executable, "scripts/secret_scan.py"])


if __name__ == "__main__":
    main()
