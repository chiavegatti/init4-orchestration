# API Exposure Matrix — MVP Contract

This document defines what the public API exposes:
- Endpoints
- Methods
- Fields returned
- Fields accepted (write)
- Authentication scope
- Rate limits (high level)
- What is INTERNAL ONLY (never exposed publicly)

The public API must never expose more data than the UI.
Any new endpoint or field requires updating this document.

---

## 1) API Principles

- All API requests are tenant-scoped via API token.
- API tokens have scopes mapped to permissions (see permission-glossary.md).
- No API endpoint returns billing PII or secrets.
- All write operations must be idempotent where applicable.
- Responses must be versioned (`/v1`).

Base URL:
- `POST /api/v1/*`

Auth:
- Bearer token (API Token)
- Scopes enforced server-side

---

## 2) Public API — Endpoints (MVP)

### 2.1 Clients

#### List Clients
- `GET /api/v1/clients`
- Scope: `clients.read`
- Returns: List of clients (public_id, name, industry, status)

#### Create Client
- `POST /api/v1/clients`
- Scope: `clients.create`
- Accepts: name, industry, web_site
- Returns: client object with public_id

#### Get Client Detail
- `GET /api/v1/clients/{public_id}`
- Scope: `clients.read`
- Returns: Full client details

#### Update Client
- `PATCH /api/v1/clients/{public_id}`
- Scope: `clients.update`
- Accepts: name, industry, web_site, status

---

### 2.2 Contacts

#### List Contacts
- `GET /api/v1/clients/{client_id}/contacts`
- Scope: `contacts.read`
- Returns: List of contacts for the client

#### Create Contact
- `POST /api/v1/clients/{client_id}/contacts`
- Scope: `contacts.create`
- Accepts: first_name, last_name, email, phone, position
- Returns: contact object

---

### 2.3 Interactions

#### List Interactions
- `GET /api/v1/clients/{client_id}/interactions`
- Scope: `interactions.read`
- Returns: Timeline of interactions

#### Create Interaction
- `POST /api/v1/clients/{client_id}/interactions`
- Scope: `interactions.create`
- Accepts: content, type
- Returns: interaction object
- Note: Immutable once created.

---

---

### 2.4 API Usage & Quotas

#### Usage Summary
- `GET /api/v1/usage`
- Scope required: `usage.view`
- Returns: active_users, clients_count, interactions_last_30d

---

## 3) Rate Limits (High Level)

Per API token:
- Default: 60 req/min
- Burst: 120 req/min
- Batch upload endpoints: custom limits per tenant plan

Rules:
- 429 on limit exceeded
- Include rate limit headers

---

## 4) Webhooks (Outbound)

Supported events:
- client.created
- contact.created
- interaction.created

Payload (public fields only):
- event_type
- timestamp
- tenant_id (public)
- resource_id
- status
- summary fields

Never include:
- PII
- billing data
- secrets
- internal job ids

---

## 5) Error Model (Public)

Standard error response:
- code
- message (user-safe)
- details (optional, sanitized)
- request_id

Never expose:
- stack traces
- internal exception messages
- provider errors verbatim

---

## 6) Versioning & Deprecation

- API version in URL: `/api/v1`
- Deprecations require:
  - 90-day notice
  - documentation update
  - changelog entry
- Breaking changes require new version (`/v2`)

---

## 7) Security Notes

- Tokens are tenant-scoped and permission-scoped.
- All endpoints validate tenant ownership of `project_id`, `item_id`, `export_id`.
- Signed URLs must expire (e.g., 5–15 minutes).
- Webhook signatures must be verified by clients.

---

## 8) Internal-Only APIs (Not Public)
- Admin ops
- Reviewer assignment
- Billing provider callbacks
- Ledger manipulation
- Model orchestration endpoints
- Internal job queue controls

These endpoints must be on a private network / protected route group.
