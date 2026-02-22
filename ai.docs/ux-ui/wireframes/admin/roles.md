# Wireframe — Roles & Permissions (Administrative)
## Route: /admin/roles

This document defines the **Roles & Permissions management screen**.

---

## 1) Screen Purpose

- View current roles and their associated permissions.
- Modify permission assignments to roles (Platform Admin only).

---

## 2) Layout Structure

### 2.1 Role Selection
- Tabs or Sidebar with existing roles: `COMPANY_OWNER`, `COMPANY_ADMIN`, `COMPANY_USER`.

### 2.2 Permissions Matrix
- A list of all atomic permissions (grouped by domain: Clients, Contacts, Interactions, etc.).
- Checkboxes for each permission.
- **Rules**: 
  - Some core permissions might be locked for specific roles (e.g., `COMPANY_OWNER` always has full access).
  - Changes must be audit-logged.

### 2.3 Actions
- **Save Changes**: Persists the role-permission mapping.

---

## 3) Constraints
- This screen is highly sensitive.
- Only users with `platform.review.reviewers.manage` (or generic `platform.admin` scope) or specific tenant owner permissions can access.
