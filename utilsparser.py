import re

def clean_price(text: str) -> str:
    if not text:
        return ""
    text = re.sub(r"[^\d.]", "", text.strip())
    return text