# Permission-Aware UI — Visual Authorization Contract
## ai.docs/ux-ui/permission-aware-ui.md

This document defines how the UI MUST behave when permissions restrict actions or data.

Permissions are enforced at backend level.
This document defines the **visual and interaction behavior** in response to permissions.

---

## 1) Purpose

Permission-aware UI exists to:
- prevent misleading interfaces
- reduce user frustration
- align UI behavior with backend authorization
- make access rules explicit and auditable

Hiding UI elements alone is NOT authorization.

---

## 2) Canonical Rules (Non-Negotiable)

- Backend authorization is the source of truth
- UI MUST reflect permission state accurately
- UI MUST NOT expose unavailable actions
- UI MUST NOT guess permissions

Permissions are defined in:
- `ai.docs/data-base-schemas/permissions.md`
- `ai.docs/ux-ui/ux-matrix.md`

---

## 3) Visibility Strategies (Mandatory)

### 3.1 Hide
Use when:
- action existence itself is sensitive
- user should not be aware of the capability

Examples:
- platform-only actions
- administrative controls

---

### 3.2 Disable
Use when:
- action exists conceptually
- user lacks permission to execute it

Rules:
- Disabled state must follow `ui-states.md`
- Explanation SHOULD be provided

---

### 3.3 Read-Only
Use when:
- data visibility is allowed
- data modification is not

Rules:
- Fields remain visible
- Editing affordances removed or disabled
- No misleading affordance (e.g. editable cursor)

---

## 4) Permission-Based Feedback

When permission blocks an action:

- Do NOT show generic errors
- Do NOT rely on backend error alone
- UI SHOULD explain:
  - what is blocked
  - why (in generic terms)
  - how to proceed (if applicable)

Tone:
- neutral
- non-judgmental
- non-technical

---

## 5) Relationship with UX Matrix

Every UI action MUST:

- Exist in `ux-matrix.md`
- Map to one or more permissions
- Match the API behavior

If a UI action exists but is missing from the matrix:
- STOP implementation
- Update the matrix first

---

## 6) Accessibility Requirements

Permission states MUST be accessible:

- Disabled elements must not receive focus
- Read-only fields must be announced correctly
- Hidden elements must not be announced
- Explanations must be readable by screen readers

---

## 7) Anti-Patterns (Forbidden)

- Hiding errors caused by missing permission
- Showing enabled controls that fail silently
- Relying on HTTP 403 as UX explanation
- Inconsistent behavior across screens

---

## 8) Enforcement Rules

- UI that violates permission behavior is INVALID
- Deviations require documentation and approval
- Security rules override UX convenience

---

## 9) Scope Reminder

This document defines **visual and interaction behavior**.

It does NOT:
- define permission logic
- define role hierarchy
- replace backend authorization
