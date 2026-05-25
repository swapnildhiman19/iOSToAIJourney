# 04 — Run Gemma 3 (1B) Locally

## 🧒 Layman explanation

**Gemma 3** is Google's open-weights LLM family (1B, 4B, 12B, 27B parameter sizes). The 1B model:
- ~600 MB download (when 4-bit-quantized)
- ~1 GB RAM in use during inference
- ~30 tokens/sec on an M3
- Surprisingly capable for size

You'll download it once via Hugging Face, then run inference in Python — entirely **offline, on your Mac**. This is your "the future is here" moment.

---

## 💻 Hands-on

### Step 1 — Make sure your venv is active

```bash
cd ~/Desktop/AI/ml-tools
source mlx-env/bin/activate
```

### Step 2 — Download + run Gemma 3 (1B, instruction-tuned, 4-bit)

The `mlx-lm` package handles download + load + inference. First call downloads the model (one-time ~600 MB).

```bash
python <<'EOF'
from mlx_lm import load, generate

print("Loading model (first time downloads ~600 MB to ~/.cache/huggingface)...")
model, tokenizer = load("mlx-community/gemma-3-1b-it-4bit")

prompt = "Explain Application Default Credentials in one paragraph."

print("\n=== Prompt ===")
print(prompt)

print("\n=== Gemma 3 1B response ===")
response = generate(
    model, tokenizer,
    prompt=prompt,
    max_tokens=200,
    verbose=False,
)
print(response)
EOF
```

First run: ~30s download + ~5s model load + ~10s generation.
Second run: ~3s load + generation. (Once downloaded, model is cached.)

You should see a coherent response about ADC, generated entirely on your machine, with no internet involved during generation.

### Step 3 — Try chat-style with the CLI

`mlx-lm` ships a CLI for interactive sessions:

```bash
mlx_lm.generate \
    --model mlx-community/gemma-3-1b-it-4bit \
    --prompt "Write a 4-line poem about Mumbai monsoon" \
    --max-tokens 100
```

### Step 4 — Watch tokens stream

For the "feel it work" experience:

```bash
python <<'EOF'
from mlx_lm import load, stream_generate

model, tokenizer = load("mlx-community/gemma-3-1b-it-4bit")

prompt = "List 5 reasons to learn AI engineering in 2026. Be concise."

print("Streaming...\n")
for token in stream_generate(model, tokenizer, prompt, max_tokens=200):
    print(token.text, end="", flush=True)
print()
EOF
```

This streams token-by-token. The same pattern you used for Gemini streaming on Day 1 — but locally.

### Step 5 — Check the model cache

```bash
du -sh ~/.cache/huggingface/
# Expected: ~600 MB - 1 GB depending on quant variant downloaded
```

This is the only persistent state. Delete to free disk later.

---

## 📊 What happens on-device

```mermaid
sequenceDiagram
    actor You
    participant Py as Python script
    participant LM as mlx-lm
    participant HF as Hugging Face Hub (network)
    participant Cache as ~/.cache/huggingface/
    participant Metal as Metal GPU
    participant RAM as Unified RAM

    You->>Py: python script.py
    Py->>LM: load("mlx-community/gemma-3-1b-it-4bit")
    LM->>Cache: model exists locally?
    alt First time
        Cache-->>LM: no
        LM->>HF: download safetensors (~600 MB)
        HF-->>Cache: save weights + tokenizer
    end
    LM->>RAM: mmap weights into unified memory
    LM->>Metal: register kernels

    Py->>LM: generate(prompt, max_tokens=200)
    loop For each new token
        Metal->>RAM: read weights + KV cache
        Metal->>Metal: forward pass
        Metal->>RAM: write next token
    end
    LM-->>Py: full response string
    Py-->>You: print

    style Metal fill:#3b82f6,color:#fff
    style RAM fill:#10b981,color:#fff
```

After the first run, no network. The model lives in your cache. **You own this stack.**

---

## 🧪 Try the 4B variant (if your Mac has 16+ GB RAM)

```bash
mlx_lm.generate \
    --model mlx-community/gemma-3-4b-it-4bit \
    --prompt "Compare RAG and long-context-stuffing in 4 bullets." \
    --max-tokens 200
```

The 4B model is ~2.4 GB and substantially better at reasoning. Phase 3's iOS app will probably use it (depending on device storage budgets).

---

## 🔧 Comparison to Gemini 2.5 Flash (the cloud counterpart)

| Aspect            | Gemma 3 1B local                   | Gemini 2.5 Flash cloud       |
|-------------------|------------------------------------|------------------------------|
| Where             | Your Mac                           | Google data center           |
| Cost              | Free                                | ~$0.0003 per call             |
| Latency           | ~500 ms TTFT, 30 tok/s             | ~300 ms TTFT, 60+ tok/s       |
| Quality           | Good for simple tasks              | Best-in-class                 |
| Multimodal        | Text-only (1B); 4B+ have vision    | Native (text+image+audio+video)|
| Context window    | 32 K tokens                         | 1 M tokens                    |
| Offline?          | ✅ Yes                              | ❌ No                          |
| Privacy           | ✅ Stays on device                  | ⚠️ Vertex enterprise gives you VPC-SC + DLP |

This trade-off matrix is **exactly** what an FDE has to articulate to a customer asking "should we run AI on-device or in the cloud?"

---

## 📚 References

- **Gemma 3 model card** — https://huggingface.co/google/gemma-3-1b-it
- **MLX community models** — https://huggingface.co/mlx-community
- **`mlx-lm` quickstart** — https://github.com/ml-explore/mlx-lm
- **Hugging Face quantization explainer** — https://huggingface.co/blog/4bit-transformers-bitsandbytes

---

## ✅ Exit criteria

- [ ] Gemma 3 1B downloaded to `~/.cache/huggingface/`
- [ ] First generation succeeded with a coherent response
- [ ] Streaming variant worked
- [ ] I can name the trade-offs vs Gemini 2.5 Flash (4+ axes)

🎉 You ran a frontier-quality LLM locally on your laptop. Take a screenshot — this is going in your blog post.

**Next:** [`05-terraform-fundamentals.md`](05-terraform-fundamentals.md) (after lunch)

---

