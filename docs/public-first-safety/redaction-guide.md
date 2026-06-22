# Redaction Guide

Use this guide before publishing examples, screenshots, logs, or docs.

## Replace

| Private source | Public replacement |
|---|---|
| real client name | `ACME Life` |
| real participant | `Learner A` |
| real internal URL | omit or use official public docs |
| real customer record | synthetic row |
| real process name | generic process label |
| real score | anonymized aggregate or omit |

## Remove

- invite links
- QR codes
- browser profile names
- email addresses
- account ids
- local file paths
- hidden comments
- terminal output with tokens

## Keep

- reusable workflow pattern
- synthetic examples
- public docs links
- validation criteria
- handoff checklist

## Final Check

```bash
make validate
```
