# FAQ Agent Lite Instructions

This starter kit must remain safe, synthetic, and easy to verify.

## Rules

- Use synthetic data only.
- Keep the demo runnable without an API key.
- Update tests and golden-set evals when changing agent behavior.
- Update `docs/validation_log.md` after running validation.
- Update `_handoff/handoff.md` before sharing the kit.

## Preferred Change Loop

1. Inspect current data and tests.
2. Make one small behavior change.
3. Run `make test`.
4. Run `make eval`.
5. Run `make validate`.
6. Document the result.

## Do Not Add

- real customer data
- private company names
- screenshots
- internal URLs
- real credentials
- paid-service dependency for the default path
