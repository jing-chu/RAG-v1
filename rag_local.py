import argparse
from src.rag.indexer import build_or_update_index
from src.rag.retriever import search
from src.rag.prompt import build_prompt
from src.llm.client import chat
from src.utils.models import LLMResponse
from src.utils.clean_json import clean_json_output
from pydantic import ValidationError
import json


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
    try:
        cleaned = clean_json_output(ans)
        response = LLMResponse.model_validate_json(cleaned)
        print(f"Answer:\n{response.answer}\n")
        print("Sources:")
        for i, src in enumerate(response.sources, 1):
            print(f"{i}) {src.source}#chunk-{src.chunk}")
    except ValidationError as e:
        print("Could not parse model response as LLMResponse:")
        print(e)

