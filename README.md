# AI Incubator

This project is a simple framework for analyzing startup ideas using a graph-based approach with AI agents.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/ai-incubator.git
   cd ai-incubator
   ```

2. **Install dependencies using uv:**
   ```bash
   uv sync
   ```

3. **Set up your environment variables:**
   - Create a `.env` file in the root of the project.
   - Add your API keys to the `.env` file.
   - By default, the project uses OpenAI. To use Ollama, set the `LLM_PROVIDER` variable to `ollama`.

     ```
     # For OpenAI (default)
     LLM_PROVIDER="openai"
     OPENAI_API_KEY="your-openai-api-key"
     TAVILY_API_KEY="your-tavily-api-key"

     # For Ollama
     # LLM_PROVIDER="ollama"
     # OLLAMA_MODEL_NAME="gemma3:4b" # Or any other Ollama model, e.g., llama3, mistral, etc.
     ```

   - **Download the Ollama model:** Before running with Ollama, ensure you have the desired model downloaded. For example, to download `gemma3:4b`:
     ```bash
     ollama run gemma3:4b
     ```

## Usage

To run the application, execute the `main.py` script within the uv-managed environment:

```bash
uv run python main.py
```

This will trigger an analysis of the sample startup idea defined in `main.py` and print the results to the console.
