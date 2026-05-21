# 04 — Draft Your Kickoff Post

> Spend 2 hours here. Goal: a complete draft saved as `posts/00-kickoff.md` in your portfolio repo. Polish on Saturday.

---

## 🧒 Layman explanation

You're writing the post that **commits you publicly** to the 8-month plan. Once it's live, you've created an accountability device that pulls you forward when motivation dips in Month 3.

The draft you write today doesn't have to be perfect. It has to be **complete enough that Saturday morning you only need to polish** — not write from scratch.

---

## 🎯 Suggested working title

> *"Going from iOS to AI Engineer in 7 months — betting on Gemini + ADK"*

Alternatives if that doesn't fit your voice:
- *"My 8-month plan to become a Forward-Deployed AI Engineer"*
- *"Why I'm quitting iOS (in my head) — and the 32-hour/week plan to become an AI Engineer"*
- *"From UIKit to Vertex AI: a Walmart engineer's career switch in public"*

Pick one. Don't agonize.

---

## 📝 Full draft template (copy this into `posts/00-kickoff.md`)

```markdown
---
title: "Going from iOS to AI Engineer in 7 months — betting on Gemini + ADK"
subtitle: "A 32-hour/week plan, in public"
slug: ios-to-ai-engineer-2026
publishedAt: "2026-05-23T08:00:00Z"
tags: ["ai", "career", "llm", "gemini", "swift"]
---

## I'm betting eight months of my life on this plan.

*(Hook — 200 words)*

In May 2026 I decided to stop being "the iOS engineer who's curious about AI" and become the AI Engineer. I am giving myself ~8 months — May 19, 2026 to January 17, 2027 — and ~32 hours per week of focused study, in addition to my Walmart day-job. The target role is **Forward-Deployed AI Engineer** at companies like Anthropic, OpenAI, or Palantir.

This post is the public commitment. Three flagship projects, seven blog posts, one career switch.

If you're an engineer thinking about the same jump, this is the plan I'm following. Steal, fork, or skip — but here it is.

---

## Why now, why this

*(Context — 300 words)*

I've spent ~4 years at Walmart Global Tech building iOS apps in Swift + UIKit. The work is good. The industry I'm in is shrinking by inches. Meanwhile, every interesting startup posting in 2026 wants someone who can wire an LLM into a Slack bot in a weekend.

Two things forced the decision:

1. **The job exists now and didn't 18 months ago.** "Forward-Deployed Engineer" / "AI Engineer" is a category. Anthropic, OpenAI, Palantir, Scale all post for it.
2. **The skills are mostly engineering, not research.** I'm not retraining as an ML PhD. I'm picking up Python + LLM APIs + cloud + product.

I'm not quitting iOS. I'll keep iOS as a secondary track (Apple Intelligence is going to matter), but the next 8 months tilt 60/40 toward AI Engineer.

---

## The plan — five phases over 35 weeks

*(Body — 1000+ words, sub-sectioned)*

### Phase 0 (1 week) — Setup

(Brief: this week. Tools, accounts, hello-world. The post you're reading is the artifact for this phase.)

### Phase 1 (9 weeks) — Foundations + Containerization

Build **Doc-Talk** — a FastAPI service that takes a PDF, answers structured questions with Gemini 2.5 Flash, returns Pydantic-validated JSON. Ship it with a Dockerfile, GitHub Actions CI, and a Slack webhook integration. Most LLM tutorials skip these production-engineering pieces — I'm putting them in from week 1.

```
Skills: Python, FastAPI, Pydantic, Gemini SDK, Anthropic SDK,
        prompt engineering, structured outputs, Docker,
        docker-compose, GitHub Actions, webhooks.
```

### Phase 2 (9 weeks) — RAG + Cloud-Native Deploy

Build **OSS-Docs RAG** — a Retrieval-Augmented Generation system over FastAPI + Swift + Kubernetes documentation. Use pgvector on Neon, hybrid retrieval (BM25 + dense), Cohere reranker. Deploy to **Cloud Run with Workload Identity Federation** so the service calls Vertex Gemini *without* an API key. Add **Redis semantic cache + Gemini context caching**. Define **SLOs** with Cloud Monitoring.

```
Skills: embeddings, chunking, hybrid retrieval, reranking,
        evals (Ragas + LLM-as-judge), observability (Langfuse),
        Cloud Run, Secret Manager, Workload Identity, Memorystore,
        SLOs.
```

### Phase 3 (9 weeks) — Agents + Apple AI + Production Infra

Build **Researcher Agent** — a multi-agent system on **Google ADK** with MCP tool integration, GraphRAG over Neo4j, and grounding-with-search. Deploy to **GKE behind a private VPC** with **all infrastructure declared in Terraform**. Side-quest: ship an **iOS Apple Intelligence companion app** using Foundation Models + on-device **Gemma 3 (1B) via MLX**. Add Bedrock literacy and a k6 load test.

```
Skills: ADK, MCP, multi-agent orchestration, GraphRAG,
        grounding, Vertex Agent Engine, AWS Bedrock, GKE,
        Terraform, Pub/Sub, VPC + Private Service Connect,
        k6 load testing, Foundation Models, MLX.
```

### Phase 4 (7 weeks) — System Design + Interview + FDE Playbook

13 mock interviews. Chip Huyen's *AI Engineering* book. The **Forward-Deployed Engineer playbook** — discovery, pilot scoping, integration patterns, success metrics, handoff. 15+ applications sent.

---

## The stack I'm betting on

*(Body continued)*

- **Primary LLM SDK:** `google-genai` (Gemini, primary). Anthropic SDK secondary.
- **Default model:** Gemini 2.5 Flash for 80% of calls, 2.5 Pro for reasoning.
- **Backend:** FastAPI + Pydantic v2.
- **Agent framework:** Google ADK + Vertex Agent Engine.
- **Vector DB:** pgvector on Neon (dev) → Memorystore + Cloud SQL (prod).
- **Cloud:** GCP primary (Vertex AI + Cloud Run + GKE), AWS Bedrock for literacy.
- **Observability:** Langfuse.
- **Eval:** Ragas + LLM-as-judge with Gemini 2.5 Pro.
- **Blog:** Hashnode (this).
- **Tracker:** Notion / Linear.

### Why Gemini-primary

Three reasons:
1. **Cost** — Gemini 2.5 Flash is ~10× cheaper than Claude Sonnet per token at similar quality on most tasks.
2. **Context** — Gemini 2.5's 1M-token window changes what's possible in retrieval and caching.
3. **Production plumbing** — Vertex AI has VPC-SC, regional residency, audit logs, IAM. Those are what enterprise customers need; and enterprise customers are who FDEs sell to.

Claude is my comparator. Every artifact runs against both providers so I can speak both ecosystems in interviews.

---

## What I'm explicitly **not** doing

- I'm **not** learning LangChain. ADK + raw SDK calls are enough for what I want to ship.
- I'm **not** learning Kubernetes deeply until Phase 3 (and only what's needed).
- I'm **not** chasing the latest model release. Stack decisions stay frozen until end of phase.
- I'm **not** building a chatbot for my portfolio. Demos lie. Production artifacts don't.

---

## How I'll measure success

*(Lessons section — 300 words)*

Three signals I'll track weekly:

1. **DSA streak** — NeetCode 150 patterns, 3 problems × 4 weekdays
2. **Blog cadence** — one substantive post per 4–5 weeks (target: 7 posts in 8 months)
3. **Project shipping** — does each phase end with a deployed, accessible artifact?

The lagging indicator I care about is **interviews booked**. That's a Phase 4 metric.

### The compounding bet

The plan compounds: Week 1 sets up tooling that Week 2 builds on. By Week 19 my OSS-Docs RAG is running on real infrastructure. By Week 28 my Researcher Agent is on GKE with Terraform-as-code, behind a private VPC. By Week 35 I have 7 blog posts, 3 production artifacts, 13 mocks, and a recruiter funnel.

This is the difference between "studying AI" and "becoming an AI Engineer." One is a hobby. The other is a job.

---

## What's next

*(Closing — 100 words)*

The first artifact is **Doc-Talk** (FastAPI + Gemini + Docker + Slack webhook), shipping by July 27, 2026. The blog post for that drops the same week — *"Shipping my first LLM app: Dockerfile, GitHub Actions CI, and a Slack webhook in a weekend."*

Subscribe to follow along. Repo is at `github.com/<your-handle>/ai-engineer-portfolio` (placeholder folders today, real code by Phase 1).

If you're on the same jump, my DMs are open.

---

*Update log:*
- *May 23, 2026 — Original post.*
```

---

## 💻 Hands-on — actually write it

1. Create `~/Desktop/AI/code/ai-engineer-portfolio/posts/` folder
2. Save the above template as `posts/00-kickoff.md`
3. **Edit it line by line** to be in your voice. Don't ship a template.
4. Insert any anecdotes / numbers / context that's true for you
5. Adjust the working title if "Going from iOS to AI Engineer in 7 months" doesn't fit
6. Don't worry about formatting yet — Saturday is polish day

### Time-box yourself

| Block             | What to do                                                  |
|-------------------|-------------------------------------------------------------|
| First 30 min      | Write the hook + context (Sections 1–2). Just type fast.    |
| Next 60 min       | Write the body (Section 3). Use the phase outlines provided.|
| Last 30 min       | Lessons + What's next (Sections 4–5).                       |

Don't edit while writing. Get a draft to "complete but rough" before going back.

---

## 📚 References

- **Anatomy of a great launch post** — Andrew Chen, Lenny Rachitsky
- **"Show your work"** — Austin Kleon (book)
- **Sample career-switch posts** — search Hashnode for "career switch software engineer"

---

## ✅ Exit criteria

- [ ] `posts/00-kickoff.md` exists with all 5 sections (hook → next)
- [ ] In my voice, not template language
- [ ] Working title chosen
- [ ] Linked to GitHub portfolio repo URL (Thursday will create it)
- [ ] Saved to git: `git add posts/ && git commit -m "draft: kickoff post"`

**Next:** [`05-end-of-day-checklist.md`](05-end-of-day-checklist.md)

---

🌀 *Magic applied with Wibey VS Code Extension 🪄*
