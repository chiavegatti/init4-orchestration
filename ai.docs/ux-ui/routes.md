# UI Routes — Navigation Contract
## ai.docs/ux-ui/routes.md

This document defines the **authoritative UI routing structure** of the application.

Routes define:
- which screens exist
- how users navigate between them
- which sections are accessible by role

Routes DO NOT define:
- API endpoints
- backend implementation
- business rules
- permission logic

Routes represent **screens**, not HTTP verbs or data mutations.

---

## 1) Route Structure Principles (Mandatory)

- Routes represent UI screens
- Each route maps to one or more UX screens
- Navigation MUST respect tenant scope and permissions
- Routes MUST align with `ux-matrix.md`
- Routes MUST align with wireframes

If a route does not exist here, the screen MUST NOT exist.

---

## 2) Global Routing Rules

- All authenticated routes are prefixed by a functional area:
  - `/app`   → standard application usage
  - `/review` → review / approval flows
  - `/admin` → administrative functions

- Tenant context is implicit after authentication
- Unauthorized routes MUST redirect to an access-denied state
- Non-authenticated users MUST be redirected to `/auth/login`

---

## 3) Authentication Routes

| Route | Description |
|------|-------------|
| `/auth/login` | Login screen |
| `/auth/forgot-password` | Password recovery |
| `/auth/reset-password` | Password reset |

Rules:
- No tenant-specific data is accessible here
- No authenticated content may be shown

---

## 4) Application Routes (`/app`)

### 4.1 Dashboard

| Route | Description |
|------|-------------|
| `/app` | Main dashboard |
| `/app/dashboard` | Alias to main dashboard |

---

### 4.2 Clients

| Route | Description |
|------|-------------|
| `/app/clients` | Clients list |
| `/app/clients/new` | Create client |
| `/app/clients/{clientId}` | Client detail |
| `/app/clients/{clientId}/edit` | Edit client |

Notes:
- `{clientId}` refers to `public_id`
- Visibility and actions are governed by `ux-matrix.md`

---

### 4.3 Contacts (Client-scoped)

| Route | Description |
|------|-------------|
| `/app/clients/{clientId}/contacts` | Contacts list for a client |
| `/app/clients/{clientId}/contacts/new` | Create contact |
| `/app/clients/{clientId}/contacts/{contactId}` | Contact detail |
| `/app/clients/{clientId}/contacts/{contactId}/edit` | Edit contact |

Notes:
- `{clientId}` refers to `clients.public_id`
- `{contactId}` refers to `contacts.public_id`
- Contacts MUST be tenant-scoped and client-scoped
- Actions are governed by `ux-matrix.md` and governance matrices
---

### 4.4 Interactions (Client-scoped)

| Route | Description |
|------|-------------|
| `/app/clients/{clientId}/interactions` | Interactions timeline |
| `/app/clients/{clientId}/interactions/new` | Create interaction |

Notes:
- `{clientId}` refers to `clients.public_id`
- Interactions are immutable once created.
- Access governed by `ux-matrix.md` and `access-control-matrix.md`.

---

## 5) Administrative Routes (`/admin`)

Administrative routes are restricted to privileged roles.

| Route | Description |
|------|-------------|
| `/admin/users` | User management |
| `/admin/users/{userId}` | User detail |
| `/admin/roles` | Role management |
| `/admin/permissions` | Permission overview |

Rules:
- Admin routes MUST NOT expose tenant data unless explicitly allowed
- Admin routes MUST be governed by access-control matrix

---

## 7) Error & System Routes

| Route | Description |
|------|-------------|
| `/error/403` | Access denied |
| `/error/404` | Not found |
| `/error/500` | System error |

Rules:
- Errors must not expose sensitive information
- Error UX must comply with `ui-states.md`

---

## 8) Relationship with Other UX Contracts

This routing contract MUST align with:

- Wireframes (`ux-ui/wireframes/`)
- UX Matrix (`ux-ui/ux-matrix.md`)
- Permission-Aware UI (`ux-ui/permission-aware-ui.md`)
- UI States (`ux-ui/ui-states.md`)

If a route exists but is missing from any of the above, the system is inconsistent.

---

## 9) Change Governance

Any change to routes requires:
- UX review
- Update to wireframes
- Update to UX Matrix
- Task creation referencing the roadmap

Routes must remain stable whenever possible.

---

## 10) Scope Reminder

This document defines **where users can navigate**.

It does NOT define:
- what actions are allowed
- how data is modified
- how APIs are called

Those concerns belong to their respective ai.docs contracts.
