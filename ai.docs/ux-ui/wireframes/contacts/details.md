# Wireframe — Contact Detail
## Route: /app/clients/{clientId}/contacts/{contactId}

This screen shows details for a single contact.

---

## 1) Screen Purpose

Allow authorized users to:
- view contact information
- see which client it belongs to
- edit contact (if permitted)

---

## 2) Route Parameters

- `{clientId}` refers to `clients.public_id`
- `{contactId}` refers to `contacts.public_id`

---

## 3) Layout Structure

### 3.1 Header
- Contact name (primary)
- Client name (secondary)
- Actions (permission-aware):
  - Edit Contact → `/edit`

### 3.2 Contact Profile Card
Fields (example):
- Name
- Role/Title
- Email
- Phone
- Notes (optional)

Rules:
- Field visibility follows governance
- Read-only users see fields without edit affordances

---

## 4) UI States

### Loading
- skeleton for header and profile card

### Error
- show retry
- do not leak technical details

### Not Found / Access Denied
- 404 / 403 routes and screens

---

## 5) Accessibility

- Focus order: header → content
- Accessible labels for actions
- Proper semantics for field display

---

## 6) Related Contracts

Must align with:
- `ux-ui/routes.md`
- `ux-ui/ux-matrix.md`
- `ux-ui/ui-states.md`
- `ux-ui/permission-aware-ui.md`
- governance matrices
