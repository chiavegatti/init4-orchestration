from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "INIT4 Cognitive Orchestrator"

    # Database
    DATABASE_URL: str = "postgresql://postgres:postgres@db:5432/orchestrator"

    # LiteLLM Proxy setup
    LITELLM_API_BASE: str = "http://localhost:4000"
    LITELLM_API_KEY: str = ""

    # Pydantic reading from the local .env file (if it exists)
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )


settings = Settings()
