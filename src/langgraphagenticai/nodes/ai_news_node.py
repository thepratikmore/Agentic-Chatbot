import os

from tavily import TavilyClient
from langchain_core.prompts import ChatPromptTemplate


class AINewsNode:
    def __init__(self, llm):
        """
        Initialize the AI News node.
        """
        self.tavily = TavilyClient()
        self.llm = llm
        self.state = {}

    def fetch_news(self, state: dict) -> dict:
        """
        Fetch AI news based on the selected frequency.
        """

        frequency = state["messages"][0].content.lower()

        self.state["frequency"] = frequency

        time_range_map = {
            "daily": "d",
            "weekly": "w",
            "monthly": "m",
            "year": "y",
        }

        days_map = {
            "daily": 1,
            "weekly": 7,
            "monthly": 30,
            "year": 366,
        }

        response = self.tavily.search(
            query="Top Artificial Intelligence (AI) technology news India and globally",
            topic="news",
            time_range=time_range_map.get(frequency, "d"),
            include_answer="advanced",
            max_results=20,
            days=days_map.get(frequency, 1),
        )

        state["news_data"] = response.get("results", [])

        self.state["news_data"] = state["news_data"]

        return state

    def summarize_news(self, state: dict) -> dict:
        """
        Summarize fetched news using the LLM.
        """

        news_items = state.get("news_data", [])

        prompt_template = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    """
Summarize AI news articles into markdown.

For each news article include:
- Date (YYYY-MM-DD)
- Short summary
- Source URL

Sort from latest to oldest.

Output format:

### YYYY-MM-DD
- Summary
- Source: URL
""",
                ),
                ("user", "Articles:\n{articles}"),
            ]
        )

        articles = "\n\n".join(
            [
                f"""
Title: {item.get('title', '')}
Content: {item.get('content', '')}
URL: {item.get('url', '')}
Date: {item.get('published_date', '')}
"""
                for item in news_items
            ]
        )

        messages = prompt_template.format_messages(
            articles=articles
        )

        response = self.llm.invoke(messages)

        state["summary"] = response.content

        self.state["summary"] = state["summary"]

        return state

    def save_result(self, state: dict) -> dict:
        """
        Save the summarized AI news to a markdown file.
        """

        frequency = self.state.get("frequency", "daily")
        summary = self.state.get("summary", "")

        os.makedirs("AINews", exist_ok=True)

        filename = f"AINews/{frequency}_summary.md"

        with open(filename, "w", encoding="utf-8") as file:
            file.write(f"# {frequency.capitalize()} AI News Summary\n\n")
            file.write(summary)

        state["filename"] = filename

        return state