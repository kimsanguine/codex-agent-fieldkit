# Facilitator Guide

Use this guide for a 60-minute or 90-minute non-engineer Codex workshop.

## Audience

- PMs
- operations managers
- service planners
- L&D / AX transformation teams
- internal AI task-force members

## Prerequisites

Participants should have:

- Codex access through an eligible account or approved organizational setup
- GitHub account or internal Git equivalent
- Python 3.10+
- terminal access
- a local copy of this repo
- explicit instruction to use only synthetic data

See [`corporate-prerequisites.md`](corporate-prerequisites.md) before running this in a company setting.

## 60-Minute Plan

| Time | Activity | Expected Output |
|---:|---|---|
| 0-5 | Explain public-first boundary | Participants can say what must never be pasted into Codex |
| 5-10 | Run `make demo` | Demo answers are visible with source ids |
| 10-15 | Run `make validate` | Participants see tests, eval, and scans pass |
| 15-25 | Codex inspect-before-edit prompt | Codex summarizes README, AGENTS.md, and starter kit |
| 25-38 | Change one synthetic FAQ row | Data and answer behavior change in a small scope |
| 38-48 | Update golden set and rerun eval | Participants see failure or pass evidence |
| 48-55 | Update validation log and handoff | Evidence and owner notes are current |
| 55-60 | Debrief | Participants explain what is not production-ready |

## 90-Minute Extension

Add:

- pair review of `git diff`
- release checklist walkthrough
- RACI signoff exercise
- "what would block production?" discussion

## Facilitator Prompts

Read-only first:

```text
Read README.md, AGENTS.md, START_HERE.md, and starter-kits/faq-agent-lite/README.md.
Explain the workflow, validation commands, and public data boundary.
Do not edit files yet.
```

Small adaptation:

```text
Change one synthetic FAQ row for a fictional employee benefits domain.
Update the golden set, validation log, and handoff.
Run make validate.
```

Debug prompt:

```text
The eval failed. Identify the first failing case, explain whether data or expected output is wrong, and make the smallest fix.
```

## Stop And Ask Moments

Stop the room if:

- someone wants to paste real customer data
- someone is in the wrong folder
- `.env` contains a real key
- validation fails and nobody can explain why
- handoff says production-ready without legal, privacy, and operational review

## Debrief Questions

1. What did Codex need before editing?
2. Which files changed together?
3. What did the golden set prove?
4. What did the safety scans not prove?
5. Who would need to sign off before production use?
