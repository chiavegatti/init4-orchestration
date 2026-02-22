# API Contracts
## INIT4 Cognitive Orchestrator — v1 MVP

## 1. Purpose

This document defines the **API contract layer** for the INIT4 Cognitive Orchestrator.

It specifies:
- the core endpoints for LLM routing
- the internal endpoints for metrics and monitoring
- the payload structures required to enforce deterministic routing

---

## 2. Core Principles (Mandatory)

- APIs MUST be designed before implementation
- No endpoint may be implemented without a documented request/response schema.
- The Cognitive Orchestrator acts as a drop-in replacement for OpenAI endpoints (via LiteLLM proxying).
- Custom routing metadata must be passed via standard channels (e.g., specific HTTP headers or injected metadata fields in the JSON payload).

---

## 3. Public Endpoints (Client Facing)

### 3.1 LLM Chat Completions Proxy
`POST /v1/chat/completions`

**Description:** Standard OpenAI-compatible format for generating text via LLMs. The orchestrator intercepts this, extracts metadata, routes the request, and returns the response in the exact same format.

**Required Custom Metadata for Routing:**
To ensure deterministic execution, clients MUST pass metadata defining the task. This can be sent via standard LiteLLM `metadata` attributes in the request body.

**Example Request:**
```json
{
  "model": "auto", // The orchestrator determines the actual model
  "messages": [
    { "role": "user", "content": "Extract details from this invoice..." }
  ],
  "metadata": {
    "task_type": "extraction",
    "tenant_id": "client-abc",
    "force_local": true
  }
}
```

**Response:** standard OpenAI ChatCompletion object.

---

## 4. Internal Endpoints (Metrics & Admin)

These endpoints are for administrative use only and MUST NOT be exposed to the public internet.

### 4.1 Usage Summary
`GET /metrics/summary`

**Description:** Returns aggregated usage and cost statistics for a given time period or tenant.

**Response Schema (Draft):**
```json
{
  "total_requests": 15420,
  "total_cost_usd": 14.52,
  "local_fallback_count": 25,
  "average_latency_ms": 230
}
```

### 4.2 Raw Request Logs
`GET /metrics/requests`

**Description:** Returns a paginated list of individual request logs for auditing.

**Query Parameters:**
- `limit` (default: 50)
- `offset` (default: 0)
- `tenant_id` (optional filter)
- `task_type` (optional filter)

---

## 5. Error Handling

- Errors MUST follow a consistent JSON structure.
- Do NOT leak internal database errors, provider API keys, or stack traces.
- Standard HTTP status codes apply:
  - `400 Bad Request`: Missing mandatory metadata (`task_type`).
  - `401 Unauthorized`: Invalid service API key.
  - `502 Bad Gateway`: Underlying requested LLM failed and no fallback succeeded.

---

## 6. Governance

Any change to API behavior (e.g., adding a new standard OpenAI endpoint like `/v1/embeddings`) MUST update:
- This document (`07_API_CONTRACTS.md`)
- `08_DATA_SCHEMA.md` (if logging logic changes)
- `09_DECISIONS_ADR.md`
