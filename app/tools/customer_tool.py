from data.customers.customers import CUSTOMERS


def get_customer_profile(customer_id: str):

    return CUSTOMERS.get(
        customer_id,
        {
            "name": "Unknown",
            "plan": "Unknown",
            "account_age": "Unknown",
            "open_tickets": 0
        }
    )