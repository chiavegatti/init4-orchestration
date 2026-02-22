# Wireframe — User Form (Invite/Edit)
## Route: /admin/users/{userId}

This document defines the **User Invite/Edit form**.

---

## 1) Screen Purpose

- Invite new users to the tenant.
- Manage roles for existing users.

---

## 2) Layout Structure

### 2.1 Form Fields
- **Email** (Input): Required for invitations. Read-only for existing users.
- **Role** (Select): `COMPANY_ADMIN`, `COMPANY_USER`.
  - Only `COMPANY_OWNER` can promote someone to `COMPANY_OWNER`.

### 2.2 Actions
- **Cancel**: Returns to users list.
- **Send Invitation / Save Changes**: Commits the user record.

---

## 3) States
- **Invite Mode**: Email field is editable.
- **Edit Mode**: Email field is read-only; Role field is editable.
