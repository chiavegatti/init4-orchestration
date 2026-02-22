# AI Execution Contract
## ai.docs — Project Rules for LLMs (Mandatory)

This file is the **primary operational contract** for any AI/LLM assisting in the **INIT4 Cognitive Orchestrator MVP** repository.

It defines:
- how to interpret the documentation
- what you are allowed to do
- what you MUST NOT do
- how to proceed when information is missing

If you violate this contract, your output is considered unreliable.

---

## 0) Golden Rule

If something is not explicitly defined in the documentation, **DO NOT invent it**.

This applies strictly to the Cognitive Orchestrator: **Do not assume generic agentic behaviors, automatic heuristics, or complex capabilities unless documented.** The orchestrator is a deterministic routing and policy engine.

When in doubt:
- stop
- list what is missing
- propose the minimum set of questions or the minimum missing artifacts needed

---

## 1) Canonical Source of Truth

The canonical documentation system lives at:

ai.docs/

The execution order is defined by the numbered documents in `ai.docs/`.
You MUST follow that order and treat it as causal dependency.

---

## 📌 Always read before coding (Mandatory)

Before generating, modifying or suggesting any code, you MUST review:

ai.docs/memories/lessons-learned.md

This file contains validated corrections and recurring learnings.
If a rule exists there, it OVERRIDES assumptions, heuristics, or default behavior.

Failure to follow this step is a contract violation.

---

## 2) Canonical Execution Order (Mandatory)

You MUST follow the documents in this order:

1. ai.docs/01_README_AI.md (this contract)
2. ai.docs/02_CONTEXT.md
3. ai.docs/03_PRD.md
4. ai.docs/04_ARCHITECTURE.md
5. ai.docs/05_SECURITY_AND_COMPLIANCE.md
6. ai.docs/06_BOILERPLATE_STRUCTURE.md
7. ai.docs/07_API_CONTRACTS.md
8. ai.docs/08_DATA_SCHEMA.md
9. ai.docs/09_DECISIONS_ADR.md
10. ai.docs/10_UX_UI_INDEX.md
11. ai.docs/11_ROADMAP.md
12. ai.docs/12_RELEASE_CHECKLIST.md

Rule:
- You must not implement “downstream” items if “upstream” definitions are missing.

---

## 3) Contract-First Development Rules

### 3.1 Schema-First
- Data models MUST exist before APIs and UX.
- Never invent tables, fields, types, relationships or constraints.
- The master index is: ai.docs/data-base-schemas/schema.md

### 3.2 API Contract-First
- No endpoint may exist without a documented contract.
- No response may include undocumented fields.
- Breaking changes require versioning and an ADR.

### 3.3 UX is a Functional Contract
- UX is not “design”; it is an access and behavior contract.
- No screen exists without:
  - permission mapping
  - data visibility rules
  - API backing

---

## 4) Security & Multi-Tenancy Rules (Non-Negotiable)

Security constraints are defined in:
ai.docs/05_SECURITY_AND_COMPLIANCE.md

Minimum mandatory rules:
- Tenant isolation is enforced at API level
- RBAC is mandatory
- Never trust client-side validation
- Audit sensitive actions
- Never leak sensitive details in errors or logs

If any requirement conflicts with security rules, security wins by default.

---

## 5) Non-Hallucination Rules (Mandatory)

You MUST NOT:
- create new requirements
- create new entities or fields not documented
- assume workflows, statuses, permissions, or roles beyond what is defined
- “fill gaps” with typical patterns unless explicitly approved
- assume or implement agentic flows or autonomous decision-making loops where deterministic routing is specified

If you detect missing definitions:
- list missing items explicitly
- propose the smallest additions needed to proceed
- stop code generation until definitions are provided or confirmed

---

## 6) Output Format Rules (How you respond)

When producing actionable output, structure it as:

1) Assumptions (only if explicitly permitted)
2) Inputs used (which ai.docs files informed the output)
3) Proposed changes (bulleted, minimal and precise)
4) Artifacts to create/update (file paths)
5) Risks / checks (tests, edge cases, release checklist impact)

Do not dump large code blocks unless:
- contracts exist (schema + API)
- the change is within defined scope
- tests are included or specified

---

## 7) Change Governance

If a change affects any of the following:
- architecture boundaries
- repo structure
- security posture
- data model fundamentals
- API versioning strategy
- execution order / workflow of ai.docs

Then it requires an ADR in:
ai.docs/09_DECISIONS_ADR.md

ADR rules:
- append-only
- do not edit accepted decisions
- supersede with a new ADR if needed

---

## 8) Definition of “Done” (Mandatory)

Work is not “done” unless:
- PRD matches behavior
- schema matches implementation
- API contracts match implementation
- UX mapping exists and matches permissions
- tests pass and quality gates are met
- release checklist items are satisfied

Canonical gate:
ai.docs/12_RELEASE_CHECKLIST.md

---

## 9) Repository Structure Rules

The canonical repo layout is defined in:
ai.docs/06_BOILERPLATE_STRUCTURE.md

Key rule:
- ai.docs/ always lives at repository root
- documentation stays inside ai.docs/
- code lives under approved app directories (e.g., apps/)
- ops/infrastructure lives under ops/ (if used)

Do not move ai.docs files or renumber them.

---

## 10) Memory System Rules (Mandatory)

The memory system exists to prevent repeat failures.

Location:
ai.docs/memories/

Files:
- ai.docs/memories/lessons-learned.md (append-only distilled rules)
- ai.docs/memories/memory-template.md (used to create new memory entries)

Memory entry naming convention:
YYYY-MM-DD__short-title.md

If a mistake repeats or a correction becomes important:
- create a memory entry
- distill the rule into lessons-learned.md

---

## 11) Quick Pre-Flight Checklist (Before producing code)

Before outputting any implementation:

- [ ] I read ai.docs/memories/lessons-learned.md
- [ ] PRD defines the behavior
- [ ] Schema defines the fields and relationships
- [ ] API contracts define request/response payloads
- [ ] UX mapping exists (if UI changes)
- [ ] Security constraints are satisfied
- [ ] ADR exists for structural decisions
- [ ] Tests and release checklist impact are considered

If any item is false, stop and request the missing definition(s).

---

## 12) Scope Reminder

This contract exists to ensure:
- predictable execution
- minimal ambiguity
- safe and consistent outputs

It is intentionally strict.
The goal is reliability, not improvisation.