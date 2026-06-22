# 06. Run, Debug, Verify Loop

Use a short loop:

```text
change -> run smallest check -> inspect failure -> fix -> run full validation
```

## Starter Kit Commands

```bash
make demo
make test
make eval
make validate
```

## Ask Codex

```text
Run make validate.
If it fails, identify the first failing command and propose the smallest fix.
After fixing, rerun the failed command first, then make validate.
```

## Evidence

Update:

```text
docs/validation_log.md
```

Do not mark handoff ready unless validation has actually run.
