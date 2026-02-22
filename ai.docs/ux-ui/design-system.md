# Design System — UI Contract
## ai.docs/ux-ui/design-system.md

This document defines the **authoritative UI and accessibility rules** for the product.

It is NOT a suggestion.
It is a **binding contract** for:
- designers
- developers
- AI systems
- QA and accessibility review

Any UI implementation MUST follow this document.

---

## 1) Role of the Design System (Mandatory)

The design system defines:
- visual language
- component behavior
- accessibility constraints
- interaction consistency

It does NOT define:
- business rules
- data models
- permissions logic

Those are defined in:
- PRD (`ai.docs/03_PRD.md`)
- Schema (`ai.docs/data-base-schemas/`)
- API Contracts (`ai.docs/07_API_CONTRACTS.md`)
- Security (`ai.docs/05_SECURITY_AND_COMPLIANCE.md`)

If a conflict exists, THIS FILE MUST BE UPDATED — not bypassed.

---

## 2) Foundations

### 2.1 Color Palette

#### Primary Colors
- primary-500: #0066FF
- primary-600: #0052CC
- primary-700: #003D99

#### Secondary Colors
- secondary-500: #00C2FF
- secondary-600: #009FCC

#### Neutral Colors
- neutral-50:  #FAFBFC
- neutral-100: #F4F5F7
- neutral-200: #E8EAED
- neutral-300: #DFE1E6
- neutral-500: #7A869A
- neutral-700: #42526E
- neutral-900: #172B4D

#### Status Colors
- success-500: #00B87C
- warning-500: #FF991F
- error-500:   #E34850
- info-500:    #0066FF

---

### 2.2 Semantic Tokens (Mandatory)

All UI MUST use semantic tokens — never raw colors.

- text.primary: neutral-900
- text.secondary: neutral-700
- text.disabled: neutral-500

- surface.background: #FFFFFF
- surface.card: neutral-50
- surface.hover: neutral-100

- action.primary: primary-500
- action.primary-hover: primary-600
- action.secondary: neutral-200

- border.default: neutral-300
- border.focus: primary-500

- status.success: success-500
- status.warning: warning-500
- status.error: error-500
- status.info: info-500

---

### 2.3 Contrast & WCAG Compliance

Minimum contrast requirements:

**Normal text (≤16px)**
- neutral-900 on white → 12.6:1 ✔
- neutral-700 on white → 7.8:1 ✔
- primary-500 on white → 4.8:1 ✔
- neutral-500 on white → 4.2:1 ⚠ (limit)

**Large text (≥18px or ≥14px bold)**
- All above combinations pass
- secondary-500 on white → 3.1:1 (ONLY for large text)

Rules:
- Never use neutral-500 or lighter for small text
- Never rely on color alone to convey meaning

---

## 3) Typography & Spacing

### 3.1 Font Family
- Primary: Inter
- Fallback: system-ui, sans-serif

### 3.2 Type Scale

(unchanged technical values — canonical)

[H1–Caption preserved exactly as defined]

---

### 3.3 Readability Rules (Mandatory)

- Minimum line-height: 1.5
- Max line length: 75 characters (~600px)
- Text smaller than 14px is forbidden
- Minimum paragraph spacing: 16px

---

### 3.4 Spacing Scale

- xs: 4px
- sm: 8px
- md: 12px
- base: 16px
- lg: 24px
- xl: 32px
- 2xl: 48px
- 3xl: 64px

Spacing consistency is mandatory to reduce cognitive load and support keyboard navigation.

---

## 4) Components (Canonical)

### 4.1 Buttons

#### Primary Button
- Use: main action per screen
- Minimum height: 44px
- Must have visible focus state
- Disabled state MUST block interaction

#### Secondary Button
- Use: cancel, back, alternative actions
- Never styled as primary

#### CTA Button
- Use: critical conversion actions only
- Must not be overused

---

### 4.2 Card
- Used for grouping related content
- Must have clear visual boundaries
- Focus state required if interactive

---

### 4.3 Inputs
- Visible labels are mandatory
- Placeholder is NOT a label
- Error state must include text + visual indicator
- Minimum touch target: 44x44px

---

## 5) Layout & Structure

### Containers
- max-width: 1200px
- responsive padding
- centered layout

### Grid
- Mobile: 4 columns
- Tablet: 8 columns
- Desktop: 12 columns

### Responsiveness
- Mobile-first
- Content priority over decoration
- No hidden critical functionality on mobile

---

## 6) Accessibility (Non-Negotiable)

All UI MUST comply with **WCAG 2.x AA minimum**.

Mandatory rules:
- Keyboard navigation for all actions
- Visible focus indicators
- Semantic HTML landmarks
- Skip links
- Logical focus order
- Support prefers-reduced-motion

Testing:
- NVDA / VoiceOver minimum
- Keyboard-only navigation
- Contrast validation before approval

If accessibility is undefined, STOP and define it.

---

## 7) Tone & Visual Principles

Design values:
- Clarity over decoration
- Consistency over creativity
- Function over aesthetics
- Accessibility over visual trends

The UI must communicate:
- technical competence
- trust
- predictability
- professionalism

---

## 8) Enforcement Rules

- UI that violates this document is INVALID
- Deviations require:
  - justification
  - documentation
  - approval (ADR if structural)

This design system exists to ensure:
- predictable behavior
- inclusive access
- long-term maintainability
