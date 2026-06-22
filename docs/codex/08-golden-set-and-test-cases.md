# 08. Golden Set And Test Cases

Tests and evals answer different questions.

## Unit Tests

Unit tests check deterministic behavior:

- routing
- fallback
- parsing
- command behavior

## Golden Set

The golden set checks whether the agent handles important user questions.

In this repo:

```text
starter-kits/faq-agent-lite/tests/golden_set.jsonl
```

Each row contains:

- case id
- question
- expected source id
- required answer phrases

## Rule

When you change the data, update the golden set.

When you change the answer logic, update both tests and golden set.
