# Wireframe — Client Form
## Routes:
- /app/clients/new
- /app/clients/{clientId}/edit

This document defines the **Client Form screen** used for both:
- client creation
- client editing

This is a **single reusable contract** with mode-based behavior.

---

## 1) Screen Purpose

The Client Form allows authorized users to:
- create a new client
- edit an existing client

The form adapts its behavior based on:
- route (new vs edit)
- permissions
- data visibility rules

---

## 2) Modes of Operation

### 2.1 Create Mode
Triggered by:
- Route: `/app/clients/new`

Behavior:
- All fields start empty
- Default values applied where applicable
- Submit action creates a new client

---

### 2.2 Edit Mode
Triggered by:
- Route: `/app/clients/{clientId}/edit`

Behavior:
- Fields prefilled with existing client data
- Only editable fields are enabled
- Submit action updates existing client

If the client does not exist or is inaccessible:
- show 404 or 403 state

---

## 3) Authorized Roles

Access and actions are governed by:
- `ux-ui/ux-matrix.md`
- `ux-ui/governance/access-control-matrix.md`
- `ux-ui/governance/data-visibility-matrix.md`

Rules:
- Create and edit permissions are independent
- Field-level editability must respect data visibility rules

---

## 4) Layout Structure

### 4.1 Header

Header includes:
- Page title:
  - "New Client" (create mode)
  - "Edit Client" (edit mode)
- Secondary info (edit mode only): client name
- Optional breadcrumb or back navigation

Header rules:
- Title must clearly indicate mode
- No destructive actions in header

---

### 4.2 Form Sections

#### Section 1: Basic Information

Fields (example):
- Client Name (required)
- Email
- Phone
- Status (active / inactive)

Rules:
- Required fields must be clearly indicated
- Field visibility and editability follow governance rules
- Status field may be hidden or read-only depending on permission

---

#### Section 2: Additional Information (Optional)

Fields (example):
- Notes
- Tags
- Custom attributes (future)

Rules:
- Optional fields must not block submission
- Hidden fields must not be rendered

---

## 5) Field Validation

Validation rules:
- Client Name is required
- Email must be valid format
- Phone must follow defined format (if provided)

Behavior:
- Client-side validation for immediate feedback
- Server-side validation is authoritative
- Validation errors must be shown inline

Error messaging:
- Clear
- Non-technical
- Associated with the field

---

## 6) Actions

### 6.1 Primary Action

- Create mode: **Create Client**
- Edit mode: **Save Changes**

Rules:
- Button disabled while submitting
- Button hidden if permission is missing

---

### 6.2 Secondary Actions

- Cancel / Back
- Optional Reset (create mode only)

Rules:
- Cancel must not discard data silently without warning
- Reset clears only editable fields

---

## 7) Confirmation & Navigation

### 7.1 Successful Submit

Create mode:
- Redirect to `/app/clients/{clientId}`

Edit mode:
- Redirect to client detail screen
- Or show success feedback and stay (implementation choice)

---

### 7.2 Cancel Behavior

If form is dirty:
- Show confirmation dialog before leaving

If form is clean:
- Navigate back immediately

---

## 8) UI States

### 8.1 Loading State
Triggered when:
- fetching client data (edit mode)

Behavior:
- Show skeleton or loading indicator
- Disable form interactions

---

### 8.2 Error State

Triggered when:
- submit fails
- client data cannot be loaded

Behavior:
- Show error message
- Preserve user input when possible
- Offer retry

---

### 8.3 Access Denied (403)

Triggered when:
- user lacks create or edit permission

Behavior:
- Show access denied screen
- Do not render form fields

---

## 9) Permission-Aware Behavior (Examples)

- User can view client but cannot edit:
  - Edit route must be blocked (403)
- User can create but not set status:
  - Status field hidden or read-only
- User can edit but not create:
  - `/new` route blocked

No permission may be inferred.

---

## 10) Accessibility Requirements

- Logical tab order
- Labels associated with inputs
- Error messages announced to screen readers
- Required fields announced
- Buttons have accessible labels
- Form usable via keyboard only

WCAG 2.1 AA compliance is mandatory.

---

## 11) Related Contracts

This wireframe MUST align with:
- `ux-ui/routes.md`
- `ux-ui/ux-matrix.md`
- `ux-ui/ui-states.md`
- `ux-ui/permission-aware-ui.md`
- `ux-ui/governance/*`
- `ai.docs/data-base-schemas/clients.md`

If inconsistencies are found, stop and resolve before implementation.

---

## 12) Notes for Implementation

- Do not reuse the same component blindly for create/edit without mode awareness
- Avoid optimistic UI on submit
- Always rely on backend response for final state
- Ensure tenant isolation is enforced by backend
