# Boilerplate Structure — Project Rules
## INIT4 Cognitive Orchestrator — v1 MVP

## 1. Purpose

Define a clear and enforceable repository structure for:
- orchestration application code (FastAPI)
- documentation (ai.docs)
- operational scaffolding (Docker, DB migrations)

This document is a **structural contract**.  
LLMs and contributors must not invent folders or move files without recording decisions.

---

## 2. Repository Rules (Mandatory)

- Any scope change MUST update the PRD and (if needed) create/update an ADR.
- Do not generate code before validating scope impact in `03_PRD.md`.
- The canonical execution order is defined by the numbered `.md` files in the repository root (`ai.docs/`).
- Do NOT create new top-level directories without updating `09_DECISIONS_ADR.md`.

---

## 3. Engineering Rules (Mandatory)

- It is forbidden to commit code without automated tests.
- Minimum global test coverage required: **90%**.
- Every change must occur in a dedicated branch.
- The `main` branch must remain stable and production-ready.
- Direct commits to `main` are forbidden.
- Merges to `main` only via Pull Request with review.
- CI must block merges if tests fail or coverage < 90%.

---

## 4. Notes for AI (Mandatory)

- Never invent requirements, schemas or permissions.
- If a file is missing required definitions, request clarification.
- Always propose tests alongside any generated code.
- Respect deterministic routing constraints defined in `02_CONTEXT.md` and `03_PRD.md`.

---

# Repository Structure Reference (Contract for LLMs)

## 5. Root Structure (Normative)

/
├── README.md
├── ai.docs/                 (Canonical documentation startkit)
│   ├── 01_README_AI.md
│   ├── ...
│   └── 12_RELEASE_CHECKLIST.md
├── src/                     (Orchestrator Application Code - FastAPI)
│   ├── api/                 (FastAPI routes and controllers)
│   ├── policy/              (Deterministic routing logic & mappings)
│   ├── gateway/             (LiteLLM integration layers)
│   ├── models/              (Data models and Pydantic schemas)
│   ├── db/                  (Database connection and query logic)
│   └── main.py              (FastAPI entry point)
├── migrations/              (PostgreSQL schema migrations - e.g., Alembic)
├── tests/                   (Automated test suites)
└── ops/                     (Operational scaffolding)
    ├── docker/              (Dockerfiles and Docker Compose for DB/Redis)
    └── ci/                  (GitHub Actions or similar CI configs)

Notes:
- The orchestrator logic strictly resides in `src/`.
- `src/gateway/` is where all LiteLLM-specific configuration and proxy handling is managed.
- Internal local model configurations (e.g., Ollama endpoints) are handled via environment variables mapped in the `src/policy/` or `src/gateway/` setup.

---

## 6. Placement Rules (Mandatory)

- All application code MUST live inside `src/`.
- Documentation and AI contracts remain in `ai.docs/`.
- Database schemas and logic changes affecting structure go into `migrations/`.
- No generated application code is allowed outside `src/`.

---

## 7. Change Control

Any change to repository structure MUST:
- be documented in `09_DECISIONS_ADR.md`
- keep the canonical documentation flow intact
- avoid breaking links referenced by README and numbered docs

---

## 8. Scope Reminder

This file defines **where things live**, not product behavior.

Behavior belongs in:
- `03_PRD.md`

Security constraints belong in:
- `05_SECURITY_AND_COMPLIANCE.md`

API contracts belong in:
- `07_API_CONTRACTS.md`

Schemas belong in:
- `08_DATA_SCHEMA.md`
