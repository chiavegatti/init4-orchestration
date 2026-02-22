# Wireframe — Interactions Timeline
## Route: /app/clients/{clientId}/interactions

This document defines the **Interactions Timeline screen**, where users can view notes, calls, and meetings related to a specific client.

---

## 1) Screen Purpose

- Provide a chronological view of all communications with a client.
- Filter interactions by type or author.
- Quick navigation to add new interactions.

---

## 2) Layout Structure

### 2.1 Header
- Title: **Interactions - {Client Name}**
- Back button to Client Details.
- Primary Action: **+ Add Note**

### 2.2 Timeline Feed
- Cards ordered from newest to oldest.
- Each Card includes:
  - Icon based on type (Phone, Email, Note, Meeting).
  - Author Name.
  - Timestamp.
  - Full content/text.
- **Rules**: Interactions are immutable; no Edit or Delete buttons are allowed.

---

## 3) States
- **Empty State**: "No interactions recorded for this client yet."
- **Loading State**: Skeleton timeline cards.

---

## 4) Permission-Aware Behavior
- User with `interaction:create` sees **Add Note** button.
- User with `interaction:view` can see the timeline.
