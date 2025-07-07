"""Tools for the Incubator Graph."""

import os

from dotenv import load_dotenv
from langchain_tavily import TavilySearch

load_dotenv()

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
tavily_tool = TavilySearch(max_results=5, tavily_api_key=TAVILY_API_KEY)
