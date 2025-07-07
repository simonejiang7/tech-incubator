"""Main entry point for the AI Incubator application."""

import logging
import os

from dotenv import load_dotenv

from ai_incubator.graph import create_incubator_graph

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def main():
    """
    Main function to run the AI Incubator.
    """
    # Ensure API keys are set
    if not os.getenv("OPENAI_API_KEY") or not os.getenv("TAVILY_API_KEY"):
        logger.error(
            "Error: Make sure to set OPENAI_API_KEY and TAVILY_API_KEY "
            "in your .env file."
        )
        return

    app = create_incubator_graph()

    # Define a sample startup idea
    startup_idea = "A platform for AI-powered personalized education."

    initial_state = {
        "startup_idea": startup_idea,
    }

    logger.info(f"Analyzing startup idea: {startup_idea}")

    # Stream the graph execution
    for event in app.stream(initial_state):
        for key, value in event.items():
            logger.info(f"--- Event: {key} ---")
            logger.info(value)
            logger.info("\n")


if __name__ == "__main__":
    main()
