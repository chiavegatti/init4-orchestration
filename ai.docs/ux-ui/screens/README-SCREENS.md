# AI Operational Guide: Screens & Layouts (Mini CRM)

This document defines **how AI models and agents must behave** when implementing the UI/UX based on the functional contracts.

## 1. Zero Tolerance Policy
- **Do not invent screens**: Only implement screens defined in `routes.md`.
- **Do not assume layouts**: Every screen must follow the corresponding wireframe in `ux-ui/wireframes/`.
- **Do not bypass permissions**: UI elements (buttons, links, fields) MUST be gated by permissions defined in `ux-matrix.md` and `permission-glossary.md`.

## 2. Implementation Workflow for AI
1. **Identify Route**: Locate the route being implemented in `routes.md`.
2. **Read Wireframe**: Access `ux-ui/wireframes/{module}/{screen_type}.md` (e.g., `clients/list.md`).
3. **Check Visibility**: Consult `governance/data-visibility-matrix.md` to ensure only authorized fields are rendered.
4. **Map Actions**: Verify every interactive element against `ux-matrix.md` and `governance/access-control-matrix.md`.
5. **Implement States**: Ensure `Loading`, `Empty`, and `Error` states are implemented exactly as described in the wireframe.

## 3. Standard Screen Types
AI must recognize and adhere to these standards:
- `list.md`: Tables, indexing, filtering, and bulk actions.
- `details.md`: Full view of a single entity, including relationships (e.g., Contacts under a Client).
- `form.md`: Data entry with validation rules and field-level permission constraints.

## 4. Accessibility & Quality
- AI MUST ensure WCAG 2.1 AA compliance as specified in wireframes.
- Focus management and keyboard navigation are functional requirements, not "extras".
- All labels and aria-attributes must be derived from the functional descriptions in the wireframes.
