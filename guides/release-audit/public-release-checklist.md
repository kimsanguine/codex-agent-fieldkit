# Public Release Checklist

Use this before pushing or announcing a public release.

## Required Commands

```bash
make validate
git status -sb
git diff --stat
```

## Local Release Candidate Gate

- [x] README explains the repo in 10 seconds.
- [x] Starter kit runs without an API key.
- [x] Tests pass locally.
- [x] Golden-set eval passes locally.
- [x] Safety scans pass locally.
- [x] Handoff package is current.
- [x] Examples are fictional or synthetic.
- [x] No private company/client names are present in the release candidate scan.
- [x] No local paths are present in the release candidate scan.
- [x] No internal URLs or QR links are present in the release candidate scan.
- [x] No `.env` file is tracked.
- [x] No screenshots with private UI are included.

## Claim Gate

- [x] Claims are framed as practice patterns, not endorsements.
- [x] Any "field-tested" wording is anonymized and non-client-specific.
- [x] The project says it is unofficial and not affiliated with OpenAI.
- [x] Limitations are visible.

## Post-Push Gate

- [x] GitHub Actions `ci` is green on the public repository.
- [x] Public repo description and topics are set.
- [x] Release audit is updated with public remote URL and initial public push commit.

## Release Decision

Release announcement should wait until the local gate and post-push gate are both checked.
