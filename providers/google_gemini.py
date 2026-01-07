import os
import requests # pyright: ignore[reportMissingModuleSource]

SYSTEM_PROMPT = (
    "You are a technical coach. "
    "You explain clearly, step by step, and encourage learners. "
    "AI tools are supports, not replacements."
)

def chat(messages: list[dict]) -> str:
    """
    Minimal Google Gemini REST call.
    Viewers provide their own GEMINI_API_KEY via .env (not committed).
    """
    api_key = os.getenv("GEMINI_API_KEY", "").strip()
    model = os.getenv("GEMINI_MODEL", "gemini-pro").strip()


    if not api_key:
        return "Missing GEMINI_API_KEY. Copy .env.example to .env and add your key."

    # Build a short transcript (keeps this starter simple and readable)
    transcript = [f"SYSTEM: {SYSTEM_PROMPT}"]
    for msg in messages[-10:]:
        transcript.append(f"{msg['role'].upper()}: {msg['content']}")
    prompt_text = "\n".join(transcript)

    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
    payload = {"contents": [{"parts": [{"text": prompt_text}]}]}

    resp = requests.post(url, params={"key": api_key}, json=payload, timeout=30)
    if resp.status_code != 200:
        return f"Gemini API error {resp.status_code}: {resp.text}"

    data = resp.json()
    try:
        return data["candidates"][0]["content"]["parts"][0]["text"]
    except Exception:
        return f"Unexpected response format: {data}"
