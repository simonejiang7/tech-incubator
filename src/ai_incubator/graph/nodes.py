"""Nodes for the Incubator Graph."""

from langchain_core.messages import HumanMessage, SystemMessage

from ai_incubator.agents.market_analyst import SYSTEM_PROMPT, get_market_analyst_llm
from ai_incubator.graph.state import IncubatorGraphState


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
                content=f"Analyze the market for a startup focused on: "
                f"{startup_idea}. Use the available tools to gather data."
            ),
        ]
    )

    analysis = response.content
    steps = ["Performed market analysis."]

    return {"market_analysis": analysis, "analysis_steps": steps}
