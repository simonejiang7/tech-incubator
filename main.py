"""Main entry point for the AI Incubator application."""

import os

from dotenv import load_dotenv

from ai_incubator.graph import create_incubator_graph

# Load environment variables from .env file
load_dotenv()


def main():
    """
    Main function to run the AI Incubator.
    """
    # Ensure API keys are set
    if not os.getenv("OPENAI_API_KEY") or not os.getenv("TAVILY_API_KEY"):
        print(
            print(
                "Error: Make sure to set OPENAI_API_KEY and TAVILY_API_KEY "
                "in your .env file."
            )
        )
        return

    app = create_incubator_graph()

    # Define a sample startup idea
    startup_idea = "A platform for AI-powered personalized education."

    initial_state = {
        "startup_idea": startup_idea,
    }

    print(f"Analyzing startup idea: {startup_idea}")

    # Stream the graph execution
    for event in app.stream(initial_state):
        for key, value in event.items():
            print(f"--- Event: {key} ---")
            print(value)
            print("\n")


if __name__ == "__main__":
    main()
