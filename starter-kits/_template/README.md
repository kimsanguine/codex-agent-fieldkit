# Starter Kit Template

Copy this folder when adding a new starter kit.

Replace placeholders with a small synthetic domain and keep the five commands:

```bash
make setup
make demo
make test
make eval
make validate
```

## Required Boundary

- synthetic data only
- no real customer records
- no internal links
- no credentials
- no production-ready claim

## Files To Update Together

| File | Why it exists |
|---|---|
| `AGENTS.md` | Project memory for Codex |
| `data/sample_records.csv` | Synthetic source data |
| `tests/golden_set.jsonl` | Expected behavior |
| `docs/validation_log.md` | Evidence trail |
| `_handoff/handoff.md` | Next-owner context |
