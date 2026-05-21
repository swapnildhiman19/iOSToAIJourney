# 05 — End of Week 1 Checklist

The final exit gate. If every box below is green, **Phase 0 is officially complete**.

---

## ✅ Tooling — everything from Week 1

```bash
# Python + uv
python --version          # 3.12.x
uv --version              # 0.x.x

# GCP
gcloud --version          # Google Cloud SDK …
gcloud config get project # your personal project
gcloud auth application-default print-access-token | head -c 20 && echo …

# Docker
docker --version
docker ps                 # daemon responsive

# Xcode + iOS
xcodebuild -version       # Xcode 16.x

# MLX
source ~/Desktop/AI/ml-tools/mlx-env/bin/activate
python -c "import mlx.core as mx; print(mx.default_device())"  # Device(gpu, 0)
deactivate

# Terraform
terraform version         # v1.9.x

# AWS
aws --version
aws sts get-caller-identity  # IAM admin Arn, not :root

# Verification script
verify-ai                 # 5/5 ✅
```

All green? Continue.

---

## ✅ Artifacts

- [ ] **Portfolio GitHub repo** exists with at least: `pyproject.toml`, `.env.example`, `Dockerfile`, `scripts/week1_verify.py`
- [ ] **Hashnode kickoff post** is live (URL recorded)
- [ ] **Hashnode Week 1 recap post** is live (URL recorded)
- [ ] **`~/Desktop/AI/Week-01-Setup/blog-posts.md`** has both URLs
- [ ] **Notion or Linear tracker** has Week 1 row marked Done with all 7 daily rows linked
- [ ] **Week 1 Reckoning** is filled in (all 7 sections)
- [ ] **`~/Desktop/AI/Week-02-LLM-Foundations/`** folder pre-created
- [ ] **GCP $50 billing alert** + **AWS $5 billing alarm** both armed

---

## ✅ Mental model checks (15 minutes — write answers in tracker)

If you can answer all 10 from memory in ≤1 sentence each, your foundation is solid:

1. What's an AI Engineer vs an ML Engineer vs an FDE? *(in your own words)*
2. What is a token, and why do prices come per-million-tokens?
3. Why is Application Default Credentials better than a service-account JSON?
4. What's the difference between `gcloud auth login` and `gcloud auth application-default login`?
5. What does `docker build` cache, and how do you invalidate the cache deliberately?
6. What's MLX's "unified memory" advantage over PyTorch + CUDA?
7. What does `terraform plan` show that `terraform apply` doesn't?
8. Why does the buffer day matter for sustainability of the 35-week roadmap?
9. What's the contract of your `week1_verify.py` script?
10. What is Week 2's one-sentence headline goal?

---

## ✅ Commit + push

If you've been committing daily, this is a no-op. If not:

```bash
cd ~/Desktop/AI/portfolio
git status
git add -A   # review carefully — make sure no .env or AWS keys
git commit -m "Phase 0 / Week 1 complete: setup + verify-ai 5/5 green

- Python 3.12 + uv venv with google-genai, anthropic, boto3, mlx, mlx-lm
- GCP + Vertex hello-world via ADC
- Docker fundamentals + first Dockerfile
- MLX + Gemma 3 1B local inference
- Terraform 1.9 CLI
- AWS account + CLI + Boto3
- scripts/week1_verify.py — all 5 checks green

🌀 Magic applied with Wibey VSCode Extension 🪄"
git push
```

> ⚠️ Open the `git status` output carefully before `git add -A`. Specifically check no `.env`, no `~/.aws/credentials` symlink, no `service-account*.json`.

---

## ✅ Final hygiene

- [ ] Close Slack work channels
- [ ] Close laptop in <30 minutes from now
- [ ] Note tomorrow's first-move task on a sticky note (or tracker)
- [ ] Optional: pour something. **You finished Phase 0 of an 8-month transition.**

---

## 🎉 The big idea of Week 1

> **Week 1 was 100% scaffolding.** No "AI feature" was actually built. And yet
> — every model API, every cloud, every local-inference toolchain that the
> next 34 weeks depend on is now installed, authenticated, and verified.
>
> That's the difference between a roadmap that survives Week 4 and one that
> dies in a debugging swamp. You bought yourself 34 weeks of velocity.

**Phase 0 is done. See you Tuesday.**

---

🌀 *Magic applied with Wibey VS Code Extension 🪄*
