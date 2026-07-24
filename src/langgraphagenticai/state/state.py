from typing import Annotated, List
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages


class State(TypedDict, total=False):
    messages: Annotated[List, add_messages]
    news_data: list
    summary: str
    filename: str

