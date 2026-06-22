# Architecture: FAQ Agent Lite

## Components

```text
data/sample_faqs.csv
        |
        v
src/faq_agent_lite/agent.py
        |
        v
src/faq_agent_lite/cli.py
        |
        +--> tests/test_agent.py
        +--> scripts/eval.py
        +--> docs/validation_log.md
        +--> _handoff/handoff.md
```

## Data Flow

1. CSV rows are loaded into `FAQRecord` objects.
2. A question is tokenized.
3. FAQ rows are scored by token overlap with a small synonym map.
4. The best row returns an answer, source id, confidence, and handoff note.
5. Unknown questions return a fallback with `NO_MATCH`.

## Why This Simple Design

The starter kit is optimized for inspection and verification, not model quality.

The retrieval logic is simple enough for Codex and non-engineer builders to inspect, change, test, and explain.

## Extension Points

- replace CSV with a public knowledge base
- add category filters
- add answer citations
- add human approval for low confidence
- add model calls after data and eval boundaries are stable
