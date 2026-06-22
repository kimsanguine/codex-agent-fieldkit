# Release Audit

Date: 2026-06-22

## Commands Run

```bash
make demo
make validate
```

## Result

Passed.

Evidence:

- Demo returned sourced answers for four in-scope questions.
- Demo also returned a fallback for one no-match question loaded from `data/demo_questions.txt`.
- Unit tests passed: 5 tests.
- Golden-set eval passed with 100% score (20/20).
- Starter secret scan passed.
- Repo-level private-term scan passed.
- Repo-level secret scan passed.
- Repo-level PII scan passed.
- Repo-level public-link scan passed.
- Generated-artifact scan passed.
- Gitleaks wrapper ran locally and reported local gitleaks was not installed; GitHub Actions is configured to run `gitleaks/gitleaks-action`.

## Release Boundary

Public release is acceptable only if independent reviewer validation scores average at least 9.0 with no category below 8.5.

## Remaining Non-Blocking Limits

- The starter agent is a deterministic teaching example, not a production customer-service system.
- The data is fictional and should not be interpreted as legal, financial, or insurance advice.
- Future starter kits should go through the same release gate.
