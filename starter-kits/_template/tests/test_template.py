from __future__ import annotations

from pathlib import Path


def test_template_has_golden_set() -> None:
    root = Path(__file__).resolve().parents[1]
    assert (root / "tests" / "golden_set.jsonl").exists()
