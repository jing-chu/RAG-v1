import chromadb

client = chromadb.PersistentClient(path=".chroma")
collection = client.get_collection("notes_v1")

query = input("Ask anything: ")

# Run a semantic search
# Chroma uses the same embedding model I used for indexing (all-MiniLM-L6-v2) to convert the question into a vector.
# It compares that query vector to all stored vectors (using cosine similarity).
# It returns the top 3 most similar chunks.
res = collection.query(query_texts=[query], n_results=3)

# print(f"res: {res}")

for i in range(len(res["ids"][0])):
    # meta = res["metadatas"][0][i]
    # src = meta.get("source", "unknown")
    print(f"\n--- Result {i+1} ---")
    print(f"Source: {res['metadatas'][0][i]['source']}")
    print(res["documents"][0][i][:400], "...")
