from app.models.state import SupportState
from app.tools.customer_tool import get_customer_profile


def customer_context_agent(state: SupportState):

    customer_id = state["customer_id"]

    customer_profile = get_customer_profile(customer_id)

    return {
        "customer_context": customer_profile
    }