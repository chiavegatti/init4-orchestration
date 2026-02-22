# TASK-2026-02-19 — Create Client CRUD (API Only)

## Objective
Implement CRUD endpoints for `clients` entity with tenant isolation.

## In Scope
- POST /clients
- GET /clients
- GET /clients/{id}
- PUT /clients/{id}

## Out of Scope
- UI screens
- Bulk import
- Soft delete

## Required References
- PRD: ai.docs/03_PRD.md (Clients section)
- Schema: ai.docs/data-base-schemas/clients.md
- API: ai.docs/07_API_CONTRACTS.md
- Security: ai.docs/05_SECURITY_AND_COMPLIANCE.md

## Impact Analysis
- Data model changes? No
- API changes? Yes (new endpoints)
- ADR required? No

## Functional Requirements
- FR-01: Create client scoped by company_id
- FR-02: Prevent cross-tenant access
- FR-03: Validate required fields

## Acceptance Criteria
- Endpoints return correct responses
- Unauthorized access returns 403
- Tests cover tenant isolation
