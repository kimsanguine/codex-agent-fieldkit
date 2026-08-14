# Eval Maturity Guide

The starter eval in this repo is intentionally small. It proves that a public
training kit can run a deterministic golden-set loop. It does not prove
production quality.

## Level 1: Training Eval

Use this for workshops and public examples.

- 10-30 synthetic cases
- deterministic inputs
- exact source-id checks
- required phrase checks
- visible pass/fail output

This repo starts here.

## Level 2: Adaptation Eval

Use this before a private internal pilot.

- domain-specific synthetic cases
- high-risk and fallback cases
- reviewer-approved expected behaviors
- validation report artifact
- owner signoff on known limitations

## Level 3: Pre-Production Eval

Use this only after data, privacy, and operational ownership are approved.

- approved private test data or fully redacted samples
- regression history across releases
- error taxonomy
- manual review sample
- monitoring plan
- incident rollback path

## Do Not Overclaim

Good public phrasing:

```text
20/20 synthetic golden-set eval passed for the starter kit.
```

Avoid:

```text
The agent is accurate.
The workflow is production-ready.
The domain is validated.
```

## Minimum Cases for a New Starter Kit

| Case type | Minimum | Purpose |
|---|---:|---|
| Happy path | 5 | Verify common source-grounded answers |
| Paraphrase | 5 | Verify similar wording still routes correctly |
| Fallback | 3 | Verify the agent does not invent unsupported answers |
| Safety stop | 3 | Verify risky requests stop or hand off |
| Edge wording | 4 | Verify fragile phrasing is caught |

Keep the first eval simple enough that a non-engineer can inspect every case.
