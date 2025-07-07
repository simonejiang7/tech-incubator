"""Router for the Incubator Graph."""

from ai_incubator.graph.state import IncubatorGraphState


def should_continue(state: IncubatorGraphState):
    """
    Determines whether to continue the analysis or end.
    """
    if state.get("market_analysis"):
        return "end"
    return "continue"
