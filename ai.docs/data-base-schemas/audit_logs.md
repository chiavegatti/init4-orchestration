# audit_logs

## Purpose
Immutable audit trail for privileged actions and sensitive events.

## Columns
- id: bigint, PK
- public_id: ulid (string 26), unique, not null
- company_id: bigint, null (null for platform-only actions)
- actor_user_id: bigint, FK -> users.id, null
- actor_role: varchar(64), not null
- action: varchar(128), not null (permission name or audited action)
- resource_type: varchar(40), not null (client|contact|interaction|user|role|...)
- resource_id: bigint, not null
- metadata: jsonb, not null (default '{}')
- created_at: timestamptz, not null (default now())

## Constraints & Indexes
- unique(public_id)
- index(company_id, created_at desc)
- index(action)
- index(resource_type, resource_id)

## Notes
- Append-only. No updates.
- Must not leak sensitive details in metadata.
