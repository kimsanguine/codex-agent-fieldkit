# Migration Checklist

Use this checklist when adapting the starter kit to a new fictional or approved public domain.

## Before Editing

- [ ] Confirm the target domain uses synthetic or approved public data.
- [ ] Read `AGENTS.md`.
- [ ] Read `docs/prd.md`.
- [ ] Run `make validate` once on the unchanged starter kit.

## During Editing

- [ ] Update `data/sample_faqs.csv`.
- [ ] Update `tests/golden_set.jsonl`.
- [ ] Update unit tests if behavior changed.
- [ ] Update `docs/prd.md`.
- [ ] Update `docs/architecture.md` if flow changed.

## Before Sharing

- [ ] Run `make validate`.
- [ ] Update `docs/validation_log.md`.
- [ ] Update `_handoff/handoff.md`.
- [ ] Confirm no private names, URLs, screenshots, or secrets are included.
