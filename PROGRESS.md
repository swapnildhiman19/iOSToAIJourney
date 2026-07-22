# Progress Ledger

> Last roadmap update: July 22, 2026
> Current block: Sprint 1 (Orientation passed Jul 20) — active  
> Target: March 31, 2027

This is the status source of truth. Update it during the Friday review. A
checkbox requires an evidence link, command, score, recording, or reproducible
result.

## Current focus

- Block: Sprint 1 - AI Software Foundations (Jul 20-Aug 2).
- Required outcome: a tested FastAPI/Postgres foundation with safe async and signed-webhook behavior (see the Sprint 1 exit test).
- This week's single most important result: a persisted vertical slice (validated request -> service -> Postgres) proven from a clean checkout.
- Current blocker: none - all Sprint 1 prerequisites confirmed Jul 20 (Python 3.14.6, uv 0.9.28, Git 2.50.1, Docker 29.6.1 / Postgres 16, Swift 6.2.4, DSA language selected).
- Orientation: passed Jul 20 - every diagnostic scored and evidenced; DSA language = Swift; Sprint 1 adjusted within the 20% limit with its exit gate preserved.
- Carry-forward from orientation (fold into Sprint 1, no scope growth): (1) FastAPI - consolidate the 409 mapping into POST /tasks and assert response bodies; (2) SQL - demonstrate ROLLBACK + a Python parameterized query live; (3) Model API - forced-failure branch + latency/usage capture (Sprint 2, where the model lands); (4) replace the real email in test_insert.sql with a synthetic identity.
- Schedule (authoritative recovery override recorded Wed Jul 22): the domain implementation and independent adapter-swap defense are reviewed; the defense passed this checkpoint at 3/4 with two corrections recorded (add a Postgres adapter and switch composition rather than rewrite the memory adapter; translate the exact database uniqueness violation inside that adapter to `DuplicateTaskTitle`). The due DSA problem is selected as **Repeating and Missing Number**, targeting O(n) time and O(1) extra space without modifying input; it remains unsolved, and its prior-mistake note is still missing. Wed FastAPI/DSA are treated as missed. Thu Jul 23 substitutes FastAPI plus minimum contract evidence; Sat Jul 25 contains the only two optional replacements (safe async, then ADR/minimal CI); Sun Jul 26 integrates Swift concurrency plus 30-minute DSA review; Mon Jul 27 recovers the selected arrays/hash revision; Tue/Wed Jul 28–29 recover the two-pointer and unseen arrays/hash outcomes inside existing DSA slots. IIT remains separate, Thu/Fri and Week-2 core work remain fixed, and the Aug 2 gate does not move. See the active sprint's Recovery override and Recovery actions below.

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
| Swift Concurrency | Completed - actor isolation, withTaskGroup child tasks, cooperative cancellation, and MainActor boundaries; ResultStore/withTaskGroup example built and reasoned through | Sprint-00-Orientation/CheckActors.swift, UnderstandingActor.swift; deep-dive in notes/sprint-00-Orientation-notes.md | None |
| Apple hardware/SDK availability | Completed; M4 Pro, active Xcode 27 beta 3, iOS 27.0 runtime, CoreAI SDK framework verified | July 16 environment baseline below | Check SystemLanguageModel once FoundationModels API is configured |
| DSA in Swift | Independent solve - Maximum Product Subarray (medium DP): rejected take/skip subset framing, derived max/min-product-ending-at-i invariant, memoized then bottom-up DP (O(n) time, O(n) space; O(1) achievable) | iOS-Apps/DSA/Sprint-Orientation-00.swift (full brute-force to DP derivation in file comments) | Sprint 1: timed array/hash + two-pointer mediums; one equivalent in Python |
| DSA in Python | Deferred by design - Swift chosen as interview-primary for Phase 1; first Python solve scheduled in Sprint 1 weekly DSA (one problem/week) | 06-DSA-Track.md language rule | Re-decide language at Consolidation 1 (Sep 14-20) |
| System design | 14/24 — RAG architecture, RBAC, async processing; gaps in quantification, failure handling, context window management | Handwritten diagram Jul 17; chat interview transcript; rubric scores: Requirements 2/3, Estimates 1/3, Contracts 2/3, Architecture 2/3, AI depth 2/3, Failure handling 1/3, Security 2/3, Communication 2/3 | Study context window mgmt, re-ranking, quantification before Sprint 1 |
| FDE discovery | Baseline 15/24 (orientation diagnostic - not a gate; the 20/24 bar is the Phase-4 Mar-2027 capstone target). Strong qualification, architecture, and security; grow communication structure and quantified baseline+threshold | notes/sprint-00-Orientation-notes.md (FDE discovery diagnostic section) | Sprint 1 embedded FDE one-pager: explain provider-neutral architecture to a non-AI engineer |

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

Primary DSA language decision: **Swift** (interview-primary through Phase 1; Python maintained one problem/week for AI-FDE fluency; firm re-decision at Consolidation 1)

## Roadmap status

Allowed status: `not-started`, `active`, `blocked`, `gate`, `partial`, `passed`,
or `repair`.

| Block | Dates | Status | Score /15 | Exit evidence | Repair |
|---|---|---|---:|---|---|
| Orientation | Jul 16–19 | passed | — | Passed Jul 20 (checklist gate): all diagnostics scored + evidenced (Python 2.5, Async 2.5, FastAPI 2.5, SQL 3, Model API 2, System design 14/24, Swift + Concurrency, DSA-Swift independent solve, FDE 15/24); DSA language = Swift; Sprint 1 adjusted within 20%, exit gate preserved | — |
| Sprint 1 | Jul 20–Aug 2 | active | — | — | — |
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

Sprint 1 (Jul 20-Aug 2) is the active block. It uses the five-part sprint rubric (/15); pass requires at least 11/15, no zero, and every item in the Sprint 1 Exit test proven. See sprints/Sprint-01-AI-Software-Foundations.md -> Exit test. The score is recorded at the Aug 2 sprint close.

### Orientation exit gate - CLOSED, passed Jul 20

- [x] Every diagnostic has a score/result and evidence - Python 2.5, Async 2.5, FastAPI 2.5, SQL/Postgres 3, Model API 2, System design 14/24, Swift + Concurrency done, DSA in Swift (independent solve), FDE 15/24. DSA in Python deferred by design (Swift primary; first Python solve in Sprint 1).
- [x] Missing Sprint 1 prerequisites installed or scheduled - PostgreSQL resolved (Postgres 16 via Docker); all remaining prerequisites confirmed Jul 20.
- [x] No credential or confidential information in the repository - .env git-ignored (verified git check-ignore Jul 18). Carry-forward hygiene: replace the real personal email in test_insert.sql with a synthetic identity at the first Sprint 1 SQL touch.
- [x] Provider and cloud budgets/alerts recorded - pay-as-you-go GCP project easyaiwithswapnil, manual spend monitoring (see Cloud cost section).
- [x] DSA language selected - Swift (interview-primary through Phase 1; Python one problem/week; re-decide at Consolidation 1).
- [x] Apple hardware, SDK, simulator, and system-model availability recorded - see the environment baseline; FoundationModels availability probe added (CheckFoundationModels.swift).
- [x] Sprint 1 has no more than a 20% evidence-based adjustment - one learning item (blocking vs non-blocking / event-loop offload) and one build item (assert success + error response bodies) added; the exit gate is preserved.

Decision: Orientation passed Jul 20. All diagnostics scored and evidenced; DSA language selected; Sprint 1 adjusted within the 20% limit with its exit gate preserved.

## Weekly hours

Target roadmap hours: 20-25. IIT is tracked separately.

| Week of | AI/platform | Apple | DSA | Design | Review/FDE | Roadmap total | IIT | Note |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Jul 13 | - | - | - | - | - | - | - | Orientation |
| Jul 20 | plan | plan | plan | plan | plan | plan 24-25 | unreported | Sprint 1 Wk1 recovery: Thu substitutes FastAPI; Sat uses exactly two optional replacements (safe async and ADR/minimal CI); Sun integrates Swift concurrency plus DSA review. Actual roadmap hours and Jul 22 IIT attendance remain unreported; record them at the Jul 24 review. |
| Jul 27 | plan | plan | plan | plan | plan | plan 24-25 | - | Sprint 1 Wk2 core sequence unchanged; existing DSA slots recover due arrays/hash on Jul 27, timed two pointers on Jul 28, and the displaced unseen arrays/hash plus repetition on Jul 29; fill actuals at the Aug 2 close. |

Two consecutive roadmap weeks above 25 hours require a scope cut.

## AI Solutions Platform milestones

- [/] Repository and CI foundation. Skeleton exists at `AI Solutions Platform/`; `src/`, `uv.lock`, `.python-version`, pyproject configuration, formatting, lint, strict type-check, and test commands were verified Jul 22. The required architecture decision and `.github/workflows/ci.yml` are absent; their single replacement is Sat Jul 25, 4:30–6:00, so this milestone remains partial.
- [x] Sprint 1 domain-boundary exercise checkpoint. Frozen domain record, domain duplicate exception, repository `Protocol`, injected application service, in-memory adapter, and create/duplicate tests were verified Jul 22. Targeted and full pytest each passed 2 tests; Ruff format/lint and strict mypy passed; the domain/application forbidden-SDK scan returned zero matches. Swapnil's independent adapter-swap defense was reviewed Jul 22 at 3/4 and accepted with corrections: add `PostgresTaskRepository` rather than rewrite the memory adapter, switch the composition/provider, and translate the exact unique-constraint failure inside the Postgres adapter to `DuplicateTaskTitle`. This closes the local exercise checkpoint, not the Aug 2 sprint gate.
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

- Primary language: Swift (interview-primary through Phase 1; Python one problem/week; re-decide at Consolidation 1). See the 06-DSA-Track.md language rule.
- Unique independent solves: 1 (Maximum Product Subarray, medium DP, Swift; derivation in iOS-Apps/DSA/Sprint-Orientation-00.swift).
- Learned/hinted: 0.
- Failed: 0.
- Repetitions completed: 0.
- Current clean medium solve rate: not yet measured (Sprint 1 starts timed array/hash + two-pointer mediums).
- Median independent medium time: not measured (the orientation solve was untimed).
- Most frequent mistake tag: pattern-selection mismatch - the Jul 21 LIS submission did not match the required arrays/hash-map revision; no timed-solve mistake tag is recorded yet.
- Most recent mock score: not measured.
- Next due repetition: Maximum Product Subarray ~Aug 3 (clean-solve 14-day interval), or replace with a harder DP variant.
- Jul 21 Sprint 1 submission review (verified Jul 22): `../iOS-Apps/DSA/sprint-01-AI-Software-Foundations.swift` is an untracked Longest Increasing Subsequence solution, not an arrays/hash-map revision. It type-checks with one trailing-closure warning; the active `firstIndex` search makes it O(n^2) time and O(n) space. No accepted run, timing, due-item provenance, mistake reflection, or next repetition date was supplied, so it is not counted above.
- Recovery queue: selected **Repeating and Missing Number** (values 1...n, one duplicate A and one missing B, input immutable) for Mon Jul 27, 9:30–10:30. The intended target is O(n) time and O(1) extra space; no algorithm, runnable/accepted result, or complexity proof has been reviewed yet, and the requested prior-mistake note is still missing. Use Tue Jul 28 for the missed timed two-pointer solve and Jul 29's existing mixed set for the displaced unseen arrays/hash problem plus two-pointer repetition.

Problem-level records may live in the selected coding platform/export, but this
summary and mock evidence stay current here.

## FDE evidence

- [x] Opportunity qualification.
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

Current FDE rubric: baseline 15/24 (orientation diagnostic; the 20/24 pass bar applies to the Phase-4 capstone simulation, not this Week-0 baseline). See notes/sprint-00-Orientation-notes.md.

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
- Apple Intelligence system-model availability: FoundationModels availability probe added (CheckFoundationModels.swift, Sprint-00-Orientation); record the concrete availability result in Sprint 1.
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

Detailed dated execution is authoritative in `sprints/Sprint-01-AI-Software-Foundations.md` under **Recovery override — recorded Wednesday, July 22**.

| Opened | Failed gate | Root cause | Smallest repair | Due | Result/evidence |
|---|---|---|---|---|---|
| Jul 21 | None - in-sprint day slip, not a gate | Sprint 1 Monday Jul 20 blocks not completed | Preserve verified domain code. Use Sat Jul 25, 4:30–6:00 for the missing ADR/minimal CI and Mon Jul 27, 9:30–10:30 for the selected Repeating and Missing Number revision. The displaced Tue safe-async and Swift work use Sat Jul 25 and Sun Jul 26; Tue's unseen arrays/hash is absorbed by Jul 29's mixed set. | Review Jul 24; execution Jul 25–29 | **Partial, verified/reviewed Jul 22:** implementation and local checks pass; the independent adapter-swap defense passed the local checkpoint at 3/4 with corrections recorded. Repeating and Missing Number is selected but unsolved, and its prior-mistake note is missing. ADR/CI and qualifying DSA execution evidence remain incomplete. |
| Jul 22 | None - in-sprint day slip, not a gate | Wednesday FastAPI and DSA blocks were not completed before their windows elapsed | Thu Jul 23 FastAPI replaces the missed flow and absorbs minimum contract evidence. Distribute remaining exit-critical tests beside safe-async, Postgres, transaction, and lifecycle blocks. Recover DSA through Sun Jul 26 review, Tue Jul 28 timed solve, and Jul 29 repetition/mixed set. Remove duplicate test-framework breadth rather than add a third optional block. | Jul 23–30 | Planned; no completion claimed. IIT attendance is unreported and, if missed, is handled separately from Sprint 1. Thu/Fri fixed work, Week-2 platform sequence, and Aug 2 gate remain unchanged. |

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
