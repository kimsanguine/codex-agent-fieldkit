# Handoff: FAQ Agent Lite

## What Exists

An offline synthetic FAQ agent with:

- CSV knowledge source
- deterministic answer selection
- CLI demo
- unit tests
- golden-set eval
- validation scripts

## How To Run

```bash
make validate
```

## What Was Verified

Verified on 2026-06-22:

- `make demo`: passed, five demo questions returned sourced answers or the fallback path.
- `make test`: passed through `make validate`, 5 unit tests.
- `make eval`: passed through `make validate`, 100% golden-set score (20/20).
- `make validate`: passed, including starter checks, repo-level safety scans, PII scan, generated-artifact scan, and gitleaks wrapper.

## Owners

For a real adaptation, assign:

- product owner
- data owner
- compliance or privacy reviewer
- support operations owner
- technical maintainer

## RACI / Signoff

| Role | Name or Team | Responsibility | Signoff Required Before Production |
|---|---|---|---|
| Business owner | TBD | Confirms user problem, scope, and success criteria | Yes |
| Data owner | TBD | Confirms source data is approved and current | Yes |
| Compliance/privacy reviewer | TBD | Reviews legal, privacy, and regulatory constraints | Yes |
| Support operations owner | TBD | Confirms escalation and fallback workflow | Yes |
| Technical maintainer | TBD | Owns code, tests, evals, and deployment path | Yes |

## Risk Acceptance

Do not use this starter kit in production until these risks are accepted or resolved:

- data source approval
- answer quality threshold
- fallback and escalation ownership
- logging and retention policy
- user consent and privacy notice
- monitoring and incident response
- legal/compliance review

## Approval Line

Workshop or prototype use:

```text
Business owner + technical maintainer
```

Production use:

```text
Business owner + data owner + compliance/privacy reviewer + support operations owner + technical maintainer
```

## Not Ready For Production

This kit is not production-ready. It does not include:

- authentication
- monitoring
- audit logging
- human approval queues
- legal review
- privacy review
- production data handling

## Next Decision Gates

1. Replace synthetic data with approved public or internal data.
2. Expand golden set to cover real high-volume and high-risk questions.
3. Add human review for low-confidence or regulated answers.
4. Add monitoring, audit logging, and incident response.
5. Complete privacy, legal, and security review.

## Handoff Checklist

- [x] Data is synthetic or approved public data.
- [x] `.env` is not committed.
- [x] Tests pass.
- [x] Eval score meets threshold.
- [x] Validation log is current.
- [x] Known limits are documented.
- [x] Next owner can run the commands without hidden setup.
