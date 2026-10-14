from typing import TypedDict
from langgraph.graph import StateGraph

from src.agents.query_agent import query_agent
from src.agents.retrieval_agent import retrieval_agent
from src.agents.sentiment_agent import sentiment_agent
from src.agents.escalation_agent import escalation_agent

class AgentState(TypedDict):

    query: str
    intent: str
    context: str
    sentiment: str
    escalation: bool

builder = StateGraph(AgentState)

builder.add_node(
    "query_agent",
    query_agent
)

builder.add_node(
    "retrieval_agent",
    retrieval_agent
)

builder.add_node(
    "sentiment_agent",
    sentiment_agent
)

builder.add_node(
    "escalation_agent",
    escalation_agent
)

builder.set_entry_point(
    "query_agent"
)

builder.add_edge(
    "query_agent",
    "retrieval_agent"
)

builder.add_edge(
    "retrieval_agent",
    "sentiment_agent"
)

builder.add_edge(
    "sentiment_agent",
    "escalation_agent"
)

builder.set_finish_point(
    "escalation_agent"
)

graph = builder.compile()