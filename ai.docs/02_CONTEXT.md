# Project Context — INIT4 Cognitive Orchestrator

## 1. Purpose

This project exists to build the **INIT4 Cognitive Orchestrator — v1 MVP**.

The orchestrator serves as the central intelligent routing and policy engine for AI requests. It is designed to evaluate requests and deterministically direct them to either local models (e.g., via Ollama) or cloud models (e.g., OpenAI, Anthropic) based on predefined policies, constraints, and tasks, aiming for a "local-first" approach to optimize costs and security.

This documentation strictly defines the scope, constraints, APIs, and data models required to build a reliable and auditable AI execution orchestrator.

---

## 2. What This System Is (Conceptual)

The reference system is a **Policy & Routing Engine** with the following conceptual goals:

- Orquestrar corretamente requisições de IA.
- Aplicar de forma determinística uma policy "local-first".
- Registrar logs completos de uso, performance e custo.
- Calcular custos estimados de requisições.
- Permitir fallback resiliente de modelos locais para cloud.
- Preparar a estrutura base de dados/endpoints para dashboards de métricas futuros (sem necessitar do dashboard UI no MVP).

---

## 3. Core Principles

- Documentation-first, execution-oriented.
- Deterministic routing and fallback over "smart AI decision-making".
- Local-first execution to reduce costs and latency where possible.
- Complete traceability and auditability of tokens, costs, and timings.
- API-first mindset.

---

## 4. Priorities

1. Clear routing boundaries (Local vs Cloud).
2. Well-defined execution logs schema (`requests` table).
3. Stable and explicit API contracts for task execution (Chat, Vision, Audio, etc.).
4. Accurate cost estimation via static configurations.
5. Reliable fallback mechanisms.

---

## 5. Constraints & Boundaries

- Este sistema **NÃO** inclui agentes autônomos na v1.
- Este sistema **NÃO** faz classificação semântica "mágica" para decidir rotas (decisões devem ser determinísticas baseadas em tamanho, tipo ou flag simples).
- Este sistema **NÃO** inclui um dashboard UI (Admin UI) na v1, mas deixa a API de métricas pronta.
- Este sistema **NÃO** suporta faturamento (billing) complexo ou multi-tenant avançado na v1.

A meta é controle técnico absoluto sobre a requisição, log e fallback.

---

## 6. Design Philosophy

- Deterministic policy engine without AI intervention.
- Simple, static rules for model selection and fallback logic (e.g. `try_local(timeout) else use_cloud()`).
- High visibility: Every request must be logged with timestamp, duration, token usage, and cost.
- Modular architecture allowing the addition of new task types across sprints (Chat -> Vision -> Audio -> Multi-modal).

---

## 7. Important Notes for AI (Mandatory)

When using AI models to implement features in this project context:

- Do not invent non-deterministic routing rules unless explicitly guided by the policy files.
- Do not add complex user isolation, subscription or billing databases.
- If information regarding a specific route or fallback logic is missing, request clarification.
- Treat schemas and APIs documents as strict contracts.

---

## 8. Engineering Governance (Mandatory)

This project adopts strict engineering practices to reinforce predictability and quality:

- No routing rule may be implemented without a documented requirement.
- The logging schema (`requests`) must be immutable/append-only logic.
- Cost metrics are always estimates based on static tables (`MODEL_COST`), not dynamic API queries.
- Decisions on infrastructure (e.g., LiteLLM, FastAPI) or routing policies must be recorded in `09_DECISIONS_ADR.md`.

---

## 9. Scope Reminder

This file defines **context only**.

Detailed requirements belong in:
- `03_PRD.md`

Architectural decisions belong in:
- `04_ARCHITECTURE.md`

Security and routing isolation rules belong in:
- `05_SECURITY_AND_COMPLIANCE.md`
