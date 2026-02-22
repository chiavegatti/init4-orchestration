# Architecture Decision Records (ADR)
## INIT4 Cognitive Orchestrator — v1 MVP

## 1. Purpose

This document records the **significant architectural and technical decisions** made for the INIT4 Cognitive Orchestrator.

These decisions are **append-only**. If a decision is reversed or modified later, a new ADR must be created superseding the old one.

---

## 2. ADR Log

### ADR 001: Use LiteLLM for Standardized Provider Access

**Date:** 2026-02  
**Status:** Accepted  

**Context:** The Orchestrator needs to speak to multiple local models (via Ollama) and cloud providers (OpenAI, Anthropic). Building and maintaining custom API clients for each provider would be a massive overhead and point of failure.

**Decision:** We will use **LiteLLM** as the core gateway proxy within our FastAPI application. LiteLLM standardizes all inputs and outputs to the OpenAI API format, allowing universal integration.

**Consequences:** 
- Downstream clients only need to know how to speak the OpenAI API format.
- We rely on the LiteLLM library to maintain compatibility with provider API changes.

---

### ADR 002: Static Cost Calculation

**Date:** 2026-02  
**Status:** Accepted  

**Context:** Accurately calculating the cost of AI requests requires knowing the exact provider pricing for input and output tokens at the time of execution. Relying on an external API or dynamic database query blocks the execution flow and adds latency.

**Decision:** We will implement **Static Cost Calculation** mapped in the application layer (e.g., via a config dictionary or YAML file) mapping model names to their prices per million tokens. The orchestrator will multiply tokens used by this static rate at runtime.

**Consequences:** 
- Drastically reduces latency and removes external dependencies for cost estimation.
- Requires manual updates to the static pricing file when providers change their rates.
- Accepted as a necessary trade-off for the v1 MVP.

---

### ADR 003: Deterministic Rule-Based Routing

**Date:** 2026-02  
**Status:** Accepted  

**Context:** Request routing could technically be done by using a "router LLM" to semantically classify user intents and forward the request. However, this introduces high latency, cost, and unpredictable non-deterministic behavior.

**Decision:** We will strictly use **Deterministic Rule-Based Routing**. Downstream clients must pass an explicit metadata tag (e.g., `task_type`) or rely on a strict set of routing tables coded into the `Policy Engine`, rather than relying on AI to route AI.

**Consequences:** 
- Routes are 100% predictable, testable, and auditable.
- Fails safely and immediately if a rule does not match.
- Places the burden of identifying the `task_type` on the downstream client application making the request.

---
