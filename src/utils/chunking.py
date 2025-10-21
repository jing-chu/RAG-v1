from pathlib import Path
import re

def split_markdown(text, max_chars=1200, overlap=120):
    blocks = re.split(r"\n(?=# )|\n(?=## )|\n\s*\n", text)
    # print(f"Blocks: {blocks}")
    chunks = []
    buf = ""
    for b in blocks:
        if len(buf) + len(b) + 1 <= max_chars:
            buf = (buf + "\n" + b).strip()
        else:
            if buf: chunks.append(buf)
            # start new with overlap tail
            tail = buf[-overlap:] if buf else ""
            buf = (tail + "\n" + b).strip()
    if buf: chunks.append(buf)
    # print(f"chunks: {chunks}")
    return chunks

    