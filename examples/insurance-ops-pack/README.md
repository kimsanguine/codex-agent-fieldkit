# Insurance Ops Pack

This pack gives insurance and service operations teams a synthetic example set
before they touch private data.

It is not a runnable production kit. It is a domain adaptation pack that can be
used with `starter-kits/faq-agent-lite/` or a private starter kit.

## Files

```text
examples/insurance-ops-pack/
├── data/synthetic_insurance_faqs.csv
├── tests/golden_set.jsonl
├── docs/validation_log.md
└── _handoff/handoff.md
```

## Use It With Codex

```text
Read examples/insurance-ops-pack/README.md,
examples/insurance-ops-pack/data/synthetic_insurance_faqs.csv,
examples/insurance-ops-pack/tests/golden_set.jsonl,
and docs/adapt-for-insurance-ops.md.

Explain how to adapt the current FAQ starter kit to this synthetic insurance
operations domain. Do not use real customer data.
```

## What This Proves

- The domain categories can be described without private data.
- High-risk insurance questions can be routed to handoff.
- Golden-set cases can test safety stops and fallback behavior.
- Validation and handoff evidence can be written before any private pilot.

## What This Does Not Prove

- Actual policy interpretation
- Claim approval or denial
- Production accuracy
- Compliance approval
- Privacy approval
