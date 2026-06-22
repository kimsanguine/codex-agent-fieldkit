# PRD: FAQ Agent Lite

## Problem

Non-engineer builders need a small agent example that shows the full Codex workflow without requiring private data, paid APIs, or production infrastructure.

## Target Users

- product managers learning agent delivery
- operations teams prototyping FAQ automation
- L&D facilitators teaching AI build workflows
- developers reviewing non-engineer handoff quality

## Job To Be Done

When I want to learn or teach Codex-based agent building, I need a starter kit that runs locally, uses synthetic data, and proves its behavior with tests and evals so I can safely adapt it.

## Scope

In scope:

- synthetic FAQ data
- deterministic retrieval-style answer selection
- CLI demo
- unit tests
- golden-set eval
- validation log
- handoff package

Out of scope:

- production deployment
- real customer data
- paid model calls
- authentication
- database integration

## Success Metrics

- `make demo` runs locally.
- `make test` passes.
- `make eval` scores at least 90%.
- `make validate` passes.
- Handoff notes identify owners, limits, and next steps.

## Acceptance Criteria

- A new builder can clone the repo and run the starter kit without hidden setup.
- Every answer includes a source id.
- Unknown or low-overlap questions use the fallback path.
- Golden-set cases include direct questions, paraphrases, near misses, and safety-sensitive questions.
- Validation evidence is recorded before handoff.

## Failure Modes

| Failure | Expected Handling |
|---|---|
| Wrong folder opened in Codex | Stop and confirm `pwd`, README, and AGENTS.md |
| Eval fails | Compare FAQ data, retrieval logic, and golden-set wording |
| Private data appears | Remove it and rerun safety scans |
| Low-confidence answer | Route to fallback and owner |
| Production request appears | Stop until business, data, compliance, support, and technical owners sign off |

## Approval Line

Prototype or workshop:

- business owner
- technical maintainer

Production adaptation:

- business owner
- data owner
- compliance/privacy reviewer
- support operations owner
- technical maintainer
