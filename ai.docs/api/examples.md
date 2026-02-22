# API Examples
## Reference Payloads — Mini CRM

Auth header (required for all requests):
Authorization: Bearer <token>

---

## General Rules

- All requests assume authenticated users
- Tenant context is derived from the token
- Fields not shown MUST NOT be assumed
- Responses include only documented fields
- All examples follow API v1

---

## POST /api/v1/clients

Create a new client inside the current tenant.

Request:
```json
{
  "name": "Acme Corporation",
  "email": "contact@acme.com",
  "status": "active"
}

Response 201:
```json
{
  "id": "01J0Z9Q5M0V4D3JH8W2Z6J2S2K",
  "name": "Acme Corporation",
  "email": "contact@acme.com",
  "status": "active",
  "created_at": "2026-02-07T23:40:00Z"
}

GET /api/v1/clients

List clients visible to the current user.

Response 200:
```json
{
  "data": [
    {
      "id": "01J0Z9Q5M0V4D3JH8W2Z6J2S2K",
      "name": "Acme Corporation",
      "status": "active"
    }
  ]
}
GET /api/v1/clients/{clientId}

Get client details.

Response 200:
```json
{
  "id": "01J0Z9Q5M0V4D3JH8W2Z6J2S2K",
  "name": "Acme Corporation",
  "email": "contact@acme.com",
  "status": "active",
  "created_at": "2026-02-07T23:40:00Z"
}

POST /api/v1/clients/{clientId}/interactions

Create a new interaction (note).

Request:
```json
{
  "type": "note",
  "content": "Initial contact with procurement team."
}

Response 201:
```json
{
  "id": "01J0Z9R1B8T3T2H4Q7P1E0F9AA",
  "client_id": "01J0Z9Q5M0V4D3JH8W2Z6J2S2K",
  "type": "note",
  "content": "Initial contact with procurement team.",
  "author_id": "01J0USER123",
  "created_at": "2026-02-07T23:45:00Z"
}
Error Model (Standard)

Response 422:
```json
{
  "code": "VALIDATION_ERROR",
  "message": "Invalid payload",
  "request_id": "req_01J0ZABCD123",
  "details": {
    "name": ["The name field is required."]
  }
}
