# Codex Agent Fieldkit

> An unofficial fieldkit for non-engineers who want to build, verify, and hand off AI agents with Codex.

Not a prompt collection. Not a slide archive.

Codex Agent Fieldkit gives product managers, operators, and corporate AI teams a practical path from idea to working agent:

1. Open the right project folder in Codex.
2. Give Codex project memory through `AGENTS.md`.
3. Adapt a runnable starter agent with synthetic data.
4. Run tests, evals, and public-release scans.
5. Capture validation evidence.
6. Package the work for a safe handoff.

This project is **unofficial** and is not affiliated with OpenAI. All examples are fictional or synthetic.

## Why This Exists

Most AI agent guides stop at prompts. In real non-engineer workflows, the hard part is the operating system around the prompt:

- folder structure
- project instructions
- dummy data boundaries
- env and secret handling
- golden-set tests
- validation logs
- handoff notes
- release audit

This repo turns those practices into a small runnable kit.

## Quickstart

Run the starter kit without an API key:

```bash
git clone https://github.com/kimsanguine/codex-agent-fieldkit.git
cd codex-agent-fieldkit
make setup
make demo
make test
make eval
make validate
```

Expected result:

- `make demo` answers sample customer questions from synthetic FAQs.
- `make eval` checks the agent against a golden set.
- `make validate` runs tests, evals, and public-release safety scans.

Sample output:

```text
Q: Can I change my billing date?
A: Yes. In this fictional ACME Life sample, customers can request one billing-date change per month before the next invoice is issued.
Source: FAQ-001 | Category: billing | Confidence: 1.00
Handoff: Owner: billing operations. Check policy before using in production.
```

## Use This When

- You are a PM or operator who wants to turn an AI agent idea into a verified working folder.
- You are an L&D or AX lead who needs a safe non-engineer workshop kit with stop conditions.
- You are an internal AI task force member who needs a public-first template before touching private data.
- You are a developer helping non-engineers produce better PRDs, evals, validation logs, and handoff packages.

## The 60-Minute Codex Path

| Time | Outcome | File |
|---:|---|---|
| 0-5 min | Understand the fieldkit | [`START_HERE.md`](START_HERE.md) |
| 5-12 min | Install and sign in to Codex | [`docs/codex/01-install-login-health-check.md`](docs/codex/01-install-login-health-check.md) |
| 12-20 min | Open the correct folder | [`docs/codex/02-open-the-right-folder.md`](docs/codex/02-open-the-right-folder.md) |
| 20-30 min | Let Codex inspect before editing | [`docs/codex/03-inspect-before-edit.md`](docs/codex/03-inspect-before-edit.md) |
| 30-42 min | Adapt the starter agent | [`starter-kits/faq-agent-lite/`](starter-kits/faq-agent-lite/) |
| 42-50 min | Run tests and evals | [`docs/codex/08-golden-set-and-test-cases.md`](docs/codex/08-golden-set-and-test-cases.md) |
| 50-56 min | Run release checks | [`docs/release-audit/public-release-checklist.md`](docs/release-audit/public-release-checklist.md) |
| 56-60 min | Prepare handoff | [`docs/codex/10-handoff-package.md`](docs/codex/10-handoff-package.md) |

For a complete narrated adaptation example, see [`examples/adaptation-walkthrough.md`](examples/adaptation-walkthrough.md).

For Korean PM/product leaders, see [`docs/ko/pm-leader-guide.md`](docs/ko/pm-leader-guide.md).

## What's Included

```text
.
├── START_HERE.md
├── starter-kits/
│   └── faq-agent-lite/        # runnable offline starter agent
├── docs/
│   ├── codex/                 # Codex workflow for non-engineers
│   ├── public-first-safety/   # anonymization and data policy
│   ├── release-audit/         # public release checklist
│   ├── rubrics/               # quality scorecard
│   └── launch/                # public launch copy
├── scripts/                   # repo-level safety checks
├── tests/                     # repo-level private-term checks
└── .agents/skills/            # optional repo-scoped Codex skill
```

## Starter Kit

The first starter kit is intentionally narrow:

[`starter-kits/faq-agent-lite`](starter-kits/faq-agent-lite/)

It is a retrieval-style FAQ agent that uses only Python standard library code and synthetic data. It is designed for PMs and operators to inspect, change, test, and hand off.

Commands:

```bash
make setup
make demo
make test
make eval
make validate
```

## Quality Gate

Before publishing or adapting this kit to a real organization, run:

```bash
make validate
```

The validation gate checks:

- Python tests
- golden-set evals
- secret-like strings
- private/client terms
- unsafe public links
- handoff and validation-log presence

For the scoring rubric, see [`docs/rubrics/agent-fieldkit-scorecard.md`](docs/rubrics/agent-fieldkit-scorecard.md).

## Public-First Safety

The repo is built around one rule:

> A public example must be safe before it is impressive.

Never publish:

- real client or company names from private engagements
- participant names, group numbers, scores, submissions, or screenshots
- internal URLs, QR codes, workspace links, or private repo links
- `.env` files, API keys, access tokens, logs, or local config
- real customer data, real policy data, or proprietary workflows

Use fictional examples such as `ACME Life` and synthetic sample data.

## Codex References

This fieldkit follows the current public Codex docs:

- Codex CLI can run locally in a selected directory and inspect, edit, and run code: <https://developers.openai.com/codex/cli>
- Codex app supports parallel threads, worktrees, automations, and Git workflows: <https://developers.openai.com/codex/app>
- Codex skills package reusable instructions, resources, and optional scripts: <https://developers.openai.com/codex/skills>

## Repository Relationship

Recommended public positioning:

- `AI_PM`: broad AI PM operating system and strategy hub
- `ai-prompts-playbook`: reusable prompt cards
- `codex-agent-fieldkit`: runnable Codex agent build, verification, and handoff kit

## License

MIT. See [`LICENSE`](LICENSE).
