# 00. What Codex Is For Non-Engineers

Codex is useful when the work can be represented as files, commands, tests, and evidence.

For non-engineers, the important shift is:

```text
from "write a perfect prompt"
to "create a project folder Codex can inspect, edit, run, and verify"
```

## Codex Is Good At

- reading an existing folder
- explaining project structure
- making scoped edits
- running local commands
- interpreting failures
- updating tests and docs
- preparing handoff notes

## Codex Still Needs From You

- clear goal
- safe data boundary
- acceptance criteria
- examples of good and bad answers
- approval for risky actions
- final judgment on whether the result is useful

## Fieldkit Rule

Start with a folder that contains:

```text
README.md
AGENTS.md
docs/prd.md
docs/validation_log.md
tests/golden_set.jsonl
_handoff/handoff.md
```

Codex performs better when the work surface is explicit.
