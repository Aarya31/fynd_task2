# llm_utils.py
import os
import requests
import json
import re
from typing import Tuple

# Read API_KEY from env variable for safety
API_KEY = os.getenv("OPENROUTER_API_KEY", "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")
MODEL = os.getenv("OPENROUTER_MODEL", "deepseek/deepseek-chat")

BASE_URL = "https://openrouter.ai/api/v1/chat/completions"

def call_llm_raw(prompt: str, temperature: float = 0.0, max_tokens: int = 256) -> dict:
    """
    Call OpenRouter / OpenAI-like endpoint and return parsed JSON response.
    """
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    payload = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": temperature,
        "max_tokens": max_tokens
    }

    resp = requests.post(BASE_URL, headers=headers, json=payload, timeout=30)
    try:
        return resp.json()
    except:
        return {"error": {"message": "invalid_json_response", "raw_text": resp.text}}

def extract_json_from_text(text: str) -> str:
    """
    Extract JSON object from any given text by finding outermost braces.
    If none found, return the original text (caller should handle).
    """
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        return match.group(0)
    return text

def llm_generate_json(prompt: str, temperature: float = 0.0) -> dict:
    """
    Call LLM and attempt to return a JSON-parsable object (dict).
    Falls back to dict with 'text' key if JSON parse fails.
    """
    data = call_llm_raw(prompt, temperature=temperature)
    if "choices" not in data:
        # return error wrapper
        return {"error": True, "text": data.get("error", {}).get("message", str(data))}

    content = data["choices"][0]["message"]["content"]
    # extract potential JSON
    extracted = extract_json_from_text(content)
    try:
        return json.loads(extracted)
    except Exception:
        # fallback: return raw content in a field
        return {"error": True, "text": content}

# Convenience functions for the three required types:
def generate_user_response(review_text: str) -> str:
    """
    Return a friendly user-facing response string.
    """
    prompt = f"""
You are a polite assistant that writes a short, empathetic reply to a customer's review.
Return ONLY the reply text (no JSON). Keep it to 1-2 short sentences.

Review:
\"\"\"{review_text}\"\"\"
"""
    data = call_llm_raw(prompt, temperature=0.2)
    if "choices" in data:
        return data["choices"][0]["message"]["content"].strip()
    return "Thanks for your feedback!"

def generate_summary(review_text: str) -> str:
    """
    Return a short summary of the review (1 line). JSON not required.
    """
    prompt = f"""
Summarise the following customer review in ONE short sentence (no JSON, only one sentence):

\"\"\"{review_text}\"\"\"
"""
    data = call_llm_raw(prompt, temperature=0.0)
    if "choices" in data:
        return data["choices"][0]["message"]["content"].strip()
    return review_text[:120]

def generate_recommended_actions(review_text: str) -> str:
    """
    Return 1-3 recommended actions for admins based on the review.
    Return as a short bullet list or sentence.
    """
    prompt = f"""
You are a helpful assistant providing recommended next actions for a business based on a customer review.
Return 1-3 short recommended actions, separated by semicolons or newlines. No JSON required.

Review:
\"\"\"{review_text}\"\"\"
"""
    data = call_llm_raw(prompt, temperature=0.0)
    if "choices" in data:
        return data["choices"][0]["message"]["content"].strip()
    return "No action suggested."
