# UX Matrix — Screens × Permissions × Actions
## ai.docs/ux-ui/ux-matrix.md

This document defines the **explicit mapping** between:
- screens
- user roles / permissions
- allowed actions

No action may exist in the UI without being defined here.

---

## 1) Purpose

The UX Matrix exists to:
- prevent unauthorized UI actions
- make permissions visible and auditable
- ensure UI reflects backend authorization
- remove ambiguity for AI-generated interfaces

This document is **authoritative**.

---

## 2) Rules (Non-Negotiable)

- Every screen MUST appear in this matrix
- Every UI action MUST map to an existing route defined in `routes.md`
- Every action MUST map to one or more permissions
- UI MUST NOT expose actions without permission
- Backend authorization MUST match this matrix
- Hiding buttons is NOT authorization

If an action is not listed here, it does not exist.

---

## 3) Matrix Structure

Each entry MUST define:

- Screen
- Action
- Permission required
- Role(s) allowed
- API endpoint(s) involved
- Notes (optional)

---

## 4) Example — Clients

| Screen | Action | Permission | Role(s) | API |
|------|--------|------------|---------|-----|
| Clients List | View list | clients.read | COMPANY_USER+ | GET /clients |
| Clients List | Create client | clients.create | COMPANY_ADMIN+ | POST /clients |
| Client Detail | View details | clients.read | COMPANY_USER+ | GET /clients/{id} |
| Client Detail | Edit client | clients.update | COMPANY_ADMIN+ | PUT /clients/{id} |
| Client Detail | Add interaction | interactions.create | COMPANY_USER+ | POST /clients/{id}/interactions |

---

## 5) Roles Legend

- COMPANY_USER+ means COMPANY_USER and higher
- COMPANY_ADMIN+ means COMPANY_ADMIN and higher
- PLATFORM_ADMIN bypasses tenant restrictions where allowed

Roles are defined in:
ai.docs/data-base-schemas/roles.md

---

## 6) Change Governance

Any change to this matrix requires:

- PRD update (if behavior changes)
- API contract update
- Schema update (if needed)
- ADR if permission model changes

---

## 7) AI Usage Rules

When generating UI:

- Always consult this matrix
- Never infer permissions
- Never expose disabled actions
- If matrix entry is missing, STOP and request clarification

---

## 8) Scope Reminder

This document defines **who can do what, where** in the UI.

It does NOT define:
- visual styling
- navigation aesthetics
- backend logic

## Module: Clients

This section defines all UI actions related to client management.

All actions are permission-based and tenant-scoped.
If an action is not listed here, it MUST NOT exist in the UI.

---

### Screen: Clients List
Route: `/app/clients`

| Action | Permission | Notes |
|------|-----------|-------|
| View clients list | client:view | Required to access the screen |
| Search clients | client:view | Includes text search and filters |
| View client detail | client:view | Navigates to client detail |
| Create client | client:create | Controls visibility of "New Client" CTA |

Rules:
- Without `client:view`, access to this route is forbidden (403)
- Actions must be hidden if permission is missing
- Data visibility follows `data-visibility-matrix.md`

---

### Screen: Client Detail
Route: `/app/clients/{clientId}`

| Action | Permission | Notes |
|------|-----------|-------|
| View client profile | client:view | Required to access the screen |
| Edit client | client:edit | Controls "Edit Client" action |
| View contacts | contact:view | Governs Contacts section visibility |
| Add contact | contact:create | Controls "Add Contact" CTA |
| View interactions | interaction:view | Governs Interactions timeline |
| Add interaction | interaction:create | Controls interaction form |

Rules:
- Sections may be hidden entirely if permission is missing
- Read-only users may view but not act
- No destructive actions allowed without explicit permission

---

### Screen: Client Form (Create)
Route: `/app/clients/new`

| Action | Permission | Notes |
|------|-----------|-------|
| Access create form | client:create | Required to access the screen |
| Submit new client | client:create | Final submission |

Rules:
- Without `client:create`, route access is forbidden (403)
- Fields must respect data visibility rules
- Default values may be applied by backend only

---

### Screen: Client Form (Edit)
Route: `/app/clients/{clientId}/edit`

| Action | Permission | Notes |
|------|-----------|-------|
| Access edit form | client:edit | Required to access the screen |
| Update client | client:edit | Final submission |

Rules:
- Without `client:edit`, route access is forbidden (403)
- Field-level editability must follow governance rules
- Hidden fields must not be rendered

---

### Global Clients Rules

- All client actions are tenant-scoped
- UI must not infer permissions from role names
- UI must not expose partial actions
- Permission checks must be explicit and deterministic

## Module: Contacts

This section defines all UI actions related to contacts management within a client context.

Contacts are tenant-scoped and always associated with a client.
If an action is not listed here, it MUST NOT exist in the UI.

---

### Screen: Contacts List
Route: `/app/clients/{clientId}/contacts`

| Action | Permission | Notes |
|------|-----------|-------|
| View contacts list | contact:view | Required to access the screen |
| Search contacts | contact:view | Includes text search and filters |
| View contact detail | contact:view | Navigates to contact detail |
| Create contact | contact:create | Controls visibility of "New Contact" CTA |

Rules:
- Without `contact:view`, access to this route is forbidden (403)
- Field visibility follows `data-visibility-matrix.md`
- Contacts MUST belong to the referenced clientId

---

### Screen: Contact Detail
Route: `/app/clients/{clientId}/contacts/{contactId}`

| Action | Permission | Notes |
|------|-----------|-------|
| View contact profile | contact:view | Required to access the screen |
| Edit contact | contact:edit | Controls "Edit Contact" action |

Rules:
- Without `contact:view`, route access is forbidden (403)
- UI must not expose edit affordances without `contact:edit`

---

### Screen: Contact Form (Create)
Route: `/app/clients/{clientId}/contacts/new`

| Action | Permission | Notes |
|------|-----------|-------|
| Access create contact form | contact:create | Required to access the screen |
| Submit new contact | contact:create | Final submission |

Rules:
- Without `contact:create`, route access is forbidden (403)
- New contact MUST be created under the referenced clientId
- Field visibility and editability follow governance

---

### Screen: Contact Form (Edit)
Route: `/app/clients/{clientId}/contacts/{contactId}/edit`

| Action | Permission | Notes |
|------|-----------|-------|
| Access edit contact form | contact:edit | Required to access the screen |
| Update contact | contact:edit | Final submission |

Rules:
- Without `contact:edit`, route access is forbidden (403)
- Contact MUST belong to the referenced clientId and tenant
- Hidden fields must not be rendered

---

### Global Contacts Rules

- Contacts are tenant-scoped and client-scoped
- UI must not infer permissions from roles
- UI must not allow cross-client navigation by manipulating IDs
- All permission checks must be explicit and deterministic

## Module: Interactions

This section defines all UI actions related to recording and viewing interactions within a client context.
Interactions are immutable once created, as defined in `03_PRD.md`.

---

### Screen: Interactions List
Route: `/app/clients/{clientId}/interactions`

| Action | Permission | Notes |
|------|-----------|-------|
| View interactions timeline | interaction:view | Required to access the screen |
| Filter interactions | interaction:view | Filter by date or author |
| Create interaction | interaction:create | Controls visibility of "New Note" CTA |

Rules:
- Without `interaction:view`, access to this route is forbidden (403)
- Interactions are always client-scoped
- Data visibility follows `data-visibility-matrix.md`

---

### Screen: Interaction Form (Create)
Route: `/app/clients/{clientId}/interactions/new`

| Action | Permission | Notes |
|------|-----------|-------|
| Access creation form | interaction:create | Required to access the screen |
| Submit interaction | interaction:create | Final submission (immutable) |

Rules:
- Without `interaction:create`, route access is forbidden (403)
- Author is automatically set to the current user
- Timestamp is automatically set by the system
- Once submitted, interactions cannot be edited or deleted (functional constraint)

---

### Global Interactions Rules

- Interactions are tenant-scoped and client-scoped
- Interactions are immutable once created
- UI must not provide any edit or delete affordances for interactions
- All permission checks must be explicit and deterministic
