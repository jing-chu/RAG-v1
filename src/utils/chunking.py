from pathlib import Path
import re

def split_markdown(text, max_chars=400, overlap=40):
    blocks = re.split(r"\n(?=# )|\n(?=## )|\n\s*\n", text)
    chunks = []
    buf = ""
    for b in blocks:
        while len(b) > max_chars:
            part = b[:max_chars]
            chunks.append(part.strip())
            b = b[max_chars - overlap:] 
        if len(buf) + len(b) + 1 <= max_chars:
            buf = (buf + "\n" + b).strip()
        else:
            if buf: chunks.append(buf)
            # start new with overlap tail
            tail = buf[-overlap:] if buf else ""
            buf = (tail + "\n" + b).strip()
    if buf: chunks.append(buf)
    return chunks

    