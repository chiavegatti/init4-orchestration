# Access Control Matrix (RBAC) — MVP Contract

This document defines access rules for:
- Routes
- Actions
- Data visibility
- Tenant isolation

No screen/route may be implemented without mapping it here.

---

## 1) Roles (Canonical)

### Company (Tenant) Roles
- **COMPANY_OWNER**: Full control within tenant (billing, users, API, settings)
- **COMPANY_ADMIN**: Same as owner except ownership-critical actions
- **COMPANY_USER**: Operational usage (clients, contacts, interactions)

### Platform Roles
- **PLATFORM_ADMIN**: Full platform control (support, global management)

---

## 2) Global Security Rules (Mandatory)

### Tenant Isolation
- All `/app/*` routes MUST be scoped to `company_id` (tenant).
- A company user MUST NEVER access another company’s projects, assets, exports, billing, or tokens.
- API tokens are company-scoped and enforce tenant isolation at the API layer.

### Platform Admin Isolation
- Platform Admin can access all tenants.
- All admin actions must be logged in audit logs.

### Logging / Audit
Audit logs are mandatory for:
- Billing & credit adjustments
- Token creation/revocation
- Tenant suspension/reactivation
- Review approvals/returns
- Export generation and downloads

---

## 3) Route-Level Access Matrix (MVP)

Legend:
- R = Read
- W = Write/Create/Update
- A = Admin action (dangerous/privileged)
- N/A = not allowed

### 3.1 Public Routes
| Route | Access |
|------|--------|
| GET / | Public |
| GET /pricing | Public |
| GET /docs/api | Public |
| GET /contact | Public |
| GET /legal/terms | Public |
| GET /legal/privacy | Public |

### 3.2 Auth & Onboarding
| Route | COMPANY_OWNER | COMPANY_ADMIN | COMPANY_USER | PLATFORM_ADMIN |
|------|---------------|---------------|--------------|----------------|
| /auth/* | R/W | R/W | R/W | R/W |
| /onboarding/* | R/W | R/W | N/A | N/A |

Notes:
- Onboarding is only for newly created tenants.
- Users cannot run onboarding.

Notes:
- Onboarding is only for newly created tenants.
- Operators cannot run onboarding.

### 3.3 Client App — Dashboard
| Route | OWNER | ADMIN | USER |
|------|-------|-------|------|
| GET /app/dashboard | R | R | R |

### 3.4 Client App — Clients
| Route | OWNER | ADMIN | USER |
|------|-------|-------|------|
| GET /app/clients | R | R | R |
| GET /app/clients/new | W | W | N/A |
| POST /app/clients | W | W | N/A |
| GET /app/clients/{id} | R | R | R |
| GET /app/clients/{id}/edit | W | W | N/A |
| PUT /app/clients/{id} | W | W | N/A |

### 3.5 Client App — Contacts (Client-scoped)
| Route | OWNER | ADMIN | USER |
|------|-------|-------|------|
| GET /app/clients/{id}/contacts | R | R | R |
| GET /app/clients/{id}/contacts/new | W | W | W |
| POST /app/clients/{id}/contacts | W | W | W |
| GET /app/clients/{id}/contacts/{id} | R | R | R |
| GET /app/clients/{id}/contacts/{id}/edit | W | W | W |

### 3.6 Client App — Interactions (Timeline)
| Route | OWNER | ADMIN | USER |
|------|-------|-------|------|
| GET /app/clients/{id}/interactions | R | R | R |
| POST /app/clients/{id}/interactions | W | W | W |

Rules:
- Interactions are immutable (no Edit/Delete).
- Author is captured from session.

### 3.7 Client App — API Access
| Route | OWNER | ADMIN | USER |
|------|-------|-------|------|
| GET /app/api | R | R | R |
| GET /app/api/tokens | R/W | R/W | N/A |
| POST /app/api/tokens | A | A | N/A |
| DELETE /app/api/tokens/{id} | A | A | N/A |

### 3.8 Client App — Team & Permissions
| Route | OWNER | ADMIN | USER |
|------|-------|-------|------|
| GET /app/team | R/W | R/W | R |
| POST /app/team/invite | A | A | N/A |
| PATCH /app/team/members/{u_id} | A | A | N/A |

### 3.9 Client App — Billing
| Route | OWNER | ADMIN | USER |
|------|-------|-------|------|
| GET /app/billing | R/W | R/W | N/A |
| GET /app/billing/history | R | R | N/A |

Rules:
- Only privileged roles can initiate checkout.
- Ledger is read-only and must be auditable.
- Operators may see pack offerings (read-only).

---

---

Rules:
- All admin actions must require confirmation UI.
- All admin actions must be audit-logged.
- Credit adjustments require a reason field.

---

## 4) Action-Level Rules (Critical)

### Interaction Rules
- Interactions are immutable once created.
- The author user_id is automatically captured.
- Tenant isolation is strictly enforced.

---

## 7) Future (Out of MVP)
- PLATFORM_SUPPORT (read-only ops with limited actions)
- REVIEWER_LEAD (assign reviewers, prioritize queue)
- Enterprise roles (compliance officer)

---

## 8) Implementation Notes (Non-Functional)
- RBAC must be enforced at:
  - Route middleware
  - Query scoping
  - Service layer
- Never trust client-side gating.
- Always log privileged actions.
