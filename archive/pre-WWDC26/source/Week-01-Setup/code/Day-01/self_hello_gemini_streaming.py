import os
import dotenv 
from google import genai
from google.genai import types

dotenv.load_dotenv()

USE_VERTEX = os.environ.get('GOOGLE_GENAI_USER_VERTEX_AI',"false").lower() == "true"

client = (
    genai.Client(
        vertexai=True,
        project = os.environ["GOOGLE_CLOUD_PROJECT"],
        location = os.environ.get("GOOGLE_CLOUD_LOCATION","us-central1"),
    )
    if USE_VERTEX
    else genai.Client(api_key = os.environ["GOOGLE_API_KEY"])
)

for chunk in client.models.generate_content_stream(
    model="gemini-2.5-flash",
    contents="Introduce yourself as a platform to build the characters",
    config = types.GenerateContentConfig(
        temperature=0.9,
        max_output_tokens=1024, 
    )
):
    print(chunk.text, end="", flush=True)

print()   