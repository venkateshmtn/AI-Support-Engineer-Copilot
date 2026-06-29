from app.models.state import SupportState


def root_cause_agent(state: SupportState):

    docs = state["retrieved_docs"]

    if not docs:
        return {
            "root_cause": "Unknown Issue"
        }

    top_doc = docs[0].lower()

    if "fraud" in top_doc:
        root_cause = "Fraud Detection Block"

    elif "bank" in top_doc:
        root_cause = "Bank Rejection"

    elif "expired" in top_doc:
        root_cause = "Expired Card"

    elif "password" in top_doc:
        root_cause = "Forgot Password"

    else:
        root_cause = "Unknown Issue"

    return {
        "root_cause": root_cause
    }