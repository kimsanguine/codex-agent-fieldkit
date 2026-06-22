# 03. Inspect Before Edit

The first Codex prompt should usually be read-only.

## Read-Only First Prompt

```text
Read README.md, AGENTS.md, START_HERE.md, and the starter kit README.
Summarize the current workflow, validation commands, and public data boundary.
Do not edit files yet.
```

## Why

Inspection prevents:

- edits in the wrong folder
- style mismatch
- deleting useful scaffolding
- leaking private data
- solving the wrong problem

## Edit Prompt

After inspection:

```text
Make the smallest change needed to adapt the FAQ examples to a fictional benefits domain.
Update data, tests, golden set, validation log, and handoff notes.
Run make validate.
```
