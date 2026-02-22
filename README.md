# INIT4 Cognitive Orchestrator

![Python Validated](https://img.shields.io/badge/python-3.11-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110.0-009688.svg)
![Docker](https://img.shields.io/badge/Docker-Enabled-2CA5E0.svg)

The **INIT4 Cognitive Orchestrator** is the central routing and policy engine ("Middle-Layer") for Artificial Intelligence calls in the INIT4 project. Built on top of FastAPI and operating as a transparent intelligent proxy via LiteLLM, it does not think for itself (it is not an agent), but rather it acts as a **Deterministic Routing Engine** focused on cost reduction, resilience, and auditing.

## What is it for?
1. **Local-First Routing**: Upon receiving OpenAI-Compatible requests from your frontend/backend application, it uses its internal Policy Engine to inspect the payload's `metadata`. If a user requests an `extraction` task, the orchestrator actively rewrites the target and sends it to the local/free cloud model (`ollama/mistral:latest`), saving extremely high API costs, all invisibly to the end user.
2. **Resilience and Fallbacks**: If the local LLaMA/Mistral goes down or is rate-limited, the Orchestrator doesn't crash. It retries up to 3 times through an automatic "Fallback Chaining" loop, falling back to cloud models like `openai/deepseek-chat` or `gpt-4o-mini` if the primary model fails.
3. **Auditing and Monitoring (Metrics)**: Every request generates an immutable Log (Input tokens, Output tokens, Calculated numeric cost via Pricing Table, and Latency) in a PostgreSQL database.
4. **Integrated API Endpoint**: An endpoint already aggregates all this data to be listed by an Administrative Dashboard (`/v1/metrics`), accounting for the financial usage of the AI.

## How to Use (Quick Start)

### 1. Requirements
- [Docker](https://www.docker.com/) and Docker Compose installed.
- A local/remote instance of [LiteLLM Proxy](https://docs.litellm.ai/) or Native Provider.

### 2. Setting Up Keys
Copy the development template and populate it with your real keys (URL and Key):
```bash
cp .env.example .env
```
*(In the `.env` file, change `LITELLM_API_BASE` to the location of your remote proxy/model and `LITELLM_API_KEY` to your API Key, or insert the Cloud key.)*

### 3. Running the Application
The project orchestrates a Postgres Database, Redis Cache, and FastAPI API with a single command in a self-contained manner.
```bash
docker-compose up -d --build
```
> The database (Alembic) will automatically run migrations to the latest version!

### 4. Accessing Interfaces and APIs
* FastAPI Health Check: `http://localhost:8000/health`
* Swagger / Automatic OpenAPI: `http://localhost:8000/docs`
* Dashboard Metrics MVP: `http://localhost:8000/v1/metrics`

### Importing into Postman for Testing
There is a file generated for you in the root directory: **`init4_orchestrator.postman_collection.json`**. 
- Open Postman.
- Click **"Import"**.
- Drag and drop this `.json` file.
- Fire the **"Chat Completions (Proxy)"** route, playing around with different `"task_type"` values (`extraction`, `reasoning`) in the JSON to see Routing and Fallbacks happening in practice.

---
## CI Pipeline and Code Quality
The repository already features automated Actions at a production standard (flake8, unit tests with pytest, black formatter). Every push to Main block and evaluates the health of the orchestration codebase. Run local tests with:
```bash
docker-compose exec orchestrator bash -c "pytest tests/"
```
