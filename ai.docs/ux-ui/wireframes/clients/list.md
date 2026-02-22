# Wireframe — Clients List
## Route: /app/clients

This document defines the **Clients List screen** for the Mini CRM.

It describes:
- screen purpose
- layout structure
- user interactions
- states
- permission-aware behavior
- accessibility requirements

This is a **wireframe contract**, not a visual mockup.

---

## 1) Screen Purpose

The Clients List screen allows authorized users to:
- view existing clients
- search and filter clients
- navigate to client details
- initiate client creation (if permitted)

This screen is the primary entry point for client management.

---

## 2) Authorized Roles

Access to this screen is governed by `ux-matrix.md`.

Typical roles:
- COMPANY_OWNER
- COMPANY_ADMIN
- COMPANY_USER
- PLATFORM_ADMIN (read-only monitoring)

Behavior varies by permission.

---

## 3) Layout Structure

### 3.1 Header

- Page title: **Clients**
- Optional subtitle: tenant or account context
- Primary action (if permitted): **+ New Client**

Header rules:
- Primary action MUST be hidden or disabled if permission is missing
- Header must remain visible at all times

---

### 3.2 Filters & Search

Located below the header.

Components:
- Search input (by name, identifier, email)
- Status filter (active / inactive / archived)
- Optional advanced filters (future)

Rules:
- Filters MUST be keyboard accessible
- Filters MUST preserve state on navigation
- Filters MUST NOT expose unauthorized data

---

### 3.3 Clients Table

Primary content area.

Columns (example):
- Client Name
- Status
- Primary Contact
- Created At
- Actions

Rules:
- Column visibility MUST follow `data-visibility-matrix.md`
- Actions column MUST adapt to permissions
- Row click navigates to client detail screen

---

### 3.4 Row Actions

Possible actions (permission-based):
- View details
- Edit client
- Archive / deactivate

Rules:
- Actions MUST NOT appear if permission is missing
- Disabled actions MUST explain why (tooltip or helper text)
- No destructive action without confirmation

---

## 4) Empty State

Triggered when:
- no clients exist
- filters return no results

Behavior:
- Show friendly explanation
- Show CTA **only if** user can create clients
- Never suggest actions the user cannot perform

---

## 5) Loading State

Triggered when:
- initial load
- filter change
- pagination

Behavior:
- Use skeleton loaders
- Maintain layout stability
- Do not block navigation entirely

---

## 6) Error State

Triggered when:
- data fetch fails
- permission mismatch occurs

Behavior:
- Show non-technical message
- Do not expose system details
- Offer retry if applicable

---

## 7) Permission-Aware Behavior

Examples:
- User with `client:create` → sees **New Client** button
- User without `client:edit` → edit action hidden
- User with read-only permission → table visible, actions limited

No permission may be inferred.

---

## 8) Accessibility Requirements

- Full keyboard navigation
- Proper focus order
- Table headers associated with cells
- Action buttons must have accessible labels
- Status must not rely on color alone

WCAG 2.1 AA compliance is mandatory.

---

## 9) Related Contracts

This wireframe MUST align with:
- `ux-ui/routes.md`
- `ux-ui/ux-matrix.md`
- `ux-ui/permission-aware-ui.md`
- `ux-ui/ui-states.md`
- `ux-ui/governance/*`

If inconsistencies are found, stop and resolve before implementation.

---

## 10) Notes for Implementation

- Do not hardcode role names in UI
- Always rely on permission checks
- Avoid optimistic UI for destructive actions
