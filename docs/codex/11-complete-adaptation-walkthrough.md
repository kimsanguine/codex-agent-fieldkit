# 11. Complete Adaptation Walkthrough

This walkthrough shows the full loop for a small fictional adaptation:

```text
change synthetic FAQ -> run eval -> see intentional failure -> diagnose -> fix -> update evidence and handoff
```

The goal is not a perfect chatbot. The goal is a visible operating loop that a PM, CPO, operator, or non-engineer builder can review.

## Scenario

Adapt FAQ Agent Lite from fictional customer-service FAQs to fictional employee benefits FAQs.

Do not use real HR, employee, claim, payroll, or benefits data. Keep all examples fictional and safe to publish.

## Step 1: Fresh Clone

```bash
git clone https://github.com/kimsanguine/codex-agent-fieldkit.git
cd codex-agent-fieldkit
make validate
```

Expected output:

```text
eval score: 100.00% (20/20)
secret scan: pass
private term scan: pass
public link scan: pass
```

What this proves:

```text
The starting kit is clean before the adaptation.
```

What it does not prove:

```text
The future benefits adaptation is correct.
```

## Step 2: Codex Health Check

Prompt:

```text
Confirm the current folder. Read README.md, AGENTS.md, and starter-kits/faq-agent-lite/README.md.
Summarize what files must change together when adapting the starter kit.
Do not edit files yet.
```

Expected response:

```text
Data, tests, golden set, validation_log.md, and handoff.md should move together.
```

For this walkthrough, the main files are:

```text
starter-kits/faq-agent-lite/data/sample_faqs.csv
starter-kits/faq-agent-lite/tests/golden_set.jsonl
starter-kits/faq-agent-lite/docs/validation_log.md
starter-kits/faq-agent-lite/_handoff/handoff.md
```

## Step 3: Change One Synthetic FAQ

Ask Codex to change one FAQ row or add one new row:

```text
Add one fictional employee benefits FAQ about changing a benefit contribution date.
Use synthetic ACME Benefits data only.
Do not use real HR, employee, claim, payroll, or benefits data.
Do not update validation_log.md or handoff.md until after eval has run.
```

Expected FAQ row shape:

```csv
FAQ-021,benefits,Can I change my benefit contribution date?,"In this fictional benefits sample, employees can request one contribution-date change per quarter before payroll cutoff.","Owner: benefits operations. Confirm policy before real use."
```

Product decision captured in the row:

```text
The intended fictional policy is "one contribution-date change per quarter."
```

That sentence matters. It is the local source of truth for the next diagnosis step.

## Step 4: Add An Intentional Eval Failure

Now add golden-set rows that point to the new FAQ but intentionally expect the wrong policy phrase.

Prompt:

```text
Add three golden-set cases for FAQ-021.
Intentionally make them fail by expecting the phrase "twice per year" even though the FAQ says "per quarter."
This is a training failure so we can practice diagnosis.
```

Expected `golden_set.jsonl` additions:

```json
{"id":"G021","question":"Can I change my benefit contribution date?","expected_source_id":"FAQ-021","must_include":["twice per year"]}
{"id":"G022","question":"How often can I move my benefits contribution date?","expected_source_id":"FAQ-021","must_include":["twice per year"]}
{"id":"G023","question":"Can payroll move my contribution date this month?","expected_source_id":"FAQ-021","must_include":["twice per year"]}
```

This is intentionally wrong. Do not ship this state.

## Step 5: Run Eval And Read The Failure

```bash
make eval
```

Expected output:

```text
FAIL G021 expected=FAQ-021 actual=FAQ-021
FAIL G022 expected=FAQ-021 actual=FAQ-021
FAIL G023 expected=FAQ-021 actual=FAQ-021
eval score: 86.96% (20/23)
Eval score below threshold: 86.96% < 90%
```

If you run from the repo root, `make` may also print wrapper lines like:

```text
make -C starter-kits/faq-agent-lite eval
make[1]: *** [eval] Error 1
make: *** [eval] Error 2
```

For a non-engineer reviewer, the important part is this:

```text
expected=FAQ-021 actual=FAQ-021
```

The agent found the intended FAQ. The failing part is the required answer phrase.

## Step 6: Diagnose Data, Golden Set, Or Retrieval

Ask Codex to explain the failure before fixing it:

```text
The eval failed for G021-G023.
Diagnose whether the FAQ data, golden set, or retrieval behavior is wrong.
Use only the synthetic FAQ row and these golden-set cases.
Do not weaken the eval just to make it pass.
Return the smallest safe fix.
```

Use this diagnosis table:

| Eval signal | Likely issue | PM/CPO question | Smallest safe fix |
|---|---|---|---|
| `expected=FAQ-021 actual=FAQ-021`, but status is `FAIL` | Required phrase does not appear in the answer | Which policy is intended: `per quarter` or `twice per year`? | Fix the golden set if the FAQ is right; fix the FAQ if the golden set is right |
| `expected=FAQ-021 actual=NO_MATCH` | Retrieval missed the new FAQ | Does the FAQ include the words users actually ask? | Add synthetic user wording to the FAQ question or answer |
| `expected=FAQ-021 actual=FAQ-009` | Retrieval selected a different FAQ | Are two rows competing for the same wording? | Clarify category, question, or answer text |
| Several unrelated cases fail | The adaptation changed shared behavior | Did we touch code or broad data by accident? | Revert only the accidental local change, then rerun eval |

The correct diagnosis for this walkthrough:

```text
The golden set is wrong. It expects "twice per year," but the intended fictional FAQ policy is "per quarter."
```

## Step 7: Fix The Smallest Wrong Artifact

Prompt:

```text
Fix G021-G023 so they match the intended fictional policy: one contribution-date change per quarter.
Do not change the FAQ answer unless the policy decision changes.
Rerun make eval.
```

Expected fixed golden-set rows:

```json
{"id":"G021","question":"Can I change my benefit contribution date?","expected_source_id":"FAQ-021","must_include":["contribution-date change","per quarter"]}
{"id":"G022","question":"How often can I move my benefits contribution date?","expected_source_id":"FAQ-021","must_include":["contribution-date change","per quarter"]}
{"id":"G023","question":"Can payroll move my contribution date this month?","expected_source_id":"FAQ-021","must_include":["contribution-date change","per quarter"]}
```

Run the failed check first:

```bash
make eval
```

Expected output:

```text
PASS G021 expected=FAQ-021 actual=FAQ-021
PASS G022 expected=FAQ-021 actual=FAQ-021
PASS G023 expected=FAQ-021 actual=FAQ-021
eval score: 100.00% (23/23)
```

Then run the broader gate:

```bash
make validate
```

Expected output:

```text
Ran 6 tests in 0.00s
OK
eval score: 100.00% (23/23)
secret scan: pass
```

## Step 8: Update Validation Log

Update:

```text
starter-kits/faq-agent-lite/docs/validation_log.md
```

Expected entry:

```markdown
| 2026-06-22 | `make eval` | Failed, then passed | First run failed G021-G023 because the golden set expected `twice per year`; corrected to the intended synthetic policy `per quarter`; final score 100% (23/23) | Fictional benefits adaptation only |
| 2026-06-22 | `make validate` | Passed | Tests, eval, and safety scans passed after the golden-set fix | Not production-ready; synthetic data only |
```

Why this matters:

```text
A future reviewer can see not only the green result, but also what failed and why it was safe to fix.
```

## Step 9: Update Handoff

Update:

```text
starter-kits/faq-agent-lite/_handoff/handoff.md
```

Expected handoff notes:

```markdown
## Latest Adaptation

- Added fictional ACME Benefits contribution-date FAQ.
- Added G021-G023 to cover direct, paraphrased, and payroll-adjacent wording.
- Eval intentionally failed first because the golden set expected `twice per year`.
- Diagnosis: retrieval selected the right FAQ; the golden set phrase was inconsistent with the intended synthetic policy.
- Fix: changed G021-G023 to require `contribution-date change` and `per quarter`.

## Production Status

Not production-ready. The data is synthetic, the policy is fictional, and no real benefits, legal, privacy, or support owner has approved it.
```

The handoff should also name the next reviewers:

- business owner
- data owner
- compliance or privacy reviewer
- support operations owner
- technical maintainer

## Step 10: Final Gate

```bash
make validate
git diff --stat
```

Expected result:

```text
make validate passes
only intended files changed
validation_log.md records failed-then-passed evidence
handoff.md says not production-ready
```

Expected changed files for the fictional adaptation:

```text
starter-kits/faq-agent-lite/data/sample_faqs.csv
starter-kits/faq-agent-lite/tests/golden_set.jsonl
starter-kits/faq-agent-lite/docs/validation_log.md
starter-kits/faq-agent-lite/_handoff/handoff.md
```

## Done Means

The adaptation is complete only when another person can clone the repo, run the commands, and understand:

- what synthetic FAQ changed
- what eval failed
- whether the failure was data, golden set, or retrieval
- what was fixed
- what was verified after the fix
- why the handoff is still not production-ready
