from langgraph.graph import StateGraph

from app.models.state import SupportState

from app.agents.triage_agent import triage_agent
from app.agents.customer_context_agent import customer_context_agent
from app.agents.retrieval_agent import retrieval_agent
from app.agents.root_cause_agent import root_cause_agent
from app.agents.resolution_agent import resolution_agent
from app.agents.escalation_agent import escalation_agent
from app.agents.final_response_agent import final_response_agent


workflow = StateGraph(SupportState)

workflow.add_node("triage", triage_agent)

workflow.add_node(
    "customer_context",
    customer_context_agent
)

workflow.add_node(
    "retrieval",
    retrieval_agent
)

workflow.add_node(
    "root_cause",
    root_cause_agent
)

workflow.add_node(
    "resolution",
    resolution_agent
)

workflow.add_node(
    "escalation",
    escalation_agent
)

workflow.add_node(
    "final_response",
    final_response_agent
)

workflow.set_entry_point("triage")

workflow.add_edge(
    "triage",
    "customer_context"
)

workflow.add_edge(
    "customer_context",
    "retrieval"
)

workflow.add_edge(
    "retrieval",
    "root_cause"
)

workflow.add_edge(
    "root_cause",
    "resolution"
)

workflow.add_edge(
    "resolution",
    "escalation"
)

workflow.add_edge(
    "escalation",
    "final_response"
)

support_graph = workflow.compile()