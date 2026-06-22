# 09. GitHub Repo Path

Use private repos while adapting this kit with real organizational context.

Use public repos only when all examples are fictional or approved public material.

## Before Public Push

Run:

```bash
make validate
git status -sb
git diff --stat
```

Confirm:

- no private terms
- no local paths
- no `.env`
- no screenshots with private UI
- no unverified claims

## Public Repo Description

Suggested:

```text
Unofficial Codex fieldkit for non-engineers building verifiable AI agents with starter kits, evals, safety scans, and handoff templates.
```
