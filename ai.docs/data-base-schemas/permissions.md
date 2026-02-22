# permissions

## Purpose
Atomic permission registry used by RBAC.

Examples:
- clients.read
- clients.create
- clients.update
- clients.delete
- contacts.read
- contacts.create
- interactions.create
- users.manage
- roles.manage

## Columns
- id: bigint, PK
- name: varchar(128), unique, not null
- scope: varchar(20), not null (company|platform)
- created_at: timestamptz, not null
- updated_at: timestamptz, not null

## Constraints & Indexes
- unique(name)
- index(scope)

## Notes
- Permissions are mapped to roles via `role_permissions`.
