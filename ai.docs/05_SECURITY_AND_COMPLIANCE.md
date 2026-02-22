# Security and Compliance
## INIT4 Cognitive Orchestrator — v1 MVP

## 1. Purpose

This document defines the **mandatory security and compliance guidelines** for the INIT4 Cognitive Orchestrator.

These rules are **constraints**, not suggestions.  
They influence architecture, routing policies, APIs, and operational decisions.

---

## 2. Security Principles (Baseline)

The system MUST adhere to the following principles:

- **Deterministic Routing as Security:** AI models MUST NOT autonomously decide which endpoints, tools, or models to call. Routing is strictly controlled by predefined, deterministic rules.
- **Least privilege by default:** Access to the orchestrator and downstream models is explicitly granted via API keys.
- **Secure-by-default configuration:** Fallbacks and timeouts must fail safely without leaking internal architecture details.
- **No trust based on client-side validation.**

---

## 3. Authentication & Authorization

### 3.1 Service-Level Authentication
- All access to the Orchestrator MVP MUST be authenticated via service-level API keys (e.g., Bearer tokens).
- The Orchestrator acts as the trusted gateway and holds the actual provider API keys (OpenAI, Anthropic, etc.).
- Downstream clients **never** receive or handle the actual provider keys.

### 3.2 Endpoint Authorization
- The core completion API (`/v1/chat/completions`) requires standard client API keys.
- Internal metrics and administration APIs (e.g., `/metrics`) MUST NOT be exposed to the public internet and should require separate administrative authentication.

---

## 4. Safe Logging Practices

### 4.1 Request and Response Logging
- The orchestrator logs complete request and response payloads to PostgreSQL for auditability and cost tracking.
- **PII and Sensitive Data:** For the v1 MVP, raw payloads may be logged. However, the system architecture MUST support the future addition of PII-scrubbing middleware before persistence. Clients should be advised to avoid sending highly sensitive compliance-bound data (e.g., PCI/HIPAA) unless explicitly supported by the deployed local model.

### 4.2 Error Handling and Leakage
- Never leak sensitive details (like provider API keys, database connection strings, or internal stack traces) in API error responses.
- API errors must be sanitized and standardized.

---

## 5. Local-First Policies and Data Privacy

- The "Local-First" routing policy is inherently a privacy feature. 
- Requests designated for local models (e.g., via Ollama) ensure that data never leaves the internal network.
- The policy engine MUST guarantee that tasks strictly flagged for local execution **cannot** fallback to cloud models, even if the local model fails.

---

## 6. Audit & Traceability

The system MUST record audit events for:

- Every incoming LLM request and its routing decision.
- The actual model used for execution.
- Token counts and calculated static costs.
- Failures, timeouts, and fallback triggers.

Audit logs in the PostgreSQL database must be **append-only** and immutable.

---

## 7. Compliance Awareness

This orchestrator enables compliance for downstream applications by providing:

- Centralized traceability of AI logic execution.
- Predictable cost and usage attribution.
- Data sovereignty options (via local models).

This document does **not** replace project-specific legal or regulatory assessments for the data being processed.

---

## 8. Governance

Any change affecting security, routing policies, or data access MUST update:

- this document
- related API contracts (`07_API_CONTRACTS.md`)
- relevant ADRs (`09_DECISIONS_ADR.md`)