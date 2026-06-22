# FAQ Agent Lite

An offline starter agent for learning the Codex build, verify, and handoff loop.

It uses only:

- Python standard library
- synthetic FAQ data
- golden-set evals
- local scripts

No API key is required.

## Quickstart

From this folder:

```bash
make setup
make demo
make test
make eval
make validate
```

From the repo root:

```bash
make validate
```

## What It Does

The agent loads `data/sample_faqs.csv`, scores each FAQ against a user question, and returns the best answer with a source id.

This is intentionally simple. The goal is not to be a production chatbot. The goal is to make the verification loop visible:

```text
synthetic data -> deterministic answer -> unit test -> golden-set eval -> validation log -> handoff
```

## Files To Edit First

```text
data/sample_faqs.csv
tests/golden_set.jsonl
docs/prd.md
docs/validation_log.md
_handoff/handoff.md
```

## Ask Codex

```text
Read this starter kit. Explain how data, tests, evals, and handoff notes connect.
Do not edit files yet.
```

Then:

```text
Adapt this starter kit to a fictional employee benefits FAQ.
Keep all data synthetic. Update tests, golden set, validation_log.md, and handoff.md.
Run make validate.
```
