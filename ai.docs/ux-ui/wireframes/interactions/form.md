# Wireframe — Interaction Form (Create)
## Route: /app/clients/{clientId}/interactions/new

This document defines the **Interaction Creation Form**.

---

## 1) Screen Purpose

- Record a new interaction with a client.
- Ensure all interactions are client-scoped and immutable.

---

## 2) Layout Structure

### 2.1 Form Fields
- **Type** (Select): Call, Email, Meeting, Note.
- **Content** (Rich Text/Textarea): The actual description of the interaction.
- **Rules**: 
  - Author is automatically set to the logged-in user.
  - Date is automatically set to current timestamp.

### 2.2 Actions
- **Cancel**: Returns to the timeline.
- **Save Interaction**: Persists the note (immutable).

---

## 3) Validation Rules
- Type is mandatory.
- Content is mandatory (minimum 5 characters).

---

## 4) Constraints
- Once saved, the interaction cannot be modified or deleted.
