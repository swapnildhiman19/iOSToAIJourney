"""First Claude call. Day 1 of the AI Engineer roadmap.

Run with:
    uv run python hello_anthropic.py
"""
import anthropic
from dotenv import load_dotenv

load_dotenv()

# 1. Initialize client — uses ANTHROPIC_API_KEY from env automatically
client = anthropic.Anthropic()

# 2. Make the call.
#    Check https://docs.anthropic.com/en/docs/about-claude/models for the current Sonnet alias.
response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=200,  # REQUIRED for Anthropic, unlike Gemini
    system="You are a friendly AI assistant. Keep responses brief.",
    messages=[
        {"role": "user", "content": "Introduce yourself in one sentence."},
    ],
)

# 3. Print the answer
print("=== Response ===")
# .content is a list of blocks; for text-only responses, the first block holds text
print(response.content[0].text)

# 4. Print the cost footprint
print("\n=== Usage ===")
print(f"Input tokens:     {response.usage.input_tokens}")
print(f"Output tokens:    {response.usage.output_tokens}")
print(f"Stop reason:      {response.stop_reason}")
print(f"Model:            {response.model}")
