from app.models.state import SupportState


def triage_agent(state: SupportState):

    ticket = state["ticket"].lower()

    category = "Other"
    priority = "Medium"
    sentiment = "Neutral"

    if "payment" in ticket:
        category = "Payment"
        priority = "High"
        sentiment = "Frustrated"

    elif "login" in ticket:
        category = "Login"
        priority = "High"
        sentiment = "Frustrated"

    elif "subscription" in ticket:
        category = "Subscription"

    elif "invoice" in ticket:
        category = "Billing"

    return {
        "category": category,
        "priority": priority,
        "sentiment": sentiment
    }