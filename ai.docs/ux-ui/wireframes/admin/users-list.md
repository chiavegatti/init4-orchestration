# Wireframe — Users List (Administrative)
## Route: /admin/users

This document defines the **User Management screen** within a tenant context.

---

## 1) Screen Purpose

- View all users belonging to the current tenant.
- Manage user invitation and activation status.
- Primary entry point for Role-Based Access Control management at the user level.

---

## 2) Layout Structure

### 2.1 Header
- Title: **Users & Permissions**
- Primary Action: **+ Invite User**

### 2.2 Users Table
- Columns:
  - Name
  - Email
  - Role (`COMPANY_OWNER`, `COMPANY_ADMIN`, `COMPANY_USER`)
  - Status (Active, Pending Invitation, Disabled)
  - Last Login
- Actions:
  - Edit Role
  - Disable User (Soft Delete)

---

## 3) Permission-Aware Behavior
- User with `platform.tenants.view` (Platform Admin) or `team.members.invite` (Company Owner/Admin) can see this screen.
- Modification actions are restricted to `COMPANY_OWNER` or `COMPANY_ADMIN`.
