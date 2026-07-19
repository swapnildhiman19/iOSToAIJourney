# System-Design Track

System design starts immediately and runs every Friday. The target is 34 unique
cases:

- 18 AI systems;
- 10 iOS systems;
- 6 backend/distributed systems.

Consolidation and final weeks repeat weak cases rather than adding scope.

## The one design method

Use the same sequence for every case.

### 1. Clarify the problem

- Who uses it?
- What are the primary and non-goals?
- What is the critical user journey?
- What quality, privacy, availability, and compliance constraints exist?

### 2. Quantify it

- users, requests/tasks/turns per second;
- payload, corpus, state, and retention size;
- latency budget per critical hop;
- availability and recovery target;
- AI token/audio/GPU and dollar budget.

State assumptions. The numbers do not need to match an interviewer’s hidden
answer; they must be coherent.

### 3. Define contracts

- synchronous APIs;
- streams and events;
- schemas and versioning;
- idempotency and authorization;
- client-visible states and errors.

### 4. Model the data

- source of truth;
- indexes and caches;
- ownership/tenant boundaries;
- lifecycle, freshness, deletion, and audit;
- consistency requirements.

### 5. Draw the high-level flow

Show the smallest design that satisfies the requirements. Then trace one read,
one write/action, and one failure.

### 6. Deep-dive the risky part

Choose one or two:

- context/retrieval quality;
- agent/tool execution;
- real-time latency;
- offline synchronization;
- queue semantics;
- model/runtime routing;
- security boundary;
- scaling bottleneck.

### 7. Operate it

- timeouts, retries, circuit breakers, load shedding;
- telemetry, SLI/SLO, alerts, and runbook;
- deployment, migration, rollback, backup, and recovery;
- abuse, privacy, and incident response.

### 8. Scale and compare

- identify the first bottleneck;
- scale 10x and 100x;
- estimate cost;
- compare at least one credible alternative;
- state what evidence would change the decision.

### 9. Close

Summarize the design and its three most important trade-offs in 90 seconds.

## AI design checklist

In addition to the common method:

- Is an LLM necessary?
- Which steps are deterministic?
- What is the model/capability routing policy?
- What enters context, under which trust and authorization boundary?
- Is retrieval required? What is the quality baseline?
- What state and memory persist, and how are they corrected/deleted?
- Why is an agent or multi-agent topology justified?
- How are tools authorized and side effects made safe?
- What is the evaluation dataset and release threshold?
- What are the latency, token, and cost budgets?
- How does the system degrade when a model/provider fails?
- How are prompt injection, PII, audit, and tenant isolation handled?

## iOS design checklist

- UIKit, SwiftUI, or mixed surface and why.
- State ownership and data flow.
- Concurrency domains, cancellation, actor isolation, and main-thread policy.
- API/stream contract and network failure behavior.
- Memory/disk cache, offline behavior, sync, and conflict resolution.
- Feature modules and dependency boundaries.
- Background execution, push, and lifecycle.
- Model availability, on-device/cloud routing, thermal/energy, and privacy.
- Accessibility, adaptive layout, localization, and testability.
- Metrics, Instruments, MetricKit, rollout, and fallback.

## Backend design checklist

- consistency and transaction boundary;
- partitioning/index strategy;
- cache correctness and invalidation;
- queue delivery semantics and idempotency;
- backpressure and overload behavior;
- rate limits, tenancy, and authorization;
- observability, SLO, disaster recovery, and cost.

## Scoring rubric

Score each dimension from 0 to 3.

1. Requirements and scope.
2. Estimates and budgets.
3. Contracts and data model.
4. Coherent architecture and critical flows.
5. Domain depth: AI, iOS, or backend.
6. Failure handling and operations.
7. Security, privacy, and cost.
8. Communication and trade-offs.

Interpretation:

- **0:** missing or materially unsafe.
- **1:** recognized only after prompting.
- **2:** independently correct with reasonable trade-offs.
- **3:** precise, quantified, and adapts under challenge.

Phase expectations:

- End Phase 1: at least 12/24, with no zero in requirements or critical flow.
- End Phase 2: at least 15/24, with no zero in failure or security.
- End Phase 3: at least 18/24 and a numbered latency/cost budget.
- Phase 4 pass: at least 20/24 twice consecutively in 45-minute mocks.

The score is diagnostic. Never inflate it to preserve a streak.

## Scheduled case order

### Orientation

**Diagnostic, not counted:** design a basic AI assistant with a mobile client.
This exposes assumptions before the method is taught.

### Sprint 1

#### B1 — Reliable webhook ingestion

Receive bursty signed events, acknowledge quickly, deduplicate retries, process
asynchronously, expose status, and replay dead letters.

#### I1 — Offline-first adaptive feed

Design pagination, image loading, memory/disk cache, offline reads, refresh,
state ownership, cancellation, and modular boundaries.

### Sprint 2

#### A1 — Provider-neutral model gateway

Route requests by capability/quality/latency/cost, normalize streaming/tools/
errors/usage, handle rate limits, and migrate models safely.

#### A2 — Streaming multimodal conversation service

Support text, image, audio/file attachments, cancellation, partial output,
session state, abuse controls, telemetry, and provider failure.

### Sprint 3

#### A3 — Context assembly and long-context service

Budget and order policy, conversation, evidence, memory, and tool output while
handling compaction, trust, provenance, caching, and context overflow.

#### A4 — Permission-aware enterprise knowledge system

Ingest changing documents, apply ACLs, combine exact/sparse/dense search,
rerank, cite, evaluate, delete, and prevent stale or unauthorized retrieval.

### Sprint 4

#### A5 — Privacy-aware AI memory service

Separate session state from long-term memory; design write/retrieval policy,
correction, contradiction, TTL, deletion, tenant boundaries, and memory evals.

#### I2 — On-device/PCC/cloud model-routing app

Route Apple AI tasks based on capability, availability, privacy, latency,
energy, cost, and connectivity while keeping a coherent user experience.

### Consolidation 1

#### B2 — Durable background-job system

Design enqueue, scheduling, leases, retries, heartbeat, cancellation,
idempotency, progress, dead letters, and worker autoscaling.

### Sprint 5

#### A6 — Evaluation platform

Version datasets/prompts/models, run deterministic and model graders, calibrate
judges, slice results, gate releases, and connect offline evals to online
outcomes.

#### A7 — Reliable single-agent runtime

Design the model/tool loop, typed events, budgets, checkpoints, approvals,
resume, termination, sandboxing, telemetry, and trajectory evaluation.

### Sprint 6

#### A8 — Human-approved action agent

An agent reads enterprise systems and proposes high-impact changes; design
delegated authorization, preview, approval, idempotency, compensation, audit,
and denial behavior.

#### A9 — Multi-agent research and verification workflow

Justify coordinator/specialist boundaries, context isolation, parallelism,
evidence contracts, disagreement, timeout, aggregation, and quality evaluation.

### Sprint 7

#### A10 — MCP/A2A interoperability platform

Connect agents to tools through MCP and independent agents through A2A; design
discovery, auth, delegated authority, streaming, async tasks, versioning,
failure, and untrusted results.

#### I3 — Resilient real-time voice iOS client

Design WebRTC session lifecycle, audio interruptions, route changes,
background/system integration, reconnect, transcript state, accessibility,
privacy, and degraded modes.

### Sprint 8

#### A11 — Low-latency production voice agent

Compare cascaded and native audio, allocate latency per stage, design VAD,
endpointing, barge-in, tools, fallback, resumption, recording policy, and voice
evaluation.

#### A12 — Multi-voice-agent handoff platform

Route a live conversation among specialists while preserving explicit shared
state, authority, transcript consistency, interruption behavior, and graceful
failure.

### Sprint 9

#### A13 — AI observability and cost-control platform

Trace context, retrieval, models, tools, agents, queues, and voice; design
redaction, GenAI telemetry, SLOs, budgets, anomaly alerts, and quality-adjusted
cost.

#### I4 — Siri, App Intents, and Core Spotlight system

Model entities/actions, semantic indexing, on-screen awareness, parameter
resolution, confirmation, privacy, testing, freshness, and unavailable
capabilities.

### Sprint 10

#### B3 — Event-driven document-processing pipeline

Process uploads through parse, scan, classify, enrich, index, and delete stages
with versioning, replay, poison events, observability, and tenant ACLs.

#### A14 — Secure multi-tenant AI platform

Design identity, tenant isolation, end-user delegation, agent identity, PII,
audit, prompt/tool security, quotas, retention, and incident response.

### Sprint 11

#### A15 — Cloud Run and Agent Runtime architecture

Place API, events, long-running agents, voice workers, state, and tools across
Cloud Run services/functions and Agent Runtime; defend lifecycle, identity,
scale, and lock-in.

#### B4 — Rate-limited multi-tenant API and cache

Design per-user/tenant quotas, distributed limiting, cache keys/invalidation,
hot keys, abuse, consistency, fairness, and observability.

### Sprint 12

#### I5 — Local generative-AI application

Package and run a local model with Core AI/MLX, budget memory/energy/startup,
manage model assets, route tasks, handle unsupported devices, and evaluate
quality.

#### A16 — Scale the AI Solutions Platform 100x

Start from measured traffic and scale models, retrieval, queues, workers,
voice rooms, storage, telemetry, and cost while preserving SLO and tenant
fairness.

### Consolidation 3

#### I6 — End-to-end Apple AI application

Combine Foundation Models, Dynamic Profiles, Evaluations, App Intents, Core
Spotlight, Core AI/Core ML availability, and safe fallback in a modular design.

### Sprint 13

#### A17 — Fine-tuning and data-flywheel platform

Collect permissioned feedback, curate/version data, prevent leakage, train
LoRA/SFT, evaluate, approve, deploy, monitor, roll back, and decide when not to
fine-tune.

#### B5 — Reusable enterprise integration platform

Connect REST/OpenAPI, databases, webhooks, GitHub, and chat systems with
credential brokering, schemas, retries, change detection, policy, and audit.

### Sprint 14

#### I7 — Modular iOS application at scale

Design feature packages, dependency direction, navigation, design system,
state, networking, storage, testing, CI, ownership, and incremental migration
from UIKit.

#### A18 — Regulated-customer AI pilot

Design a time-boxed pilot under PII, residency, audit, private access,
human-approval, and change-control constraints. Tie architecture to success and
kill metrics.

### Sprint 15

#### I8 — Offline sync and conflict resolution

Design local source of truth, operation log, sync protocol, conflict policy,
background work, retries, schema migration, observability, and user-visible
resolution.

#### B6 — Reliable notification and webhook delivery

Deliver email/push/webhooks with preferences, templates, fan-out, retries,
ordering, deduplication, provider failover, status, and abuse control.

### Sprint 16

#### I9 — Performance- and energy-aware iOS AI runtime

Design model loading, memory pressure, thermal/energy budgets, inference
queues, cancellation, background behavior, caching, telemetry, and fallback
across device classes.

#### I10 — Full iOS AI capstone

A 45-minute unseen design combining adaptive UI, concurrency, offline state,
real-time networking, Apple AI, local/cloud routing, security, testing,
performance, and rollout.

## Consolidation practice

Consolidation 2 repeats the weakest Phase 2 AI case under a 45-minute limit.
Consolidation 4 repeats the two lowest-scoring cases from the entire ledger.
Repeated attempts retain the original score and add a new score; never overwrite
history.

## Evidence template for every case

Create one note with:

- prompt and date;
- clarified requirements/non-goals;
- assumptions and calculations;
- API/events and data model;
- diagram;
- critical read/write/action flow;
- failure, security, privacy, observability, and cost;
- 10x/100x changes;
- alternatives and rejected choices;
- score by rubric;
- interviewer/self feedback;
- next repetition date.

## Resource strategy

Use resources to answer a design gap, not to postpone practice:

- Google Cloud Architecture Center for current AI/GCP references.
- Apple WWDC sessions and platform documentation for iOS/Apple AI.
- *Designing Data-Intensive Applications* for data/distributed fundamentals.
- Chip Huyen’s *AI Engineering* for AI application trade-offs.
- Production incident reports and engineering blogs for failure evidence.

One design attempt followed by targeted reading is worth more than a week of
passive system-design videos.
