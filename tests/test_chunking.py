import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.utils.chunking import split_markdown

def test_split_markdown_basic():
    text = "# Title\n" + "A" * 2500
    chunks = split_markdown(text, max_chars=1000)
    assert len(chunks) >= 2
    assert all(len(c) <= 1000 for c in chunks)

def test_split_markdown_overlap():
    text = "1234567890" * 200
    chunks = split_markdown(text, max_chars=100, overlap=20)   
    assert chunks[0][-20:] in chunks[1]