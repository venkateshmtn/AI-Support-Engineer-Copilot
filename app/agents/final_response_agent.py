from app.models.state import SupportState


def final_response_agent(state: SupportState):

    customer = state["customer_context"]

    response = f"""
SUPPORT CASE SUMMARY

Customer:
{customer['name']}

Plan:
{customer['plan']}

Issue Category:
{state['category']}

Priority:
{state['priority']}

Customer Sentiment:
{state['sentiment']}

Root Cause:
{state['root_cause']}

Recommended Actions:
"""

    for step in state["resolution"]:
        response += f"\n• {step}"

    response += f"""

Confidence Score:
{state['confidence_score']}%

Escalation Required:
{'YES' if state['escalate'] else 'NO'}

Escalation Reason:
{state['escalation_reason']}
"""

    return {
        "final_response": response
    }