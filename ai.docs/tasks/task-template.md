# Task Template — AI Execution Unit
## ai.docs/tasks

This template defines a **single, atomic unit of work** to be executed with AI assistance.

A task:
- has one clear objective
- has explicit scope boundaries
- references authoritative documents
- produces verifiable outcomes

This file is copied to create new tasks.
Do NOT edit this template directly.

---

## Roadmap Reference (Mandatory)

Every task MUST reference exactly one roadmap item.

Format:
- Roadmap Item ID or Title:
- Roadmap Phase (if applicable):

Example:
- Roadmap Item: Phase 2 — Client Management
- Roadmap Phase: Core CRM

Tasks without a roadmap reference are INVALID.


## 1. Task Identification
- ID: TASK-YYYY-MM-DD-XXX
- Title: Short, clear, action-oriented title

---

## 2. Objective (Mandatory)
Describe **one single objective** this task must achieve.

Rules:
- No multiple goals
- No vague intentions
- No future work

---

## 3. Scope Definition (Mandatory)

### In Scope
Explicitly list what this task includes.

### Out of Scope
Explicitly list what this task does NOT include.

If something is not listed as in scope, it is out of scope by default.

---

## 4. Required References (Mandatory)

List the ai.docs files that MUST be consulted before execution.

Example:
- Context: ai.docs/02_CONTEXT.md
- PRD: ai.docs/03_PRD.md (sections X, Y)
- Architecture: ai.docs/04_ARCHITECTURE.md
- Security: ai.docs/05_SECURITY_AND_COMPLIANCE.md
- Data Schema: ai.docs/data-base-schemas/schema.md
- API Contracts: ai.docs/07_API_CONTRACTS.md
- ADRs: ai.docs/09_DECISIONS_ADR.md (if any)

If a required document does not exist, STOP execution.

---

## 5. Impact Analysis (Mandatory)

Answer explicitly:

- Data model changes?
  - [ ] No
  - [ ] Yes → list entities and update schemas

- API contract changes?
  - [ ] No
  - [ ] Yes → specify endpoints and versions

- UX impact?
  - [ ] No
  - [ ] Yes → reference UX docs

- Security or permission impact?
  - [ ] No
  - [ ] Yes → specify rules affected

- ADR required?
  - [ ] No
  - [ ] Yes → decision must be recorded before execution

---

## 6. Functional Requirements
List concrete, testable requirements.

Format:
- FR-01:
- FR-02:

---

## 7. Non-Functional Requirements
List constraints:
- performance
- security
- compliance
- observability
- accessibility (if applicable)

---

## 8. Acceptance Criteria (Definition of Done)

This task is DONE only if:

- [ ] Objective achieved
- [ ] Scope respected
- [ ] Schema/API/UX updated if impacted
- [ ] Tests added or updated
- [ ] Security rules respected
- [ ] Release checklist impact evaluated
- [ ] Memory entry created (if corrections occurred)

---

## 9. Implementation Notes (Optional)
Clarifications, constraints, or known edge cases.

---

## 10. Test Plan (Mandatory)
Describe:
- what is tested
- key scenarios
- failure cases

---

## 11. Rollback & Safety
Describe:
- rollback strategy
- feature flags (if any)
- blast radius

---

## 12. Post-Execution Memory (Mandatory if issues occurred)

If AI output required correction:
- create a memory entry in `ai.docs/memories/`
- distill the rule into `lessons-learned.md`
