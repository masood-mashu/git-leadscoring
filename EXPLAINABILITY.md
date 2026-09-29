# Explainability, Auditability & Decision Logic: GitLeadScoring

This document details the transparent decision architecture, algorithmic criteria, data provenance, and operational boundaries of **GitLeadScoring**, ensuring complete compliance with OpenGAP standards and Checkpoint 02 requirements.

---

## 1. Input Data and Data Sources Used

**GitLeadScoring** ingests structured, machine-verifiable data artifacts from well-defined sources to ensure total repeatability:
- **Inbound**: Inbound demo request forms and enterprise content download events.
- **B2B**: B2B firmographic enrichment feeds (Clearbit, ZoomInfo, Apollo).
- **Intent**: Intent surveillance signals (Bombora, G2 Crowd product page comparisons).
- **OpenGAP Specification Manifests**: Ingests `agent.yaml`, `RULES.md`, and local state from `memory/MEMORY.md`.

All data sources are parsed deterministically without dynamic external unverified calls, ensuring that evaluations reflect the exact state of the repository at the moment of inspection.

---

## 2. How It Decides and Reasoning Process

The decision pipeline operates through a multi-stage validation sequence designed to eliminate subjective ambiguity:

1. **Syntax & Schema Verification**: Ingested inputs are first validated against strict JSON and YAML schemas defined in `tools/`. Any malformed payloads are immediately rejected.
2. **Deterministic Metric Extraction**:
   - **score_icp_fit**: Uses `icp-fit-scorer` to calculate evaluates enterprise company size and revenue against ideal customer profile tiers.
   - **classify_behavioral_intent**: Uses `behavioral-intent-classifier` to calculate calculates composite buyer intent score from multi-touch website interactions.
   - **route_sales_lead**: Uses `sdr-routing-engine` to calculate assigns lead to specialized enterprise account executive or inbound sdr queue.
3. **Policy Boundary Checks**: Extracted metrics are evaluated against the non-negotiable rules defined in `RULES.md`.
4. **Verdict Synthesis**:
   - **`APPROVED`**: Issued when all criteria strictly pass thresholds, zero compliance violations are detected, and data integrity is certified.
   - **`NEEDS_REVIEW`**: Issued when borderline metrics or ambiguous edge cases require human supervisor assessment.
   - **`BLOCKED`**: Issued immediately upon detecting any violation of zero-tolerance rules, severe risk factors, or non-compliant parameters.

When an inbound lead is ingested, the agent executes icp_fit_scorer, behavioral_intent_classifier, and sdr_routing_engine. If ICP is Tier 1 and intent is High, it issues APPROVED. If firmographics match but intent is cold, it issues NEEDS_REVIEW. If invalid contact data or competitor IP is identified, it issues BLOCKED.

---

## 3. Constraints, Limitations, and Known Issues

To ensure reliable and safe operation, the following constraints and operational boundaries apply:
- **Operates**: Operates deterministically (temperature = 0.1) based on firmographic scoring matrices.
- **Requires**: Requires verified corporate email domain to initiate enterprise enrichment pipelines.
- **Complies**: Complies with global anti-spam mandates (CAN-SPAM, CASL).
- **Deterministic Execution Constraint**: All model prompts and evaluations must run with low temperature (`0.1`) to ensure predictable, reproducible scoring and eliminate hallucinated findings.
- **Human Authority**: The agent cannot self-execute irreversible external mutations; final approval is reserved strictly for human authorities as specified in `DUTIES.md`.
