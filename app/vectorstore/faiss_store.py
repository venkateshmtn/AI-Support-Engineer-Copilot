from sentence_transformers import SentenceTransformer
import faiss
import pickle


model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

index = faiss.read_index(
    "data/support_docs/faiss_index.bin"
)

with open(
    "data/support_docs/documents.pkl",
    "rb"
) as f:

    documents = pickle.load(f)


def search_documents(
    query,
    top_k=1
):

    query_embedding = model.encode(
        [query]
    )

    distances, indices = index.search(
        query_embedding,
        top_k
    )

    results = []

    for idx in indices[0]:
        results.append(
            documents[idx]
        )

    return results