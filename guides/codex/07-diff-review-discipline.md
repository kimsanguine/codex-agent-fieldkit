# 07. Diff Review Discipline

Before committing or sharing, review the diff.

## Commands

```bash
git status -sb
git diff --stat
git diff
```

## Review Questions

- Did the change stay inside the intended files?
- Did data, tests, evals, and docs move together?
- Did any private term or local path appear?
- Did validation evidence get updated?
- Is the handoff note honest about limits?

## Ask Codex

```text
Review the current diff for scope creep, private data leakage, and missing tests.
Return findings first. Do not edit files.
```
