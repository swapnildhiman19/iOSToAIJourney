import os
from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel

# Load environment variables from .env file
load_dotenv()

api_key = os.environ["GOOGLE_API_KEY"]

class DiagnosticResult(BaseModel):
    summary: str
    risk: str

client = genai.Client(api_key=api_key)

model_id = os.environ.get('GEMINI_MODEL', "gemini-2.5-pro")
response = client.models.generate_content(
    model=model_id,
    contents="Explain the future of AI on iOS developer if his job would survive in future,be brutally honest",
    config={
        "response_mime_type":"application/json",
        "response_json_schema": DiagnosticResult.model_json_schema(),
    }
)

result = DiagnosticResult.model_validate_json(response.text)
print(result.model_dump())
# print(client.models.list)