# System Architecture
## INIT4 Cognitive Orchestrator — v1 MVP

## 1. Overview

This document defines the **high-level system architecture** for the INIT4 Cognitive Orchestrator.

The architecture is intentionally:
- simple,
- deterministic,
- local-first,
- API-first,
- and highly auditable.

It focuses on **responsibilities and boundaries** for routing AI requests, tracking costs, and logging execution metrics.

---

## 2. Architectural Principles

- **API-first:** All orchestration functionality is accessible via API.
- **Local-first Routing:** Prefer local models (e.g., Ollama) to optimize cost and data privacy where eligible.
- **Deterministic Policy:** Routing decisions must be based on explicit rules, not autonomous AI reasoning.
- **Immutable Auditability:** Every request and routing decision must be logged permanently.
- **Resilience:** Graceful fallback mechanisms from local to cloud providers.

---

## 3. High-Level Components

### 3.1 Orchestrator API (FastAPI)

Responsibilities:
- Intercept incoming AI requests from downstream applications.
- Extract task metadata and constraints.
- Execute the routing policy.
- Handle fallback and retry logic.
- Log transactions to the database.

This is the **core engine** enforcing all business and routing rules.

---

### 3.2 Policy Engine (Internal Module)

Responsibilities:
- Evaluate the `task_type` and requested constraints.
- Consult the deterministic mapping to select the primary target model.
- Determine the eligible fallback chain if the primary model fails.

---

### 3.3 LLM Gateway (LiteLLM)

Responsibilities:
- Provide a standardized integration layer (OpenAI-compatible SDK) to all underlying model providers.
- Pass translated requests to local models (Ollama) or cloud APIs (OpenAI, Anthropic).
- Handle underlying API formatting nuances.

---

### 3.4 Database Layer (PostgreSQL)

Responsibilities:
- Persist all request and response metadata.
- Store cost estimations and execution metrics.
- Support querying for analytics and dashboards.

Characteristics:
- PostgreSQL relational database.
- Append-only schema for request logs.

---

### 3.5 Caching Layer (Optional - Redis)

Responsibilities:
- Cache frequent, identical deterministic requests to reduce LLM overhead and costs.
- Store rate-limiting counters.

*Note: Redis is considered an optional enhancement for later phases of the MVP.*

---

## 4. Execution Flow

1. **Client** sends request to Orchestrator API (FastAPI).
2. **Orchestrator** parses the request and invokes the **Policy Engine**.
3. **Policy Engine** deterministically assigns a target model (e.g., Local Llama 3).
4. **Orchestrator** forwards the formatted request via **LiteLLM Gateway** to the selected Local/Cloud Model.
5. Model generates a response and returns it to the Orchestrator via LiteLLM.
6. **Orchestrator** calculates estimated statically-defined costs.
7. **Orchestrator** logs the entire transaction (metrics, latency, cost) asynchronously to **PostgreSQL**.
8. **Client** receives the final response.

---

## 5. Deployment Model

- **Gateway/Orchestrator:** Containerized stateless service (Docker).
- **Database:** Managed PostgreSQL instance.
- **Local LLMs:** Separate GPU-enabled server/container running Ollama or similar.

---

## 6. Security Boundaries

- Service-to-service authentication via secure API keys.
- Orchestrator must hold the actual provider API keys (OpenAI, Anthropic); downstream clients only hold Orchestrator keys.
- No direct database modifications allowed outside the Orchestrator API.

Detailed security rules are defined in:
- `05_SECURITY_AND_COMPLIANCE.md`

---

## 7. Scalability & Evolution (Conceptual)

The architecture allows future evolution via:
- horizontal scaling of the FastAPI orchestrator layer.
- adding message queues (e.g., Celery/RabbitMQ) for asynchronous batch request handling.
- integrating semantic caching mechanisms.

These are **design allowances**, not MVP requirements.

---

## 8. Out of Scope

This architecture does not cover:
- Infrastructure-as-Code (Terraform, etc.) provisioning scripts.
- Admin Dashboard UI implementation (only the backend metrics APIs are in scope).
- Semantic intent classification (using an LLM to decide routing).

---

## 9. Architecture Governance

Any architectural change MUST:
- be documented here.
- reference an ADR in `09_DECISIONS_ADR.md`.
- respect existing API and data contracts.
