"""Market Analyst Agent for the AI Incubator."""

import logging

from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI

from ai_incubator.config import settings

SYSTEM_PROMPT = (
    "You are a world-class market researcher and startup analyst. "
    "Your analysis is sharp, insightful, and based on verifiable data."
)


def get_market_analyst_llm():
    """Returns a ChatOpenAI instance for the market analyst."""
    try:
        if settings.llm_provider == "ollama":
            return ChatOllama(
                model=settings.ollama_model_name,
                temperature=0,
                timeout=30,  # Add 30 second timeout
            )
        return ChatOpenAI(model=settings.model_name, temperature=0)
    except Exception as e:
        logging.error(f"Failed to connect to LLM: {e}")
        raise
