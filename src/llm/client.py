import ollama
from typing import List, Dict

# sends messages to Phi-3 via Ollama
def chat(messages: List[Dict[str, str]], model: str = "phi3") -> str:
    response = ollama.chat(model=model, messages=messages)
    return response["message"]["content"]