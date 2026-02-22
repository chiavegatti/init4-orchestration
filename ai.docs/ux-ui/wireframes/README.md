# Wireframes — Structural UX Contract
## ai.docs/ux-ui/wireframes

This directory defines the **authoritative structural UX** of the product.

Wireframes define:
- which screens exist
- layout hierarchy
- information structure
- user flows
- states (loading, empty, error)

Wireframes DO NOT define:
- visual styling
- colors
- typography
- branding

Those concerns belong to:
ai.docs/ux-ui/design-system.md

---

## 1) Role of Wireframes (Mandatory)

Wireframes are the **source of truth** for:

- screen existence
- navigation structure
- content grouping
- interaction flow

If a screen does not exist in wireframes, it MUST NOT exist in implementation.

---

## 2) Authority Order (Non-Negotiable)

When conflicts exist, the following order applies:

1. Wireframes (this directory)
2. Design System
3. Prototypes
4. Screenshots

Wireframes override visual interpretations.

---

## 3) Required Content per Screen (Mandatory)

Every wireframe MUST explicitly define:

- Screen name
- Purpose
- Data displayed
- Primary actions
- Secondary actions
- Empty states
- Error states
- Loading states

If any item is missing, the wireframe is INVALID.

---

## 4) Relationship with Other ai.docs

Wireframes MUST be consistent with:

- PRD (`ai.docs/03_PRD.md`)
- Data Schemas (`ai.docs/data-base-schemas/`)
- API Contracts (`ai.docs/07_API_CONTRACTS.md`)
- Security & Permissions (`ai.docs/05_SECURITY_AND_COMPLIANCE.md`)

Wireframes MUST NOT:
- invent data
- invent actions
- bypass permissions

---

## 5) Accessibility (Mandatory)

Wireframes MUST consider accessibility from the start:

- Logical reading order
- Keyboard navigation flow
- Focus order
- Error messaging placement
- Form labeling

Accessibility rules are enforced by:
ai.docs/05_SECURITY_AND_COMPLIANCE.md

---

## 6) File Organization (Recommended)

Recommended structure:

wireframes/
├── global/
│ ├── navigation.md
│ ├── layout.md
│
├── clients/
│ ├── list.md
│ ├── detail.md
│ └── form.md
│
├── contacts/
│ ├── list.md
│ └── form.md
│
├── auth/
│ ├── login.md
│ └── forgot-password.md


Files may be Markdown, image exports or links to design tools,
but the **contractual information MUST be written**, not implied.

---

## 7) AI Usage Rules (Mandatory)

When generating or modifying wireframes:

- Never infer screens from API endpoints
- Never infer actions from data models
- Ask for clarification if flows are missing
- Respect existing patterns

Violating wireframe contracts is considered a system failure.

---

## 8) Scope Reminder

Wireframes define **structure and behavior**.

They do NOT define:
- business logic
- validation rules
- backend workflows
