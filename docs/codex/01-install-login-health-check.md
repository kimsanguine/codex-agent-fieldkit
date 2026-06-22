# 01. Install, Login, Health Check

Use the official Codex docs for current installation details:

- CLI: <https://developers.openai.com/codex/cli>
- App: <https://developers.openai.com/codex/app>

## CLI Path

Install Codex CLI from the official docs, then run:

```bash
codex
```

The first run prompts you to sign in with a ChatGPT account or API key.

## App Path

The Codex app is available for macOS and Windows. It is useful when you want parallel threads, worktree support, and Git workflow support in one desktop surface.

## Health Check

Ask Codex:

```text
Tell me which folder you are working in. Then read README.md and AGENTS.md.
Do not edit files yet.
```

Stop if Codex is pointed at the wrong folder.
