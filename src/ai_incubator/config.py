"""Configuration for the AI Incubator project."""

import os


class Config:
    """Simple configuration class."""

    LLM_PROVIDER = os.getenv("LLM_PROVIDER", "openai")
    MODEL_NAME = "gpt-4o"
    OLLAMA_MODEL_NAME = os.getenv("OLLAMA_MODEL_NAME", "llama3")
