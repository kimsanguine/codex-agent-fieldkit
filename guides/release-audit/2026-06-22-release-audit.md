# Release Audit

Date: 2026-06-22

## Commands Run

```bash
make demo
make validate
make validate-report
npm install
npm run still
npm run render
```

## Result

Passed.

## Artifact

- Local standalone git repository: yes
- Latest local validation before first public push covered content through `dd59494`
- Latest local validation report was regenerated after hero image, Remotion intro video, workshop pack, insurance pack, starter template, and validation-report additions.
- Branch: `main`
- Remote: <https://github.com/kimsanguine/codex-agent-fieldkit>
- Initial public push commit: `dd59494`
- Post-push CI: green on run `27923085361` for commit `5053bd0`
- Later public CI: green on run `27929277731` for commit `5a791ba`

Evidence:

- Demo returned sourced answers for four in-scope questions.
- Demo also returned a safety stop for one real-data question loaded from `data/demo_questions.txt`.
- Unit tests passed: 6 tests.
- Golden-set eval passed with 100% score (20/20).
- Starter secret scan passed.
- Repo-level private-term scan passed.
- Repo-level secret scan passed.
- Repo-level PII scan passed.
- Repo-level public-link scan passed.
- Generated-artifact scan passed.
- Gitleaks wrapper ran locally and reported local gitleaks was not installed; GitHub Actions is configured to run `gitleaks/gitleaks-action`.
- GitHub Actions gitleaks scan passed on the public repository.
- `make validate-report` generated `reports/validation.md`.
- README hero image was rendered to `assets/images/banner.png` from `assets/images/banner.svg`.
- Remotion still frame and MP4 were rendered to `assets/video/`.
- Remotion source is isolated under `media/fieldkit-intro-video/`.

## Release Boundary

Public release is acceptable only if AI expert/persona reviewer validation scores average at least 9.0 with no category below 8.5.

## Remaining Non-Blocking Limits

- The starter agent is a deterministic teaching example, not a production customer-service system.
- The data is fictional and should not be interpreted as legal, financial, or insurance advice.
- The Remotion project has a separate Node dependency surface and is not required for the Python starter workflow.
- Future starter kits should go through the same release gate.
