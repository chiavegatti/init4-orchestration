# Wireframe — Contacts List
## Route: /app/clients/{clientId}/contacts

This screen lists all contacts for a given client.

It defines:
- structure and behavior
- states (loading/empty/error)
- permission-aware actions
- accessibility rules

---

## 1) Screen Purpose

Allow authorized users to:
- view contacts belonging to a client
- search/filter contacts
- navigate to contact detail
- create a new contact (if permitted)

---

## 2) Route Parameters

- `{clientId}` refers to `clients.public_id`

If client is inaccessible:
- show 403 or 404 accordingly.

---

## 3) Layout Structure

### 3.1 Header
- Title: **Contacts**
- Context: client name (read-only)
- Primary action (if permitted): **+ New Contact**

### 3.2 Search & Filters
- Search by name/email/phone
- Optional filter: role/title (future)

### 3.3 Contacts Table/List
Columns (example):
- Name
- Role/Title
- Email
- Phone
- Actions

Rules:
- Field visibility follows `data-visibility-matrix.md`
- Actions adapt to permissions
- Row click navigates to contact detail

---

## 4) Row Actions (Permission-aware)

Possible actions:
- View contact detail (contact:view)
- Edit contact (contact:edit)

Rules:
- Hide actions if permission is missing
- No destructive actions unless explicitly defined

---

## 5) UI States

### Loading
- skeleton rows

### Empty
- message: “No contacts yet.”
- CTA: “Add contact” only if contact:create is allowed

### Error
- non-technical message
- retry option

---

## 6) Accessibility

- Keyboard navigation across table and actions
- Proper labels for action buttons
- No color-only meaning

---

## 7) Related Contracts

Must align with:
- `ux-ui/routes.md`
- `ux-ui/ux-matrix.md`
- `ux-ui/ui-states.md`
- `ux-ui/permission-aware-ui.md`
- governance matrices
