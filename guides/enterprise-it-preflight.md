# Enterprise IT Preflight

Use this before a corporate workshop or internal adaptation.

## Account And Access

- [ ] Participants know whether to use a personal approved account, company
  account, or managed workspace account.
- [ ] Codex access is confirmed before the session.
- [ ] GitHub, GitHub Enterprise, or internal Git access is confirmed.
- [ ] The support owner for login failures is named.

## Device Checks

### macOS

```bash
python3 --version
git --version
make --version
```

If `make` is missing, install command line tools or ask Codex for the equivalent
direct Python commands.

### Windows

Confirm one of these paths before the workshop:

- PowerShell with Python and Git available
- WSL2 with Python, Git, and `make`
- a cloud development workspace approved by IT

Avoid mixing Windows paths and WSL2 paths inside one exercise.

### Proxy Or VPN

- [ ] Git clone works on the chosen network.
- [ ] Package installation is either allowed or not required.
- [ ] Browser sign-in is allowed.
- [ ] Terminal commands are not blocked by endpoint protection.

## Workshop Fallbacks

| Blocker | Fallback |
|---|---|
| Cannot clone public repo | Provide an approved zip copy through the internal channel |
| `make` missing | Use direct Python commands from the starter kit Makefile |
| Python missing | Pair with a prepared machine; do not edit data until setup is fixed |
| GitHub blocked | Use internal Git mirror or local zip copy |
| Codex access blocked | Run as facilitator-led inspection, then schedule setup follow-up |

## Data Boundary

Participants must not paste:

- customer records
- claim files
- account data
- policy text from private systems
- internal links
- screenshots
- API keys or tokens

Use the synthetic data that ships with the repo.
