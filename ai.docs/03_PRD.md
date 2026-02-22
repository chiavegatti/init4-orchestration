# Product Requirements Document (PRD)
## INIT4 Cognitive Orchestrator — v1 MVP

Version: 1.0  
Status: Reference – Ready for Execution  
Owner: Product / Tech Lead  
Date: 2026-02  

---

## 1. Overview

### 1.1 Problem Statement

As AI adoption scales across multiple internal and client-facing tools, directly integrating applications with cloud LLMs (like OpenAI or Anthropic) introduces significant challenges:
- High and unpredictable API costs.
- Lack of centralized logging, visibility, and auditability.
- Inability to enforce security, data privacy, or a "local-first" execution policy without modifying every downstream application.

This PRD defines the **INIT4 Cognitive Orchestrator v1 MVP**, designed to resolve these issues by acting as an intelligent routing and policy engine acting as a gateway for all AI requests.

---

### 1.2 Proposed Solution

A **deterministic AI request orchestrator** that intercepts requests, evaluates them against predefined policies, and routes them to the appropriate model (local or cloud). It provides:

- Deterministic local-first execution policies based on task type.
- Unified, centralized logging of requests, responses, models used, and latency.
- Cost estimation and tracking for every request.
- Graceful fallbacks from local to cloud models if required.
- A standardized API layer using LiteLLM to maintain compatibility with existing OpenAI SDK clients.

This system is intentionally limited in v1 to remain predictable, serving as a reliable backbone rather than an autonomous agent.

---

## 2. Target Users

- Internal engineering teams building AI-powered applications.
- System administrators needing cost and usage visibility.
- Product teams enforcing data privacy policies (ensuring specific data stays local).

---

## 3. MVP Goals

The MVP MUST provide:

- **Correct Orchestration:** Accurately parse and route requests.
- **Local-First Policy:** Always attempt to fulfill eligible requests using local models (e.g., Ollama) before falling back to cloud providers.
- **Complete Logging:** 100% capture of incoming requests, model selections, execution outcomes, and latency.
- **Cost Estimation:** Statically calculate and log the estimated cost of each transaction.
- **Resilient Fallback:** Automatically retry with secondary/cloud models if the primary model fails or times out.

---

## 4. Core Functional Requirements

### 4.1 Request Interception and Formatting
- Expose an API endpoint that mirrors or wraps standard LLM communication protocols (via LiteLLM).
- Extract necessary metadata (task type, tokens, constraints) for routing decisions.

### 4.2 Deterministic Routing Policy Engine
- Maintain a configuration map mapping `task_type` to specific models.
- Support logic to prioritize local models (e.g., Llama 3 via Ollama) for simple tasks (summarization, simple extraction).
- Route complex tasks (complex coding, advanced reasoning) to cloud models.

### 4.3 Execution & Fallback Mechanism
- Execute the request against the selected LLM provider.
- Implement a timeout and retry mechanism.
- If a local model fails, fallback to a pre-defined cloud alternative.

### 4.4 Logging and Metrics
- Log every single request to a PostgreSQL database.
- Key metrics to capture: Request ID, timestamp, original app/tenant (if applicable), routed model, latency (ms), input tokens, output tokens, total cost, success/failure status.

### 4.5 Cost Engine
- Maintain a static pricing table for supported models.
- Calculate cost post-execution and append it to the transaction log.

---

## 5. App Capabilities (Sprint Progression)

- **Sprint 1 (Architecture & Setup):** Basic FastAPI setup, DB schema creation, LiteLLM integration.
- **Sprint 2 (Core Routing & Logging):** Simple pass-through routing, initial DB logging for requests and responses.
- **Sprint 3 (Policy Engine v1):** Implementation of deterministic "local-first" logic based on static rules.
- **Sprint 4 (Cost Estimation & Fallback):** Integration of the static cost calculator and retry/fallback logic.
- **Sprint 5 (Tool Calling Pass-through):** Ensuring the orchestrator correctly handles and passes along OpenAI-style tool calling parameters.
- **Sprint 6 (Analytics API & Polish):** Developing internal metrics endpoints for future dashboards (`GET /metrics`).

---

## 6. Security & Access Rules (High-Level)

- Service-level authentication via API keys.
- No direct external internet access to the admin/metrics endpoints.
- Secure handling of provider API keys (OpenAI, Anthropic).
- No sensitive PII leakage in application-level error logs.
- Detailed rules in: `05_SECURITY_AND_COMPLIANCE.md`

---

## 7. Non-Functional Requirements

- **Latency:** The orchestrator must add minimal overhead (<50ms processing time, excluding LLM generation time).
- **Throughput:** Must handle concurrent requests gracefully, leveraging async I/O.
- **Determinism:** Routing decisions must be predictable and strictly follow the defined policy matrix.
- **Auditability:** Logs must be append-only and immutable.

---

## 8. Out of Scope (MVP)

- Autonomous agent behavior or "AI reasoning" to decide routing (must be deterministic rules).
- Semantic classification of intents (using an LLM to decide where to route an LLM request).
- A web-based Dashboard UI (v1 provides the API data only).
- Complex, dynamic billing engines or tenant quotas.
- Multi-region deployments.

---

## 9. Success Criteria

- The orchestrator successfully routes a local-first request.
- The orchestrator successfully logs a transaction with accurate token counts and calculated static cost.
- Fallback mechanics are proven to work when a primary model is simulated to fail.
- All API contracts and schemas match the implementation exactly.

---

## 10. Change Governance

Any change to scope or behavior MUST update:

- this PRD
- API contracts (`07_API_CONTRACTS.md`)
- data schemas (`08_DATA_SCHEMA.md`)
- decision records (`09_DECISIONS_ADR.md`)
