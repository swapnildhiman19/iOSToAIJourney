"""First Gemini call. Day 1 of the AI Engineer roadmap.

Run with:
    uv run python hello_gemini.py
"""
import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

# 1. Initialize a client (AI Studio path — uses GOOGLE_API_KEY env var)
client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])

# 2. Make the call
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Introduce yourself in one sentence.",
    config=types.GenerateContentConfig(
        temperature=0.7,
        max_output_tokens=100,
    ),
)

# 3. Print the human-readable answer
print("=== Response ===")
print(response.text)

# 4. Print the cost footprint (you'll do this for every call from now on)
print("\n=== Usage ===")
print(f"Prompt tokens:    {response.usage_metadata.prompt_token_count}")
print(f"Output tokens:    {response.usage_metadata.candidates_token_count}")
print(f"Total tokens:     {response.usage_metadata.total_token_count}")

# 5. Bonus — finish_reason tells you why generation stopped
print(f"\nFinish reason:    {response.candidates[0].finish_reason}")
