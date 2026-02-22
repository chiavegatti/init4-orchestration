# user_roles

## Purpose
Many-to-many mapping between users and roles (RBAC assignment).

This table defines which roles a user has.
In MVP, users still belong to a single company via `users.company_id`, but role assignment is independent and explicit.

## Columns
- user_id: bigint, FK -> users.id, not null
- role_id: bigint, FK -> roles.id, not null
- created_at: timestamptz, not null
- created_by_user_id: bigint, FK -> users.id, null (recommended for auditability)

## Constraints & Indexes
- primary key (user_id, role_id)
- index(role_id)
- index(user_id)

## Notes
- Role assignment changes should be audited in `audit_logs`.
- `created_by_user_id` is optional but recommended to track who granted the role.
- If you need tenant-scoped role assignment in the future, create an ADR and extend the model accordingly.
