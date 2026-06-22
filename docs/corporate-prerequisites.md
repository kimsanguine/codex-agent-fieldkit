# Corporate Prerequisites

Use this checklist before running Codex Agent Fieldkit inside an organization.

## Access

- [ ] Participants have approved Codex access.
- [ ] The organization has decided whether users sign in with ChatGPT accounts or API keys.
- [ ] Usage and cost expectations are explained.
- [ ] Participants know who to contact if login fails.

## Device Setup

- [ ] Python 3.10+ is installed.
- [ ] `make` is available or an equivalent command runner is approved.
- [ ] Git is installed.
- [ ] Terminal access is allowed.
- [ ] Windows users have PowerShell or WSL2 guidance.
- [ ] Corporate proxy/VPN constraints are known.

## Repository Setup

- [ ] Use a private repo for internal adaptations.
- [ ] Do not commit `.env`.
- [ ] Do not paste private data into public examples.
- [ ] Decide whether GitHub, GitHub Enterprise, or an internal Git server is used.
- [ ] Confirm branch and review policy.

## Data Boundary

- [ ] Synthetic data is the default.
- [ ] Public data sources are approved before use.
- [ ] Private customer data is out of scope for the workshop.
- [ ] Screenshots are prohibited unless reviewed and redacted.

## Governance

- [ ] Business owner is named.
- [ ] Data owner is named.
- [ ] Compliance/privacy reviewer is named.
- [ ] Technical maintainer is named.
- [ ] Production-use approval is explicitly out of scope unless separately reviewed.

## Readiness Decision

Run the workshop only when access, data boundary, and support path are clear.
