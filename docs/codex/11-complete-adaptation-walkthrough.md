# 11. Complete Adaptation Walkthrough

This walkthrough shows the full loop for a small fictional adaptation.

## Scenario

Adapt FAQ Agent Lite from fictional customer-service FAQs to fictional employee benefits FAQs.

Do not use real HR, employee, claim, or benefits data.

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

## Step 3: Make One Safe Change

Prompt:

```text
Change one FAQ row to a fictional employee benefits question.
Use synthetic data only.
Update golden_set.jsonl with one matching case.
Run make eval.
```

Expected changed files:

```text
starter-kits/faq-agent-lite/data/sample_faqs.csv
starter-kits/faq-agent-lite/tests/golden_set.jsonl
```

## Step 4: Interpret Failure

If eval fails:

```text
FAIL G021 expected=FAQ-006 actual=NO_MATCH
```

Ask:

```text
Explain whether the failure comes from the FAQ data, retrieval synonyms, or golden-set wording.
Make the smallest fix and rerun make eval.
```

## Step 5: Update Evidence

Update:

```text
starter-kits/faq-agent-lite/docs/validation_log.md
starter-kits/faq-agent-lite/_handoff/handoff.md
```

Evidence should include:

- command
- result
- score
- known limitation
- owner or next reviewer

## Step 6: Final Gate

```bash
make validate
git diff --stat
```

Expected result:

```text
make validate passes
only intended files changed
handoff says not production-ready
```

## Done Means

The adaptation is complete only when another person can clone the repo, run the commands, and understand what was verified.
