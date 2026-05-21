# 06 — Anthropic SDK + First Claude Call

## 🧒 Layman explanation

You just talked to Gemini. Now you'll do the same with **Claude** — Anthropic's flagship model. Why both?

1. **Cross-provider literacy is an FDE-interview signal.** Every FDE interview asks "how would you switch providers?" — the only way to answer is to have done both.
2. **Different models excel at different tasks.** Claude is famous for nuanced writing and long-form reasoning; Gemini for multimodal and cost.
3. **In Phase 2 onward you'll build a provider-agnostic wrapper.** Today is the foundation.

The Anthropic SDK is **simpler than `google-genai`**: one client, one method (`messages.create`), one API surface. There's no "Vertex" equivalent — Anthropic is its own provider (though you can also reach Claude *through* Vertex AI Model Garden and AWS Bedrock — you'll do that in Phase 3).

---

## 🔧 Technical deep-dive — Anthropic's `messages` API

The mental model is the **"conversation as a list of messages"** pattern:

```python
client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    system="You are a helpful, concise assistant.",
    messages=[
        {"role": "user",      "content": "What is 2+2?"},
        {"role": "assistant", "content": "4."},
        {"role": "user",      "content": "Why?"},
    ],
)
```

Key differences from Gemini's API:

| Concept                 | Gemini (`google-genai`)         | Anthropic                              |
|-------------------------|----------------------------------|-----------------------------------------|
| Conversation format     | `contents=[Content(role, parts)]` | `messages=[{role, content}]`            |
| System prompt           | `system_instruction` in config   | `system=` parameter (top-level)         |
| Generation method       | `generate_content`               | `messages.create`                       |
| Streaming method        | `generate_content_stream`        | `messages.stream` (or `stream=True`)    |
| Tools                   | `tools=` in config               | `tools=` top-level                      |
| Cost field              | `usage_metadata.total_token_count` | `usage.input_tokens` + `output_tokens` |
| Required parameter      | None — defaults sensible         | **`max_tokens` is required**            |

> ⚠️ The `max_tokens` parameter is **required** by Anthropic. It's optional in Gemini (defaults exist). Forgetting this is the #1 first-call error.

### The four current Claude model names

| Model name (May 2026)                  | Speed     | Cost rank   | Best for                            |
|----------------------------------------|-----------|-------------|-------------------------------------|
| `claude-haiku-4-...`                   | Fastest   | $           | Cheap classification, light tasks   |
| `claude-sonnet-4-...`                  | Fast      | $$          | **Default workhorse**               |
| `claude-opus-4-...`                    | Slowest   | $$$$        | Reasoning, complex chains, agents   |
| `claude-instant-4-...` (legacy aliases)| —         | —           | Avoid; using newer is better        |

Use Anthropic's [model list page](https://docs.anthropic.com/en/docs/about-claude/models) for the exact current model strings — they bump versions every few weeks.

---

## 💻 Hands-on — get your Anthropic API key

### Step 1 — Create an account + key

1. Open https://console.anthropic.com/
2. Sign up (or log in if you already have an account)
3. Add **$5** to your account billing — Anthropic doesn't have a generous free tier; $5 is plenty for Week 1 + 2
4. Navigate to **Settings → API Keys**
5. Click **Create Key**
6. Name it `ai-engineer-portfolio-dev`
7. Copy the key — starts with `sk-ant-…`

### Step 2 — Set a spend limit (do this NOW)

Anthropic's console has a **Workspace → Limits** page. Set:

- **Monthly limit:** $20 (you'll spend ~$2/month in Phase 1, but this is your safety net)

You can raise it later if you're doing heavy eval runs.

### Step 3 — Paste into `.env`

```bash
# In ~/Desktop/AI/code/ai-engineer-portfolio/.env
ANTHROPIC_API_KEY=sk-ant-api03-your_real_key_here
```

### Step 4 — Verify it's loaded

```bash
uv run python code/check_env.py
```

You should now see all three keys filled in (or two — `GOOGLE_CLOUD_PROJECT` fills on Friday).

---

## 💻 Write `hello_anthropic.py`

Create `code/hello_anthropic.py`:

```python
"""First Claude call. Day 1 of the AI Engineer roadmap."""
import os

import anthropic
from dotenv import load_dotenv

load_dotenv()

# 1. Initialize client — uses ANTHROPIC_API_KEY from env automatically
client = anthropic.Anthropic()  # picks up ANTHROPIC_API_KEY from os.environ

# 2. Make the call
response = client.messages.create(
    model="claude-sonnet-4-20250514",   # Use Anthropic's latest Sonnet alias when you run this
    max_tokens=200,                      # REQUIRED for Anthropic, unlike Gemini
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
```

Run it:

```bash
uv run python code/hello_anthropic.py
```

Expected:

```
=== Response ===
Hi! I'm Claude, an AI assistant made by Anthropic. How can I help you today?

=== Usage ===
Input tokens:     21
Output tokens:    18
Stop reason:      end_turn
Model:            claude-sonnet-4-20250514
```

> 💡 If the model name fails with `not_found_error`, check https://docs.anthropic.com/en/docs/about-claude/models and copy the current Sonnet alias into the script.

---

## 📊 Side-by-side — same task, two providers

```mermaid
flowchart LR
    subgraph Gemini
        G1[client.models.generate_content<br/>contents='Hello']
        G2[Gemini 2.5 Flash]
        G3[response.text<br/>response.usage_metadata]
    end

    subgraph Claude
        C1[client.messages.create<br/>messages=List, max_tokens=200]
        C2[Claude Sonnet 4]
        C3[response.content_0_.text<br/>response.usage]
    end

    APP[Your Python code] --> G1
    APP --> C1
    G1 --> G2 --> G3
    C1 --> C2 --> C3

    style Gemini fill:#dbeafe
    style Claude fill:#fde68a
```

Same idea, two dialects. The **provider-agnostic wrapper** you'll write in Phase 2 hides this difference behind one interface.

---

## 🧪 Bonus — streaming Claude

```python
"""Streaming version with Anthropic SDK."""
import anthropic
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic()

with client.messages.stream(
    model="claude-sonnet-4-20250514",
    max_tokens=200,
    messages=[{"role": "user", "content": "Write a haiku about Mumbai monsoon rain."}],
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)
print()
```

---

## 🐛 Common errors

| Symptom                              | Cause                                            | Fix                                   |
|--------------------------------------|--------------------------------------------------|---------------------------------------|
| `BadRequestError: max_tokens required` | Forgot `max_tokens` param                        | Add `max_tokens=...`                  |
| `AuthenticationError`                | Wrong/expired key, or no whitespace allowed       | Regenerate key                        |
| `OverloadedError`                    | Anthropic infra is busy (rare)                    | Retry with exponential backoff        |
| `not_found_error model:claude-...`   | Model alias changed                              | Look up current alias in Anthropic docs |

---

## 📚 References

- **Anthropic Python SDK** — https://github.com/anthropics/anthropic-sdk-python
- **Messages API reference** — https://docs.anthropic.com/en/api/messages
- **Model list & pricing** — https://docs.anthropic.com/en/docs/about-claude/models
- **Anthropic Prompt Engineering course (free)** — https://github.com/anthropics/courses/tree/master/prompt_engineering_interactive_tutorial

---

## ✅ Exit criteria

- [ ] Anthropic key created, $5 funded, $20 spend cap set
- [ ] `ANTHROPIC_API_KEY` in `.env`, loads via `check_env.py`
- [ ] `code/hello_anthropic.py` exists and prints a response + usage
- [ ] I can name the differences in `messages` vs `contents` mental models
- [ ] I tried the streaming variant

**Next:** [`07-end-of-day-checklist.md`](07-end-of-day-checklist.md) — commit, push, sleep.

---

🌀 *Magic applied with Wibey VS Code Extension 🪄*
