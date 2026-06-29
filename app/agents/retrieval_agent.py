from app.vectorstore.faiss_store import (
    search_documents
)


def retrieval_agent(state):

    query = state["ticket"]

    results = search_documents(
        query
    )

    return {
        "retrieved_docs": results
    }