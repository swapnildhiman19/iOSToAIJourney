"""Streaming version — feels 5× faster even though it isn't.

Run with:
    uv run python hello_gemini_streaming.py
"""
import os

from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])

for chunk in client.models.generate_content_stream(
    model="gemini-2.5-flash",
    contents="Write a haiku about Mumbai monsoon rain.",
):
    print(chunk.text, end="", flush=True)

print()  # final newline
