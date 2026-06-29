from typing import TypedDict, List


class SupportState(TypedDict):
    ticket: str

    category: str
    priority: str
    sentiment: str

    customer_id: str
    customer_context: dict

    retrieved_docs: List[str]

    root_cause: str

    resolution: List[str]

    confidence_score: int

    escalate: bool

    escalation_reason: str

    final_response: str