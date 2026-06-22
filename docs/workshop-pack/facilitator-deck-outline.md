# Facilitator Deck Outline

## 1. Title

Codex Agent Fieldkit: From prompt docs to verified agent handoff.

## 2. Why Prompt Literacy Is Not Enough

- Prompts do not show source data, tests, risk boundaries, or owner handoff.
- Teams need delivery literacy: folder, memory, data, eval, safety, handoff.

## 3. Public-Safe Boundary

- Use synthetic data.
- Do not paste private records.
- Do not claim production readiness.

## 4. Folder Tour

Show:

- `README.md`
- `AGENTS.md`
- `starter-kits/faq-agent-lite/`
- `docs/validation_log.md`
- `_handoff/handoff.md`

## 5. Run The Demo

Command:

```bash
make demo
```

Expected output: a source-grounded synthetic FAQ answer.

## 6. Run The Gate

Command:

```bash
make validate
```

Explain tests, eval, and safety scans separately.

## 7. Make One Safe Change

Edit one synthetic FAQ row. Do not add real data.

## 8. Watch Eval Fail Or Pass

Run:

```bash
make eval
```

Explain why a failing eval is a useful signal.

## 9. Write Evidence

Update validation log and handoff notes.

## 10. Production Bridge

Explain the extra gates: business owner, data owner, compliance/privacy,
technical maintainer, support owner.
