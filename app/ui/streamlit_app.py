import streamlit as st

from app.graph.support_graph import support_graph

st.set_page_config(
    page_title="AI Support Copilot",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Support Engineer Copilot")

ticket = st.text_area(
    "Enter Customer Ticket",
    height=150
)

if st.button("Analyze Ticket"):

    # Run LangGraph Workflow
    state = support_graph.invoke(
        {
            "ticket": ticket,
            "customer_id": "CUST_001"
        }
    )

    st.subheader("🎯 Triage Results")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="Category",
            value=state["category"]
        )

    with col2:
        st.metric(
            label="Priority",
            value=state["priority"]
        )

    with col3:
        st.metric(
            label="Sentiment",
            value=state["sentiment"]
        )

    st.subheader("👤 Customer Profile")

    customer = state["customer_context"]

    col1, col2 = st.columns(2)

    with col1:
        st.write("**Name:**", customer["name"])
        st.write("**Plan:**", customer["plan"])

    with col2:
        st.write("**Account Age:**", customer["account_age"])
        st.write("**Open Tickets:**", customer["open_tickets"])

    st.subheader("📚 Retrieved Knowledge")

    for doc in state["retrieved_docs"]:
        
        st.info(doc)

    st.subheader("🔍 Root Cause Analysis")

    st.warning(
        state["root_cause"]
    )

    st.subheader("🛠 Recommended Resolution")

    for step in state["resolution"]:
        st.success(step)

    st.subheader("📊 Confidence Score")

    st.progress(
        state["confidence_score"] / 100
    )

    st.write(
        f"Confidence: {state['confidence_score']}%"
    )

    st.subheader("🚨 Escalation Decision")

    if state["escalate"]:

        st.error(
            f"""
Escalate: YES

Reason:
{state['escalation_reason']}
"""
        )

    else:

        st.success(
            f"""
Escalate: NO

Reason:
{state['escalation_reason']}
"""
        )

    st.subheader("📄 Final Support Summary")

    st.text_area(
        "Generated Report",
        value=state["final_response"],
        height=350
    )