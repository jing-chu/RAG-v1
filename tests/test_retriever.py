import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.rag.retriever import search
from src.rag.indexer import build_or_update_index
import chromadb
from pathlib import Path

def test_search_returns_results(tmp_path):
    corpus = tmp_path / "corpus"
    corpus.mkdir()
    (corpus / "b.md").write_text("Embeddings convert text into vectors")

    build_or_update_index(str(corpus), collection_name="test_rag",db_dir=str(tmp_path))
    results = search("embedding", k=1, collection="test_rag", db_dir=str(tmp_path))
    print(results)
    assert len(results) > 0
    assert "text" in results[0]