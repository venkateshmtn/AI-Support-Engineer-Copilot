from app.models.state import SupportState


def resolution_agent(state: SupportState):

    root_cause = state["root_cause"]

    resolution = []

    if root_cause == "Fraud Detection Block":

        resolution = [
            "Verify customer identity",
            "Confirm billing information",
            "Retry payment",
            "Escalate if issue persists"
        ]

    elif root_cause == "Expired Card":

        resolution = [
            "Verify card expiry date",
            "Update payment method",
            "Retry transaction"
        ]

    elif root_cause == "Bank Rejection":

        resolution = [
            "Contact issuing bank",
            "Verify transaction limits",
            "Retry payment"
        ]

    elif root_cause == "Account Locked":

        resolution = [
            "Reset password",
            "Unlock account",
            "Retry login"
        ]

    else:

        resolution = [
            "Review support documentation",
            "Escalate to support team"
        ]

    return {
        "resolution": resolution
    }