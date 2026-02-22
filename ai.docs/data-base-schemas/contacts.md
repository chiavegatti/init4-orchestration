# contacts

## Purpose
Contacts linked to a client (people inside the client organization).

## Columns
- id: bigint, PK
- public_id: ulid (string 26), unique, not null
- company_id: bigint, FK -> companies.id, not null
- client_id: bigint, FK -> clients.id, not null
- name: varchar(160), not null
- email: varchar(255), null
- phone: varchar(40), null
- role_title: varchar(120), null
- created_at: timestamptz, not null
- updated_at: timestamptz, not null
- deleted_at: timestamptz, null (optional soft delete)

## Constraints & Indexes
- unique(public_id)
- index(company_id, client_id)
- index(client_id)

## Notes
- Contacts are tenant-scoped and client-scoped.
