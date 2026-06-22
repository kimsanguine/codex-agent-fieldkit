from __future__ import annotations

import json
from pathlib import Path

from faq_agent_lite import FAQAgent


ROOT = Path(__file__).resolve().parents[1]
GOLDEN_SET = ROOT / "tests" / "golden_set.jsonl"
PASS_THRESHOLD = 0.9


def load_cases() -> list[dict]:
    return [json.loads(line) for line in GOLDEN_SET.read_text(encoding="utf-8").splitlines() if line.strip()]


def main() -> None:
    agent = FAQAgent()
    cases = load_cases()
    passed = 0

    for case in cases:
        result = agent.answer(case["question"])
        source_ok = result.source_id == case["expected_source_id"]
        includes_ok = all(term.lower() in result.answer.lower() for term in case["must_include"])
        ok = source_ok and includes_ok
        passed += int(ok)
        status = "PASS" if ok else "FAIL"
        print(f"{status} {case['id']} expected={case['expected_source_id']} actual={result.source_id}")

    score = passed / max(len(cases), 1)
    print(f"eval score: {score:.2%} ({passed}/{len(cases)})")

    if score < PASS_THRESHOLD:
        raise SystemExit(f"Eval score below threshold: {score:.2%} < {PASS_THRESHOLD:.0%}")


if __name__ == "__main__":
    main()
