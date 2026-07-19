# Current Stack Snapshot

> Verified: July 16, 2026  
> Purpose: pin the learning environment for the current phase without pretending
> that model IDs and preview APIs will remain unchanged through March 2027.

This file is refreshed during orientation and every consolidation week. The
roadmap names capabilities first and products second.

## Model strategy

### Primary implementation: Gemini

- **Default production workhorse:** `gemini-3.5-flash` (stable).
- **Hard reasoning comparator:** `gemini-3.1-pro-preview`; because it is a
  preview model, it cannot become a production dependency without a fallback
  and migration test.
- **Real-time native audio experiment:** `gemini-3.1-flash-live-preview`.
  The Gemini Live API remains preview and uses a stateful WebSocket.
- **Embeddings:** `gemini-embedding-2` (stable), including multimodal
  text/image/video/audio/PDF embeddings and selectable output dimensions.
- **SDK:** Google Gen AI SDK with AI Studio for low-friction experiments and
  Vertex/Gemini Enterprise Agent Platform for production identity, governance,
  and deployment.

Do not use a `-latest` alias in a reproducible benchmark or release. Pin a
specific stable model and store the model ID with every evaluation result.

Official sources:

- [Gemini models](https://ai.google.dev/gemini-api/docs/models)
- [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash)
- [Gemini Live API](https://ai.google.dev/gemini-api/docs/live-api)
- [Gemini Embedding 2](https://ai.google.dev/gemini-api/docs/models/gemini-embedding-2)

### Secondary provider: Anthropic

Use one current generally available Claude model for a real provider adapter
and comparison. The July 2026 family has moved far beyond the old Claude 3.5
assumption, so discover capabilities through the Models API and pin the chosen
ID in the platform repository.

Suggested July 2026 experiment tiers:

- balanced production comparator: `claude-sonnet-5`;
- low-latency/cost experiment: the current Haiku tier;
- hard reasoning/enterprise comparator: `claude-opus-4-8`, only when an eval
  shows enough gain to justify its latency and cost;
- long-running-agent research: `claude-fable-5` is current but optional and
  must not expand the provider-adapter scope.

Do not build separate business logic for Claude. The internal message, tool,
streaming, usage, and error contracts remain provider-neutral.

Official source:

- [Claude models overview](https://docs.anthropic.com/en/docs/about-claude/models/overview)

### Provider policy

Before adopting any model:

1. Verify availability in the target region and backend.
2. Record stable/preview status.
3. Run the project evaluation set.
4. Compare quality, p50/p95 latency, input/output tokens, and cost per
   successful task.
5. Test structured output, tools, streaming, multimodal input, and caching
   separately; support differs by model.
6. Define fallback behavior and a migration owner.

## Agent framework and runtime

### Google ADK 2.0

- ADK Python 2.0 is generally available.
- Its key change is the Workflow Runtime: agents, tools, functions, and control
  steps become nodes in a graph.
- It supports static graphs, dynamic workflows, collaborative agents, and a
  deliberate mix of deterministic code and probabilistic reasoning.
- Python is the roadmap implementation language. Go support is not a reason to
  learn Go for this plan.

Official sources:

- [ADK documentation](https://adk.dev/)
- [ADK 2.0 overview](https://adk.dev/2.0/)
- [Why Google built ADK 2.0](https://developers.googleblog.com/why-we-built-adk-20/)

### Google Cloud agent platform

The active product surface is **Gemini Enterprise Agent Platform**. Its managed
deployment service is **Agent Runtime**. “Vertex Agent Engine” is legacy
roadmap language and must not be used as the default current target.

Deployment decision:

- Cloud Run: default for the FastAPI platform and independently deployable
  agent/tool services.
- Cloud Run functions + Eventarc: small HTTP or CloudEvent handlers.
- Agent Runtime: long-running managed agents when its memory, identity,
  governance, and lifecycle features justify the dependency.
- GKE: literacy and comparison only unless a measured requirement cannot be met
  by Cloud Run or Agent Runtime.

Official sources:

- [Gemini Enterprise Agent Platform](https://cloud.google.com/blog/products/ai-machine-learning/introducing-gemini-enterprise-agent-platform)
- [Agent Runtime](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/runtime)
- [ADK and Cloud Run reference architecture](https://docs.cloud.google.com/architecture/single-agent-ai-system-adk-cloud-run)
- [Cloud Run functions](https://cloud.google.com/run/docs/functions/overview)

## Context and retrieval

RAG is active and relevant in the current Google platform: RAG Engine remains a
first-class part of Gemini Enterprise Agent Platform. That fact does not make
RAG the automatic design.

Current learning sequence:

1. deterministic code/SQL;
2. exact and filtered search;
3. model-native file search or cached long context;
4. hybrid sparse+dense retrieval and reranking;
5. graph retrieval for measured multi-hop needs;
6. iterative/agentic retrieval for genuinely dynamic research.

Official sources:

- [RAG Engine overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/rag-engine/rag-overview)
- [RAG Engine API](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/rag-api)

## Agent interoperability

### MCP

- Current production specification on July 16: `2025-11-25`.
- Current remote transport: Streamable HTTP; stdio remains useful for local
  process integrations.
- Authorization requires an OAuth/OIDC threat model; a tool schema is not a
  security boundary.
- The `2026-07-28` revision is a release candidate, not yet the stable spec on
  this snapshot date. It introduces major modern/stateless changes. Recheck on
  or after July 28 before Sprint 6 instructions are authored.

Official sources:

- [Current MCP specification](https://modelcontextprotocol.io/specification/2025-11-25)
- [MCP versioning](https://modelcontextprotocol.io/docs/learn/versioning)
- [2026-07-28 release candidate](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/)

### A2A

A2A is for communication among independently runnable agents. MCP is for an
agent’s tools and resources. The roadmap implements one small A2A interaction
only after local multi-agent boundaries are understood.

Official source:

- [A2A protocol](https://a2a-protocol.org/latest/)

## Real-time voice

- LiveKit/WebRTC is the media and room layer.
- The platform owns task orchestration, agent handoff, context, tools, evals,
  latency measurement, provider fallback, and enterprise policy.
- Implement both a cascaded ASR → LLM → TTS pipeline and one native-audio
  provider behind a shared session contract.
- Learn UDP and QUIC because WebRTC and modern transports depend on their
  properties. Do not build a media stack from scratch.

Official sources:

- [LiveKit voice AI quickstart](https://docs.livekit.io/agents/start/voice-ai/)
- [LiveKit agents and handoffs](https://docs.livekit.io/agents/logic/agents-handoffs/)
- [Gemini Live API](https://ai.google.dev/gemini-api/docs/live-api)

## Observability and security

- Use OpenTelemetry traces, metrics, and logs.
- Adopt current GenAI semantic conventions for provider, model, token, data
  source, and agent metadata.
- Do not capture prompt, tool arguments, or tool output by default; those fields
  can contain secrets and PII.
- Use workload identity, Secret Manager, least privilege, audit logs, and
  explicit end-user delegation.
- Evaluate Google Agent Identity, Agent Gateway, and Model Armor as managed
  production controls; first understand and implement the underlying policy
  boundaries.

Official sources:

- [OpenTelemetry GenAI attributes](https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/)
- [Agent Identity](https://docs.cloud.google.com/iam/docs/agent-identity-overview)
- [Google Cloud multi-agent reference architecture](https://docs.cloud.google.com/architecture/multiagent-ai-system)

## Apple stack

WWDC26 APIs are current but pre-release in July 2026. Required work must be
availability-gated and must not depend on beta behavior remaining unchanged.

### Foundation Models v2 and Apple Intelligence

- Any conforming language-model provider through the `LanguageModel` protocol.
- Multimodal text + image input.
- Dynamic Profiles for context, model, instruction, and tool changes.
- Evaluations framework and Foundation Models Instruments.
- Foundation Models utilities for context management, skills, and sub-agents.
- App Intents schemas, Core Spotlight, view annotations, and
  AppIntentsTesting.
- On-device model availability depends on supported hardware, region, assets,
  and Apple Intelligence settings.

### Core AI, Core ML, and MLX

- Core AI: Apple’s path for bringing modern generative models on-device.
- Core ML: retained for traditional tree, regression, classifier, vision, and
  similar models.
- MLX: research, experimentation, fine-tuning, local serving, and SLM agent
  work on Apple Silicon.
- Core AI ahead-of-time compilation support is hardware-dependent; verify the
  target device family.

### Toolchain

- **Xcode 26.3** (build 17C519) is the current stable active toolchain.
- **Xcode 27 beta 3** is downloaded at `/Applications/Xcode-beta.app` and
  available for OS 27 SDK and Swift 6.4 preview work.
- **Swift 6.2.4** (swiftlang-6.2.4.1.4, clang-1700.6.4.2) is the active
  compiler; target `arm64-apple-macosx26.0`.
- Current SwiftUI toolbar/reorderable-container/Document APIs and the Liquid
  Glass, SF Symbols 8, and Icon Composer 2 design updates are beta-era tools,
  not reasons to delay functional Apple AI work.
- Metal 4 quantized-tensor/neural-accelerator support informs Core AI
  performance analysis; custom kernels remain out of scope.
- Apple Silicon Mac (M4 Pro, 24 GB) is available.
- Physical Apple Intelligence device and paid developer account are a later
  checkpoint, not an immediate prerequisite.

Official sources:

- [WWDC26 Apple Intelligence guide](https://developer.apple.com/wwdc26/guides/apple-intelligence/)
- [WWDC26 Machine Learning guide](https://developer.apple.com/wwdc26/guides/machine-learning/)
- [Core AI](https://developer.apple.com/core-ai/)
- [Foundation Models availability guidance](https://developer.apple.com/documentation/foundationmodels/generating-content-and-performing-tasks-with-foundation-models)

## Phase-boundary refresh checklist

At each consolidation week:

- [ ] Query provider model catalogs and record deprecations.
- [ ] Replace preview dependencies when a stable equivalent exists.
- [ ] Re-run provider contract tests and the golden evaluation set.
- [ ] Check ADK, Agent Runtime, MCP, A2A, LiveKit, and OpenTelemetry release
      notes.
- [ ] Check Xcode/OS SDK release status and Apple API changes.
- [ ] Update this file’s verification date and explain every changed choice.
- [ ] Do not upgrade during a demo/interview week unless a dependency is
      unavailable or insecure.
