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
   - Add your API keys to the `.env` file:
     ```
     OPENAI_API_KEY="your-openai-api-key"
     TAVILY_API_KEY="your-tavily-api-key"
     ```

## Usage

To run the application, execute the `main.py` script within the uv-managed environment:

```bash
uv run python main.py
```

This will trigger an analysis of the sample startup idea defined in `main.py` and print the results to the console.