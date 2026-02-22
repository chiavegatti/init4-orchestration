# Wireframe — Client Detail
## Route: /app/clients/{clientId}

This document defines the **Client Detail screen** for the Mini CRM.

It describes:
- screen purpose
- information architecture
- actions and interactions
- UI states
- permission-aware behavior
- accessibility requirements

This is a **wireframe contract**, not a visual mockup.

---

## 1) Screen Purpose

The Client Detail screen allows authorized users to:
- view client profile information
- view contacts associated with the client
- view interaction history (append-only notes)
- perform allowed actions (edit, add contact, add interaction)

It is the main hub for a single client record.

---

## 2) Route Parameters

- `{clientId}` refers to `clients.public_id` (ULID)
- The UI MUST NOT use internal numeric IDs

If the client does not exist or is not accessible:
- show 404 or 403 state accordingly

---

## 3) Authorized Roles

Access and actions are governed by:
- `ux-ui/ux-matrix.md`
- `ux-ui/governance/access-control-matrix.md`
- `ux-ui/governance/data-visibility-matrix.md`

No role or permission may be inferred.

---

## 4) Layout Structure

### 4.1 Header (Client Context)

Header includes:
- Client name (primary)
- Status badge (active/inactive)
- Secondary info (optional): email / phone summary

Header actions (permission-aware):
- Edit Client (if permitted) → navigates to `/app/clients/{clientId}/edit`
- Add Contact (if permitted) → navigates to `/app/clients/{clientId}/contacts/new`
- Add Interaction (if permitted) → opens inline form or modal (see section 6)

Rules:
- Actions must be hidden/disabled according to permissions
- Status must not rely on color only
- Header must remain stable across states

---

### 4.2 Client Profile Card

Shows key client fields (visibility governed):
- Name
- Email
- Phone
- Status
- Created At
- Created By (optional / permission-based)

Rules:
- Field visibility MUST follow data visibility governance
- If a field is hidden, it MUST NOT appear as blank; it must be omitted
- Read-only users see the same fields but no edit affordances

---

### 4.3 Tabs / Sections (Recommended)

The screen is divided into sections:

1) Overview (default)
2) Contacts
3) Interactions

Tabs are optional. If not used, sections are stacked vertically.

---

## 5) Contacts Section
## Route reference: /app/clients/{clientId}/contacts

### 5.1 Contacts List (Embedded)

Displays a list/table of contacts belonging to the client.

Columns (example):
- Name
- Role/Title
- Email
- Phone
- Actions

Actions (permission-aware):
- View contact detail (if implemented)
- Edit contact (if permitted)

Rules:
- Contact data visibility must follow governance rules
- If no contacts exist, show empty state with CTA only if permitted

### 5.2 Contacts Empty State

- Message: "No contacts yet."
- CTA: "Add contact" only if user can create contacts

---

## 6) Interactions Section (Append-Only)
## Primary action: Add Interaction

### 6.1 Interaction List (Timeline)

Displays chronological interaction records:
- Author
- Timestamp
- Content preview / full content

Rules:
- Interactions are append-only
- No edit buttons
- Delete is forbidden unless explicitly allowed and audited

### 6.2 Add Interaction (Permission-Aware)

If permitted, user can add a new interaction via:
- Inline form at top of section, OR
- Modal

Form fields:
- Content (required)
- Type (default: note)

Rules:
- Submit disabled while loading
- On success: show success feedback and append to timeline
- On failure: show error state and keep content in form
- Must not allow HTML injection

---

## 7) UI States

### 7.1 Loading State
Triggered on initial load and section refresh.

- Use skeleton loaders for header + profile card + list placeholders
- Maintain layout stability

### 7.2 Error State
Triggered when data fetch fails.

- Show non-technical message
- Provide retry action if applicable
- Do not leak backend details

### 7.3 Not Found (404)
Triggered when:
- clientId is invalid
- record not found

Show 404 screen.

### 7.4 Access Denied (403)
Triggered when:
- user lacks permission to view this client

Show 403 screen.

### 7.5 Empty States
- No contacts
- No interactions

Must guide user appropriately and respect permissions.

---

## 8) Permission-Aware Behavior (Examples)

- User can view client but cannot edit:
  - Profile is read-only
  - Edit button hidden or disabled
- User can add interactions:
  - Interaction form visible
- User cannot add interactions:
  - Timeline visible (if allowed), form hidden
- User lacks contacts permission:
  - Contacts section hidden OR replaced with access notice (per policy)

All decisions must align with `permission-aware-ui.md`.

---

## 9) Accessibility Requirements

- Proper focus order (header → tabs → content)
- Keyboard accessible tabs (if tabs exist)
- All action buttons have aria-labels
- Timeline content is readable by screen readers
- Form errors are announced and placed near fields
- Status badge has text, not color-only meaning

WCAG 2.1 AA compliance is mandatory.

---

## 10) Related Contracts

This wireframe MUST align with:
- `ux-ui/routes.md`
- `ux-ui/ux-matrix.md`
- `ux-ui/ui-states.md`
- `ux-ui/permission-aware-ui.md`
- `ux-ui/governance/*`
- `ai.docs/data-base-schemas/clients.md`
- `ai.docs/data-base-schemas/contacts.md`
- `ai.docs/data-base-schemas/interactions.md`

If inconsistencies exist, stop and resolve before implementation.

---

## 11) Notes for Implementation

- Never assume permission from role label; always check permissions
- Avoid optimistic UI for create interaction unless backend confirms
- Ensure tenant isolation is enforced by backend; UI must not attempt cross-tenant access
