import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.rag.prompt import build_prompt

def test_build_prompt_contains_context():
    chunks = [{"text": "Embeddings are vectors"}, {"text": "Used for search"}]
    msgs = build_prompt("what are embeddings?", chunks)
    # Should contain system and user messages
    print(msgs)
    assert any(m["role"] == "system" for m in msgs)
    assert any("Embeddings are vectors" in m["content"] for m in msgs)