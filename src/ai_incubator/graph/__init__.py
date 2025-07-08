"""Main graph assembly for the AI Incubator."""

from langgraph.graph import END, StateGraph

from .nodes import market_analysis_node
from .router import should_continue
from .state import IncubatorGraphState


def create_incubator_graph():
    """
    Creates the main incubator graph.
    """
    graph = StateGraph(IncubatorGraphState)

    graph.add_node("market_analysis", market_analysis_node)

    graph.set_entry_point("market_analysis")

    graph.add_conditional_edges(
        "market_analysis",
        should_continue,
        {
            "continue": "market_analysis",  # Loop in a real scenario
            "end": END,
        },
    )

    return graph.compile()
