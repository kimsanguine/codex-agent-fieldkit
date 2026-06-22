# 05. Safe Env And Secrets

The default starter kit does not need an API key.

## Rules

- Commit `.env.example`.
- Never commit `.env`.
- Use placeholders, not real keys.
- Do not paste keys into prompts.
- Do not include screenshots that reveal keys or internal URLs.

## Safe Example

```text
OPENAI_API_KEY=
```

## Unsafe Example

```text
OPENAI_API_KEY=<real value here>
```

## Check

```bash
make safety
```
