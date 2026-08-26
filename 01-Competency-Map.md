# Competency Map

This document defines the target skill set. It prevents two common roadmap
failures:

1. collecting tools without understanding the system underneath; and
2. trying to become an AI researcher, platform engineer, backend specialist,
   mobile specialist, and networking specialist simultaneously.

## Depth labels

- **Deep** — build it without a tutorial, debug it, measure it, and defend its
  trade-offs in an interview.
- **Working** — implement a realistic version with documentation and explain
  operational consequences.
- **Literacy** — explain when it applies, read an existing implementation, and
  avoid obvious design mistakes.
- **Deferred** — valuable, but outside the May 2027 target.

## 1. AI software engineering

### Plain meaning

An AI system is still software. If the API, database, background job, or test
suite is unreliable, a better model will not rescue it.

### Deep

- Python data structures, functions, classes, protocols, dataclasses, typing,
  exceptions, iterators, generators, context managers, and packaging with
  `uv`.
- `asyncio`, cancellation, timeouts, task groups, bounded concurrency,
  backpressure, connection pooling, and avoiding blocking work in the event
  loop.
- FastAPI request/response models, dependency injection, middleware,
  lifespan management, streaming responses, OpenAPI, authentication, and
  error contracts.
- Pydantic validation and provider-neutral domain models.
- Unit, integration, contract, property-based, and asynchronous tests.
- SQL, transactions, indexes, query plans, migrations, Postgres, and data
  modeling.
- Clean module boundaries: domain logic must not depend directly on a model
  provider SDK.

### Working

- Redis for cache, rate limits, ephemeral state, locks, and streams.
- Object storage, webhooks, background jobs, CloudEvents, Pub/Sub, and Cloud
  Tasks.
- A thin Flutter client in Dart for text and voice demonstration.
- Enough TypeScript to read SDK examples and integration code.

### Literacy

- Go service structure and goroutines. No Go project is required; Python is
  sufficient for the target role.

## 2. Minimum ML and inference foundations

### Plain meaning

You do not need to train a frontier model. You do need to know why a model has
limits, why inference becomes slow or expensive, and when an embedding,
fine-tune, quantized local model, or larger model is appropriate.

### Deep

- Tokens, tokenization, embeddings, attention, transformer blocks, positional
  information, context windows, and next-token prediction.
- Training versus inference; pretraining, supervised fine-tuning, preference
  optimization, distillation, and retrieval as different interventions.
- Sampling controls, deterministic constraints, calibration, hallucination,
  and model uncertainty.
- Prefill versus decode, time to first token, tokens per second, KV cache,
  batching, quantization, and model routing.
- Evaluation basics: train/validation/test separation, precision/recall,
  ranking metrics, confidence intervals, and data leakage.

### Working

- One small SFT/LoRA experiment with a baseline, held-out evaluation, artifact
  version, and written decision on whether the fine-tune was justified.
- Embedding dimensionality, similarity measures, approximate nearest-neighbor
  indexes, and rerankers.

### Deferred

- Training a base model, deep optimizer mathematics, distributed GPU training,
  CUDA kernel development, and research-level post-training.

The IIT KGP program owns broader ML theory. This roadmap supplies only the
foundations needed to build and defend LLM systems.

## 3. Model API and provider engineering

### Plain meaning

The model is a dependency, not the architecture. The platform must be able to
change model, provider, and capability without rewriting business logic.

### Deep

- Provider adapters with a small internal contract for messages, structured
  output, tools, streaming events, usage, errors, and trace metadata.
- Gemini through the Google Gen AI SDK as the main implementation.
- One non-Google provider as a real fallback/comparator.
- System, developer, user, tool, and model message semantics.
- Native structured output and schema validation.
- Function/tool calling: selection, forced calls, parallel calls, result
  validation, retries, and side-effect safety.
- Streaming over SSE/WebSocket, cancellation, reconnect behavior, and partial
  result handling.
- Multimodal text, image, audio, video, PDF, files, and URL inputs where the
  selected model supports them.
- Rate-limit handling, exponential backoff with jitter, idempotency, quotas,
  token accounting, cost attribution, and model fallbacks.
- Stable versus preview model policy and capability-based routing.

### Working

- Prompt caching, semantic caching, batch inference, long-context requests,
  search grounding, code execution, and provider-native file search.
- Model routing using quality, latency, cost, context, modality, and data
  policy—not brand preference.

### Exit evidence

- The same evaluated task runs through at least two providers.
- A provider outage or rate limit causes a controlled fallback.
- Unsupported capabilities fail before an external API call.
- Every call emits normalized usage, latency, model, and finish-reason data.

## 4. Prompt and context engineering

### Plain meaning

Prompt engineering writes instructions. Context engineering decides everything
the model sees, in what order, for how long, and under which trust boundary.

### Deep

- Clear task contracts, examples, delimiters, output schemas, refusal behavior,
  and prompt versioning.
- Context budgets and priority: policy, user intent, current state, retrieved
  evidence, memory, tool output, and conversation history.
- Context compaction, summarization, sliding windows, selective replay, and
  lost-in-the-middle mitigation.
- Trusted versus untrusted context and provenance labels.
- Token and cache economics.
- Regression testing prompt changes rather than choosing prompts by intuition.

### Working

- Dynamic context assembly based on task and model capability.
- Prompt registry with version, owner, evaluation result, and rollback.

## 5. Knowledge systems: beyond “build a RAG app”

### Plain meaning

RAG remains relevant, but it is one way to supply knowledge. The correct design
may instead use a SQL query, exact search, a model-native file tool, cached long
context, or no retrieval at all.

### Decision order

1. Use normal code or SQL for deterministic structured facts.
2. Use exact/filter search for identifiers, names, versions, and ACLs.
3. Use model-native file search or long context for a small, stable corpus.
4. Use retrieval for large, changing, permissioned, or cost-sensitive corpora.
5. Add graph retrieval only for measured multi-hop relationship failures.
6. Add agentic retrieval only when the query genuinely needs iterative search
   and planning.

### Deep

- Ingestion, parsing, normalization, deduplication, versioning, deletion, and
  freshness.
- Structural and semantic chunking; code-aware splitting where relevant.
- Dense and sparse retrieval, hybrid fusion, metadata and ACL filters,
  reranking, query rewriting, and context assembly.
- Citation provenance and source-level authorization.
- Retrieval evaluation: recall@k, MRR/nDCG where appropriate, context precision,
  citation correctness, answer faithfulness, latency, and cost.
- Long-context versus retrieval experiments on the same dataset.

### Working

- Postgres/pgvector plus lexical search.
- A managed retrieval option on GCP.
- Graph/relationship retrieval as a measured experiment, not a required
  flagship.

### Deferred

- Comparing five vector databases and building a large Neo4j platform without a
  validated relationship-heavy use case.

## 6. State and memory

### Plain meaning

Context is what the model sees now. State is what the workflow needs to resume.
Memory is selected information retained for later. Treating all three as chat
history creates expensive and unsafe systems.

### Deep

- Request state, session state, workflow checkpoints, and long-term memory as
  separate stores.
- Working, episodic, semantic, and procedural memory.
- Memory write policy, retrieval policy, confidence, provenance, TTL,
  deletion, and user controls.
- Conversation compaction and summary invalidation.
- Tenant and user boundaries.
- Memory evaluation: useful recall, irrelevant recall, contradiction,
  staleness, privacy, latency, and cost.

### Working

- Postgres as durable source of truth, Redis for ephemeral state, and vector
  retrieval only where semantic recall is justified.

## 7. AI harness and runtime engineering

### Plain meaning

The harness is the reliable software around the model: it chooses context,
calls tools, persists state, enforces budgets, recovers from failure, and
records what happened.

### Deep

- Explicit event model for model requests, tool requests, tool results,
  approvals, errors, cancellations, and final results.
- Deterministic state machines for predictable work.
- Agent loop termination, step/time/token/cost budgets, and recursion guards.
- Tool registry, typed arguments/results, authorization, timeouts, retries,
  idempotency, and compensation for side effects.
- Durable checkpoints, resume, replay, cancellation, and human-in-the-loop
  approval.
- Parallel fan-out with bounded concurrency and deterministic aggregation.
- Failure classification: transient, permanent, policy, invalid model output,
  unavailable dependency, and user cancellation.

### Working

- Background execution using queues/events.
- Sandboxed code execution with explicit resource and network policy.
- Provider and framework adapters around stable internal domain events.

## 8. Agents and ADK 2.0

### Plain meaning

An agent is useful when the model must make decisions under ambiguity. A
workflow is better when the route is known. ADK 2.0 allows both in one graph.

### Deep

- Agent versus workflow decision criteria.
- ADK 2.0 Workflow Runtime: agents, tools, functions, and control logic as graph
  nodes.
- Static and dynamic workflows; native Python control flow where appropriate.
- Collaborative agents, delegation, task boundaries, shared versus isolated
  state, and result contracts.
- Human approval nodes and policy gates.
- Session, artifact, context, memory, callback, and evaluation surfaces.
- Trajectory evaluation as well as final-answer evaluation.
- Local execution, Cloud Run deployment, and managed Agent Runtime deployment.

### Working

- MCP tools consumed by an ADK agent.
- An ADK agent exposed for remote collaboration through A2A.
- Comparison with LangGraph concepts sufficient for an interview.

### Required restraint

A design with multiple agents must demonstrate at least one benefit that a
single agent with tools cannot provide: isolation, ownership, parallelism,
different policies/models, independent deployment, or external
interoperability.

## 9. Agent and tool protocols

### Deep

- MCP mental model: host, client, server, tools, resources, prompts,
  capabilities, and trust boundaries.
- Streamable HTTP transport, process-local stdio, OAuth/OIDC authorization,
  user delegation, timeouts, schema evolution, and tool-result validation.
- Current production spec plus a dated migration check for newer MCP releases.
- OpenAPI and webhooks for ordinary service integrations.
- A2A mental model: agent discovery, capabilities, task delegation, streaming,
  asynchronous updates, artifacts, and agent-to-agent trust.
- Difference: MCP equips an agent with tools; A2A lets independent agents
  collaborate.

### Working

- One production-shaped MCP server and client.
- One small A2A collaboration between independently runnable agents.

### Literacy

- ACP and IDE agent plug-ins as developer-tooling concepts.

## 10. Real-time text and voice AI

### Plain meaning

A voice agent is a latency-sensitive distributed system. Natural speech
requires more than adding speech-to-text and text-to-speech around a chatbot.

### Deep

- Text streaming lifecycle, partial output, cancellation, reconnect, and
  backpressure.
- Audio sampling rate, PCM, channels, frames, jitter, buffering, codecs, VAD,
  endpointing, echo cancellation, and noise handling.
- Cascaded ASR → LLM → TTS versus native speech-to-speech.
- WebRTC signaling, ICE, STUN, TURN, tracks, rooms, and SFU at architectural
  depth.
- LiveKit room and worker lifecycle, dispatch, agent handoff, shared state, and
  graceful worker draining.
- Turn detection, backchannels, interruption/barge-in, preemptive generation,
  transcript reconciliation, and tool calls during a live turn.
- Stage latency budget: capture, network, VAD/ASR, model first token, TTS first
  audio, and playback.
- Provider fallbacks, session resumption, degraded modes, consent, recording
  policy, and transcript privacy.
- Voice evaluation: task success, word error rate where relevant, interruption
  accuracy, false interruption, time to first audio, end-to-end latency, and
  subjective conversation quality.

### Working

- One production-grade multi-voice-agent system using LiveKit/WebRTC.
- One native-audio provider and one cascaded pipeline behind a common session
  contract.

### Literacy

- UDP, QUIC, HTTP/3, and WebTransport semantics and trade-offs.
- A short protocol lab may inspect packet/latency behavior, but implementing a
  media transport from scratch is deferred.

## 11. Evaluation engineering

### Plain meaning

An AI feature is not “working” because five demos looked good. Evals turn
quality into a repeatable engineering signal.

### Deep

- Define the task, failure taxonomy, risk level, and acceptance threshold before
  optimizing.
- Curate representative datasets with provenance, versions, hard cases, and
  slices.
- Deterministic graders, model graders, pairwise comparison, rubric graders,
  human review, and judge calibration.
- Retrieval, generation, tool-use, trajectory, memory, safety, and voice
  evaluation.
- Offline regression gates and online outcome/feedback metrics.
- Statistical uncertainty, repeated runs for nondeterminism, and avoiding test
  leakage.
- Cost and latency included in the scorecard.

### Working

- Evaluation service or package shared by all AI platform modules.
- CI blocks a release when a defined quality, safety, latency, or cost budget
  regresses beyond tolerance.

Ragas may be used for selected retrieval metrics, but it is not the evaluation
architecture.

## 12. Observability, reliability, latency, and cost

### Deep

- OpenTelemetry traces, metrics, and logs with current GenAI semantic
  conventions.
- Trace model calls, context assembly, retrieval, tool calls, agent nodes,
  queues, voice stages, and user-visible outcome.
- Sensitive prompt/tool content is opt-in and redacted; metadata is the
  default.
- SLIs, SLOs, error budgets, burn-rate alerts, and runbooks.
- Timeouts, retries, circuit breakers, bulkheads, rate limits, load shedding,
  and graceful degradation.
- Cache hierarchy, prompt caching, semantic caching, batching, connection
  pooling, asynchronous work, and model tiering.
- p50/p95/p99, throughput, queue age, token usage, cache hit rate, cost per
  successful task, and quality-adjusted cost.
- Load, spike, soak, and fault-injection tests.

### Working

- Cloud Monitoring dashboards fed by OpenTelemetry.
- k6 or an equivalent load harness checked into the platform repository.
- A written latency budget and two measured optimization iterations.

## 13. Security and enterprise controls

### Plain meaning

The model is exposed to untrusted text and can call powerful tools. Normal
application security still applies, plus new risks such as prompt injection and
tool poisoning.

### Deep

- Authentication with OIDC, authorization with roles/policies, tenant-scoped
  data, and least privilege.
- Service identity versus end-user delegated authority.
- Secret Manager, workload identity, token rotation, and no long-lived cloud
  keys.
- Direct and indirect prompt injection, instruction/data separation, tool
  poisoning, confused deputy, data exfiltration, and excessive agency.
- Tool allowlists, argument validation, output validation, approval for
  high-impact actions, and sandboxing.
- PII detection/redaction, retention/deletion, audit events, encryption, and
  logging policy.
- Per-tenant quotas, cost budgets, rate limits, and abuse controls.
- Dependency, container, and CI supply-chain hygiene.

### Working

- Basic multi-tenant implementation: organization/user identity,
  tenant-scoped rows and indexes, roles, audit trail, usage limits, and PII
  redaction.
- Google Agent Identity, Agent Gateway, Model Armor, and VPC Service Controls as
  production options with a clear build-versus-managed analysis.

### Literacy

- SSO/SCIM, data residency, CMEK, private connectivity, SOC 2/HIPAA/FedRAMP
  conversations, and threat modeling with STRIDE.

## 14. GCP production engineering

### Deep

- Containers, reproducible builds, non-root runtime, health/readiness, image
  scanning, and local compose-based dependencies.
- GitHub Actions for lint, type check, test, evaluation, image build, deploy,
  smoke test, and rollback.
- Cloud Run services for FastAPI and stateful-over-request agent APIs.
- Cloud Run functions with Eventarc for focused event handlers.
- Pub/Sub and Cloud Tasks for asynchronous or scheduled work.
- Postgres, Redis, object storage, Secret Manager, Artifact Registry, IAM,
  workload identity, and budgets.
- Traffic splitting, concurrency, min/max instances, cold starts, graceful
  shutdown, and streaming behavior.
- Agent Runtime for managed long-running agents, memory, identity, and
  governance when those features justify it.

### Working

- Terraform fundamentals, remote state concepts, plan review, and reading or
  modifying a small module.
- Kubernetes/GKE concepts, deployments, services, probes, resources,
  autoscaling, and logs.
- VPC ingress/egress, private service access/Private Service Connect, Private
  Google Access, and VPC Service Controls at architecture and configuration
  literacy depth.
- AWS Bedrock model invocation, model/region availability, IAM, guardrails,
  knowledge/agent surfaces, and the architectural comparison with Gemini on
  Google Cloud. This is literacy through one small API exercise, not a second
  production deployment.

### Deferred

- Operating a private GKE platform, writing a large Terraform monorepo, and
  deep multi-cloud deployment. They are not required to prove production AI
  engineering by March.

## 15. FDE delivery

### Plain meaning

The AI FDE owns the journey from a vague business problem to a measurable
production deployment, not only the model code.

### Deep

- Discovery interviews and current-workflow mapping.
- Value, feasibility, data, integration, risk, and adoption assessment.
- Pilot scope with users, baseline, success metric, guardrails, kill criteria,
  and time box.
- Architecture and build decisions tied to customer constraints.
- Integration through generic REST/OpenAPI, Postgres, webhooks, and small
  GitHub/Slack-or-Teams examples.
- Eval-driven iteration with domain experts.
- Rollout, operational ownership, runbook, training, handoff, and expansion.
- Communicating trade-offs to both engineers and non-technical stakeholders.
- Turning field work into a reusable adapter, template, or playbook.

### Evidence

- Two written discovery simulations.
- One complete pilot simulation using the AI Solutions Platform.
- One go/no-go decision that recommends not building or stopping a pilot.
- One architecture review and one handoff/runbook presentation.

## 16. iOS and Apple AI

### Plain meaning

This track demonstrates that you can apply AI principles on Apple platforms
without making the main AI platform an iOS product.

### Deep

- Modern Swift Concurrency: structured tasks, actors, isolation, cancellation,
  `Sendable`, `AsyncSequence`, testing, and Instruments.
- SwiftUI state, navigation, data flow, adaptive layout, UIKit interop,
  accessibility, and performance.
- Modular architecture, dependency boundaries, offline behavior, networking,
  caching, observability, and testability.
- Foundation Models v2: model availability, multimodal prompts, structured
  generation, tools, streaming, context limits, prewarming, and fallbacks.
- Dynamic Profiles for changing model/tools/instructions while preserving an
  intentional context boundary.
- Evaluations framework and Foundation Models Instruments.
- Foundation Models v2 context utilities, reusable skills, and sub-agent
  composition, with the same “justify every agent boundary” rule as the backend
  track.
- App Intents, schemas, Core Spotlight retrieval, view annotations,
  AppIntentsTesting, and safe action confirmation.
- Core AI model lifecycle: convert, optimize, package, specialize, load, run,
  profile, manage state/memory, and select compute.
- Core ML for traditional classifiers/regressors and Vision/NaturalLanguage
  integrations.
- MLX and SLM workflows on Apple Silicon: local server, quantization, memory,
  tokens per second, tool use, and benchmark design.

### Working

- Xcode 27 agent workflow, Swift 6.4 changes, Swift Testing migration, Device
  Hub, MetricKit, and Xcode Cloud.
- Current SwiftUI additions where they improve the lab: updated toolbar APIs,
  reorderable containers, and the Document API.
- Liquid Glass refinements, Icon Composer 2, and SF Symbols 8 at practical
  design-system/accessibility depth; they are polish after behavior and tests.
- Metal 4 quantized-tensor and neural-accelerator concepts needed to explain
  Core AI performance. Profiling is required; custom Metal implementation is
  not.
- LiveCommunicationKit and gRPC Swift concepts for real-time Apple clients.
- Language-model provider adapters through the Foundation Models protocol.
- MLX multi-Mac RDMA/distributed-training architecture literacy only.

### Device gate

Mac-compatible work begins immediately. On-device Apple Intelligence features
must check `SystemLanguageModel` availability and provide a fallback. A later
checkpoint determines access to a supported physical iPhone/iPad and paid
developer account; unavailable hardware cannot silently block the whole track.

### Deferred

- Custom Metal kernels, multi-Mac RDMA training, visionOS, game technology, and
  broad WWDC session completion.

## 17. System design and DSA

### System design — deep

- Requirements and scope.
- Capacity estimates and latency budgets.
- API/events and data model.
- Component and data-flow design.
- Failure modes, consistency, retries, and recovery.
- Security, privacy, multi-tenancy, and observability.
- Cost, scaling, alternatives, and explicit trade-offs.
- Clear 45-minute communication.

The required case mix is 18 AI, 10 iOS, and 6 backend/distributed systems.

### DSA — working interview depth

- Arrays/hash maps, two pointers, sliding window, stack/queue, binary search,
  linked lists, trees, tries, heaps, graphs, backtracking, intervals, greedy,
  one- and two-dimensional dynamic programming, and bit operations.
- Pattern recognition, complexity analysis, clean Swift or Python
  implementation, test cases, and verbal communication.
- Four hours per week with spaced repetition and timed unseen problems.

## Explicitly excluded from the core roadmap

- Deep Go.
- Deep Kubernetes/platform engineering.
- A full AWS/Bedrock deployment.
- Building a custom UDP/QUIC/WebRTC stack.
- Training a foundation model.
- Making GraphRAG a flagship without evidence.
- Learning several agent frameworks in parallel.
- Comparing many vector databases.
- Publishing eight shallow posts.
- Building three unrelated backend applications.

These exclusions protect the actual target: a production AI engineer and AI FDE
who has a current, credible Apple AI differentiator.
