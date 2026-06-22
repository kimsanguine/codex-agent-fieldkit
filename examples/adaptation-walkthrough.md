# Example: One Small Adaptation

This example shows a safe adaptation with one intentional eval failure and fix.

The point is not to make the agent impressive. The point is to make the change, the evidence, and the handoff move together.

## Starting Point

Default domain:

```text
fictional ACME Life customer-service FAQ
```

Target domain:

```text
fictional ACME Benefits employee FAQ
```

Use synthetic data only. Do not use real employee, HR, payroll, claim, or benefits data.

## Step 1: Change One Synthetic FAQ

Before:

```csv
FAQ-001,billing,Can I change my billing date?,...
```

After:

```csv
FAQ-021,benefits,Can I change my benefit contribution date?,"In this fictional benefits sample, employees can request one contribution-date change per quarter before payroll cutoff.","Owner: benefits operations. Confirm policy before real use."
```

Run the eval before declaring the adaptation ready:

```bash
make eval
```

## Step 2: Create An Intentional Golden-Set Failure

For practice, add three synthetic golden-set cases that intentionally expect the wrong policy phrase:

```json
{"id":"G021","question":"Can I change my benefit contribution date?","expected_source_id":"FAQ-021","must_include":["twice per year"]}
{"id":"G022","question":"How often can I move my benefits contribution date?","expected_source_id":"FAQ-021","must_include":["twice per year"]}
{"id":"G023","question":"Can payroll move my contribution date this month?","expected_source_id":"FAQ-021","must_include":["twice per year"]}
```

Expected eval output:

```text
FAIL G021 expected=FAQ-021 actual=FAQ-021
FAIL G022 expected=FAQ-021 actual=FAQ-021
FAIL G023 expected=FAQ-021 actual=FAQ-021
eval score: 86.96% (20/23)
Eval score below threshold: 86.96% < 90%
```

This is a useful failure. The expected and actual source ids match, so retrieval found the right FAQ. The failure is in the required answer phrase.

## Step 3: Diagnose Before Fixing

Ask Codex:

```text
The benefits eval failed. Diagnose whether the data, golden set, or retrieval behavior is wrong.
Use the synthetic FAQ row and G021-G023 only.
Do not weaken the eval just to make it pass.
```

Use this decision table:

| Signal | Likely issue | Fix |
|---|---|---|
| `expected=FAQ-021 actual=FAQ-021` but row fails | Golden set phrase or answer wording is inconsistent | Align the golden set with the intended synthetic policy, or change the FAQ answer if the policy text is wrong |
| `actual=NO_MATCH` | Retrieval did not find the FAQ | Add user wording to the synthetic FAQ question or answer |
| `actual=FAQ-009` | Retrieval found the wrong FAQ | Clarify categories, question wording, or overlapping terms |
| The FAQ says one rule and the golden set says another | Product/data decision is unresolved | Pick the intended fictional policy before changing files |

## Step 4: Fix The Wrong Artifact

In this example, the intended fictional policy is "per quarter." The golden set is wrong because it expects "twice per year."

Fixed golden-set examples:

```json
{"id":"G021","question":"Can I change my benefit contribution date?","expected_source_id":"FAQ-021","must_include":["contribution-date change","per quarter"]}
{"id":"G022","question":"How often can I move my benefits contribution date?","expected_source_id":"FAQ-021","must_include":["contribution-date change","per quarter"]}
{"id":"G023","question":"Can payroll move my contribution date this month?","expected_source_id":"FAQ-021","must_include":["contribution-date change","per quarter"]}
```

Run the failed check again:

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

Then run the full gate:

```bash
make validate
```

Expected evidence:

```text
make test: pass
make eval: pass, 100.00% (23/23)
make validate: pass
```

## Step 5: Update Validation Log And Handoff

`docs/validation_log.md` should include the failure and the fix:

```markdown
| 2026-06-22 | `make eval` | Failed, then passed | First run failed G021-G023 because the golden set expected `twice per year`; corrected to the intended synthetic policy `per quarter`; final score 100% (23/23) | Fictional benefits adaptation only |
```

`_handoff/handoff.md` should tell the next owner what changed:

```markdown
- Added fictional benefits contribution-date FAQ.
- Verified eval failure diagnosis and fix loop.
- Current data is synthetic and not approved for production use.
- Next reviewer: benefits policy owner and compliance/privacy reviewer.
```

## Codex Prompt

```text
Adapt one FAQ row to a fictional employee benefits contribution-date question.
Add three golden-set cases.
First make the eval fail intentionally with an inconsistent expected phrase.
Diagnose whether data, golden set, or retrieval is wrong.
Fix the smallest wrong artifact.
Update validation_log.md and handoff.md with the failed-then-passed evidence.
Use synthetic data only.
Run make validate.
```

## What This Proves

It proves the builder changed data, evals, evidence, and handoff together.

It does not prove production readiness, legal correctness, privacy approval, HR policy correctness, or employee-service quality.
