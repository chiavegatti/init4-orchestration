from typing import Dict, Optional

# Static mapping for the deterministic routing policy
# task_type -> model_string
# This is a v1 MVP implementation, mapping known tasks directly to their designated models.

ROUTING_RULES: Dict[str, str] = {
    # Simple formatting/extraction: highly suited for local LLMs
    "extraction": "ollama/mistral:latest",
    "summarization": "ollama/mistral:latest",
    "translation": "ollama/mistral:latest",
    # Complex tasks: might require cloud capabilities or heavy reasoning in v1
    "reasoning": "openai/deepseek-chat",
    "complex_coding": "openai/deepseek-chat",
    "vision": "ollama/qwen3-vl:8b",
    # Fallback/default logic
    "default_local": "ollama/mistral:latest",
    "default_cloud": "gpt-4o-mini",
}

# Mapping of which model to fallback to if the primary one fails
FALLBACK_RULES: Dict[str, str] = {
    # If our local mistral goes down or the server is busy, fallback to a cheap and fast cloud model
    "ollama/mistral:latest": "gpt-4o-mini",
    # If the default cloud goes down, fallback to deepseek
    "gpt-4o-mini": "openai/deepseek-chat",
    # If reasoning model fails, fallback to gpt-4o-mini
    "openai/deepseek-chat": "gpt-4o-mini",
    # Vision models fallback
    "ollama/qwen3-vl:8b": "gpt-4o-mini",
}
