# Separation of Duties (SOD) & Operational Boundaries

To ensure robust compliance, security, and verification, **GitLeadScoring** implements a strict tripartite Separation of Duties architecture.

---

### 1. Maker
* **Assigned Entity**: `GitLeadScoring Automation Engine`
* **Responsibilities**:
  * Enriches corporate domain firmographics, computes engagement intent scores, and assigns target reps.
  * Ingests raw repository data, configurations, and input artifacts.
  * Formulates candidate evaluations and structured recommendation summaries.
  * Records execution logs into `memory/audit.log`.

---

### 2. Checker
* **Assigned Entity**: `GitLeadScoring Verification & Policy Enforcer`
* **Responsibilities**:
  * Validates lead routing deduplication against existing active CRM opportunity accounts.
  * Audits calculations, parameter boundary limits, and zero-tolerance rule compliance.
  * Asserts schema validity on all output manifests.
  * Issues preliminary assessment: `APPROVED`, `BLOCKED`, or `NEEDS_REVIEW`.

---

### 3. Approver
* **Assigned Entity**: `Head of Revenue Operations / VP of Sales (Reserved for human review).`
* **Responsibilities**:
  * Final sign-off authority for high-impact production actions.
  * Mandatory human oversight on security, legal, financial, or regulatory decisions.
  * Reviews unresolvable edge cases and policy override exceptions.
