# companies (tenants)

## Purpose
Represents a B2B tenant (company). All tenant data is scoped by `company_id`.

## Columns
- id: bigint, PK
- public_id: ulid (string 26), unique, not null
- name: varchar(160), not null
- primary_contact_email: varchar(255), null
- status: varchar(20), not null  (active|suspended)
- created_at: timestamptz, not null
- updated_at: timestamptz, not null
- deleted_at: timestamptz, null (optional soft delete)

## Constraints & Indexes
- unique(public_id)
- index(status)

## Notes
- Tenant isolation is mandatory across all tables.
- If soft delete is enabled, ensure queries default to `deleted_at is null`.
