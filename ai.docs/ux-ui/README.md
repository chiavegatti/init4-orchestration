# UX / UI — Source of Truth
## ai.docs/ux-ui

This directory defines the **authoritative UX and UI contracts** for the product.

UX/UI here is NOT decorative.
It defines:
- what screens exist
- what data is visible
- what actions are allowed
- under which permissions
- and how accessibility is enforced

Any UI implementation MUST follow this directory.

---

## 1) Order of Authority (Mandatory)

When conflicts exist, the following order MUST be respected:

1. wireframes/  
   → Defines **what exists**, structure, flows and states  
   (authoritative)

2. design-system.md  
   → Defines **how it looks and behaves**  
   (colors, spacing, components, accessibility)

3. ux-matrix.md (if present)  
   → Maps screens × permissions × actions

4. prototypes/  
   → Visual validation only (Figma, exports)

5. screenshots/  
   → Reference only, NEVER authoritative

---

## 2) Relationship with Other ai.docs (Mandatory)

UX/UI is constrained by:

- PRD  
  → Defines business behavior and scope  
  (`ai.docs/03_PRD.md`)

- Data Schema  
  → Defines what data exists  
  (`ai.docs/data-base-schemas/`)

- API Contracts  
  → Defines how data is retrieved and mutated  
  (`ai.docs/07_API_CONTRACTS.md`)

- Security & Permissions  
  → Defines what actions are allowed  
  (`ai.docs/05_SECURITY_AND_COMPLIANCE.md`)

If UX conflicts with any of the above, UX MUST be corrected.

---

## 3) Non-Negotiable Rules

- Never invent screens not present in wireframes
- Never expose data not defined in schemas
- Never enable actions without permission mapping
- Never rely on frontend-only validation
- UX MUST reflect backend authorization rules

If a new screen is needed:
- update PRD
- update wireframes
- update permissions
- update tasks

---

## 4) Accessibility (Mandatory)

All UI MUST comply with:
- WCAG 2.x AA (minimum)
- Keyboard navigation
- Screen reader compatibility
- Proper contrast and focus states
- Semantic HTML

Accessibility rules are defined in:
ai.docs/05_SECURITY_AND_COMPLIANCE.md

If accessibility is not defined for a component, STOP and define it.

---

## 5) UX Is a Contract (Important)

UX is not subjective.

Each screen MUST explicitly define:
- data displayed
- available actions
- required permissions
- empty states
- error states
- loading states

If any of these are missing, the UX is incomplete.

---

## 6) AI Usage Rules (Mandatory)

When generating or modifying UI:

- Always read wireframes first
- Never infer UI from API structure
- Never infer permissions
- Ask for clarification if flows are unclear
- Reflect existing patterns, do not create new ones

Violating UX contracts is considered a system failure.

---

## 7) Scope Reminder

This directory defines **UX and UI behavior**.

It does NOT:
- define business rules
- define API logic
- define database structure

Those concerns belong to their respective ai.docs sections.
