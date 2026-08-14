# Production Bridge

Use this document when a PM, CPO, or enterprise reviewer is deciding whether a
public synthetic fieldkit should become a private internal adaptation.

The public fieldkit is a learning and prototyping surface. It is not production
software. Production use starts only after ownership, data, compliance,
operations, and technical controls are approved.

## Bridge Path

1. Keep the public repo synthetic.
   Do not replace public examples with private data, client names, screenshots,
   internal links, support tickets, or copied policy documents.

2. Create a private adaptation space.
   Use a private repository or approved internal workspace with branch review,
   access control, secret handling, and a named maintainer.

3. Map the synthetic example to the real workflow.
   Define the business outcome, target users, allowed questions, excluded
   questions, source systems, and human fallback path before connecting data.

4. Approve the data boundary.
   The data owner must approve exact sources, fields, freshness expectations,
   prohibited fields, retention period, and whether any personal or regulated
   data is allowed.

5. Add production controls before pilot use.
   Auth, logging, monitoring, escalation, incident response, auditability, and
   model/API cost boundaries must be designed before users rely on the agent.

6. Promote only with evidence.
   A demo, test pass, or workshop handoff is not enough. Promotion requires
   signed-off ownership gates, evaluated behavior, support readiness, and a
   rollback or disable path.

## Ownership Gates

| Gate | Required decision | Minimum evidence |
|---|---|---|
| Business owner | Approves the user problem, production scope, success metric, risk appetite, and stop conditions. | PRD, decision note, or launch approval. |
| Data owner | Approves data sources, fields, access level, retention, and prohibited data. | Data inventory and approval record. |
| Compliance/privacy | Reviews privacy, regulatory, vendor, disclosure, and sensitive-data handling requirements. | Review note with unresolved risks listed. |
| Support operations | Owns user support, human escalation, operating hours, response expectations, and customer-facing copy. | Support runbook and escalation path. |
| Technical maintainer | Owns repository, deployment, auth, secrets, logs, monitoring, incident response, and rollback. | Architecture note, runbook, and on-call or maintainer assignment. |

## Production Controls

| Control | Minimum requirement before production |
|---|---|
| Data approval | Approved source list, field list, data classification, freshness rules, and data minimization. |
| Auth and access | Role-based access, least privilege, account lifecycle process, and no shared credentials. |
| Logging | Structured logs with request ids, redaction of sensitive content, and clear access controls. |
| Retention | Defined retention period for prompts, outputs, logs, eval records, and user feedback. |
| Monitoring | Health, latency, error rate, refusal/escalation rate, cost, and quality signals. |
| Human escalation | Clear handoff trigger, owner, queue, SLA or response expectation, and user-facing message. |
| Incident response | Severity levels, owner, disable path, notification process, evidence capture, and post-incident review. |
| Auditability | Traceable approvals, dataset versions, prompt/config versions, eval results, releases, and operator actions. |
| Model/API cost boundary | Approved provider/model, budget owner, rate limits, per-user or per-team caps, and alert thresholds. |

## Not Production-Ready Until

- [ ] A business owner has approved the production use case, success metric, and stop conditions.
- [ ] A data owner has approved exact data sources, fields, retention, and prohibited data.
- [ ] Compliance/privacy has reviewed sensitive-data handling and unresolved risks.
- [ ] Authentication and role-based access are implemented for the real user group.
- [ ] Secrets and API keys are stored in an approved secret manager or deployment environment.
- [ ] Logs are structured, redacted, access-controlled, and tied to request ids.
- [ ] Retention rules exist for prompts, outputs, logs, eval records, and feedback.
- [ ] Monitoring covers health, errors, latency, quality, escalation, and model/API cost.
- [ ] Human escalation is staffed and visible to users.
- [ ] Incident response has an owner, severity model, disable path, and evidence process.
- [ ] Audit records can connect approvals, data versions, config versions, evals, and releases.
- [ ] Model/API usage has an approved budget owner, caps, and alerts.
- [ ] Golden-set evals include approved internal scenarios and known failure cases.
- [ ] Support operations has a runbook and user-facing fallback language.
- [ ] The technical maintainer can deploy, roll back, rotate secrets, and explain current risk.

## Public-to-Private Rule

Private adaptations may borrow structure from this fieldkit, but private facts
must stay private. If a learning from the private adaptation returns to the
public fieldkit, convert it back into a fictional, synthetic, non-identifying
pattern before publishing.
