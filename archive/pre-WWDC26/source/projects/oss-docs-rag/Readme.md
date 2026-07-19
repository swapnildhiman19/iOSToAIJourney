# OSS-Docs RAG

> **Status:** Coming Phase 2 (Jul 28 – Sep 28, 2026)

A production-grade RAG system over FastAPI + Swift + Kubernetes documentation.
Hybrid retrieval (BM25 + dense), Cohere reranker, Gemini context caching +
Redis semantic cache, deployed to Cloud Run via Workload Identity Federation.

## Planned stack
- Embeddings: `gemini-embedding-001`
- Vector DB: pgvector → Memorystore in prod
- Retrieval: BM25 + dense + Cohere rerank
- Caching: Gemini context cache + Redis semantic cache
- Evals: Ragas + LLM-as-judge (Gemini 2.5 Pro as judge)
- Observability: Langfuse
- Deploy: Cloud Run + Workload Identity for Vertex
- Monitoring: Cloud Monitoring + SLOs

## Companion blog posts
*(Coming Aug + Sep 2026)*
1. "Embeddings + Matryoshka truncation: when 768 dims beats 3072"
2. "From localhost to Cloud Run: Workload Identity + context cache + Redis"