# 04. AGENTS.md As Project Memory

`AGENTS.md` tells Codex how to work inside a specific project.

Use it for durable rules:

- public/private boundary
- commands to run
- files to update together
- style preferences
- stop conditions
- verification standard

## Minimal Pattern

```markdown
# Project Instructions

Run `make validate` before claiming completion.

Use synthetic data only.

When changing behavior, update:

- tests
- golden set
- validation log
- handoff notes
```

## Keep It Operational

Avoid generic values. Put commands and file paths where possible.
