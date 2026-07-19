"""First Gemini call via Vertex AI (ADC auth, no API key).

Prerequisites:
- gcloud auth application-default login
- gcloud config set project <your-project-id>
- Vertex AI API enabled

Run with:
    uv run python hello_vertex.py
"""
import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

# 1. Initialize client for VERTEX AI backend.
#    No api_key. Auth happens via Application Default Credentials.
client = genai.Client(
    vertexai=True,
    project=os.environ["GOOGLE_CLOUD_PROJECT"],
    location=os.environ.get("GOOGLE_CLOUD_LOCATION", "us-central1"),
)

# 2. Same call as AI Studio path — note the same method/args.
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Introduce yourself and mention you're being called via Vertex AI.",
    config=types.GenerateContentConfig(
        temperature=0.7,
        max_output_tokens=120,
    ),
)

# 3. Same response shape.
print("=== Response (via Vertex AI) ===")
print(response.text)

print("\n=== Usage ===")
print(f"Prompt tokens:    {response.usage_metadata.prompt_token_count}")
print(f"Output tokens:    {response.usage_metadata.candidates_token_count}")
print(f"Total tokens:     {response.usage_metadata.total_token_count}")
