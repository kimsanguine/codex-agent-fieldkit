# Add a Starter Kit

Use this contract when adding a new starter kit under `starter-kits/`.

The goal is not to add more demos. The goal is to add another small, runnable
delivery loop with data, tests, evals, validation evidence, and handoff notes.

## Required Shape

```text
starter-kits/<kit-name>/
├── AGENTS.md
├── README.md
├── Makefile
├── START_HERE.md
├── data/
├── docs/
│   ├── architecture.md
│   ├── prd.md
│   ├── progress.md
│   └── validation_log.md
├── scripts/
├── src/
├── tests/
│   └── golden_set.jsonl
└── _handoff/
    ├── handoff.md
    └── migration_checklist.md
```

## Required Commands

Every starter kit should support:

```bash
make setup
make demo
make test
make eval
make validate
```

`make validate` must run the smallest complete loop for that kit: setup check,
unit tests, golden-set eval, and kit-local safety checks.

## Required Public Boundary

- Use fictional organizations such as `ACME Life`.
- Use synthetic data only.
- Do not add private screenshots, internal links, access tokens, or real customer
  records.
- Do not claim production readiness.

## Eval Contract

Each `tests/golden_set.jsonl` row should include:

```json
{"id":"G001","question":"sample question","expected_source_id":"SOURCE-001","must_include":["required phrase"]}
```

The eval should prove at least three behaviors:

- happy-path retrieval
- fallback when no confident source exists
- safety stop or human handoff for risky requests

## Handoff Contract

Each starter kit must keep:

- `docs/validation_log.md`: commands run, result, evidence, remaining risk
- `_handoff/handoff.md`: current owner, verified state, known limits, next step
- `_handoff/migration_checklist.md`: what can and cannot move into a private adaptation

## Review Checklist

- [ ] The kit runs offline or clearly labels its required dependency.
- [ ] The README can be understood in 60 seconds.
- [ ] The golden set covers happy path, fallback, and safety behavior.
- [ ] The validation log records the current checked state.
- [ ] The handoff does not say production-ready.
- [ ] `make validate` passes from the repo root after adding the kit.
