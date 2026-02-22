# Data Visibility Matrix — MVP Contract

This document defines what data fields are visible to each role.
It complements RBAC (route/action permissions) by preventing sensitive data leakage
even when a user has access to a screen.

Roles:
- COMPANY_OWNER
- COMPANY_ADMIN
- COMPANY_USER
- PLATFORM_ADMIN

Rules:
- Tenant data is isolated by default.
- “Need-to-know” principle applies.
- If a field is not explicitly allowed, it must be hidden.

---

## 1) Company / Tenant Profile

### Fields
- company_id (internal)
- company_name
- company_branding (logo/colors, if any)
- primary_contact_email
- billing_contact_email
- default_language
- output_profile_defaults
- created_at
- status (active/suspended)

### Visibility
| Field | OWNER | ADMIN | USER | PLATFORM_ADMIN |
|------|-------|-------|------|----------------|
| company_name | Yes | Yes | Yes | Yes |
| primary_contact_email | Yes | Yes | No | Yes |
| billing_contact_email | Yes | Yes | No | Yes |
| default_language | Yes | Yes | View-only | Yes |
| status | Yes | Yes | Yes | Yes |
| company_id | No (UI) | No (UI) | No (UI) | Yes |

---

## 2) Users (Team)

### Fields
- user_id (internal)
- name
- email
- role
- last_login_at
- invited_at
- status (active/invited/disabled)

### Visibility
| Field | OWNER | ADMIN | USER | PLATFORM_ADMIN |
|------|-------|-------|------|----------------|
| name | Yes | Yes | Yes (list) | Yes |
| email | Yes | Yes | No | Yes |
| role | Yes | Yes | Yes | Yes |
| last_login_at | Yes | Yes | No | Yes |
| invited_at | Yes | Yes | No | Yes |
| status | Yes | Yes | Yes | Yes |
| user_id | No (UI) | No (UI) | No (UI) | Yes |

Notes:
- Regular users can view team list but should not see emails or sensitive metadata.

---

## 3) Clients

### Fields
- client_id (internal)
- public_id
- name
- industry
- web_site
- status (active/archived)
- created_at
- updated_at

### Visibility
| Field | OWNER | ADMIN | USER | PLATFORM_ADMIN |
|------|-------|-------|------|----------------|
| name | Yes | Yes | Yes | Yes |
| industry | Yes | Yes | Yes | Yes |
| web_site | Yes | Yes | Yes | Yes |
| status | Yes | Yes | Yes | Yes |
| created_at | Yes | Yes | Yes | Yes |
| public_id | Yes | Yes | Yes | Yes |

---

## 4) Contacts

### Fields
- contact_id
- client_id
- first_name
- last_name
- email
- phone
- position
- created_at

### Visibility
| Field | OWNER | ADMIN | USER | PLATFORM_ADMIN |
|------|-------|-------|------|----------------|
| first_name | Yes | Yes | Yes | Yes |
| last_name | Yes | Yes | Yes | Yes |
| email | Yes | Yes | Yes | Yes |
| phone | Yes | Yes | Yes | Yes |
| position | Yes | Yes | Yes | Yes |
| created_at | Yes | Yes | Yes | Yes |

---

## 5) Interactions (Notes)

### Fields
- interaction_id
- client_id
- author_id
- content (note)
- type (call/email/meeting/note)
- created_at

### Visibility
| Field | OWNER | ADMIN | USER | PLATFORM_ADMIN |
|------|-------|-------|------|----------------|
| content | Yes | Yes | Yes | Yes |
| type | Yes | Yes | Yes | Yes |
| author_id | Yes | Yes | Yes | Yes |
| created_at | Yes | Yes | Yes | Yes |

---

## 6) API Tokens & Webhooks

### API Tokens Fields
- token_id
- token_name
- token_prefix (masked)
- created_at
- last_used_at
- scopes
- status
- full_secret (only once)

Visibility:
| Field | OWNER | ADMIN | USER | PLATFORM_ADMIN |
|------|-------|-------|------|----------------|
| token_name/scopes/status | Yes | Yes | No | Yes |
| token_prefix (masked) | Yes | Yes | No | Yes |
| last_used_at | Yes | Yes | No | Yes |
| full_secret | Only once | Only once | No | Yes |
| token_id | No (UI) | No (UI) | No | Yes |

### Webhooks Fields
- webhook_id
- url
- events
- secret (masked)
- status
- last_delivery_at
- last_status

Visibility:
| Field | OWNER | ADMIN | USER | PLATFORM_ADMIN |
|------|-------|-------|------|----------------|
| url/events/status | Yes | Yes | No | Yes |
| secret (masked) | Yes | Yes | No | Yes |
| delivery logs (summary) | Yes | Yes | No | Yes |

---

## 7) Billing, Transactions, Ledger (Highly Sensitive)

### Billing Fields
- customer_id (provider)
- invoices
- transactions
- payment_method (masked)
- billing_address (if any)
- tax_id (if any)
- credit_packs purchased
- chargebacks/refunds

Visibility:
| Field | OWNER | ADMIN | USER | PLATFORM_ADMIN |
|------|-------|-------|------|----------------|
| packs purchased (summary) | Yes | Yes | No | Yes |
| invoices/transactions | Yes | Yes | No | Yes |
| payment_method (masked) | Yes | Yes | No | Yes |
| billing_address/tax_id | Yes | Yes | No | Yes |
| chargebacks/refunds | Yes | Yes | No | Yes |
| provider customer_id | No (UI) | No (UI) | No | Yes |

### Credit Ledger Fields
- ledger_entry_id
- type (credit/debit/reserve/release)
- amount
- reason
- resource_type/resource_id
- actor_id
- created_at
- idempotency_key

Visibility:
| Field | OWNER | ADMIN | USER | PLATFORM_ADMIN |
|------|-------|-------|------|----------------|
| amount/type/reason/date | Yes | Yes | No | Yes |
| resource references | Yes | Yes | No | Yes |
| actor_id | Limited** | Limited** | No | Yes |
| idempotency_key | No | No | No | Yes |

*Operator may see high-level “credits remaining” and job estimated cost, not ledger entries.
**Mask actor identity where appropriate; show “system” / “admin action” without exposing personal data unnecessarily.

---

## 8) Audit Logs

Fields:
- audit_id
- action (permission)
- actor_role
- actor_id
- tenant_id
- resource_type/resource_id
- timestamp
- metadata (reason)

Visibility:
| Field | OWNER | ADMIN | USER | PLATFORM_ADMIN |
|------|-------|-------|------|----------------|
| tenant-level audit view | Yes | Yes | No | Yes |
| actor identity | Limited* | Limited* | No | Yes |
| metadata | Yes (sanitized) | Yes (sanitized) | No | Yes |

*For tenant audit logs, avoid exposing personal reviewer identity; keep privacy-friendly.

---

## 9) Implementation Notes (Mandatory)
- Do not rely on UI-only hiding; enforce field filtering server-side (DTO/transformers/resources).
- Prefer explicit serializers per role.
- Default stance: hide sensitive fields unless required.
- Any new data field must be added here with visibility rules.

---

## 10) Privacy & Compliance Notes
- Avoid unnecessary exposure of personally identifiable information (PII).
- Reviewers should not see tenant contact emails or billing details.
- Operators should not see payment history, ledger entries, or API secrets.
