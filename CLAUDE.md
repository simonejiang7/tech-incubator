# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

AI Incubator is a graph-based startup analysis framework using LangGraph and LangChain. The application analyzes startup ideas through AI agents and provides market analysis using either OpenAI or Ollama models.

## Development Commands

### Environment Setup
```bash
# Install dependencies
uv sync

# Run the application
uv run python main.py

# Install pre-commit hooks
pre-commit install
```

### Code Quality
```bash
# Format code
black .

# Sort imports
isort --profile black .

# Lint code
flake8

# Type checking
mypy .

# Run all pre-commit hooks
pre-commit run --all-files
```

### Testing
```bash
# Run tests
pytest

# Run tests with coverage
pytest --cov=ai_incubator
```

## Architecture

### Core Components

- **Graph-based execution**: Uses LangGraph StateGraph for workflow orchestration
- **Agent system**: Market analyst agent with configurable LLM providers
- **State management**: TypedDict-based state tracking through IncubatorGraphState
- **Configuration**: Pydantic Settings with .env file support

### Key Files

- `main.py`: Application entry point with sample startup analysis
- `src/ai_incubator/config.py`: Settings management with pydantic-settings
- `src/ai_incubator/graph/`: Graph workflow definition and state management
  - `state.py`: IncubatorGraphState TypedDict definition
  - `nodes.py`: Graph node implementations (market_analysis_node)
  - `router.py`: Conditional logic for graph flow control
- `src/ai_incubator/agents/market_analyst.py`: LLM provider abstraction with error handling

### LLM Provider Configuration

The system supports both OpenAI and Ollama through configuration:
- Set `LLM_PROVIDER=openai` (default) or `LLM_PROVIDER=ollama`
- Default models: `gpt-4o` for OpenAI, `gemma2:9b` for Ollama
- Ollama includes 30-second timeout for connection reliability

### Environment Variables

Required for OpenAI:
- `OPENAI_API_KEY`
- `TAVILY_API_KEY`

Optional configuration:
- `LLM_PROVIDER` (openai/ollama)
- `MODEL_NAME` (for OpenAI)
- `OLLAMA_MODEL_NAME` (for Ollama)

## Code Style

- Uses Black for formatting with line length 120 (flake8 configured)
- isort with Black profile for import sorting
- Type hints enforced with mypy
- Pre-commit hooks ensure code quality
