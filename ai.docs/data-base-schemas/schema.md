# Database Schema — Master Index
## Mini CRM (B2B, Multi-Tenant)

This document is the **canonical index of all data schemas** for the project.

It defines:
- global database conventions
- data modeling rules
- the authoritative list of entities
- navigation to detailed schema definitions

This file does NOT replace entity-level schemas.  
Each table/entity MUST have its own dedicated schema file.

---

## 1. Global Conventions (Mandatory)

### 1.1 Primary Keys

- `id`: bigint auto-increment  
  Internal primary key, used for joins and performance.

- `public_id`: ULID (string, 26 chars)  
  Public identifier exposed via APIs and UI.

Rules:
- APIs MUST expose `public_id`, never internal `id`
- Internal joins MUST use bigint `id`

---

### 1.2 Timestamps

All tables MUST include:
- `created_at`
- `updated_at`

Optional:
- `deleted_at` (soft delete — only if explicitly justified)

---

### 1.3 Multi-Tenant Scope

- All tenant-owned entities MUST include `company_id`
- All queries MUST be tenant-scoped
- Cross-tenant access is forbidden by default

Tenant rules are defined in:
- `ai.docs/02_CONTEXT.md`
- `ai.docs/05_SECURITY_AND_COMPLIANCE.md`

---

### 1.4 Referential Integrity

- All relationships MUST use explicit foreign keys
- No implicit or polymorphic relationships
- Append-only tables MUST be documented as such

---

## 2. Canonical Entity List (MVP)

The following entities define the **MVP data model** for the Mini CRM.

Each entity below links to a detailed schema file that MUST be kept in sync.

---

### 2.1 Tenant & Identity

| Entity | Description | Schema |
|------|-------------|--------|
| companies | B2B tenants (companies) | `companies.md` |
| users | Authenticated users | `users.md` |

---

### 2.2 Authorization (RBAC)

| Entity | Description | Schema |
|------|-------------|--------|
| roles | Role registry | `roles.md` |
| permissions | Atomic permissions | `permissions.md` |
| user_roles | User ↔ role assignments | `user_roles.md` |
| role_permissions | Role ↔ permission mapping | `role_permissions.md` |

---

### 2.3 CRM Core

| Entity | Description | Schema |
|------|-------------|--------|
| clients | Customer accounts | `clients.md` |
| contacts | Contacts per client | `contacts.md` |
| interactions | Immutable interaction records | `interactions.md` |

---

### 2.4 Auditing & Traceability

| Entity | Description | Schema |
|------|-------------|--------|
| audit_logs | Security and audit trail | `audit_logs.md` |

---

## 3. Schema Governance Rules (Mandatory)

- No entity may exist without:
  - an entry in this index
  - a dedicated schema file
- Schema changes MUST be reflected:
  - here (index)
  - in the entity schema file
  - in API contracts
  - in ADRs (`ai.docs/09_DECISIONS_ADR.md`) if impactful
- APIs MUST NOT expose fields not defined in schemas
- UX MUST NOT display data not allowed by schema + permissions

---

## 4. Schema Evolution

Any schema evolution MUST:
- be backward compatible, OR
- introduce a versioned change with migration strategy

Breaking changes require:
- PRD update
- API versioning
- ADR

---

## 5. Notes for AI (Mandatory)

When generating or modifying data models:

- Do not invent entities or fields
- Do not infer relationships
- Always consult this index first
- If an entity is missing, request clarification

This file is the **source of truth** for all data modeling decisions.

---

## 6. Scope Reminder

This document defines **what data exists and where it is documented**.

It does NOT define:
- API behavior
- business rules
- UX flows
- infrastructure

Those concerns belong to their respective documents.
