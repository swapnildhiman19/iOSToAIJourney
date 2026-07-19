# Progress Ledger

> Last roadmap update: July 18, 2026
> Current block: Orientation — active  
> Target: March 31, 2027

This is the status source of truth. Update it during the Friday review. A
checkbox requires an evidence link, command, score, recording, or reproducible
result.

## Current focus

- Block: Orientation.
- Required outcome: complete diagnostics and choose Sprint 1 adjustments.
- This week’s single most important result: establish honest baselines.
- Current blocker: none — Docker verified Jul 18; Postgres 16 container run Jul 18 (see below).
- **One prerequisite most likely to block Sprint 1: PostgreSQL availability — RESOLVED Jul 18 (Postgres 16 in Docker, schema + transaction + `EXPLAIN` demonstrated).**
- Recovery action: Saturday's SQL/Postgres (3/3) and model API (2/3) diagnostics completed; FastAPI/HTTP raised to 2.5/3. Remaining Sprint 1 cleanups noted per row. Sunday's DSA-language and FDE diagnostics still pending (owner-completed).

## Orientation diagnostics

| Diagnostic | Score/result | Evidence | Action |
|---|---:|---|---|
| Python fundamentals | 2.5/3 — Strong understanding of Protocol, dataclasses, type hints; minor terminology gaps | `diagnostics/python_baseline.py`; Jul 17 verbal explanation | None |
| Async/concurrency | 2.5/3 — Solid grasp of semaphore, timeout, concurrency control; blocking vs non-blocking concept inverted in explanation | `diagnostics/python_baseline.py`; Jul 17 verbal explanation | Review asyncio.sleep vs time.sleep distinction |
| FastAPI/HTTP | 2.5/3 — Validation, `/health` test, and a clear `DuplicateTask` → HTTP 409 boundary with a passing error test; the clean boundary lives in a parallel `/v2/tasks` route rather than consolidated into `POST /tasks`, and success/error bodies are not asserted | `AI Solutions Platform/diagnostics/Sprint-00-Orientation-diagnostics/fast_api.py`; `uv run --extra dev pytest "diagnostics/Sprint-00-Orientation-diagnostics/fast_api.py" -q` → 2 passed (verified Jul 18) | Sprint 1 cleanup: consolidate the 409 mapping into `POST /tasks` and assert success/error bodies |
| SQL/Postgres | 3/3 — PK, FK, UNIQUE, CHECK, and FK index defined; transaction `COMMIT` persisted; `EXPLAIN` shows Bitmap Index Scan on `idx_orders_customer_id`; `ROLLBACK`, parameterized query, and index write-cost explained in notes | `diagnostics/Sprint-00-Orientation-diagnostics/schema.sql`, `.../test_insert.sql`, `notes/sprint-00-Orientation-notes.md`; demonstrated on Postgres 16 in Docker (container `orientation-pg`, db `diag`) — `\dt`, row selects, and `EXPLAIN` verified Jul 18 | Sprint 1: demonstrate `ROLLBACK` and a Python parameterized query live |
| Model API | 2/3 — Structured output via `response_json_schema` + Pydantic `model_validate_json`, configurable model ID, `.env`-based key handling; no forced invalid-output/missing-key failure and no latency/usage capture | `diagnostics/Sprint-00-Orientation-diagnostics/gemini_model_api_diagnostic.py`; google-genai 2.12.1 (GA), model `gemini-2.5-pro` (stable/GA; newer Gemini 3.x line exists); successful run user-reported, not independently executed (paid call) | Sprint 1: add a forced-failure branch and record latency/token usage |
| Git/Docker/CI | Partial: Git available; Docker verified Jul 18 and used to run a Postgres 16 container (`orientation-pg`) for the SQL diagnostic; `.env` confirmed git-ignored; CI still untested | July 16 environment baseline below; Jul 18 terminal output (`docker --version`, `docker compose version`, `docker ps`, `git check-ignore`) | Configure CI in Sprint 1 (repository ignores verified) |
| Swift/SwiftUI | Completed; SwiftUI view built, Swift Testing suite configured & verified passing | `Sprint-00-Orientation/Test.swift` | None |
| Swift Concurrency | Completed; actor `DiagnosticReporter` created and compiled | `Sprint-00-Orientation/CheckActors.swift` | None |
| Apple hardware/SDK availability | Completed; M4 Pro, active Xcode 27 beta 3, iOS 27.0 runtime, CoreAI SDK framework verified | July 16 environment baseline below | Check SystemLanguageModel once FoundationModels API is configured |
| DSA in Swift | — | — | Pending |
| DSA in Python | — | — | Pending |
| System design | 14/24 — RAG architecture, RBAC, async processing; gaps in quantification, failure handling, context window management | Handwritten diagram Jul 17; chat interview transcript; rubric scores: Requirements 2/3, Estimates 1/3, Contracts 2/3, Architecture 2/3, AI depth 2/3, Failure handling 1/3, Security 2/3, Communication 2/3 | Study context window mgmt, re-ranking, quantification before Sprint 1 |
| FDE discovery | — | — | Pending |

### Environment baseline — July 16, 2026 (revised)

Source: direct version, hardware, and simulator commands run from the roadmap
root in the active `(base)` shell. Hardware and simulator data corrected after
`system_profiler` and `xcrun simctl list devices` on July 16.

| Tool | Recorded result | Requirement assessment |
|---|---|---|
| Git | 2.50.1 (Apple Git-155) | Available |
| Python | 3.14.6 | Python 3.12+ confirmed |
| uv | 0.9.28 (0e1351e40 2026-01-29) | Available |
| Docker | 29.6.1, build 8900f1d; Compose v5.3.0 | **Available** — verified Jul 18; ran Postgres 16 container `orientation-pg` for the SQL diagnostic |
| Google Cloud CLI | 574.0.0; core 2026.06.22 | CLI available; GCP project `easyaiwithswapnil` confirmed |
| Mac hardware | MacBook Pro (`Mac16,8`), Apple M4 Pro, 12 cores (8P + 4E), 24 GB memory | Apple Silicon hardware confirmed |
| Swift | 6.2.4 (swiftlang-6.2.4.1.4 clang-1700.6.4.2); target `arm64-apple-macosx26.0` | Available |
| Xcode (stable) | 26.3, build 17C519 | Available |
| Xcode (beta) | 27 beta 3 at `/Applications/Xcode-beta.app` | Active developer directory (`xcode-select`) |
| Simulators | iOS 26.0, 26.2, and **27.0** (24A5380i) runtimes verified | iOS 27.0 simulator and OS 27 SDK confirmed ✅ |

The baseline was captured without upgrading. Google Cloud CLI reported that
component updates are available. Docker was verified available on Jul 18
(29.6.1, Compose v5.3.0), resolving the Jul 17 blocker. The earlier
hardware record (M3 Pro/36 GB) was from a different machine. Serial numbers,
UUIDs, provisioning identifiers, simulator IDs, and activation-lock state were
intentionally excluded from this ledger.

Primary DSA language decision: **Pending diagnostic**

## Roadmap status

Allowed status: `not-started`, `active`, `blocked`, `gate`, `partial`, `passed`,
or `repair`.

| Block | Dates | Status | Score /15 | Exit evidence | Repair |
|---|---|---|---:|---|---|
| Orientation | Jul 16–19 | active | — | Partial: environment baselines revised, Apple hardware/simulator verified, AI Solutions Platform skeleton created, Swift diagnostics completed; backend diagnostics done Jul 18 — FastAPI/HTTP 2.5/3, SQL/Postgres 3/3 (demonstrated on Postgres 16), Model API 2/3. Remaining: DSA-language + FDE diagnostics, DSA language selection, Sprint 1 ≤20% adjustment | — |
| Sprint 1 | Jul 20–Aug 2 | not-started | — | — | — |
| Sprint 2 | Aug 3–16 | not-started | — | — | — |
| Sprint 3 | Aug 17–30 | not-started | — | — | — |
| Sprint 4 | Aug 31–Sep 13 | not-started | — | — | — |
| Consolidation 1 | Sep 14–20 | not-started | — | — | — |
| Sprint 5 | Sep 21–Oct 4 | not-started | — | — | — |
| Sprint 6 | Oct 5–18 | not-started | — | — | — |
| Sprint 7 | Oct 19–Nov 1 | not-started | — | — | — |
| Sprint 8 | Nov 2–15 | not-started | — | — | — |
| Consolidation 2 | Nov 16–22 | not-started | — | — | — |
| Sprint 9 | Nov 23–Dec 6 | not-started | — | — | — |
| Sprint 10 | Dec 7–20 | not-started | — | — | — |
| Sprint 11 | Dec 21–Jan 3 | not-started | — | — | — |
| Sprint 12 | Jan 4–17 | not-started | — | — | — |
| Consolidation 3 | Jan 18–24 | not-started | — | — | — |
| Sprint 13 | Jan 25–Feb 7 | not-started | — | — | — |
| Sprint 14 | Feb 8–21 | not-started | — | — | — |
| Sprint 15 | Feb 22–Mar 7 | not-started | — | — | — |
| Sprint 16 | Mar 8–21 | not-started | — | — | — |
| Consolidation 4 | Mar 22–28 | not-started | — | — | — |
| Final verification | Mar 29–31 | not-started | — | — | — |

## Active sprint gate

Orientation uses a checklist exit gate (not the five-dimension `/15` sprint
rubric). Criteria mirror `sprints/Sprint-00-Orientation.md` → "Orientation exit
gate". (Aligned Jul 18 — the previous generic sprint template did not match the
active sprint.)

- [ ] Every diagnostic has a score/result and evidence — Python 2.5, Async 2.5,
      FastAPI 2.5, SQL/Postgres 3, Model API 2, System design 14/24, Swift
      diagnostics done; **still pending: DSA in Swift, DSA in Python, FDE
      discovery**.
- [ ] Missing Sprint 1 prerequisites installed or scheduled — PostgreSQL
      resolved (Postgres 16 via Docker); confirm remainder during Sunday close.
- [x] No credential or confidential information in the repository — `.env`
      git-ignored (verified `git check-ignore` Jul 18). Note: `test_insert.sql`
      uses a real personal email as sample data; prefer a synthetic identity.
- [x] Provider and cloud budgets/alerts recorded — pay-as-you-go GCP project
      `easyaiwithswapnil`, manual spend monitoring (see Cloud cost section).
- [ ] DSA language selected or Consolidation 1 decision explicit — pending DSA
      diagnostic.
- [x] Apple hardware, SDK, simulator, and system-model availability recorded —
      [PROGRESS.md](file:///Users/swapnildhiman/Desktop/AI/iOSToAIJourney/PROGRESS.md#L37-L61).
- [ ] Sprint 1 has no more than a 20% evidence-based adjustment — pending
      Sunday close.

Decision: Orientation **not yet passed** — backend diagnostics recorded, but
DSA-language and FDE diagnostics plus the Sprint 1 adjustment remain
(owner-completed Sunday Jul 19).

## Weekly hours

Target roadmap hours: 20–25. IIT is tracked separately.

| Week of | AI/platform | Apple | DSA | Design | Review/FDE | Roadmap total | IIT | Note |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Jul 13 | — | — | — | — | — | — | — | Orientation |

Two consecutive roadmap weeks above 25 hours require a scope cut.

## AI Solutions Platform milestones

- [/] Repository and CI foundation. Skeleton created at `AI Solutions Platform/` with 11 module packages, pyproject.toml, .env.example, and root .gitignore. CI not yet configured.
- [ ] FastAPI/Postgres vertical slice.
- [ ] Two-provider model contract.
- [ ] Streaming, structured output, tools, approval, and cancellation.
- [ ] Measured context strategy.
- [ ] State, memory, harness, and shared evals.
- [ ] ADK 2.0 reliable workflow.
- [ ] Multi-agent, MCP, A2A, and durable background work.
- [ ] Cascaded voice agent.
- [ ] Native-audio comparator and multi-agent voice handoff.
- [ ] Identity, tenant isolation, audit, quotas, and PII controls.
- [ ] GCP staging deployment and rollback.
- [ ] OpenTelemetry, SLO, load/fault/latency/cost report.
- [ ] LoRA experiment and adopt/reject decision.
- [ ] Generic integration adapters.
- [ ] Thin Flutter text/voice demo.
- [ ] Public production-beta sample and runbook.

## Apple AI Lab milestones

- [ ] Availability/fallback shell.
- [ ] Foundation Models v2 text/image and structured generation.
- [ ] Tools and streaming.
- [ ] Dynamic Profiles.
- [ ] Evaluations and Instruments evidence.
- [ ] App Intents and AppIntentsTesting.
- [ ] Core Spotlight and safe private retrieval.
- [ ] Alpha demo and documentation.
- [ ] Physical-device checkpoint recorded.

## Local AI Workbench milestones

- [ ] Current SLM selection with license/hardware rationale.
- [ ] MLX local run and compatible endpoint.
- [ ] Quantization comparison.
- [ ] Tool-use/local-agent experiment.
- [ ] Core AI model conversion/run.
- [ ] Traditional Core ML model.
- [ ] Core AI/Core ML/MLX/cloud benchmark.
- [ ] Memory, startup, speed, quality, privacy, energy, and cost report.
- [ ] Reproducible public demo.

## System-design ledger

Required: 18 AI, 10 iOS, 6 backend.

- AI complete: **1/18** (Orientation diagnostic)
- iOS complete: **0/10**
- Backend complete: **0/6**
- Total complete: **1/34**
- Two most recent scores: 14/24 (Orientation)
- Lowest current dimension: Estimates and budgets (1/3), Failure handling (1/3)

Completed case IDs:

- AI: Orientation diagnostic (Enterprise AI Assistant with RAG)
- iOS: —
- Backend: —

Next scheduled case: B1 — Reliable webhook ingestion (Sprint 1, Week 1).

## DSA ledger summary

- Primary language: pending.
- Unique independent solves: 0.
- Learned/hinted: 0.
- Failed: 0.
- Repetitions completed: 0.
- Current clean medium solve rate: not measured.
- Median independent medium time: not measured.
- Most frequent mistake tag: not measured.
- Most recent mock score: not measured.
- Next due repetition: —

Problem-level records may live in the selected coding platform/export, but this
summary and mock evidence stay current here.

## FDE evidence

- [ ] Opportunity qualification.
- [ ] Current-state workflow map.
- [ ] Two discovery simulations.
- [ ] Ranked use cases.
- [ ] Pilot charter and scorecard.
- [ ] Explicit no-go recommendation.
- [ ] Integration contracts.
- [ ] Security/data-boundary review.
- [ ] Deployment and rollback presentation.
- [ ] Incident/SLO communication.
- [ ] Executive demo.
- [ ] Technical demo with failure mode.
- [ ] Rollout and handoff package.
- [ ] Full capstone simulation.

Current FDE rubric: —/24

## Public case studies

| Case study | Target | Status | Evidence/data | Public link |
|---|---|---|---|---|
| RAG vs long context vs normal search | Phase 1 | not-started | — | — |
| Reliable ADK 2.0 workflows | Phase 2 | not-started | — | — |
| Production voice latency/reliability | Phase 3 | not-started | — | — |
| Discovery-to-production FDE pilot | Phase 4 | not-started | — | — |

## Stack refreshes

| Checkpoint | Due | Completed | Material changes | Migration/eval |
|---|---|---|---|---|
| Orientation | Jul 19 | Jul 16 snapshot; google-genai 2.12.1 confirmed Jul 18 | google-genai SDK GA (2.12.1); `gemini-2.5-pro` GA with a newer Gemini 3.x line now available | Pending contract setup; re-evaluate model choice (2.5-pro vs 3.x) in Sprint 1 |
| Consolidation 1 | Sep 20 | — | — | — |
| Consolidation 2 | Nov 22 | — | — | — |
| Consolidation 3 | Jan 24 | — | — | — |
| Consolidation 4 | Mar 28 | — | — | — |

## Device and account gates

- Apple Silicon Mac: MacBook Pro (`Mac16,8`), M4 Pro, 12 cores (8P + 4E), 24 GB memory.
- Xcode 26.3 (build 17C519) and Xcode 27 beta 3 (`/Applications/Xcode-beta.app`)
  are installed; iOS 26.0, 26.2, and **27.0** simulators available.
- OS 27 SDK: **Active** via Xcode 27 beta 3 selection (verified iphoneos27.0 and iphonesimulator27.0 SDKs).
- Apple Intelligence system-model availability: pending orientation.
- Supported physical iPhone/iPad: pending Consolidation 3 checkpoint.
- Paid Apple Developer account: pending Consolidation 3 checkpoint.
- GCP project: `easyaiwithswapnil` (ID: easyaiwithswapnil, number: 377345686823, no organization).
- Provider API budgets: pay-as-you-go; no fixed monthly cap; funds added per requirement.

## Cloud cost and teardown

- Monthly budget: **pay-as-you-go** (GCP project `easyaiwithswapnil`); funds added per requirement.
- Current month spend: not yet checked.
- Active billable resources: none yet.
- Automatic budget alerts: not using fixed alerts; will monitor spend manually.
- Teardown command/runbook: pending.
- Unexpected cost incident: none.

## Blockers

| Opened | Blocker | Type | Evidence | Substitute | Recheck | Owner | Status |
|---|---|---|---|---|---|---|---|
| Jul 17 | Docker not installed | Prerequisite | Environment baseline Jul 16; resolved Jul 18 (`docker --version` 29.6.1, `docker compose version` v5.3.0) | Could use managed Postgres (Cloud SQL) but local preferred for Sprint 1 | Before Sat diagnostic | Swapnil | **Closed Jul 18** |

## Recovery actions

| Opened | Failed gate | Root cause | Smallest repair | Due | Result/evidence |
|---|---|---|---|---|---|
| — | None | — | — | — | — |

## Application readiness

- Networking starts: December 2026.
- Selective applications start: January 2027.
- Resume v1: not-started.
- Resume v2: not-started.
- Portfolio landing page: not-started.
- AI demo: not-started.
- Apple AI Lab demo: not-started.
- Local AI Workbench demo: not-started.
- Consecutive passing AI system-design mocks: 0/2.
- Consecutive passing coding mocks: 0/2.
- Complete FDE simulation: not-started.

## Weekly review entry template

### Week of YYYY-MM-DD

- Planned roadmap hours:
- Actual roadmap hours:
- IIT hours:
- Result I can now produce without a tutorial:
- Strongest evidence:
- Failed or partial gate:
- Root cause:
- Quality/latency/cost/security/reliability measurement:
- DSA pattern and mistake:
- System-design case and score:
- Apple evidence:
- FDE/customer-delivery evidence:
- Scope removed:
- Recovery action:
- Next week’s single most important result:
