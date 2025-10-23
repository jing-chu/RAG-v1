import chromadb
from sentence_transformers import SentenceTransformer
from pathlib import Path
from src.utils.chunking import split_markdown
from src.utils.models import ChunkMetadata

# builds or updates the Chroma index(like a database builder)
def build_or_update_index(corpus_dir, collection_name="notes_v1", db_dir=".chroma", embed_model="sentence-transformers/all-MiniLM-L6-v2"):
    client = chromadb.PersistentClient(path=db_dir) #creates a local Chroma database folder
    col = client.get_or_create_collection(collection_name)
    encoder = SentenceTransformer(embed_model) #loads the embedding model into memory
    docs, ids, metas = [], [], [] #like 3 columns: content, ID, metadata
    for fp in Path(corpus_dir).rglob("*.md"):
        text = fp.read_text(encoding="utf-8", errors="ignore") #reads all .md files under corpus_dir
        chunks = split_markdown(text) # splits them into chunks
        for i, c in enumerate(chunks):
            meta = ChunkMetadata(source=str(fp), chunk=i) # a Pydantic object
            docs.append(c)
            ids.append(f"{fp}:{i}")
            metas.append(meta.model_dump()) # validated and converted to plain dict for Chroma db
    embs = encoder.encode(docs, convert_to_numpy=True).tolist() #embeds them: chunk (string) → numeric vector (embedding)
    col.add(documents=docs, embeddings=embs, ids=ids, metadatas=metas) #stores in Chroma
    print(f"Indexed {len(docs)} chunks from {len(list(Path(corpus_dir).glob('*.md')))} files.")