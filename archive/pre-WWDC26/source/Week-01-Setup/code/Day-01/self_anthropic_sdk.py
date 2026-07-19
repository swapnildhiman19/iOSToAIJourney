import os 
from dotenv import load_dotenv
import anthropic

load_dotenv()

client = anthropic.Anthropic()

# response = client.messages.create(
#     model="claude-haiku-4-5-20251001",
#     max_tokens=100,
#     system="You are friendly AI assistant, Keep responses brief",
#     messages=[
#         {"role":"user", "content":"Introduce yourself in one sentence."}
#     ]
# )

# print(response.content[0].text)
# print("\n")
# print(response.usage.input_tokens)
# print(response.usage.output_tokens)
# print(response.stop_reason)
# print(response.model)

with client.messages.stream(
    model="claude-haiku-4-5",
    max_tokens=100,
    messages=[
        {"role":"user","content":"Introduce yourself as helpful AI streaming LLM in one sentence"}
    ],    
) as stream:
    for text in stream.text_stream:
        print(text, end="",flush=True)
print()        