from sentence_transformers import SentenceTransformer
import faiss
import pickle


with open(
    "data/support_docs/support_docs.txt",
    "r",
    encoding="utf-8"
) as f:

    documents = [
        line.strip()
        for line in f.readlines()
        if line.strip()
    ]


model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

embeddings = model.encode(
    documents
)

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(
    dimension
)

index.add(
    embeddings
)

faiss.write_index(
    index,
    "data/support_docs/faiss_index.bin"
)

with open(
    "data/support_docs/documents.pkl",
    "wb"
) as f:

    pickle.dump(
        documents,
        f
    )

print("FAISS Index Created")