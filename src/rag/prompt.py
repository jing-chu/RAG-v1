# formats the text context into a proper LLM prompt
def build_prompt(question, chunks):
    ctx = "\n---\n".join(c["text"] for c in chunks) #loops through chunks, extracts "text" from each, and then joins them with the separator.
    system = (
        "You answer strictly from the provided CONTEXT. "
        "If the answer is not present, say: \"I don't know from the provided notes.\""
    )
    #CONTEXT: what background text to use
    messages = [
        {"role":"system","content":system},
        {"role":"user","content":f"CONTEXT:\n{ctx}\n\nQUESTION: {question}\nAnswer briefly and cite sources by index."}
    ]
    return messages