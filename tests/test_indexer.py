import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.rag.indexer import build_or_update_index
import chromadb
from pathlib import Path

def test_indexer_creates_collection(tmp_path): #tmp_path is a pytest built-in fixture
    # it gives each test function a fresh, unique temporary folder (a pathlib.Path object) that automatically gets cleaned up after the test runs.
    corpus = tmp_path / "corpus"
    corpus.mkdir()
    (corpus / "a.md").write_text("Test embedding text")

    build_or_update_index(str(corpus), collection_name="test_notes", db_dir=str(tmp_path)) #create a chroma db

    client = chromadb.PersistentClient(path=str(tmp_path)) #open it 
    col = client.get_collection("test_notes") 
    assert col.count() > 0