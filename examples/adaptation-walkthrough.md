# Example: One Small Adaptation

This example shows what a safe adaptation looks like.

## Starting Point

Default domain:

```text
fictional ACME Life customer-service FAQ
```

Target domain:

```text
fictional employee benefits FAQ
```

## Before

```csv
FAQ-001,billing,Can I change my billing date?,...
```

## After

```csv
FAQ-001,benefits,Can I change my benefit contribution date?,"In this fictional benefits sample, employees can request one contribution-date change per quarter before payroll cutoff.","Owner: benefits operations. Confirm policy before real use."
```

## Golden Set Update

```json
{"id":"G001","question":"Can I change my benefit contribution date?","expected_source_id":"FAQ-001","must_include":["contribution-date change","per quarter"]}
```

## Codex Prompt

```text
Adapt FAQ-001 to a fictional employee benefits contribution-date question.
Update the golden set, validation log, and handoff.
Use synthetic data only.
Run make validate.
```

## Expected Evidence

```text
make test: pass
make eval: pass
make validate: pass
```

## Handoff Update

The handoff should name:

- business owner
- data owner
- compliance or policy reviewer
- technical maintainer
- production blockers

## What This Proves

It proves the builder changed data and validation together.

It does not prove production readiness, legal correctness, privacy approval, or customer-service quality.
