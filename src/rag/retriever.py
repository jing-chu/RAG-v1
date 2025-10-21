import chromadb

#performs similarity query on stored embeddings(like SQL)
def search(query, k=5, collection="notes_v1", db_dir=".chroma"):
    client = chromadb.PersistentClient(path=db_dir) #open database
    col = client.get_collection(collection) #retrieves collection
    res = col.query(query_texts=[query], n_results=k, include=["documents","metadatas","distances"]) # run a semantic search
    hits = []
    for i in range(len(res["ids"][0])):
        hits.append({
            "id": res["ids"][0][i],
            "text": res["documents"][0][i],
            "meta": res["metadatas"][0][i],
            "score": res["distances"][0][i],
        })
    return hits