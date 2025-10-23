import chromadb
from src.utils.models import ChunkMetadata, RetrievedChunk

#performs similarity query on stored embeddings(like SQL)
def search(query, k=5, collection="notes_v1", db_dir=".chroma"):
    client = chromadb.PersistentClient(path=db_dir) #open database
    col = client.get_collection(collection) #retrieves collection
    res = col.query(query_texts=[query], n_results=k, include=["documents","metadatas","distances"]) # run a semantic search
    chunks = [
        RetrievedChunk(text=doc, meta=ChunkMetadata(**meta), distance=dist)
        for doc, meta, dist in zip(res["documents"][0], res["metadatas"][0], res["distances"][0])
    ]
    return chunks