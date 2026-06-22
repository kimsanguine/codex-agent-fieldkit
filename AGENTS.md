# Codex Agent Fieldkit Instructions

This repository is a public, synthetic fieldkit for Codex-based agent building.

## Scope

Optimize for:

- non-engineer builders
- runnable starter kits
- public-first safety
- verification evidence
- handoff readiness

Do not turn this repo into:

- a private course archive
- a prompt-only collection
- a vendor endorsement
- a client-specific case study

## Public Boundary

All public examples must use fictional names and synthetic data.

Never add:

- real client names
- participant data
- internal workspace links
- QR codes
- API keys or tokens
- private screenshots
- production customer data

Use fictional examples such as `ACME Life`.

## Coding Rules

- Keep the starter kit runnable without paid services.
- Prefer Python standard library code unless a dependency is clearly needed.
- Keep scripts deterministic.
- Make validation commands easy to run from the repo root.
- Update tests and evals when behavior changes.

## Verification

Before claiming a change is complete, run:

```bash
make validate
```

If a check fails, document the failure and practical next step.
