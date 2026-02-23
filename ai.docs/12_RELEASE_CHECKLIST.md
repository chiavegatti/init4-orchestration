# Release Checklist
## INIT4 Cognitive Orchestrator — v1 MVP

## 1. Purpose

This checklist defines the **Definition of Done** for releasing the MVP of the Cognitive Orchestrator. No release may occur unless all conditions below are satisfied.

---

## 2. Core Functionality & Determinism

- [x] **Pass-Through Accuracy:** Orchestrator transparently passes and receives standard OpenAI-compatible requests and responses.
- [x] **Routing Determinism:** Requests with specific `task_type` metadata are correctly routed to their designated local/cloud model without hallucinated routing decisions.
- [x] **Tool Calling:** The orchestrator correctly proxies tool/function schemas to supporting models without dropping metadata.

## 3. Resilience & Fallback

- [x] **Timeout Handling:** Requests gracefully time out if the primary model hangs.
- [x] **Fallback Chain:** When a primary local model is simulated to fail (e.g., stopping Ollama), the request successfully falls back to the designated cloud model.

## 4. Logging & Auditing

- [x] **Log Completeness:** Every processed request writes exactly one row to the `requests` table in PostgreSQL.
- [x] **Cost Calculation:** Static cost is correctly calculated and logged based on token counts resulting from the completion.
- [x] **Error Logging:** Failed requests (without successful fallbacks) are logged with non-leaking, sanitized error messages.

## 5. Security & Isolation

- [x] **Authentication:** `POST /v1/chat/completions` correctly rejects requests without a valid service-level API key.
- [x] **Metrics Protection:** Internal metrics APIs (e.g., `/metrics`) are secured with a separate administrative API key.
- [x] **Key Secrecy:** Upstream provider API keys (OpenAI, Anthropic) are never exposed in error traces or response payloads.

## 6. Architecture & Code Quality

- [x] **Test Coverage:** Automated tests cover at least 90% of the routing logic, fallback mechanics, and cost calculation.
- [x] **Statelessness:** The FastAPI application maintains no in-memory state that would break horizontal scaling.
- [x] **Documentation Alignment:** Implementation exactly matches the schemas defined in `07_API_CONTRACTS.md` and `08_DATA_SCHEMA.md`.
