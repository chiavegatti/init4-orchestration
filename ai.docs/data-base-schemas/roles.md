# roles

## Purpose
Role registry for RBAC.

Canonical roles (initial):
- COMPANY_OWNER (scope: company)
- COMPANY_ADMIN (scope: company)
- COMPANY_USER  (scope: company)
- PLATFORM_ADMIN (scope: platform)

## Columns
- id: bigint, PK
- name: varchar(64), unique, not null
- scope: varchar(20), not null (company|platform)
- created_at: timestamptz, not null
- updated_at: timestamptz, not null

## Constraints & Indexes
- unique(name)
- index(scope)

## Notes
- Role behavior is enforced through permissions.
