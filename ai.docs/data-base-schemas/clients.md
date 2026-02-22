# clients

## Purpose
Core CRM entity representing an account/customer inside a tenant.

## Columns
- id: bigint, PK
- public_id: ulid (string 26), unique, not null
- company_id: bigint, FK -> companies.id, not null
- created_by_user_id: bigint, FK -> users.id, not null
- name: varchar(200), not null
- email: varchar(255), null
- phone: varchar(40), null
- status: varchar(20), not null (active|inactive)
- created_at: timestamptz, not null
- updated_at: timestamptz, not null
- deleted_at: timestamptz, null (optional soft delete)

## Constraints & Indexes
- unique(public_id)
- index(company_id, created_at desc)
- index(company_id, status)
- unique(company_id, email) WHERE email IS NOT NULL

## Notes
- All reads and writes must be tenant-scoped (company_id).
- Soft delete is optional; if used, ensure API and UX reflect it.
