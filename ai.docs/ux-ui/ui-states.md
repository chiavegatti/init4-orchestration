# UI States — Behavioral Contract
## ai.docs/ux-ui/ui-states.md

This document defines the **mandatory UI states** that every screen and component MUST support.

UI states are NOT optional.
They are part of the functional UX contract.

Any UI that does not define its states is considered INCOMPLETE.

---

## 1) Purpose

UI states exist to:
- ensure predictable behavior
- reduce ambiguity for users
- prevent UI improvisation by AI or developers
- enforce accessibility and consistency

These states apply to:
- full screens
- sections
- components (tables, forms, buttons, cards)

---

## 2) Canonical UI States (Mandatory)

Every screen and major component MUST define behavior for the following states:

1. Loading  
2. Empty  
3. Error  
4. Disabled  
5. Read-Only  
6. Success (when applicable)

If a state is not applicable, this MUST be explicitly documented.

---

## 3) Loading State

### Definition
Displayed while data is being fetched or an action is being processed.

### Rules
- Must appear within 300ms of action
- Must not block navigation unless necessary
- Must be accessible to screen readers

### UI Behavior
- Use skeletons for structured content
- Use spinners only for short operations
- Disable triggering actions while loading

### Accessibility
- Announce loading state to screen readers
- Do not trap keyboard focus

---

## 4) Empty State

### Definition
Displayed when data exists but is empty (e.g. no records).

### Rules
- Must explain why the state exists
- Must guide the next possible action
- Must NOT be treated as an error

### UI Behavior
- Clear message (neutral tone)
- Primary CTA if user has permission
- No CTA if user lacks permission

---

## 5) Error State

### Definition
Displayed when an operation fails or data cannot be retrieved.

### Rules
- Must never expose sensitive data
- Must be actionable or informative
- Must be consistent across the system

### UI Behavior
- Short explanation
- Clear recovery action if possible
- Error code or reference (optional)

### Accessibility
- Error must be announced to assistive tech
- Error must be visually distinct AND textual

---

## 6) Disabled State

### Definition
Displayed when an action exists but is temporarily unavailable.

### Common Causes
- Missing permission
- Invalid form state
- System constraints

### UI Behavior
- Component is visible but inactive
- Tooltip or helper text SHOULD explain why
- Disabled elements must not be focusable

---

## 7) Read-Only State

### Definition
Displayed when data is visible but cannot be modified.

### Rules
- Data MUST remain visible
- Editing controls MUST be removed or disabled
- Visual distinction must be subtle, not hidden

### Common Use
- Permission-limited users
- Audit or historical views

---

## 8) Success State

### Definition
Displayed after successful completion of an action.

### Rules
- Must confirm the action clearly
- Must not block further interaction
- Must disappear automatically or on next action

### UI Behavior
- Short confirmation message
- No unnecessary animation
- Must not require dismissal unless critical

---

## 9) Enforcement Rules

- No component may skip state definitions
- No custom states without documentation
- States MUST be consistent across screens
- States MUST respect accessibility rules

Violations of this document are UX contract failures.

---

## 10) Relationship with Other ai.docs

UI states MUST align with:
- Design System (`design-system.md`)
- UX Matrix (`ux-matrix.md`)
- Security & Permissions (`05_SECURITY_AND_COMPLIANCE.md`)

If a conflict exists, this file MUST be updated explicitly.
