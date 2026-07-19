# 06 — Day 3 End-of-Day Checklist

## ✅ Verification

```bash
# 1. GitHub repo is live and public
open https://github.com/<your-handle>/ai-engineer-portfolio

# 2. Three flagship folders exist
ls projects/
# Expected: doc-talk  oss-docs-rag  researcher-agent

# 3. Docker works
docker run hello-world | tail -5

# 4. Personal Dockerfile builds + runs
cd ~/Desktop/AI/code/ai-engineer-portfolio
docker build -t hello-gemini:demo .
docker run --rm --env-file .env hello-gemini:demo
# Expected: Gemini response printed

# 5. .env NOT visible on GitHub
# Open https://github.com/<your-handle>/ai-engineer-portfolio in browser
# Confirm there's no .env file in the file tree
```

---

## 💾 Commit + push today's work

```bash
git add Dockerfile .dockerignore projects/ README.md
git commit -m "feat: add Dockerfile + .dockerignore + 3 flagship placeholders"
git push
```

---

## 📓 Journal (3 min)

1. Did Docker concepts click? Which layer / cache idea surprised me?
2. What does my GitHub profile look like to a recruiter right now?
3. Tomorrow: GCP. What am I nervous about?

---

## 🌙 Prep for tomorrow (Fri May 22)

Tomorrow is **GCP + Vertex AI + `gcloud` CLI**. Prep:

- [ ] Decide which personal email to use for GCP — must be a personal Google account, NOT @walmart
- [ ] Have a credit card handy (GCP free tier requires CC for verification; you won't be charged for hello-world)
- [ ] Open https://cloud.google.com/free in advance — read the free-tier limits

---

## ✅ Day 3 final exit criteria

- [ ] GitHub repo `ai-engineer-portfolio` is public + has Day 1+2 work pushed
- [ ] 3 flagship folders with placeholder READMEs exist
- [ ] Top-level README has the projects table
- [ ] Docker Desktop installed; `docker run hello-world` works
- [ ] `Dockerfile` + `.dockerignore` created
- [ ] `docker build` + `docker run` of `hello-gemini:demo` succeeds
- [ ] All committed + pushed
- [ ] Journal written

✅ Tomorrow: [`../Day-04-Fri-May-22/README.md`](../Day-04-Fri-May-22/README.md)

---

