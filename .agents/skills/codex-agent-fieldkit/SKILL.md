---
name: codex-agent-fieldkit
description: Use when adapting, validating, or handing off Codex Agent Fieldkit starter kits with synthetic data and public-release checks.
---

# Codex Agent Fieldkit Skill

Use this skill inside this repository when adapting a starter kit.

## Workflow

1. Read `README.md`, `AGENTS.md`, and the starter kit `README.md`.
2. Confirm the target domain uses synthetic or approved public data.
3. Inspect before editing. Summarize the files that define data, tests, evals, validation, and handoff.
4. Make the smallest coherent change.
5. Update these files together when behavior changes:

```text
starter-kits/faq-agent-lite/data/sample_faqs.csv
starter-kits/faq-agent-lite/tests/golden_set.jsonl
starter-kits/faq-agent-lite/tests/test_agent.py
starter-kits/faq-agent-lite/docs/validation_log.md
starter-kits/faq-agent-lite/_handoff/handoff.md
```

6. Run:

```bash
make validate
```

## Failure Triage

If `make validate` fails, inspect in this order:

1. Unit test failure: check `starter-kits/faq-agent-lite/tests/test_agent.py`.
2. Eval failure: compare `starter-kits/faq-agent-lite/tests/golden_set.jsonl` with `starter-kits/faq-agent-lite/data/sample_faqs.csv`.
3. Secret or PII scan failure: remove the value, do not add allowlists unless the value is a documented placeholder.
4. Public-link scan failure: remove local/private URLs from docs and examples.
5. Handoff gap: update validation evidence and production-readiness limits.

After fixing, rerun the smallest failed command first, then rerun `make validate`.

## Stop Conditions

Stop and ask for clarification if:

- the user provides real customer data
- the user asks to commit secrets
- the requested domain requires legal, financial, or medical advice
- validation fails and the fix is not obvious

## Completion

Report:

- what changed
- exact validation command result
- remaining risks
- handoff status

Use this format:

```text
Changed:
Validation:
Known limits:
Handoff:
```
