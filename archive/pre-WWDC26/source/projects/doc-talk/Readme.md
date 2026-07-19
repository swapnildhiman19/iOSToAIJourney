# Doc-Talk

> **Status:** Coming Phase 1 (May 26 – Jul 27, 2026)

A FastAPI service that ingests PDFs and answers structured questions using
Gemini 2.5 Flash, returning Pydantic-validated JSON (`answer`, `citations`,
`confidence`).

## Planned stack
- FastAPI + Pydantic + Instructor
- `google-genai` SDK (Gemini 2.5 Flash + Pro)
- Pgvector on Neon (dev)
- Docker multi-stage build
- GitHub Actions CI (lint + test + build + push)
- Slack `/docTalk` webhook integration
- Deployed to Render

## What I'll learn
- Production FastAPI patterns (async, dep injection, streaming)
- Structured generation with Gemini schema
- Cross-provider parity (Gemini + Anthropic)
- Dockerfile best practices
- GitHub Actions CI/CD
- Webhooks (Slack-style)

## Companion blog post
*(Coming Jul 27, 2026)* — "Shipping my first LLM app: Dockerfile, CI, and a Slack webhook"