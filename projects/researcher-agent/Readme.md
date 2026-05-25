# Researcher Agent

> **Status:** Coming Phase 3 (Sep 29 – Nov 30, 2026)

A multi-agent research assistant built on Google ADK with MCP tool
integration, GraphRAG over Neo4j, grounding-with-Google-Search,
deployed to GKE behind a private VPC, infrastructure as Terraform.

## Planned stack
- Framework: Google ADK
- Models: Gemini 2.5 Pro (supervisor) + Flash (workers)
- Tools: MCP toolset, Google Search grounding, Code execution
- Memory: Vertex AI Memory Bank
- Graph layer: Neo4j + entity extraction via Gemini
- Async: Pub/Sub for long-running tools
- Deploy: GKE + Vertex Agent Engine
- Infra: 100% Terraform
- Cross-cloud: AWS Bedrock literacy (Claude-via-Bedrock comparison)
- Load test: k6 (steady, spike, soak)
- Networking: Private Service Connect to Memorystore

## Companion blog posts
*(Coming Oct + Nov 2026)*
1. "Vertex Agent Engine vs Bedrock Agents for an ADK-style agent"
2. "Cloud Run vs GKE for AI agents — when each wins"
3. "GraphRAG vs hybrid RAG on a real corpus"
4. "Load-testing an LLM agent: what k6 told me about my p95"