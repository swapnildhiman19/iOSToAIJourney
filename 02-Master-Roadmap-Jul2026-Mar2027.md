# Master Roadmap — July 2026 to March 2027

## Outcome and pacing

- Start: Thursday, July 16, 2026.
- Interview-ready target: Wednesday, March 31, 2027.
- Required roadmap budget: 20–25 hours per week.
- IIT KGP ML sessions: four additional hours per week, outside this budget.
- Structure: orientation, sixteen two-week sprints, four consolidation weeks,
  and a final three-day readiness check.

This calendar is competency-gated. Dates determine when to attempt a skill; an
exit gate determines whether it is complete.

## Calendar

| Block | Dates | Primary outcome |
|---|---|---|
| Orientation | Jul 16–19 | Baseline diagnostics, environment, evidence ledger |
| Sprint 1 | Jul 20–Aug 2 | Python/FastAPI/backend foundation |
| Sprint 2 | Aug 3–16 | Provider-neutral model API and context foundation |
| Sprint 3 | Aug 17–30 | Knowledge and retrieval decision system |
| Sprint 4 | Aug 31–Sep 13 | State, memory, harness, and eval foundation |
| Consolidation 1 | Sep 14–20 | Repair Phase 1 gaps |
| Sprint 5 | Sep 21–Oct 4 | ADK 2.0 graph workflows |
| Sprint 6 | Oct 5–18 | Multi-agent, MCP/A2A, and durable work |
| Sprint 7 | Oct 19–Nov 1 | Real-time voice foundations |
| Sprint 8 | Nov 2–15 | Production multi-text and multi-voice agents |
| Consolidation 2 | Nov 16–22 | Repair Phase 2 gaps |
| Sprint 9 | Nov 23–Dec 6 | Enterprise security and tenant controls |
| Sprint 10 | Dec 7–20 | GCP deployment and event-driven execution |
| Sprint 11 | Dec 21–Jan 3 | Reliability, observability, scale, latency, cost |
| Sprint 12 | Jan 4–17 | LoRA experiment and production beta |
| Consolidation 3 | Jan 18–24 | Repair Phase 3 gaps and device checkpoint |
| Sprint 13 | Jan 25–Feb 7 | FDE discovery, pilot, and integration |
| Sprint 14 | Feb 8–21 | Public platform release and portfolio evidence |
| Sprint 15 | Feb 22–Mar 7 | Interview loops and architecture defense |
| Sprint 16 | Mar 8–21 | Final FDE simulation and market readiness |
| Consolidation 4 | Mar 22–28 | Last gap repair; no new scope |
| Final verification | Mar 29–31 | Readiness decision and next actions |

## Prerequisite chain

The immediate predecessor’s gate must be passed, or partial with no missing
prerequisite for the next sprint.

- Sprint 1: Orientation diagnostics and required local tools.
- Sprint 2: typed/tested FastAPI, async, database, and error boundaries.
- Sprint 3: provider contract, structured output, tools, streaming, and usage.
- Sprint 4: measured context strategies and authorized source lifecycle.
- Sprint 5: Phase 1 harness/eval/state foundation and Consolidation 1 repairs.
- Sprint 6: one reliable ADK graph with checkpoint and trajectory evaluation.
- Sprint 7: durable multi-agent/tool boundaries and failure behavior.
- Sprint 8: working cascaded voice flow with stage latency traces.
- Sprint 9: Phase 2 text/voice alpha and Consolidation 2 threat model.
- Sprint 10: tenant/identity/policy controls and security tests.
- Sprint 11: reproducible staging deployment and rollback.
- Sprint 12: telemetry, SLO, load/fault, latency, and cost baselines.
- Sprint 13: Phase 3 production beta and Consolidation 3 repairs.
- Sprint 14: discovery evidence, scoped pilot, and reusable integrations.
- Sprint 15: reproducible public platform and Apple evidence.
- Sprint 16: completed portfolio surfaces plus recorded mock weaknesses.

## Phase 1 — AI software and context systems

### Orientation — July 16–19

**Purpose:** establish the real baseline before assigning difficulty.

**AI/backend**

- Run the Python, async, FastAPI, SQL, HTTP, model API, and cloud diagnostics
  defined in Sprint 00.
- Verify only tools required for Sprint 1; do not provision the entire future
  stack.
- Create the AI Solutions Platform repository and evidence conventions.

**Apple**

- Record Mac model, memory, OS, Xcode version, simulator availability, and
  Apple Intelligence availability.
- Run Swift, Swift Testing, SwiftUI, and concurrency diagnostics.

**Interviews**

- Complete the DSA and system-design baselines without preparation.
- Record weaknesses rather than changing the roadmap from one poor result.

**Exit gate**

- Every diagnostic has a score and evidence link in `PROGRESS.md`.
- Sprint 1 scope is adjusted only where the evidence shows a prerequisite gap.

**Cut first:** account creation and optional cloud provisioning.

### Sprint 1 — July 20–August 2

**Theme:** AI software and backend foundations.

**AI/backend**

- Python typing, dataclasses/protocols, exceptions, generators, context
  managers, packaging, linting, type checking, and pytest.
- `asyncio`: task groups, timeouts, cancellation, bounded concurrency, and
  avoiding blocking calls.
- FastAPI: domain/request separation, dependencies, middleware, error
  contracts, lifecycle, OpenAPI, and streaming basics.
- Postgres schema, migrations, transactions, and integration tests.
- HMAC-verified webhook with idempotency and fast acknowledgement.

**Platform milestone**

- Repository skeleton with `domain`, `providers`, `api`, `persistence`,
  `telemetry`, `tests`, and `docs`.
- Health/readiness endpoints, one persisted resource, and one background task.
- CI runs formatting, lint, type checking, unit tests, and integration tests.

**Apple parallel lane**

- Swift structured concurrency, actor isolation, cancellation, `Sendable`,
  `AsyncSequence`, and Swift Testing.
- SwiftUI observation/state and a small adaptive screen backed by an actor.

**DSA**

- Arrays/hash maps and two pointers.
- Four hours each week: learn/revise, solve, and repeat from memory.

**System design**

- B1: reliable webhook ingestion platform.
- I1: offline-first adaptive iOS feed.

**Exit gate**

- Explain event-loop blocking and demonstrate a test that catches it.
- API tests cover validation, error mapping, cancellation, database rollback,
  duplicate webhook delivery, and one concurrency boundary.
- A fresh checkout starts through documented commands and CI is green.
- The Swift sample passes a concurrency test and handles task cancellation.

**Evidence**

- Architecture decision record: why domain code does not import provider SDKs.
- Recorded five-minute walkthrough of the API flow.

**Cut first:** Flutter and cloud deployment. They are not Sprint 1
prerequisites.

### Sprint 2 — August 3–16

**Theme:** model API engineering and intentional context.

**AI/backend**

- Minimum transformer/inference mental model: tokens, attention, context,
  prefill/decode, KV cache, sampling, and inference latency.
- Google Gen AI SDK as primary; current Anthropic SDK as comparator.
- Internal provider contract for messages, capabilities, structured output,
  tools, streams, usage, and normalized errors.
- Pydantic structured output, tool argument/result validation, manual tool
  loop, retries, idempotency, and side-effect policy.
- SSE streaming, cancellation, partial output, timeout, and provider fallback.
- Prompt versioning, context layers, trust labels, and token budgets.

**Platform milestone**

- Provider gateway with Gemini and one Claude implementation.
- `/responses` non-streaming and streaming APIs.
- One read-only tool and one side-effecting tool requiring approval.
- Normalized telemetry for model, usage, latency, finish reason, tool call, and
  error.

**Apple parallel lane**

- Xcode 27 workflow and Swift 6.4 changes relevant to concurrency, testing, and
  performance.
- Start the Apple AI Lab shell with explicit model-availability states and a
  non-AI fallback UI.

**DSA**

- Sliding window, stack, and binary-search introduction.

**System design**

- A1: provider-neutral model gateway.
- A2: streaming multimodal conversation service.

**Exit gate**

- The same request and schema pass through two provider adapters.
- A simulated provider timeout falls back once without duplicating a tool side
  effect.
- Streaming cancellation releases the upstream request and records a terminal
  event.
- Unsupported capability requests fail locally before calling a provider.
- A 20-case contract suite verifies structured output and tool behavior.

**Evidence**

- Model/provider decision record with quality, latency, and cost fields ready
  for later measurements.
- Sequence diagram covering stream, tool call, approval, result, and
  cancellation.

**Cut first:** advanced multimodal features and provider-native convenience
abstractions. Preserve the internal contract and failure behavior.

### Sprint 3 — August 17–30

**Theme:** knowledge systems and the modern RAG decision.

**AI/backend**

- Deterministic SQL/exact search versus long context, native file search, and
  retrieval.
- Ingestion lifecycle: parse, normalize, deduplicate, version, authorize,
  update, and delete.
- Structural chunking, embeddings, lexical search, hybrid fusion, metadata/ACL
  filters, reranking, context assembly, and citations.
- Retrieval metrics and a shared evaluation dataset.
- Compare at least three strategies on one corpus:
  - cached/native long context;
  - exact/structured search;
  - hybrid retrieval plus reranking.

**Platform milestone**

- Context service with a strategy interface rather than a hard-coded vector
  database.
- Postgres source records, versioned chunks, lexical index, pgvector index, and
  source-level ACL metadata.
- Evaluation report containing quality, retrieval, latency, and cost results.

**Apple parallel lane**

- Foundation Models v2 basics: availability, sessions, instructions, prompts,
  structured generation, streaming, tools, multimodal input, context limits,
  and prewarming.
- Use a provider adapter or Mac-capable model when the system model is
  unavailable.

**DSA**

- Binary search completion and linked lists.

**System design**

- A3: context assembly and long-context service.
- A4: permission-aware enterprise knowledge system.

**Exit gate**

- At least 30 representative questions with source and expected evidence.
- Retrieval reports recall@k and citation correctness; generation reports
  faithfulness/task success; every strategy reports latency and cost.
- Deletion and ACL tests prove stale or unauthorized content cannot be
  retrieved.
- The architecture decision chooses a strategy from evidence, not from a
  benchmark blog.

**Evidence**

- Draft of case study 1: “RAG, long context, or normal search?”

**Cut first:** GraphRAG and agentic retrieval. Add them only after the baseline
shows a specific multi-hop or iterative-search failure.

### Sprint 4 — August 31–September 13

**Theme:** state, memory, harness, and evaluation.

**AI/backend**

- Separate request context, session state, durable workflow state, and
  long-term memory.
- Memory types, write/retrieval policy, provenance, TTL, user controls, and
  contradiction handling.
- Explicit runtime event model for model/tool/approval/error/cancel/result.
- Step, time, token, and cost budgets; retries, idempotency, checkpoints,
  resume, and deterministic termination.
- Evaluation taxonomy, representative dataset, deterministic graders, model
  judge, judge calibration, repeated runs, and slices.
- OpenTelemetry spans across context, model, tool, and persistence steps.

**Platform milestone**

- Framework-independent harness v0 around the provider and context services.
- Postgres checkpoints, Redis ephemeral session state, and a deliberate memory
  store.
- Shared eval package with at least 50 cases across normal, hard, adversarial,
  and failure-recovery slices.

**Apple parallel lane**

- Dynamic Profiles, context trimming/summary, tool and model boundaries,
  Evaluations framework, and Foundation Models Instruments.
- Apple AI Lab proves one profile change while preserving an intentional
  transcript.

**DSA**

- Trees: traversal, DFS/BFS, recursion, and iterative forms.

**System design**

- A5: privacy-aware AI memory service.
- I2: on-device/PCC/cloud model-routing iOS app.

**Exit gate**

- Kill the process mid-workflow and resume once without repeating a committed
  side effect.
- A memory can be inspected, corrected, expired, and deleted.
- The eval suite detects one deliberately introduced prompt or retrieval
  regression.
- Traces reconstruct the complete execution without capturing sensitive
  content by default.
- Apple evaluation compares at least two prompt/profile versions.

**Evidence**

- Publish case study 1 only after its data and reproduction instructions pass
  review.

**Cut first:** autonomous memory writing. Retain explicit, testable write rules.

### Consolidation 1 — September 14–20

- No new AI topic.
- Re-run all four exit gates and repair the oldest failure first.
- Reduce flaky tests and remove unused abstractions.
- Refresh the stack snapshot and author Sprint 3/4 retrospective.
- System design B2: durable background-job and retry system.
- If all gates passed early, improve case study 1 or take recovery time.

## Phase 2 — Agents and real-time systems

### Sprint 5 — September 21–October 4

**Theme:** ADK 2.0 graph workflows.

**AI/backend**

- Agent versus workflow decision.
- ADK 2.0 agents, tools, functions, graph nodes, edges, workflow state, static
  and dynamic workflows, callbacks, artifacts, and evaluation.
- Deterministic nodes for policy, validation, persistence, and side effects;
  model nodes only for ambiguous reasoning.
- Human approval and policy gates.

**Platform milestone**

- Port one harness scenario into ADK 2.0 without leaking ADK types into domain
  services.
- One deterministic workflow, one model-led branch, one approval branch, and
  one resumable error path.

**Apple parallel lane**

- App Intents, schemas, entities, Core Spotlight semantic indexing, view
  annotations, confirmation, and AppIntentsTesting.
- Add one safe intent and one private on-device search path to Apple AI Lab.

**DSA**

- Trees completion, tries, and heaps.

**System design**

- A6: evaluation platform for models, retrieval, and agents.
- A7: reliable single-agent runtime.

**Exit gate**

- Defend why each graph node is deterministic or model-driven.
- Resume after a failed tool call and preserve the state/event history.
- Trajectory eval detects an incorrect route even when the final text looks
  acceptable.
- App Intent tests verify parameter resolution and confirmation.

**Evidence**

- Public-safe ADK graph diagram, node-boundary decision, and trajectory-eval
  summary linked from the platform README.

**Cut first:** decorative sub-agents. Preserve one reliable graph.

### Sprint 6 — October 5–18

**Theme:** multi-agent boundaries, interoperability, and long-running work.

**AI/backend**

- Collaboration patterns: router, supervisor, delegation, parallel workers,
  critic, and handoff.
- Shared versus isolated context and minimum result contracts.
- MCP host/client/server, tools/resources/prompts, Streamable HTTP, stdio,
  authorization, and untrusted results.
- Recheck the now-current MCP version before implementation.
- A2A discovery, task delegation, streaming, asynchronous updates, and
  artifacts.
- Pub/Sub/Cloud Tasks patterns, at-least-once delivery, deduplication,
  dead-letter handling, and cancellation.

**Platform milestone**

- Multi-text workflow with a coordinator and two independently testable
  specialists.
- Production-shaped MCP server for generic REST/OpenAPI and Postgres access.
- One independently runnable agent exposed through A2A.
- Long task executes outside the request lifecycle and publishes progress.

**Apple parallel lane**

- Integrate Foundation Models tools, Dynamic Profiles, App Intents, and
  Evaluations into one coherent Apple AI Lab workflow.
- Add explicit privacy boundaries between local and remote models.

**DSA**

- Graph BFS/DFS, topological order, union-find, and shortest-path recognition.

**System design**

- A8: human-approved action agent.
- A9: multi-agent research and verification workflow.

**Exit gate**

- Show a measured or architectural reason for every agent boundary.
- Duplicate event delivery does not duplicate a side effect.
- MCP calls enforce user/tenant authorization outside the model.
- One remote agent failure degrades predictably.
- A2A and MCP responsibilities can be explained without conflating them.

**Evidence**

- Architecture draft for case study 2: reliable workflows with ADK 2.0.

**Cut first:** a third specialist, dynamic discovery, and nonessential MCP
features.

### Sprint 7 — October 19–November 1

**Theme:** real-time voice foundations.

**AI/backend**

- PCM, sample rates, frames, buffering, codecs, jitter, VAD, endpointing, echo
  cancellation, and noise.
- WebRTC signaling, ICE, STUN/TURN, tracks, rooms, and SFU concepts.
- LiveKit room/worker/job lifecycle and graceful shutdown.
- Cascaded ASR → LLM → TTS pipeline with shared text-agent tools.
- Turn detection, interruption, transcript reconciliation, and latency spans.

**Platform milestone**

- A thin Flutter client can join a LiveKit room and complete a voice turn.
- One cascaded voice agent can call a read-only tool.
- Every stage records start/end timing and a shared correlation ID.

**Apple parallel lane**

- LiveCommunicationKit and gRPC Swift concepts.
- Prototype a separate Swift real-time client flow or simulator UI without
  coupling it to the backend portfolio deliverable.

**DSA**

- Backtracking and intervals.

**System design**

- A10: MCP/A2A interoperability platform.
- I3: resilient real-time voice iOS client.

**Exit gate**

- Demonstrate interruption and cancellation without overlapping stale audio.
- Produce a measured stage-by-stage latency budget.
- Disconnect/reconnect leaves no orphan worker and no unauthorized room.
- Explain WebRTC versus WebSocket and where UDP/QUIC matter.

**Evidence**

- Public-safe voice protocol diagram and first latency trace/report using only
  synthetic audio and identities.

**Cut first:** video and custom signaling. Preserve reliable audio and metrics.

### Sprint 8 — November 2–15

**Theme:** production multi-text and multi-voice agents.

**AI/backend**

- Multi-agent handoff during a live session with explicit shared state.
- Native speech-to-speech comparator behind the same session contract.
- Semantic turn detection, backchannel versus interruption, preemptive
  generation, provider fallback, and session resumption.
- Voice eval dataset and graders.
- Load behavior, worker draining, rate limits, consent, retention, and transcript
  policy.

**Platform milestone**

- Multi-text workflow and multi-voice workflow share tools, policy, eval, and
  telemetry services without sharing transport-specific code.
- Voice supervisor hands off to two specialists and can recover control.
- Cascaded and native-audio modes are feature-flagged and compared.

**Apple parallel lane**

- Apple AI Lab alpha: Foundation Models v2, Dynamic Profiles, Evaluations, one
  App Intent, Core Spotlight, fallback behavior, and current SwiftUI patterns.
- Profile with Instruments and fix one measured issue.

**DSA**

- One-dimensional dynamic programming.

**System design**

- A11: low-latency production voice agent.
- A12: multi-voice-agent handoff platform.

**Exit gate**

- Voice scorecard includes task success, first-audio latency, end-to-end
  latency, interruption accuracy, false interruption, failure recovery, and
  cost.
- A forced provider outage activates a tested fallback or a clear degraded
  mode.
- A graceful deployment drains active rooms.
- Apple AI Lab has deterministic fallback when model assets are unavailable.

**Evidence**

- Publish case study 2 only if the ADK graph, failure tests, and trajectory
  evaluations are reproducible.

**Cut first:** visual/video input and extra voices. Preserve one excellent
multi-agent audio flow.

### Consolidation 2 — November 16–22

- No new system-design case.
- Repair failed Phase 2 gates.
- Run a full text and voice failure-injection day.
- Remove any agent that lacks a documented reason to exist.
- Refresh the stack snapshot and author the production-security threat model
  before Phase 3.

## Phase 3 — Enterprise production engineering

### Sprint 9 — November 23–December 6

**Theme:** enterprise security and multi-tenant controls.

**AI/backend**

- OIDC login, organization/user identity, roles, tenant-scoped data, and
  end-user delegation.
- Agent/service identity, least privilege, Secret Manager, workload identity,
  and audit events.
- Direct/indirect prompt injection, tool poisoning, confused deputy, excessive
  agency, exfiltration, and unsafe output.
- PII detection/redaction, retention/deletion, quota, rate, and cost controls.
- Evaluate Agent Identity, Agent Gateway, Model Armor, and VPC Service Controls.

**Platform milestone**

- Practical tenant foundation with login, role checks, tenant-scoped rows,
  audit trail, quotas, and PII redaction.
- Threat model and abuse test suite.
- High-impact tools require policy and human confirmation.

**Apple parallel lane**

- Core AI introduction and model lifecycle.
- Choose one small generative or multimodal model appropriate for the Mac and
  define memory, startup, quality, and latency budgets.

**DSA**

- Two-dimensional dynamic programming.

**System design**

- A13: AI observability and cost-control platform.
- I4: Siri/App Intents/Core Spotlight architecture.

**Exit gate**

- Automated tests attempt cross-tenant reads/writes and all fail closed.
- Tool authorization uses server-side identity/policy, never model text.
- Audit events explain who/which agent did what, under whose authority, and
  with which result.
- Sensitive content is absent from default telemetry.

**Evidence**

- Redacted/public threat model plus tenant-isolation, authorization, and PII
  test summary with synthetic data.

**Cut first:** SCIM and private networking implementation. Retain the design and
threat model.

### Sprint 10 — December 7–20

**Theme:** GCP deployment and event-driven execution.

**AI/backend**

- Container build, non-root runtime, health/readiness, graceful shutdown, and
  image scanning.
- Cloud Run services, streaming, concurrency, min/max instances, traffic
  splitting, and rollback.
- Cloud Run functions + Eventarc for focused event handlers.
- Pub/Sub and Cloud Tasks for durable asynchronous work.
- Postgres, Redis, object storage, Secret Manager, Artifact Registry, IAM, and
  workload identity.
- Agent Runtime deployment and Cloud Run/Agent Runtime decision.
- GitHub Actions from test/eval to deployment and smoke test.
- One small AWS Bedrock invocation/IAM comparison through the existing provider
  contract when an account is available; otherwise complete the same comparison
  from an official request/architecture trace. No AWS deployment is added.

**Platform milestone**

- Staging deployment with no long-lived service-account key.
- FastAPI platform on Cloud Run; one event-driven function; one background
  agent task; one managed Agent Runtime deployment for comparison.
- Automated deploy, smoke test, traffic shift, and documented rollback.

**Apple parallel lane**

- Convert/optimize the chosen model for Core AI.
- Load, run, and inspect it through the Core AI toolchain or document an exact
  hardware/API blocker with a substitute model.

**DSA**

- Greedy and bit operations.

**System design**

- B3: event-driven document-processing pipeline.
- A14: secure multi-tenant AI solutions platform.

**Exit gate**

- Fresh staging deployment is reproducible from source and documented inputs.
- Duplicate CloudEvent delivery is safe.
- Secret scanning finds no credentials; runtime access is least-privilege.
- Roll back a deliberately bad release.
- Defend Cloud Run versus function versus Agent Runtime for each component.

**Evidence**

- Begin case study 3 with deployment and latency traces.

**Cut first:** Terraform automation and GKE. Preserve repeatable commands and
identity correctness.

### Sprint 11 — December 21–January 3

**Theme:** reliability, observability, scale, latency, and cost.

**AI/backend**

- OpenTelemetry GenAI spans/metrics/logs and trace propagation through
  LiveKit, queues, retrieval, agents, and tools.
- SLIs/SLOs, error budgets, burn-rate alerts, and runbooks.
- Timeouts, retries, circuit breakers, bulkheads, load shedding, and graceful
  degradation.
- Cache hierarchy, prompt/semantic cache, batching, pooling, model routing, and
  asynchronous work.
- k6 steady, spike, and soak scenarios; fault injection.
- Cost per successful task and quality-adjusted routing.

**Platform milestone**

- Dashboard for task success, p50/p95/p99, first token/audio, queue age, tool
  failure, token usage, cache hit, and cost.
- Two SLOs with alerts and runbooks.
- Baseline, two bottleneck fixes, and rerun report.

**Apple parallel lane**

- Add one traditional Core ML model that provides a deterministic local
  feature or routing signal.
- Profile CPU/GPU/ANE, memory, energy, and startup; compare against Core AI.
- Explain how Metal 4 quantized-tensor/neural-accelerator support affects the
  measured Core AI path without writing a custom kernel.

**DSA**

- Mixed completed-pattern review.

**System design**

- A15: Cloud Run/Agent Runtime deployment architecture.
- B4: rate-limited multi-tenant API and cache.

**Exit gate**

- Load thresholds are defined from an SLO, not an arbitrary concurrency count.
- Fault tests verify provider timeout, database saturation, queue backlog, and
  worker termination behavior.
- Two measured fixes improve the selected bottlenecks without violating
  quality or cost limits.
- On-call runbook can diagnose one injected incident from telemetry.

**Evidence**

- Reproducible load/fault report, SLO dashboard sample, and before/after
  bottleneck measurements.

**Cut first:** distributed load generation and custom dashboards. Preserve
instrumentation, SLOs, and one credible load environment.

### Sprint 12 — January 4–17

**Theme:** fine-tuning decision and production beta.

**AI/backend**

- Diagnose whether failures require prompt/context/tool/retrieval changes,
  routing, or post-training.
- Prepare a small clean dataset, baseline, held-out set, SFT/LoRA run, artifact
  version, and evaluation.
- Compare fine-tuned versus base model on quality, generalization, latency,
  serving complexity, and cost.
- Platform hardening, dependency review, backup/restore, and beta checklist.

**Platform milestone**

- One LoRA experiment with a written adopt/reject decision.
- Production beta containing text, voice, context, memory, agents, evals,
  security, telemetry, and GCP deployment.

**Apple parallel lane**

- Start Local AI Workbench with MLX/MLX-LM.
- Run an SLM locally, expose an OpenAI-compatible local endpoint, measure
  memory, startup, tokens/second, and tool behavior.

**DSA**

- Company-tagged mediums begin; continue spaced repetition.

**System design**

- I5: local generative-AI application.
- A16: scale the AI Solutions Platform 100x.

**Exit gate**

- Fine-tune evaluation uses untouched cases and reports uncertainty/slices.
- Reject the fine-tune if it does not beat the simpler baseline enough to
  justify operational cost.
- Restore platform state from a backup in a clean environment.
- Beta demo works from the thin Flutter client for both text and voice.

**Evidence**

- Publish case study 3: production voice latency/reliability, including failed
  approaches and measured fixes.

**Cut first:** serving the fine-tuned model in production. The experiment and
decision are the required evidence.

### Consolidation 3 — January 18–24

- Repair failed Phase 3 gates.
- Refresh models, ADK, cloud, protocol, and Apple stack snapshot.
- Make the physical Apple device/developer-account decision.
- System design I6: end-to-end Apple AI application.
- Freeze new platform features after this week.

## Phase 4 — FDE delivery and interviews

### Sprint 13 — January 25–February 7

**Theme:** FDE discovery, pilot, and integration.

**AI/FDE**

- Run two simulated discovery interviews.
- Map the current workflow, users, baseline, value, data, integrations, risk,
  adoption, and ownership.
- Rank use cases; write one pilot and one explicit no-go recommendation.
- Define success metric, eval set, guardrails, users, time box, kill criteria,
  deployment boundary, and handoff owner.
- Implement generic REST/OpenAPI, Postgres, webhook, and small GitHub and
  Slack/Teams-style adapter examples.

**Platform milestone**

- Configure the reusable platform for a new customer scenario without
  modifying core domain/runtime code.
- Pilot dashboard ties technical evals to workflow outcomes.

**Apple parallel lane**

- MLX/SLM tool use, local agent loop, quantization comparison, and failure
  handling.

**DSA**

- Tagged mediums, one mock, and weakest-pattern repair.

**System design**

- A17: fine-tuning and data-flywheel platform.
- B5: reusable enterprise integration platform.

**Exit gate**

- A reviewer can trace every pilot feature to a discovery finding or success
  metric.
- The no-go document is technically and commercially defensible.
- A new adapter is added without changing agent business logic.
- Present discovery and pilot scope in 15 minutes, then handle objections.

**Evidence**

- Public synthetic discovery pack containing workflow map, pilot charter,
  integration contract, scorecard, and no-go memo.

**Cut first:** a polished customer UI. Preserve discovery, integration,
measurement, and operational proof.

### Sprint 14 — February 8–21

**Theme:** public release and portfolio proof.

**AI/FDE**

- Harden public setup, sample data, threat model, architecture diagrams,
  runbooks, cost controls, and demo scripts.
- Thin Flutter client supports text, voice, session state, and visible agent
  handoff; it is not an admin platform.
- Record five-minute technical and two-minute executive demos.
- Resume v1, LinkedIn evidence, and referral-ready project summary.

**Apple parallel lane**

- Complete Local AI Workbench benchmark: Core AI versus Core ML role, MLX/SLM,
  quantization, memory, startup, speed, quality, privacy, and energy.
- Add reproducible sample inputs and fallback behavior.
- Apply relevant SwiftUI 2027 toolbar/reorderable/Document APIs and the current
  Liquid Glass/SF Symbols/Icon Composer design pass only after behavior,
  accessibility, and benchmark evidence are stable.

**DSA**

- Timed mixed mediums and one mock.

**System design**

- I7: modular iOS application at scale.
- A18: regulated-customer AI pilot under strict constraints.

**Exit gate**

- A new developer can run the public sample from the README.
- No secret/customer/Walmart data appears in the repositories.
- Demo survives a provider failure and explains the degraded state.
- Architecture, eval, security, latency, cost, and operations evidence are
  directly linked.

**Evidence**

- Draft case study 4: discovery-to-production FDE pilot.

**Cut first:** visual polish in Flutter. Preserve reliable demonstration and
operator visibility.

### Sprint 15 — February 22–March 7

**Theme:** interview loops and architecture defense.

**AI/FDE**

- Two AI system-design mocks per week.
- One iOS design and one backend design per week.
- LLM/agent deep-dive interviews using actual platform decisions.
- FDE role-play: difficult stakeholder, changing scope, eval regression,
  security constraint, and adoption failure.
- Resume v2, networking follow-ups, and selective applications.

**Apple parallel lane**

- Harden both Apple projects, tests, Instruments evidence, architecture
  walkthroughs, and device-fallback story.

**DSA**

- Two timed mock sessions and targeted remediation.

**System design**

- I8: offline sync and conflict resolution.
- B6: reliable notification and webhook-delivery platform.

**Exit gate**

- Complete a 45-minute AI design with quantified traffic/latency/cost and
  failure/security trade-offs.
- Complete a 45-minute iOS design with data flow, offline behavior,
  concurrency, performance, and tests.
- Explain three production incidents/failures from the platform and the
  evidence used to fix them.

**Evidence**

- Public portfolio evidence index updated with mock-score trend, three
  incident narratives, and only resume claims that link to proof.

**Cut first:** new project features. Interview weakness repair is the only
allowed scope.

### Sprint 16 — March 8–21

**Theme:** final integrated simulation.

**AI/FDE**

- Four-hour discovery-to-design-to-demo simulation.
- Production incident drill and handoff/runbook drill.
- Five-minute platform demo, five-minute Apple AI Lab demo, and five-minute
  Local AI Workbench demo.
- Final four case studies, resume, LinkedIn, and application package.
- Continue mocks and applications based on the active interview slate.

**Apple parallel lane**

- If a supported physical device is available, validate device-only features
  and TestFlight.
- If not, publish the Mac/simulator evidence and a precise device-validation
  checklist; do not fake completion.

**DSA**

- Interview-mode mixed sets and confidence maintenance.

**System design**

- I9: performance- and energy-aware iOS AI runtime.
- I10: full 45-minute iOS AI capstone.

**Exit gate**

- Pass two consecutive mock loops without the same critical weakness.
- Platform and Apple demos run from clean documented environments.
- FDE simulation produces discovery notes, pilot, architecture, eval result,
  incident response, and handoff package.
- Every resume claim links to evidence or is removed.

**Evidence**

- Publish case study 4 and the portfolio landing page.

**Cut first:** anything not required for a current interview, failed gate, or
public evidence.

### Consolidation 4 — March 22–28

- No new content, model migration, framework, or feature.
- Repair only failed exit gates and active interview weaknesses.
- Rehearse demos from fresh environments.
- Verify public links, redaction, costs, and cloud teardown controls.
- Decide which optional topics move to the post-March backlog.

### Final verification — March 29–31

Use the assessment rubric, not emotion.

Required:

- [ ] AI Solutions Platform production beta and public reproducible sample.
- [ ] Multi-text and multi-voice agent demos with eval and failure evidence.
- [ ] Apple AI Lab and Local AI Workbench evidence.
- [ ] Four published engineering case studies.
- [ ] 18 AI, 10 iOS, and 6 backend system-design cases completed.
- [ ] DSA review ledger and mock evidence.
- [ ] Complete FDE discovery-to-handoff simulation.
- [ ] Resume/application claims linked to artifacts.

If one area fails, label it precisely and create a two-week remediation plan.
Do not extend the entire roadmap or restart from Sprint 1.

## Phase boundary rule

At every consolidation week:

1. Re-run exit gates.
2. Refresh `09-Current-Stack-Snapshot.md`.
3. Author detailed guides only for the next immediate sprints.
4. Remove obsolete or unmeasured features.
5. Reallocate at most 20% of the next phase based on evidence.
6. Never borrow sleep, IIT class time, or the following consolidation week.
