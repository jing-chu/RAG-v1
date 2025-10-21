import argparse
from src.rag.indexer import build_or_update_index
from src.rag.retriever import search
from src.rag.prompt import build_prompt
from src.llm.client import chat

# Command-line arguments
# --index data/corpus: Build / update index from that folder
# --query "What is embedding?": Run a query through retriaval and Phi3 
parser = argparse.ArgumentParser()
parser.add_argument("--index", type=str)
parser.add_argument("--query", type=str)
parser.add_argument("--k", type=int, default=5)
args = parser.parse_args()

if args.index:
    build_or_update_index(args.index)

if args.query:
    chunks = search(args.query, k=args.k)
    msgs = build_prompt(args.query, chunks)
    ans = chat(msgs)
    print(ans)
    print("\nSources:")
    for i, c in enumerate(chunks, 1):
        print(f"{i}) {c['meta']['source']}#chunk-{c['meta']['chunk']}")