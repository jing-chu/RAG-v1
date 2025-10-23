import re

def clean_json_output(text: str) -> str:
    # remove markdown fences like ```json or ``` 
    cleaned = re.sub(r"^```(?:json)?|```$", "", text.strip(), flags=re.MULTILINE)
    return cleaned.strip()