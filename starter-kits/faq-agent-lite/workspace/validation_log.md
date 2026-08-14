# Validation Log

Keep this file current whenever behavior changes.

| Date | Command | Result | Evidence | Notes |
|---|---|---|---|---|
| 2026-06-22 | `make demo` | Passed | Five demo questions loaded from `data/demo_questions.txt`, including one safety-stop case | Offline demo path works |
| 2026-06-22 | `make test` | Passed | 6 unit tests passed through `make validate` | Covers routing, fallback, demo file loading, and safety stop |
| 2026-06-22 | `make eval` | Passed | Golden-set score 100% (20/20) through `make validate` | Covers direct questions, paraphrases, safety-sensitive questions, and fallback |
| 2026-06-22 | `make validate` | Passed | Starter tests, golden-set eval, starter secret scan, root tests, secret scan, private-term scan, PII scan, public-link scan, generated-artifact scan, and gitleaks wrapper passed | Local gitleaks binary not installed; CI runs gitleaks action |

## Known Limits

- The agent uses simple token overlap, not semantic retrieval.
- The data is fictional and should not be treated as legal, financial, or insurance advice.
- The fallback path is a demo pattern, not a production escalation workflow.
