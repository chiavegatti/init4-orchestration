# Permission Glossary (Atomic Permissions) — MVP Contract

This document defines canonical, atomic permissions used across:
- Laravel policies/middleware
- UI gating (secondary)
- API authorization
- Audit logging rules

Roles must map to permissions explicitly.
No route/action may exist without a corresponding permission.

---

## 1) Naming Convention
Permissions follow the format:

<domain>.<resource>.<action>

Examples:
- clients.create
- contacts.view
- interactions.create

Actions:
- view
- list
- create
- update
- delete
- manage (dangerous / privileged)
- approve (review actions)
- download (exports)

---

## 2) Domains & Permissions

### 2.1 Tenant / Company
- company.profile.view
- company.profile.update
- company.settings.view
- company.settings.update

### 2.2 Team & Roles
- team.members.list
- team.members.view
- team.members.invite
- team.members.update_role
- team.members.remove

### 2.3 Clients
- clients.list
- clients.view
- clients.create
- clients.update
- clients.archive

### 2.4 Contacts
- contacts.list
- contacts.view
- contacts.create
- contacts.update

### 2.5 Interactions
- interactions.list
- interactions.view
- interactions.create

### 2.6 API & Webhooks
- api.tokens.manage
- api.usage.view

### 2.7 Billing
- billing.view
- billing.history.view

### 2.10 Audit & Logs (Tenant)
- audit.view (tenant-level audit for own company)

---

---

---

## 5) Role → Permissions Mapping (MVP)

### 5.1 COMPANY_OWNER
Grants everything within tenant scope:
- All `company.*`
- All `team.*`
- All `clients.*`
- All `contacts.*`
- All `interactions.*`
- All `api.*`
- All `billing.*`
- audit.view

### 5.2 COMPANY_ADMIN
Same as owner for MVP.

### 5.3 COMPANY_USER
Operational permissions only:
- company.profile.view
- team.members.list
- clients.list
- clients.view
- contacts.*
- interactions.*
- api.usage.view

### 5.4 PLATFORM_ADMIN
Full platform control.

---

## 6) Audit Logging Rules (Mandatory)

Any action requiring audit logs:
- api.tokens.manage
- billing.view
- clients.archive

Audit entry minimum fields:
- actor_id
- actor_role
- tenant_id (when applicable)
- action (permission name)
- resource_type + resource_id
- timestamp
- metadata (reason, notes)

---

## 7) Notes
- UI gating is secondary; authorization must be enforced server-side.
- Every route/action must map to one or more permissions above.
- New permissions require updating this file + PRD if scope changes.
