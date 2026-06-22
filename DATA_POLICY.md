# Data Policy

## Allowed

- fictional company names
- synthetic FAQ rows
- synthetic golden-set questions
- anonymized process patterns
- public documentation links

## Not Allowed

- real customer data
- private course material copied verbatim
- client names from private engagements
- participant scores or submissions
- real internal process documents
- private URLs or QR codes
- credentials, tokens, cookies, or `.env` files

## Synthetic Data Checklist

Before committing data:

1. Confirm every entity is fictional.
2. Confirm every URL is public documentation or example-only.
3. Confirm no row came from customer systems.
4. Confirm no local path reveals private project names.
5. Run `make validate`.
