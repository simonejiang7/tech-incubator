"""Nodes for the Incubator Graph."""

from ..agents.market_analyst import get_market_analyst_llm, SYSTEM_PROMPT
from ..tools import tavily_tool
from .state import IncubatorGraphState
from langchain_core.messages import SystemMessage, HumanMessage


def market_analysis_node(state: IncubatorGraphState):
    """
    Analyzes the startup idea and provides a market analysis.
    """
    analyst_llm = get_market_analyst_llm()
    startup_idea = state["startup_idea"]

    # This is a simplified example. In a real-world scenario, you'd
    # likely have a more complex chain or agent here.
    response = analyst_llm.invoke(
        [
            SystemMessage(content=SYSTEM_PROMPT),
            HumanMessage(
                content=f"Analyze the market for a startup focused on: {startup_idea}. "
                f"Use the available tools to gather data."
            ),
        ]
    )

    analysis = response.content
    steps = ["Performed market analysis."]

    return {"market_analysis": analysis, "analysis_steps": steps}