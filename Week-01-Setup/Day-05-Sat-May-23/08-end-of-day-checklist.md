# 08 — Day 5 End-of-Day Checklist

You did a *lot* today. Validate before you close the laptop.

---

## ✅ Tooling verification

```bash
# Xcode + iOS
xcodebuild -version                                # Xcode 16.x ✅
xcrun simctl list runtimes | grep "iOS 18"         # iOS 18.x runtime present ✅

# MLX + Gemma 3
source ~/Desktop/AI/ml-tools/mlx-env/bin/activate
python -c "import mlx.core as mx; print(mx.default_device())"  # Device(gpu, 0) ✅
du -sh ~/.cache/huggingface/                       # ~600 MB ✅ (Gemma cached)

# Terraform
terraform version                                  # v1.9.x ✅
```

If every command above is green, Day 5 tooling is solid.

---

## ✅ Knowledge checks

Answer these from memory. If you can't, re-skim that lesson.

- [ ] Why is MLX faster than PyTorch on a Mac? *(unified memory — no CPU↔GPU copy)*
- [ ] What's the difference between Foundation Models and MLX? *(Apple's native shipped LLM vs. open-source framework you control)*
- [ ] What does `terraform plan` do that `terraform apply` doesn't? *(plan shows the diff but mutates nothing; apply executes it)*
- [ ] Where does Terraform store the "real cloud truth"? *(`terraform.tfstate`)*
- [ ] What was the model you ran locally and roughly how big is it on disk? *(`mlx-community/gemma-3-1b-it-4bit`, ~600 MB at 4-bit quant)*

---

## ✅ Artifacts saved

- [ ] Kickoff blog post is **live** with a public URL
- [ ] Blog URL written to `~/Desktop/AI/Week-01-Setup/blog-posts.md`
- [ ] Gemma 3 first-generation screenshot saved (for the next blog post)
- [ ] `~/Desktop/AI/ml-tools/` exists with `mlx-env/` and `mlx-examples/`

---

## 🧠 The big idea of Day 5

> **You compressed three trillion-dollar trends into one Saturday:**
> on-device AI (MLX + Gemma), infrastructure-as-code (Terraform),
> and learning-in-public (the kickoff post going live).
>
> From here, every week stacks more leverage on this base.

Tomorrow (Sunday) is lighter — Notion/Linear tracker setup, free AWS account, and verifying all three hello-world scripts (Gemini AI Studio, Gemini Vertex, Anthropic) still pass.

**Go for a walk. You earned it.**

---

🌀 *Magic applied with Wibey VS Code Extension 🪄*
