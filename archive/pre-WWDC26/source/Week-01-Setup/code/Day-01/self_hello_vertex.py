"""
Gemini call via Vertex AI (ADC auth, no API key)
Run with:
    uv run python self_hello_vertex.py
"""

import os 

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client(
    vertexai=True,
    project=os.environ["GOOGLE_CLOUD_PROJECT"],
    location=os.environ.get("GOOGLE_CLOUD_LOCATION","us-central1"),
)

response = client.models.generate_content(
    model = "gemini-2.5-flash-lite",
    contents = "Introduce yourself and mention that you are being called via VertexAI",
    config=types.GenerateContentConfig(
        temperature=0.7,
        max_output_tokens=120
    ),
)

print("RESPONSE VIA VERTEX AI")
print(response.candidates[0].content.parts[0].text)
print(response.usage_metadata.candidates_token_count)