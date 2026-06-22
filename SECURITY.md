# Security Policy

## Supported Scope

This repository is an educational fieldkit. It is not a production security product.

Security issues that matter here:

- exposed secrets
- private company or customer data
- unsafe public links
- misleading handoff notes
- starter kits that encourage unsafe data handling

## Reporting

Open a GitHub issue with:

- affected file or command
- why the behavior is unsafe
- suggested remediation if known

Do not include secrets or private data in the issue.

## Release Gate

Before public release, run:

```bash
make validate
```

The repository includes lightweight scans. They do not replace professional security review.
