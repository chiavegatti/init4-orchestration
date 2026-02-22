# interactions

## Purpose
Immutable interaction records (notes/events) linked to a client.

## Rules
- Interactions are append-only:
  - no updates after creation
  - deletions should be avoided; if required, must be audited

## Columns
- id: bigint, PK
- public_id: ulid (string 26), unique, not null
- company_id: bigint, FK -> companies.id, not null
- client_id: bigint, FK -> clients.id, not null
- author_user_id: bigint, FK -> users.id, not null
- type: varchar(20), not null (note)
- content: text, not null
- created_at: timestamptz, not null (default now())

## Constraints & Indexes
- unique(public_id)
- index(company_id, client_id, created_at desc)
- index(author_user_id)

## Notes
- If future types are added, they must be documented in PRD and API contracts.
