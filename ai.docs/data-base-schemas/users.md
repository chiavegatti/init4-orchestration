# users

## Purpose
Authenticated users. In MVP, each user belongs to exactly one company (tenant).

## Columns
- id: bigint, PK
- public_id: ulid (string 26), unique, not null
- company_id: bigint, FK -> companies.id, not null
- name: varchar(160), not null
- email: varchar(255), not null
- password_hash: varchar(255), not null
- status: varchar(20), not null (active|invited|disabled)
- last_login_at: timestamptz, null
- invited_at: timestamptz, null
- created_at: timestamptz, not null
- updated_at: timestamptz, not null
- deleted_at: timestamptz, null (soft delete)

## Constraints & Indexes
- unique(public_id)
- unique(company_id, email)
- index(company_id)
- index(status)

## Notes
- Email uniqueness is tenant-scoped (company_id + email).
- Authentication and authorization rules are enforced at API level.
