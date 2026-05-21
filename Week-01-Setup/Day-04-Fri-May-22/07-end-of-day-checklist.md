# 07 — Day 4 End-of-Day Checklist

> 18:30. Big day. Verify, commit, decompress.

---

## ✅ Verification — run all 5

```bash
# 1. GCP authenticated
gcloud auth list
# Expected: my personal email as ACTIVE

# 2. Project set
gcloud config get-value project
# Expected: ai-engineer-portfolio-123456 (or your real ID)

# 3. APIs enabled
gcloud services list --enabled --filter="name~aiplatform OR name~generativelanguage"
# Expected: both visible

# 4. ADC works
gcloud auth application-default print-access-token | head -c 40 && echo
# Expected: an access-token string (40 chars)

# 5. Vertex hello-world runs
cd ~/Desktop/AI/code/ai-engineer-portfolio
uv run python code/hello_vertex.py
# Expected: a Gemini response

# 6. AI Studio path still works
uv run python code/hello_gemini.py
# Expected: a Gemini response (using API key path)

# 7. Anthropic still works
uv run python code/hello_anthropic.py
# Expected: a Claude response
```

You now have **three working LLM call paths**: Gemini via AI Studio, Gemini via Vertex, and Claude direct. This is the production-flavored setup.

---

## 💾 Commit + push

```bash
cd ~/Desktop/AI/code/ai-engineer-portfolio
git add code/hello_vertex.py .env.example
git commit -m "feat(gcp): add Vertex AI hello-world via ADC; update .env.example"
git push
```

(Don't commit `.env` — only `.env.example` with placeholders.)

---

## 📓 Journal (5 min today — bigger day)

1. What clicked about ADC that didn't before?
2. Did `$50 billing alert` give me peace of mind? (yes/no — and why)
3. What's the most-likely place I'll lose money in this account? (think ahead)
4. How confident am I that I could re-do today from scratch in 90 minutes?

---

## 🌙 Prep for tomorrow (Sat May 23)

Tomorrow is the **biggest day of the week**: Xcode + MLX + Gemma 3 + Terraform + publish blog post. Prep:

- [ ] Open Xcode (or download Xcode 16+ from the Mac App Store) — it's 7+ GB; start downloading **tonight** before bed so it's ready Saturday morning
- [ ] Confirm 30+ GB of free disk (MLX models are 1–4 GB each)
- [ ] Bookmark https://github.com/ml-explore/mlx-examples
- [ ] Bookmark https://developer.hashicorp.com/terraform/install
- [ ] Re-read your kickoff post draft tonight (in bed, ideally) — Saturday is publish day

---

## ✅ Day 4 final exit criteria

- [ ] GCP project created + billing attached
- [ ] $50/month budget + email alerts configured
- [ ] Vertex AI + Generative Language APIs enabled
- [ ] `gcloud` CLI installed + both auth flows done (`login` and `application-default login`)
- [ ] `.env` updated with `GOOGLE_CLOUD_PROJECT` + `GOOGLE_CLOUD_LOCATION`
- [ ] `hello_vertex.py` runs and prints a response using ADC (no API key!)
- [ ] All three hello-worlds still work
- [ ] Committed + pushed
- [ ] Journal written

🎉 You're past the steepest infrastructure day of Week 1.

✅ Tomorrow: [`../Day-05-Sat-May-23/README.md`](../Day-05-Sat-May-23/README.md)

---

🌀 *Magic applied with Wibey VS Code Extension 🪄*
