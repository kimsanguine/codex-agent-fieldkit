# Start Here: FAQ Agent Lite

## Outcome

After 15 minutes, you should be able to:

- run the demo
- ask one custom question
- update one FAQ row
- update one golden-set case
- run validation
- explain what is ready and what is not ready

## Commands

```bash
make demo
make test
make eval
make validate
```

## Manual Question

```bash
PYTHONPATH=src python3 -m faq_agent_lite.cli ask "Can I change my billing date?"
```

## Evidence To Capture

After each meaningful change, update:

```text
docs/validation_log.md
```

Include:

- command run
- result
- date
- known limitation
- next step
