# Lessons Learned
## Human ↔ AI Operational Memory

This document consolidates **recurring corrections and learnings** identified during AI-assisted development.

Its purpose is to:
- reduce repeated mistakes
- reinforce correct patterns
- act as a pre-flight checklist for future work

This file is **append-only**.

---

## How to Use (Mandatory)

- Review this file before starting a new task with AI
- Update it when a mistake is corrected more than once
- Prefer rules over explanations
- Keep entries short and precise

---

## Canonical Rules

### Architecture & Scope
- Never implement behavior not explicitly defined in the PRD.
- Architectural assumptions require an ADR.
- If scope is unclear, stop and ask.

### Data & Schema
- Never invent fields or relationships.
- Schema is the source of truth for APIs and UX.
- Always validate tenant scoping (`company_id`).

### API Contracts
- No endpoint without a documented contract.
- API responses must not include undocumented fields.
- Breaking changes require versioning.

### UX
- UX must reflect permissions, not guess them.
- No screen exists without API backing and permission mapping.
- Data visibility must be explicit.

### Security
- Authorization is enforced at API level, not UI.
- Audit all permission and role changes.
- Never trust client-side validation.

---

## Project-Specific Learnings

(Add new items below as they emerge)

- YYYY-MM-DD — Short rule describing the learning.
- YYYY-MM-DD — Short rule describing the learning.
