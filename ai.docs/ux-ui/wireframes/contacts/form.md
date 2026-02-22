# Wireframe — Contact Form
## Routes:
- /app/clients/{clientId}/contacts/new
- /app/clients/{clientId}/contacts/{contactId}/edit

Single reusable form contract for create + edit.

---

## 1) Screen Purpose

Allow authorized users to:
- create a new contact for a client
- edit an existing contact

---

## 2) Modes

### Create Mode
Route: `/contacts/new`
- empty fields
- submit creates contact

### Edit Mode
Route: `/contacts/{contactId}/edit`
- fields prefilled
- submit updates contact

---

## 3) Layout Structure

### Header
- Create: “New Contact”
- Edit: “Edit Contact”
- Client context always visible

### Form Fields (example)
- Full Name (required)
- Role/Title
- Email
- Phone
- Notes (optional)

Rules:
- Labels required (placeholder is not a label)
- Field visibility and editability follow governance

---

## 4) Validation Rules

- Full Name required
- Email format if provided
- Phone format if provided

Behavior:
- inline errors
- preserve user input on failure
- backend validation is authoritative

---

## 5) Actions

Primary:
- Create: “Create Contact”
- Edit: “Save Changes”

Secondary:
- Cancel / Back

Rules:
- Disable submit while loading
- Confirm before leaving if dirty

---

## 6) UI States

- Loading (edit mode prefill)
- Error (load/submit failures)
- 403/404 handling

---

## 7) Accessibility

- Keyboard-only usability
- Errors announced to screen readers
- Required fields announced

---

## 8) Related Contracts

Must align with:
- `ux-ui/routes.md`
- `ux-ui/ux-matrix.md`
- `ux-ui/ui-states.md`
- `ux-ui/permission-aware-ui.md`
- governance matrices

## Module: Contacts

### Purpose
Manage contacts (people/organizations) for each tenant (company). Contacts are tenant-scoped and must never leak across companies.

### Screens (Wireframes)
- Contacts List
- Contact Create
- Contact Detail
- Contact Edit

> If any screen does not exist in wireframes yet: mark as TBD and add it to wireframes before implementing.

---

### Routes (UI)
| Screen | Route | Notes |
|---|---|---|
| Contacts List | /app/contacts | Search + filters + pagination |
| Contact Create | /app/contacts/new | Form with validation |
| Contact Detail | /app/contacts/{contactId} | Read-only view + actions |
| Contact Edit | /app/contacts/{contactId}/edit | Edit form |

---

### Permissions (RBAC)
> Permission names MUST match `ai.docs/ux-ui/permission-glossary.md`. If your glossary uses different names, rename here accordingly.

| Capability | Permission | Who typically has it |
|---|---|---|
| List contacts | contacts.list | OWNER, ADMIN, OPERATOR |
| View contact | contacts.view | OWNER, ADMIN, OPERATOR |
| Create contact | contacts.create | OWNER, ADMIN |
| Update contact | contacts.update | OWNER, ADMIN |
| Delete contact | contacts.delete | OWNER, ADMIN |
| Export contacts | contacts.export | OWNER, ADMIN |
| Import contacts | contacts.import | OWNER, ADMIN |

---

### Data Visibility (Tenant Isolation)
- Contacts are ALWAYS scoped by `company_id` (tenant).
- Users can only see contacts belonging to their own company.
- Reviewers (REVIEWER scope) do not access tenant contacts unless explicitly required by PRD.
- PLATFORM_ADMIN access must be audited.

---

### API Exposure
> If this module is exposed in public API, keep it explicit. If not, mark as internal-only.

**Internal App/API (required for UI):**
- GET /api/v1/contacts
- POST /api/v1/contacts
- GET /api/v1/contacts/{contactId}
- PATCH /api/v1/contacts/{contactId}
- DELETE /api/v1/contacts/{contactId}

**Public API (optional):**
- [ ] Exposed publicly
- [x] Internal only (default)

---

### UI Rules (Design System + WCAG)
- Must comply with WCAG 2.x AA (forms, errors, focus states, keyboard navigation).
- Use components and tokens defined in `ai.docs/ux-ui/design-system.md`.

---

### Notes / Edge Cases
- Prevent duplicates (email + company_id) if email is used as identifier.
- Log audit events for create/update/delete actions.
- Bulk actions (import/export) only if in scope; otherwise remove permissions/routes.
