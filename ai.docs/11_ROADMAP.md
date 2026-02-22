# Project Roadmap
## INIT4 Cognitive Orchestrator — v1 MVP

## 1. Purpose

This document outlines the sequential implementation sprints for the Orchestrator MVP. Each sprint builds upon the previous one to deliver a reliable, deterministic AI routing engine.

---

## 2. MVP Sprints

### Sprint 1: Architecture & Setup
- [x] Initialize FastAPI project structure (`ai.docs/06_BOILERPLATE_STRUCTURE.md`).
- [x] Define and migrate PostgreSQL schema (`ai.docs/08_DATA_SCHEMA.md`).
- [x] Integrate LiteLLM basic pass-through.

### Sprint 2: Core Routing & Logging
- [x] Implement `POST /v1/chat/completions` proxy endpoint.
- [x] Capture request and response payloads.
- [x] Asynchronously write to the `requests` audit table.

### Sprint 3: Policy Engine v1
- [x] Implement deterministic mapping logic based on `task_type` metadata.
- [x] Route requests selectively to local Ollama endpoints vs cloud providers.

### Sprint 4: Cost Estimation & Fallback
- [x] Integrate static cost calculators based on token usage and mapped model prices.
- [x] Implement retry logic and fallback chaining (e.g., Local LLaMA fails -> fallback to GPT-4o-mini).

### Sprint 5: Tool Calling Pass-through & CI/CD
- [x] Ensure the orchestrator transparently handles standard OpenAI function/tool calling structures for both local and cloud models where supported.
- [x] Added automated tests and CI Pipelines inside Github Actions setup.

### Sprint 6: Analytics API & Polish
- Develop internal `GET /metrics` endpoints to expose usage and cost data.
- Finalize documentation and end-to-end testing against the Release Checklist (`ai.docs/12_RELEASE_CHECKLIST.md`).

---

## 3. Post-MVP (Future Considerations)
- Admin Dashboard UI.
- Semantic Caching (Redis).
- Dynamic Pricing API integration.
- PII Scrubbing Middleware.
