from pathlib import Path
from sentence_transformers import SentenceTransformer
import chromadb

corpus_path = Path("data/corpus")
client = chromadb.PersistentClient(path=".chroma")
collection = client.get_or_create_collection("notes_v1")
encoder = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def chunk_text(text, max_chars=1000):
    parts, buf = [], ""
    for line in text.splitlines(keepends=True):
        if len(buf) + len(line) > max_chars:
            parts.append(buf.strip())
            buf = ""
        buf += line
    if buf.strip():
        parts.append(buf.strip())
    return parts

docs, ids, metas = [], [], []
for file in corpus_path.glob("*.md"):
    text = file.read_text(encoding="utf-8", errors="ignore")
    chunks = chunk_text(text)
    for i, chunk in enumerate(chunks):
        docs.append(chunk)
        ids.append(f"{file.name}_{i}")
        metas.append({"source": file.name, "chunk": i})


#converts each chunk (string) to numeric vector (embedding)
embs = encoder.encode(docs, convert_to_numpy=True).tolist()
#save to ChromaDB
collection.add(ids=ids, documents=docs, embeddings=embs, metadatas=metas)
print(f"Indexed {len(docs)} chunks from {len(list(corpus_path.glob('*.md')))} files.")

