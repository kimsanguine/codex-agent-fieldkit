# Start Here

Use this file when you are opening the repo for the first time in Codex.

For a Korean 15-30 minute path for non-engineer operators, see
[`START_HERE_FOR_OPERATORS.md`](START_HERE_FOR_OPERATORS.md).

## Goal

Build confidence in the full loop:

```text
idea -> project context -> starter agent -> tests -> eval -> release scan -> handoff
```

The default starter kit does not require an API key.

## First Run

```bash
make setup
make demo
make test
make eval
make validate
```

If all commands pass, open:

```text
starter-kits/faq-agent-lite/docs/prd.md
starter-kits/faq-agent-lite/docs/validation_log.md
starter-kits/faq-agent-lite/_handoff/handoff.md
```

## Ask Codex

Start with inspection, not editing:

```text
Read README.md, AGENTS.md, START_HERE.md, and starter-kits/faq-agent-lite/README.md.
Explain the project structure and the validation path. Do not edit files yet.
```

Then ask for a small adaptation:

```text
Adapt starter-kits/faq-agent-lite for a fictional employee benefits FAQ.
Use only synthetic data. Update the golden set and run make validate.
```

## Stop Conditions

Do not continue if:

- you are about to paste private or customer data into the repo
- `.env` contains a real key
- a screenshot includes an internal URL or user identity
- tests or evals fail and the failure is not documented
- handoff notes do not explain what was verified

## Success

You are done only when:

- the demo runs
- tests pass
- eval score meets the threshold
- release scans pass
- handoff notes are current
