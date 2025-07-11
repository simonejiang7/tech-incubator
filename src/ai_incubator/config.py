"""Configuration for the AI Incubator project."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Simple configuration class."""

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )

    llm_provider: str = "openai"
    model_name: str = "gpt-4o"
    ollama_model_name: str = "gemma2:9b"


settings = Settings()
