## Local RAG with Phi-3

A minimal Retrieval-Augmented Generation pipeline built from scratch in Python

## Project Structure

```text
RAG-v1/
├── rag_local.py               # CLI entry point
├── data/
│   └── corpus/                # Your markdown/text documents
├── src/
│   ├── llm/
│   │   └── client.py          # Ollama chat wrapper
│   ├── rag/
│   │   ├── indexer.py         # Build / update Chroma index
│   │   ├── retriever.py       # Search similar chunks
│   │   └── prompt.py          # Format LLM prompt
│   └── utils/
│       └── chunking.py        # Text splitting utility
├── tests/
│   ├── test_chunking.py
│   ├── test_indexer.py
│   ├── test_retriever.py
│   └── test_prompt.py
├── .env                       # Configuration (model, paths)
├── .chroma/                   # Local ChromaDB storage
├── .gitignore
└── README.md
```

## Workflow
### Split Markdown files, embed them, and store in ChromaDB:

python rag_local.py --index data/corpus

### Query the index and get grounded answers:

python rag_local.py --query "What is an embedding?" --k 3

### Example output

An embedding, as described in the notes provided ([1] Embeddings), involves converting text into numerical vectors to capture semantic meaning—similar texts yield similar vector representations [2]. This process facilitates tasks like similarity search where relationships between different pieces of text can be assessed quantitatively.

Sources:
1) data/corpus/llm_concepts.md#chunk-0
2) data/corpus/rag_pipline.md#chunk-0
3) data/corpus/llm_concepts.md#chunk-1