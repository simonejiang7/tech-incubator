"""Tools for the Incubator Graph."""
import os
from langchain_tavily import TavilySearch
from dotenv import load_dotenv

load_dotenv()

tavily_tool = TavilySearch(max_results=5, tavily_api_key=os.getenv("TAVILY_API_KEY"))