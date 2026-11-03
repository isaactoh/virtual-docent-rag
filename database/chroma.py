import chromadb
from sentence_transformers import SentenceTransformer

client = chromadb.PersistentClient(path="./chromadb")

collection = client.get_or_create_collection(
    name="my_documents"
)

model = SentenceTransformer("BAAI/bge-base-en-v1.5")

def embed(chunks):
    embeddings = model.encode(chunks).tolist()

    ids = [f"doc_{i}" for i in range(len(chunks))]

    collection.upsert(
        ids = ids,
        documents=chunks,
        embeddings=embeddings
    )

    print(f"Successfully stored {len(chunks)} chunks")

def search_chunks(query, n_results = 3):
    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )

    return results["documents"][0]