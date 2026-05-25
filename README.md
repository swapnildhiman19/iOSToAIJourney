# AI Engineer Study Material — Master Index

> **Goal:** Career switch from iOS engineer (Walmart) → Forward-Deployed AI Engineer in ~8 months.
> **Window:** May 19, 2026 → mid-January 2027

This folder is the **knowledge base** — all the theory, tutorials, code, diagrams, and references — that supports the roadmap. It will grow week-by-week.

---

## How this folder is organized

```
/Users/s0d0bla/Desktop/AI/
├── README.md                  ← you are here (master index)
├── Week-01-Setup/             ← Phase 0: Tooling + accounts + first hello-world (May 19–25)
├── Week-02-...                ← (future) Phase 1 begins
├── ...
```

Each `Week-XX/` folder contains:

| Subfolder              | What lives there                                                         |
|------------------------|--------------------------------------------------------------------------|
| `Day-NN-Day-Date/`     | Daily lessons — one Markdown file per topic, with code in `code/`        |
| `theory/`              | Cross-cutting conceptual deep-dives (e.g. "What is an LLM API")          |
| `code/`                | Runnable, self-contained scripts referenced by the day notes             |

---

## Pedagogy — every topic follows the same structure

1. **🧒 Layman explanation** — what it is in plain English, a real-world analogy
2. **🔧 Technical deep-dive** — how it actually works, the API/CLI/config details
3. **📊 Flow diagram** — Mermaid diagram showing the system or data flow
4. **💻 Hands-on code** — runnable snippet you can paste into your terminal
5. **📚 References** — official docs + recommended reads
6. **✅ Exit criteria** — what "done" looks like for this topic

---

## Phase Map (from the roadmap)

| Phase | Weeks       | Window                | Outcome                                                                  |
|------:|-------------|-----------------------|--------------------------------------------------------------------------|
|     0 | 1           | May 19 – May 25       | Tooling + Hashnode + GitHub + GCP + Docker + Terraform installed         |
|     1 | 2–10        | May 26 – Jul 27       | Doc-Talk (FastAPI + LLM) dockerized, on CI, with Slack webhook           |
|     2 | 11–19       | Jul 28 – Sep 28       | OSS-Docs RAG on Cloud Run with Vertex Gemini + Redis cache + SLOs        |
|     3 | 20–28       | Sep 29 – Nov 30       | Researcher Agent on GKE + Terraform + Vertex Agent Engine + Bedrock      |
|     4 | 29–35       | Dec 1 – Jan 17, 2027  | System design + 13 mock interviews + FDE playbook + 15+ apps sent        |

---

## Week 1 Quick Reference (current week)

| Day  | Date         | Focus                                                            |
|------|--------------|------------------------------------------------------------------|
| Tue  | May 19       | `uv` + Python project + `google-genai` SDK + Anthropic SDK + keys|
| Wed  | May 20       | Hashnode blog + kickoff post draft                               |
| Thu  | May 21       | GitHub portfolio repo skeleton + Docker Desktop install          |
| Fri  | May 22       | GCP account + Vertex AI APIs + `gcloud` CLI + billing alert      |
| Sat  | May 23       | Xcode 16+ + MLX + Gemma 3 (1B) local + Terraform CLI + blog live |
| Sun  | May 24       | Notion/Linear tracker + AWS account + 3 hello-world scripts pass |
| Mon  | May 25       | Buffer day — anything that slipped + Hashnode post live          |

See `Week-01-Setup/README.md` for the full Week 1 syllabus.

---

## Core Stack Decisions (memorize these)

| Layer                  | Primary choice                          | Why                                              |
|------------------------|------------------------------------------|--------------------------------------------------|
| LLM SDK                | `google-genai` (Gemini)                  | Unified surface for AI Studio + Vertex AI        |
| LLM SDK (secondary)    | `anthropic` (Claude)                     | Cross-provider literacy, FDE interview signal    |
| Default reasoning model| Gemini 2.5 Pro                           | 1M+ context, deep reasoning                      |
| Default cheap-fast     | Gemini 2.5 Flash                         | Workhorse — multimodal, 1M context, cheap        |
| High-volume model      | Gemini 2.5 Flash-Lite                    | Cheapest tier for batch / scale                  |
| Embeddings             | `gemini-embedding-001`                   | Top MTEB, Matryoshka truncatable (768/1536/3072) |
| Backend framework      | FastAPI + Pydantic                       | Industry standard for Python LLM services        |
| Package manager        | `uv` (by Astral)                         | 10–100× faster than pip, lockfile-first          |
| Cloud (primary)        | GCP — Vertex AI, Cloud Run, GKE          | Native home of Gemini, FDE-target ecosystem      |
| Cloud (secondary)      | AWS — Bedrock                            | 40% of US enterprises are AWS-first              |
| Agent framework        | Google ADK → Vertex Agent Engine         | Production-grade, Gemini-native                  |
| Vector DB              | pgvector on Neon → Memorystore in prod   | Postgres-native, no extra service to operate     |
| Observability          | Langfuse                                 | Free tier, OSS, LLM-native traces                |
| Eval framework         | Ragas                                    | RAG-specific metrics (faithfulness, recall)      |
| Blog                   | Hashnode                                 | Free, dev-focused, custom domain support         |
| On-device LLM (iOS)    | Gemma 3 (1B/4B) via MLX                  | Apple Silicon-optimized, open weights            |

---

## Daily ritual (non-negotiables from the roadmap)

- 🧘 **8:00–9:00 AM meditation** — keystone habit, no phone for first 30 min after waking
- 🍽️ **12:00–12:30 PM team lunch** at Walmart office — social, non-negotiable
- 💃 **Sat + Sun 5–7 PM dance** — cognitive performance depends on it
- 🛌 **00:15 sleep** for 7.5 hrs minimum

---

## How to use this knowledge base each day

1. Open today's `Day-NN-Day-Date/` folder
2. Read the markdown lessons in numbered order
3. Run the code snippets in `code/` — do not just read them
4. Tick the "Exit criteria" checklist at the end of each lesson
5. Open `Week-XX/README.md` at end of week, mark week complete

---

