"""State definition for the Incubator Graph."""

from typing import List, TypedDict


class IncubatorGraphState(TypedDict):
    """Represents the state of our graph."""

    startup_idea: str
    market_analysis: str
    analysis_steps: List[str]
