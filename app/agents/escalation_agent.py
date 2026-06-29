from app.models.state import SupportState


def escalation_agent(state: SupportState):

    category = state["category"]
    root_cause = state["root_cause"]
    customer = state["customer_context"]

    confidence_score = 90
    escalate = False
    escalation_reason = "AI can handle this issue."

    # Enterprise customers get higher attention
    if customer["open_tickets"] > 5:

        confidence_score -= 20

        escalate = True

        escalation_reason = (
            "Customer has multiple open tickets."
        )

    # Unknown issues should escalate
    if root_cause == "Unknown Issue":

        confidence_score = 40

        escalate = True

        escalation_reason = (
            "Root cause could not be determined."
        )

    # High-value payment issues
    if (
        category == "Payment"
        and customer["plan"] == "Enterprise"
    ):

        confidence_score -= 10

    return {
        "confidence_score": confidence_score,
        "escalate": escalate,
        "escalation_reason": escalation_reason
    }