# Data Schema & Specifications
## INIT4 Cognitive Orchestrator — v1 MVP

## 1. Purpose

This document defines the **canonical data model** for the INIT4 Cognitive Orchestrator.

The orchestrator relies on a PostgreSQL database primarily for **audit logging, metrics, and cost tracking**. All routing policies and static costs are currently managed in code or environment configurations, not in the database for v1.

## 2. General Rules

- **Schema-First Development:** Database tables MUST be defined here before implementation.
- **Append-Only:** Audit and request logs are append-only. No `UPDATE` or `DELETE` operations are permitted on historical logs.
- **No ORM Magic:** Explicitly define relationships (if any) and constraints.
- **UUIDs:** Primary keys MUST use `UUID` (v4).

---

## 3. Core Entities

### 3.1 `requests` (Audit & Metric Logs)

This is the primary table for the Orchestrator, recording every AI request processed by the gateway.

| Field | Type | Description |
| :--- | :--- | :--- |
| `id` | `UUID` | Primary Key. |
| `timestamp` | `TIMESTAMP (UTC)` | Exact time the request was received. |
| `tenant_id` | `VARCHAR` | (Optional) Upstream tenant or application identifier. |
| `task_type` | `VARCHAR` | The mapped task category (e.g., `extraction`, `coding`). |
| `requested_model` | `VARCHAR` | (Optional) The model requested by the client, if any. |
| `routed_model` | `VARCHAR` | The actual model the policy engine routed to (e.g., `ollama/llama3`). |
| `input_tokens` | `INTEGER` | Tokens consumed in the prompt. |
| `output_tokens` | `INTEGER` | Tokens generated in the response. |
| `estimated_cost` | `DECIMAL(10, 6)` | Calculated static cost in USD. |
| `latency_ms` | `INTEGER` | Total time taken by the LLM provider. |
| `status` | `VARCHAR` | Execution result (`success`, `fallback_used`, `failed`). |
| `error_message` | `TEXT` | (Optional) Populated only if `status` is `failed`. |

---

## 4. Cost Configuration (Conceptual)

For the MVP, costs are statically mapped in the application layer (e.g., via a YAML or JSON configuration file within the policy engine), not the database.

*Example internal structure:*
- `ollama/llama3`: { input: 0.0, output: 0.0 }
- `gpt-4o-mini`: { input: 0.150, output: 0.600 } / 1M tokens

*Note: Future versions may migrate this mapping to a `model_pricing` table.*

---

## 5. Schema Evolution

- Breaking changes to the schema (e.g., dropping columns) are strictly prohibited without an ADR.
- New fields can be added via standard migration scripts (e.g., Alembic).

---

## 6. Access Control

- Downstream clients have **no direct access** to this database.
- The FastAPI orchestrator application uses a dedicated service account with write-only (append) access to the `requests` table, and read access for the `/metrics` endpoints.
