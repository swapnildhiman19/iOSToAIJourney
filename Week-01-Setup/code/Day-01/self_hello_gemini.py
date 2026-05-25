import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

USE_VERTEX = os.environ.get('GOOGLE_GENAI_USER_VERTEX_AI',"false").lower() == "true"

client = (
    genai.Client(
        vertexai=True,
        project = os.environ["GOOGLE_CLOUD_PROJECT"],
        location = os.environ.get("GOOGLE_CLOUD_LOCATION","us-central1"),
    )
    if USE_VERTEX
    else genai.Client(api_key=os.environ["GOOGLE_API_KEY"])
)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Introduce yourself as a platform to build the characters",
    config = types.GenerateContentConfig(
        temperature=0.9,
        max_output_tokens=100,
    ),
)

print(response.text)

print("=====Usage==========")
print(f" Prompt Tokens : {response.usage_metadata.prompt_token_count}")
print(f"Output Token : {response.usage_metadata.candidates_token_count}")
print(f"Total token count: {response.usage_metadata.total_token_count}")

print(f"\nFinish Reason : {response.candidates[0].finish_reason}")
