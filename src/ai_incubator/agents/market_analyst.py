"""Market Analyst Agent for the AI Incubator."""

from langchain_community.chat_models import ChatOllama
from langchain_openai import ChatOpenAI

from ai_incubator.config import Config

SYSTEM_PROMPT = (
    "You are a world-class market researcher and startup analyst. "
    "Your analysis is sharp, insightful, and based on verifiable data."
)


def get_market_analyst_llm():
    """Returns a ChatOpenAI instance for the market analyst."""
    if Config.LLM_PROVIDER == "ollama":
        return ChatOllama(model=Config.OLLAMA_MODEL_NAME, temperature=0)
    return ChatOpenAI(model=Config.MODEL_NAME, temperature=0)
