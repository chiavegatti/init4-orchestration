# UX/UI Governance — Authorization & Visibility Contracts
## ai.docs/ux-ui/governance

This directory defines the **governance layer of the UX/UI system**.

It exists to ensure that:
- UI behavior reflects authorization rules
- data exposure is intentional and auditable
- permissions are consistently understood across UI, API and schema
- no action or data is exposed by accident

These documents are **authoritative contracts**, not references.

---

## 1) What UX/UI Governance Is

UX/UI governance defines:
- who can see what
- who can do what
- where actions are exposed
- how permissions translate into UI behavior

It sits between:
- Security & RBAC (backend rules)
- UX/UI (visual and interaction layer)

Governance ensures both layers stay aligned.

---

## 2) What This Directory Is NOT

This directory does NOT:
- define visual design
- define layout or components
- define business logic
- replace backend authorization

Those concerns live in:
- Design System (`design-system.md`)
- Wireframes (`wireframes/`)
- PRD (`ai.docs/03_PRD.md`)
- Security & Compliance (`ai.docs/05_SECURITY_AND_COMPLIANCE.md`)

---

## 3) Files and Responsibilities

### 🔐 access-control-matrix.md
**Role → Permission contract**

Defines:
- which roles exist
- which permissions each role has

Rules:
- No UI or API action exists without a permission
- Roles must be explicitly mapped to permissions

This file is the **foundation of RBAC**.

---

### 👁️ data-visibility-matrix.md
**Permission → Data visibility contract**

Defines:
- which data fields are visible
- under which permissions
- per role or permission level

Rules:
- Data visibility is independent from actions
- Read access does NOT imply edit access
- Sensitive data must be explicitly allowed

This file prevents **overexposure of data**.

---

### 🌐 api-exposure-matrix.md
**Permission → API exposure contract**

Defines:
- which API endpoints are exposed
- under which permissions
- for which roles

Rules:
- UI MUST NOT call endpoints not exposed here
- API exposure must match backend authorization
- UI exposure must match API exposure

This file aligns **UI behavior with API reality**.

---

### 📚 permission-glossary.md
**Permission semantics contract**

Defines:
- the meaning of each permission
- naming conventions
- intended scope and usage

Rules:
- Permissions must be named consistently
- Permissions must describe capability, not UI elements
- Ambiguous permissions are forbidden

This file is the **semantic source of truth** for permissions.

---

## 4) Relationship with Other UX/UI Contracts

These governance files work together with:

- UX Matrix (`ux-matrix.md`)
  → screens × actions × permissions

- Permission-Aware UI (`permission-aware-ui.md`)
  → visual behavior when permissions apply

- UI States (`ui-states.md`)
  → disabled / read-only / hidden behavior

Governance defines **what is allowed**.  
UX defines **how it is presented**.

---

## 5) Order of Authority (Mandatory)

When conflicts exist, the following order applies:

1. Security & Compliance (`ai.docs/05_SECURITY_AND_COMPLIANCE.md`)
2. Access Control Matrix
3. Data Visibility Matrix
4. API Exposure Matrix
5. UX Matrix
6. Permission-Aware UI
7. Visual UX/UI

Security always wins over UX convenience.

---

## 6) Change Governance Rules

Any change to governance documents requires:

- Review of affected UX screens
- Review of affected API contracts
- Update to `ux-matrix.md`
- ADR if permission model changes

Changes must be:
- explicit
- documented
- intentional

---

## 7) AI Usage Rules (Mandatory)

When generating UI, flows or interactions:

- Always consult governance documents first
- Never infer permissions or visibility
- Never expose data “because it exists”
- Stop and ask if a mapping is missing

Violating governance contracts is considered a system failure.

---

## 8) Scope Reminder

This directory exists to:
- prevent security leaks
- prevent UX inconsistency
- prevent accidental privilege escalation

It is intentionally strict.
