---
title: "My 8-month plan to become a Forward-Deployed AI Engineer"
subtitle: "A 32-hour/week plan, in public"
slug: ios-to-ai-engineer-2026
publishedAt: "2026-05-23T08:00:00Z"
tags: ["ai", "career", "llm", "gemini", "swift"]
---

## I'm betting eight months of my life on this plan.

On May 20th 2026, the curious iOS Software Developer in me has finally decided to just jump into the field of AI. Seeing all the advancemets being going on in AI is actually a bit scary, won't deny the fact, not really sure how iOS Development would turn out to be in future. But on other hands if I am seeing it's opening so many paths of learning for me, 
if I see it is actually democratizing the education, maybe we are build to do something bigger and this the leap of faith that I am going ahead with.

## Why now, why this

I have spend around 4 years in a famous Fortune 500 company building the scalable iOS apps in Swift + UIKit, the work is good, but as we all know no one can predict the future.
Two things that forced me this decision:

1. **The job exists now and didn't 18 months ago.** "Forward-Deployed Engineer" / "AI Engineer" is a category. Anthropic, OpenAI, Palantir, Scale all post for it.
2. **The skills are mostly engineering, not research.** I'm not retraining as an ML PhD. I'm picking up Python + LLM APIs + cloud + product.

I'm not quitting iOS. I'll keep iOS as a secondary track (Apple Intelligence is going to matter), but the next 8 months tilt 60/40 toward AI Engineer.

### Phase 0 (1 week) — Setup

(Brief: this week. Tools, accounts, hello-world. The post you're reading is the artifact for this phase.)

### Phase 1 (9 weeks) — Foundations + Containerization

Build **Doc-Talk** — a FastAPI service that takes a PDF, answers structured questions with Gemini 2.5 Flash, returns Pydantic-validated JSON. Ship it with a Dockerfile, GitHub Actions CI, and a Slack webhook integration. Most LLM tutorials skip these production-engineering pieces — I'm putting them in from week 1.

Skills: Python, FastAPI, Pydantic, Gemini SDK, Anthropic SDK,
prompt engineering, structured outputs, Docker,
docker-compose, GitHub Actions, webhooks.

### Phase 2 (9 weeks) — RAG + Cloud-Native Deploy

Build **OSS-Docs RAG** — a Retrieval-Augmented Generation system over FastAPI + Swift + Kubernetes documentation. Use pgvector on Neon, hybrid retrieval (BM25 + dense), Cohere reranker. Deploy to **Cloud Run with Workload Identity Federation** so the service calls Vertex Gemini *without* an API key. Add **Redis semantic cache + Gemini context caching**. Define **SLOs** with Cloud Monitoring.

Skills: embeddings, chunking, hybrid retrieval, reranking,
evals (Ragas + LLM-as-judge), observability (Langfuse),
Cloud Run, Secret Manager, Workload Identity, Memorystore,
SLOs.

### Phase 3 (9 weeks) — Agents + Apple AI + Production Infra

Build **Researcher Agent** — a multi-agent system on **Google ADK** with MCP tool integration, GraphRAG over Neo4j, and grounding-with-search. Deploy to **GKE behind a private VPC** with **all infrastructure declared in Terraform**. Side-quest: ship an **iOS Apple Intelligence companion app** using Foundation Models + on-device **Gemma 3 (1B) via MLX**. Add Bedrock literacy and a k6 load test.
Skills: ADK, MCP, multi-agent orchestration, GraphRAG,
grounding, Vertex Agent Engine, AWS Bedrock, GKE,
Terraform, Pub/Sub, VPC + Private Service Connect,
k6 load testing, Foundation Models, MLX.

### Phase 4 (7 weeks) — System Design + Interview + FDE Playbook

13 mock interviews. Chip Huyen's *AI Engineering* book. The **Forward-Deployed Engineer playbook** — discovery, pilot scoping, integration patterns, success metrics, handoff. 15+ applications sent.

---

## The stack I'm betting on

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

Three signals I'll track weekly:

1. **DSA streak** — LeetCode 150 patterns, 3 problems × 4 weekdays
2. **Blog cadence** — one substantive post per 4–5 weeks (target: 7 posts in 8 months)
3. **Project shipping** — does each phase end with a deployed, accessible artifact?

The lagging indicator I care about is **interviews booked**. That's a Phase 4 metric.

### The compounding bet

The plan compounds: Week 1 sets up tooling that Week 2 builds on. By Week 19 my OSS-Docs RAG is running on real infrastructure. By Week 28 my Researcher Agent is on GKE with Terraform-as-code, behind a private VPC. By Week 35 I have 7 blog posts, 3 production artifacts, 13 mocks, and a recruiter funnel.

This is the difference between "studying AI" and "becoming an AI Engineer." One is a hobby. The other is a job.

---

## What's next


The first artifact is **Doc-Talk** (FastAPI + Gemini + Docker + Slack webhook), shipping by July 27, 2026. The blog post for that drops the same week — *"Shipping my first LLM app: Dockerfile, GitHub Actions CI, and a Slack webhook in a weekend."*

Subscribe to follow along. Repo is at https://github.com/swapnildhiman19/iOSToAIJourney

If you're on the same jump, my DMs are open.

---
