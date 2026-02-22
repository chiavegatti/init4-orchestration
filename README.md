# INIT4 Cognitive Orchestrator

![Python Validated](https://img.shields.io/badge/python-3.11-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110.0-009688.svg)
![Docker](https://img.shields.io/badge/Docker-Enabled-2CA5E0.svg)

O **INIT4 Cognitive Orchestrator** é o motor central ("Middle-Layer") de roteamento e políticas para chamadas de Inteligência Artificial do projeto INIT4. Construído em cima do FastAPI e operando como um proxy inteligente transparente via LiteLLM, ele não pensa por si mesmo (não é um agente), mas sim um **Agente de Roteamento Determinístico**, focado em redução de custo, resiliência, e auditoria.

## Para Que Serve?
1. **Roteamento Local-First**: Ao receber requisições OpenAI-Compatíveis da sua aplicação de frontend/backend, ele usa a engine de Políticas Interna (Policy Engine) para inspecionar `metadata` do payload. Se um usuário pedir uma tarefa de `extraction`, o orquestrador reescreve ativamente o alvo e manda para a nuvem local/gratuita (`ollama/mistral:latest`), economizando custos altíssimos de API, tudo de forma invisível para o usuário da ponta.
2. **Resiliência e Fallbacks**: Se o LLaMA/Mistral local cair ou estiver limit-rate, o Orchestrator não trava. Ele tenta 3 vezes com um loop automático de "Fallback Chaining", recuando para modelos de nuvem como `openai/deepseek-chat` ou `gpt-4o-mini` caso o primário falhe.
3. **Auditoria e Monitoramento (Metrics)**: Toda requisição gera um Log imutável (Input tokens, Output tokens, Custo calculado numérico via Tabela de Preços e Latência) em um banco de dados PostgreSQL.
4. **Endpoint API Integrado**: Um endpoint já agrega tudo isso para ser listado por um Dashboard Administrativo (`/v1/metrics`), contabilizando uso financeiro da IA.

## Como Usar (Quick Start)

### 1. Requisitos
- [Docker](https://www.docker.com/) e Docker Compose instalados.
- Uma instância local/remota de [LiteLLM Proxy](https://docs.litellm.ai/) ou Provedor Nativo.

### 2. Configurando as Chaves
Copie o template de desenvolvimento e popule suas chaves reais (URL e Key):
```bash
cp .env.example .env
```
*(No arquivo `.env`, altere o `LITELLM_API_BASE` para o local do seu proxy/modelo remoto e `LITELLM_API_KEY` para sua API Key ou insira a chave da Cloud.*)

### 3. Subindo a Aplicação
O projeto orquestra Banco de Dados Postgres, Redis Cache e API FastAPI com apenas um comando e de forma auto-contida.
```bash
docker-compose up -d --build
```
> O banco de dados (Alembic) já executará as migrações automáticas para a versão mais recente!

### 4. Acessando as Interfaces e APIs
* FastAPI Health Check: `http://localhost:8000/health`
* Swagger / OpenAPI Automático: `http://localhost:8000/docs`
* Dashboard Metrics MVP: `http://localhost:8000/v1/metrics`

### Importando no Postman para Testes
Existe um arquivo gerado para você na raiz: **`init4_orchestrator.postman_collection.json`**. 
- Abra o Postman.
- Clique em **"Import"**.
- Arraste esse arquivo `.json`.
- Dispare a rota **"Chat Completions (Proxy)"** brincando com diferentes `"task_type"` (`extraction`, `reasoning`) no JSON para ver o Roteamento e Fallbacks acontecendo na prática.

---
## Pipeline e Qualidade de Código (CI)
O repositório já conta com Actions automatizados no padrão de produção (flake8, unit tests com pytest, formatter black). Toda subida na Main bloqueia e avalia a saúde da nova orquestração. Rode testes locais com:
```bash
docker-compose exec orchestrator bash -c "pytest tests/"
```
