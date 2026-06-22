from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    cases = [
        json.loads(line)
        for line in (ROOT / "tests" / "golden_set.jsonl").read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    print(f"eval scaffold loaded: {len(cases)} cases")
    print("Replace this template eval with starter-specific behavior checks.")


if __name__ == "__main__":
    main()
