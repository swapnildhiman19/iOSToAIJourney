# Progress Ledger

> Last roadmap update: August 26, 2026 (schedule revision + restart gate opened)
> Current block: Restart gate (Aug 26–30) — active
> Target: May 12, 2027 (revised Aug 26, 2026 from March 31, 2027; +6 weeks)

> **Integrity note — Aug 26, 2026.** This file was corrupted in commit `53f549a`
> (Jul 28): a compressed tool *read* of the file was written back over it,
> replacing 134 lines across 23 sections with `[lean-ctx: omitted N lines]`
> markers and prefixing a `PROGRESS.md [332L]` tool header. It was reconstructed
> Aug 26 from the last clean revision (`79f9f93`, 332 lines) with all eight
> genuine Jul 28 additions re-applied and verified. No evidence was lost. Do not
> paste compressed tool output into a ledger file.

This is the status source of truth. Update it during the Friday review. A
checkbox requires an evidence link, command, score, recording, or reproducible
result.

## Current focus

- Block: **Restart gate (Aug 26-30)**. Sprint 1 - AI Software Foundations moves to
  its repair sprint Aug 31-Sep 13; first attempted Jul 20-Aug 2 and never closed.
- **Pause and restart, recorded Aug 26:** execution stopped after the Tue Jul 28
  evening session. Four weeks (Jul 27, Aug 3, Aug 10, Aug 17) passed with no
  recorded roadmap work, triggering the `04-Weekly-Operating-System.md` rule that
  two consecutive weeks below the minimum-viable plan require a roadmap pause and
  a smaller restart gate. Every block from Sprint 1 onward moved **+6 weeks**; no
  outcome, exit gate, prerequisite, weekly budget, or portfolio boundary changed.
  The two deferrals recorded Jul 28 (system-design I1, and the SwiftUI
  observation/state architecture) are **restored** into the repair sprint.
- **Verified state of the code as of Aug 26 (not user-reported):**
  `PostgresTaskRepository` is referenced exactly once repo-wide - its own class
  definition. `api/app.py` still hardcodes `InMemoryTaskRepository()`, so the
  running API persists nothing and exit-test items 1-2 are not achievable as
  committed. `ruff check src tests` reports 8 errors, `ruff format --check` 4
  files, and `mypy src tests` 1 error - every failure in a file introduced by
  `53f549a`. There is no `.github/`, no CI, no service Dockerfile, and no ADR;
  `tests/integration/` holds only `.gitkeep` and `tests/conftest.py` defines zero
  fixtures. All 9 passing tests exercise the in-memory adapter only.
- Required outcome: a tested FastAPI/Postgres foundation with safe async and signed-webhook behavior (see the Sprint 1 exit test).
- This week's single most important result: a persisted vertical slice (validated request -> service -> Postgres) proven from a clean checkout.
- Current blocker: none - all Sprint 1 prerequisites confirmed Jul 20 (Python 3.14.6, uv 0.9.28, Git 2.50.1, Docker 29.6.1 / Postgres 16, Swift 6.2.4, DSA language selected).
- Orientation: passed Jul 20 - every diagnostic scored and evidenced; DSA language = Swift; Sprint 1 adjusted within the 20% limit with its exit gate preserved.
- Carry-forward from orientation (fold into Sprint 1, no scope growth): (1) FastAPI 409 consolidation and response-body evidence closed Jul 23 with the in-memory HTTP contract tests; (2) SQL — **closed Jul 24, verified Jul 25**: `ROLLBACK` and a Python parameterized query both demonstrated against live PostgreSQL 16.14; (3) Model API - forced-failure branch + latency/usage capture (Sprint 2, where the model lands); (4) synthetic test fixture identity — **closed Jul 25**: `test_insert.sql` line 4 still contained a real personal email after the Jul 24 hygiene step claimed completion; it now inserts `learner@example.invalid` / `Learner One`.
- Schedule (authoritative recovery override recorded Wed Jul 22): the domain checkpoint and adapter-swap defense are reviewed. The Thu Jul 23 FastAPI replacement is verified through per-app injection, stable 404/409 contracts, default 422 validation, OpenAPI, and 9 passing tests. The Fri Jul 24 SQL and B1 blocks are complete and reviewer-verified Jul 25 (SQL artifacts executed against live Postgres; B1 scored 17/24 against the eight-dimension track rubric). The **Fri Jul 24 9:11–10:11 PM weekly review did not happen** — the B1 write-up overran its 9:11 PM stop (`notes/sprint-01-AI-Software-Foundations-notes-02-*.md` last modified Jul 25, 02:16 IST) — so the clean-checkout reproduction and Week-1 gap list move once, into the existing Fri Jul 31 gate-rehearsal block. No third Week-1 replacement block is created. The external Jul 23 Swift artifact at `../iOS-Apps/iOSToAIJourney/Sprint-01-AI-Software-Foundations/TaskListFeature.swift` has only the prior `xcrun swiftc -typecheck TaskListFeature.swift` exit-0 evidence. Its implementation was unstaged in the sibling repository when reviewed, so this is working-tree-only/non-durable evidence of a guided state/protocol/fake foundation, not a complete SwiftUI feature. **Repeating and Missing Number** remains selected but unsolved, with its prior-mistake note still missing. **Sat Jul 25 safe async block — partial**: `async_boundary_lab.py` created and staged (`AI Solutions Platform/diagnostics/Sprint-01-AI-Software-Foundations/async_boundary_lab.py`), demonstrating unbounded fan-out (peak = 50), semaphore-bounded fan-out (peak = 5), and the blocking boundary (`time.sleep` starvation vs `asyncio.to_thread` fix); the companion notes file (`notes/sprint-01-AI-Software-Foundations-notes-03-python-asyncio-complete-understanding.md`) was created but remains **empty**; timeout and cancellation-cleanup tests were not written. **Sat Jul 25 ADR/minimal CI block — not started.** **Sun Jul 26 through Tue Jul 28 afternoon — entirely missed**: Swift concurrency + DSA two-pointer review (Sun), async Postgres adapter + persisted vertical slice + Repeating and Missing Number DSA (Mon), transactions/idempotency + Apple architecture (Tue 2:15–6:30) were all not attempted. The sprint has 5 days remaining (Tue Jul 28 evening through Sun Aug 2) with significant Week-2 backlog; a recovery redistribution is recorded under Recovery actions. IIT and actual roadmap hours for both weeks remain unreported.

## Orientation diagnostics

| Diagnostic | Score/result | Evidence | Action |
|---|---:|---|---|
| Python fundamentals | 2.5/3 — Strong understanding of Protocol, dataclasses, type hints; minor terminology gaps | `diagnostics/python_baseline.py`; Jul 17 verbal explanation | None |
| Async/concurrency | 2.5/3 — Solid grasp of semaphore, timeout, concurrency control; blocking vs non-blocking concept inverted in explanation | `diagnostics/python_baseline.py`; Jul 17 verbal explanation | Review asyncio.sleep vs time.sleep distinction |
| FastAPI/HTTP | 2.5/3 — Validation, `/health` test, and a clear `DuplicateTask` → HTTP 409 boundary with a passing error test; the clean boundary lives in a parallel `/v2/tasks` route rather than consolidated into `POST /tasks`, and success/error bodies are not asserted | `AI Solutions Platform/diagnostics/Sprint-00-Orientation-diagnostics/fast_api.py`; `uv run --extra dev pytest "diagnostics/Sprint-00-Orientation-diagnostics/fast_api.py" -q` → 2 passed (verified Jul 18) | Sprint 1 cleanup: consolidate the 409 mapping into `POST /tasks` and assert success/error bodies |
| SQL/Postgres | 3/3 — PK, FK, UNIQUE, CHECK, and FK index defined; transaction `COMMIT` persisted; `EXPLAIN` shows Bitmap Index Scan on `idx_orders_customer_id`; `ROLLBACK`, parameterized query, and index write-cost explained in notes | `diagnostics/Sprint-00-Orientation-diagnostics/schema.sql`, `.../test_insert.sql`, `notes/sprint-00-Orientation-notes.md`; demonstrated on Postgres 16 in Docker (container `orientation-pg`, db `diag`) — `\dt`, row selects, and `EXPLAIN` verified Jul 18 | **Closed Jul 25.** `ROLLBACK` and the Python parameterized query are both demonstrated live on PostgreSQL 16.14 (db `learner_exercise`); see the SQL evidence row under AI Solutions Platform milestones |
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
| Sprint 1 (attempt 1) | Jul 20–Aug 2 | repair | — | Gate never attempted. 1 of 10 exit-test items proven: item 10 (B1 presented, 17/24, Jul 24). Items 1, 2, 5 blocked by the orphaned Postgres adapter; items 3, 4, 6, 7, 9 never started. | Repair sprint Aug 31–Sep 13 with the same 10-item exit test |
| Restart gate | Aug 26–30 | active | — | — | — |
| Sprint 1 (repair) | Aug 31–Sep 13 | not-started | — | — | — |
| Sprint 2 | Sep 14–27 | not-started | — | — | — |
| Sprint 3 | Sep 28–Oct 11 | not-started | — | — | — |
| Sprint 4 | Oct 12–25 | not-started | — | — | — |
| Consolidation 1 | Oct 26–Nov 1 | not-started | — | — | — |
| Sprint 5 | Nov 2–15 | not-started | — | — | — |
| Sprint 6 | Nov 16–29 | not-started | — | — | — |
| Sprint 7 | Nov 30–Dec 13 | not-started | — | — | — |
| Sprint 8 | Dec 14–27 | not-started | — | — | — |
| Consolidation 2 | Dec 28–Jan 3 | not-started | — | — | — |
| Sprint 9 | Jan 4–17 | not-started | — | — | — |
| Sprint 10 | Jan 18–31 | not-started | — | — | — |
| Sprint 11 | Feb 1–14 | not-started | — | — | — |
| Sprint 12 | Feb 15–28 | not-started | — | — | — |
| Consolidation 3 | Mar 1–7 | not-started | — | — | — |
| Sprint 13 | Mar 8–21 | not-started | — | — | — |
| Sprint 14 | Mar 22–Apr 4 | not-started | — | — | — |
| Sprint 15 | Apr 5–18 | not-started | — | — | — |
| Sprint 16 | Apr 19–May 2 | not-started | — | — | — |
| Consolidation 4 | May 3–9 | not-started | — | — | — |
| Final verification | May 10–12 | not-started | — | — | — |

## Active sprint gate

The **restart gate (Aug 26-30)** is the active block. See
`sprints/Restart-Gate-2026-08-26.md` -> Exit test. It is scored **pass/partial/fail
only** and does not use the five-part `/15` sprint rubric.

Restart-gate exit test (all seven must hold to pass):

- [ ] 1. From a fresh checkout, Postgres and the API start through the documented commands only.
- [ ] 2. `alembic upgrade head` applies cleanly.
- [ ] 3. `POST /tasks` then `GET /tasks/{task_id}` returns the record, **and** the row is visible in `psql`.
- [ ] 4. The record survives a container restart.
- [ ] 5. `ruff format --check`, `ruff check`, `mypy src tests`, and `pytest -q` are all green.
- [ ] 6. With Postgres stopped, the readiness endpoint returns 503 rather than a false green.
- [ ] 7. This file contains no claim stronger than its evidence, and the four missed weeks are marked missed with no inferred hours.

Sprint 1's own gate is unchanged and is attempted at the **Sep 13** repair-sprint
close: the five-part sprint rubric (/15), pass requires at least 11/15, no zero,
and every item in the Sprint 1 Exit test proven. See
`sprints/Sprint-01-AI-Software-Foundations.md` -> Exit test. Items 1, 2 and part
of 5 are closed by the restart gate; item 10 passed Jul 24.

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
| Jul 20 | plan | plan | plan | plan | plan | plan 24-25 | unreported | FastAPI replacement verified Jul 23; Fri Jul 24 SQL and B1 complete and reviewer-verified Jul 25 (B1 17/24). The external Swift foundation has only a prior type-check from a working-tree-only/non-durable sibling artifact; Swift concurrency continues Sun. Safe async and ADR/minimal CI remain the two Sat replacements, unreported as of Jul 25. **The Jul 24 review did not run, so actual roadmap hours and Jul 22–23 IIT attendance are still unreported and are not inferred here**; the Fri Jul 31 review is now the recording point. |
| Jul 27 | ~2.5 hrs (Tue eve) | 0 | ~1 hr (Tue eve) | 0 | 0 | ~3.5 hrs (Tue Jul 28 evening) | unreported | **Jul 27–28 daytime missed**: Mon and Tue daytime blocks not attempted. **Tue Jul 28 evening executed**: 6:00–7:30 PM Postgres setup (compose, adapter, migration, readiness) + 9:30–10:30 PM DSA (Repeating/Missing Number XOR solution + LCS bonus). Recovery redistribution recorded Jul 28 under Recovery actions. Remaining Week-2 work continues Wed–Sun. Fill complete actuals at Aug 2 close. |
| Aug 3 | 0 | 0 | 0 | 0 | 0 | **0 - missed** | unreported | No recorded roadmap work. Recorded Aug 26; hours are not inferred. |
| Aug 10 | 0 | 0 | 0 | 0 | 0 | **0 - missed** | unreported | No recorded roadmap work. Recorded Aug 26; hours are not inferred. |
| Aug 17 | 0 | 0 | ~1 hr (Sat Aug 22) | 0 | 0 | **~1 hr - missed** | unreported | Only recorded activity in the window: `DSA6.swift` (0/1 knapsack, recursive + memoization) modified Aug 22 in `../iOS-Apps/DSA`, uncommitted as of Aug 26. See DSA ledger. |
| Aug 24 | plan | plan | plan | plan | plan | plan (partial week) | unreported | Restart gate opened Wed Aug 26. Wed 2:15-4:15 and 4:30-6:30 blocks had already elapsed when the gate was authored at 18:59 IST. |

Two consecutive roadmap weeks above 25 hours require a scope cut.

## AI Solutions Platform milestones

- [/] Repository and CI foundation. Skeleton exists at `AI Solutions Platform/`; `src/`, `uv.lock`, `.python-version`, pyproject configuration, formatting, lint, strict type-check, and test commands were verified Jul 22. The required architecture decision and `.github/workflows/ci.yml` are absent; the Sat Jul 25 replacement block was not executed. Separately, `async_boundary_lab.py` (staged, not committed) demonstrates bounded/unbounded fan-out and blocking boundary as Sprint 1 async evidence; its companion notes file is empty. ADR and CI remain scheduled for Thu Jul 30 and Fri Jul 31 respectively. Milestone remains partial.
- [x] Sprint 1 domain-boundary exercise checkpoint. Frozen domain record, domain duplicate exception, repository `Protocol`, injected application service, in-memory adapter, and create/duplicate tests were verified Jul 22. Targeted and full pytest each passed 2 tests; Ruff format/lint and strict mypy passed; the domain/application forbidden-SDK scan returned zero matches. Swapnil's independent adapter-swap defense was reviewed Jul 22 at 3/4 and accepted with corrections: add `PostgresTaskRepository` rather than rewrite the memory adapter, switch the composition/provider, and translate the exact unique-constraint failure inside the Postgres adapter to `DuplicateTaskTitle`. This closes the local exercise checkpoint, not the Aug 2 sprint gate.
- [/] FastAPI/Postgres vertical slice. The in-memory HTTP boundary is verified Jul 23: app-owned repository composition, create/read, health/readiness placeholder, stable 404/409 bodies, default 422 validation, generated OpenAPI, and app-isolation evidence. Locked Ruff format/lint and strict mypy passed; full pytest passed 9 tests. **Tue Jul 28 evening (6:00–7:30 PM):** Postgres 16 container via `docker compose up -d` (compose.yaml with health check and named volume); `PostgresTaskRepository` implements `TaskRepository` protocol with `IntegrityError` → `DuplicateTaskTitle` translation; async session provider via `database.py`; first Alembic migration (`0001_create_tasks_table.py`) applied against live Postgres; `/healthz/ready` endpoint returns 200 when DB connected, 503 when unavailable. Dependencies added: `alembic>=1.18.5`, `asyncpg>=0.31.0`, `sqlalchemy[asyncio]>=2.0`. Learning notes: `notes/sprint-01-AI-Software-Foundations-notes-04-postgreSQL-connection-understanding.md` (comprehensive AsyncEngine/Session/Pool/Alembic lifecycle understanding). Clean-database integration tests remain scheduled for Wed Jul 29. **Correction recorded Aug 26, 2026 (verified, not user-reported):** the sentence above overstates what shipped. `PostgresTaskRepository` is referenced exactly once in the repository - its own class definition at `persistence/postgres_tasks.py:10`. Nothing imports it; `api/app.py` composes `InMemoryTaskRepository()` as the only reachable adapter, so the running API persists nothing and exit-test items 1-2 were never achievable from this commit. `/healthz/ready` exists but has zero test coverage, while `/ready` in `api/routes/tasks.py` returns ready unconditionally and `tests/api/test_tasks.py` asserts that placeholder behavior. The commit also landed without running the project's own gates: `ruff check src tests` reports 8 errors, `ruff format --check` 4 files, and `mypy src tests` 1 error, all in files introduced by `53f549a`. The migration file itself is real, applied, and correct. Repair is scheduled in the restart gate (Aug 28-30). This milestone stays **partial**.
- [x] Sprint 1 relational-modelling and SQL learning evidence (Fri Jul 24, reviewer-verified Sat Jul 25). Artifacts: `AI Solutions Platform/diagnostics/Sprint-01-AI-Software-Foundations/{sql_schema.sql, rollback_proof.sql, parameterized_query_proof.py, query_plan_observation.sql, sql_evidence_package.md}`; teaching record in `notes/sprint-01-AI-Software-Foundations-notes-01-sql-postgresql-deep-learning.md` with a dated reviewer appendix holding the executed transcripts. Verified on PostgreSQL **16.14** (container `orientation-pg`, db `learner_exercise`) via `docker exec -i orientation-pg psql -U postgres -d learner_exercise -v ON_ERROR_STOP=1 < <file>`: schema applies clean (3 tables, 8 indexes — **6 automatic + 2 manual**, correcting the evidence package's "5 + 3"); rollback proof returns `before_count 0 → INSERT 0 1 → visible in transaction → ROLLBACK → 0 rows → after_count 0`; the parameterized-query script inserts, fetches, matches 0 rows for a `'; DROP TABLE task; --` payload, leaves `to_regclass('task')` intact, and rolls back clean. Three claim corrections are recorded rather than silently fixed: the real plan is a forward `Index Scan using idx_task_status_recent`, not `Index Scan Backward` (a DESC index satisfies `ORDER BY … DESC` on a forward read); the printed costs and `rows=2` estimate do not match the server (`0.14..8.16`, Seq Scan `0.00..11.62`, estimate `rows=1` because the table was never `ANALYZE`d); and at 5 rows the un-indexed plan was **faster** (0.025 ms vs 0.051 ms), so index value is unproven at fixture scale. Known gap carried to Jul 27: `psycopg` is not a dependency of `AI Solutions Platform/pyproject.toml`, so the proof script runs only in an ephemeral environment, and its `except psycopg.OperationalError` branch prints "Script logic is verified" for a run that never connected. This is learning evidence for the Jul 27 adapter, not the persisted vertical slice.
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
- Backend complete: **1/6** (B1)
- Total complete: **2/34**
- Two most recent scores: **17/24 (B1, Jul 24)**, 14/24 (Orientation, Jul 17)
- Lowest current dimension: no dimension below 2/3 in the most recent case. Both orientation repair targets moved — Estimates and budgets **1/3 → 3/3**, Failure handling **1/3 → 2/3**. Weakest remaining: operational alerting (thresholds, SLO burn-rate, paging path) and document communication structure.

Completed case IDs:

- AI: Orientation diagnostic (Enterprise AI Assistant with RAG)
- iOS: —
- Backend: B1 — Reliable webhook ingestion (Jul 24)

### B1 — Reliable webhook ingestion (Fri Jul 24, scored Jul 25)

- Rubric: `05-System-Design-Track.md` → **Scoring rubric**, eight dimensions 0–3, **/24**. Phase-1 expectation is ≥12/24 with no zero in requirements or critical flow; the 20/24 bar belongs to the Phase-4 Mar-2027 mock and is not applied here.
- **Reviewer score: 17/24** — Requirements 2, Estimates and budgets 3, Contracts and data model 2, Architecture and critical flows 2, Domain depth (backend) 2, Failure handling and ops 2, Security/privacy/cost 2, Communication and trade-offs 2. Clears the Phase-1 expectation with no zero.
- **Self-assessed 24/24** is recorded in the artifact and is **not** the ledger outcome. Rubric level 3 requires adapting under challenge; this was an unchallenged solo written design, and the track file states the score is diagnostic and must never be inflated.
- Evidence: `notes/sprint-01-AI-Software-Foundations-notes-02-b1-reliable-webhook-system-design-deep-teaching.md` (design + dated evidence note + critical-flow trace + self-rubric, with a dated reviewer-scoring appendix) and the hand-drawn architecture at `notes/WhatsApp Image 2026-07-24 at 23.53.37.jpeg` (provider → HMAC gateway → durable accept + dedup → async Postgres, partition by day range, Redis-dedup substitution, the 500 → 5,000 → 50,000 RPS ladder with single-Postgres rejected, Kafka overflow, and S3 offload above 8 KB).
- Quantified where orientation was weakest: 500 avg / 5,000 peak RPS, 2 KB avg / 64 KB max payload, 43.2 M events/day, 82.4 GB/day raw → 123.6 GB/day with overhead → 3.708 TB over 30-day active retention, 2.225 TB over 90-day cold retention, ingest p95 <20 ms / p99 <50 ms, end-to-end p95 <500 ms / p99 <2 s, 99.99% availability, RTO <15 min, RPO 0, full-jitter backoff (base 2 s, cap 3600 s, 5 attempts then dead-letter), and a per-component monthly cost table. Arithmetic independently rechecked and correct.
- Recorded defects, not repaired here: the worker-lease sweeper filters on `locked_until`, which `raw_webhook_event` never declares; the critical-flow trace annotates `[00.019 ms]` as "19ms" and has a worker polling 26 µs after acknowledgement; seven metrics are defined with no thresholds, burn-rate alert, or paging path; the cost table prices AWS while the platform target is GCP; and the document carries an off-topic pasted chat block plus a duplicated summary section.
- Scope respected: design only. No routes, middleware, tables, queues, workers, retry code, or replay tooling were implemented.

Next scheduled case: **I1 — Offline-first adaptive feed** (Sprint 1, Week 2, Fri Jul 31).

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
- **Overdue as of Aug 26:** Maximum Product Subarray (due ~Aug 3, 23 days overdue)
  and Repeating and Missing Number (due ~Aug 11, 15 days overdue). Both are
  scheduled into the restart gate's Saturday Aug 29 replacement block. Repetition
  is repair, not new content.
- **Sat Aug 22 session — recorded Aug 26, partially verified.** `../iOS-Apps/DSA/DSA6.swift`
  was modified Aug 22 with +44/-19 lines implementing 0/1 knapsack (recursive, then
  memoized). Verified by file mtime and `git diff`; **uncommitted** as of Aug 26, so
  this is working-tree-only evidence until the restart gate commits it and records
  the SHA. No timing, accepted run, or mistake tag was supplied, so none is claimed.
  This is the only recorded activity in the Jul 29 - Aug 25 window.
- Jul 21 Sprint 1 submission review (verified Jul 22): `../iOS-Apps/DSA/sprint-01-AI-Software-Foundations.swift` is an untracked Longest Increasing Subsequence solution, not an arrays/hash-map revision. It type-checks with one trailing-closure warning; the active `firstIndex` search makes it O(n^2) time and O(n) space. No accepted run, timing, due-item provenance, mistake reflection, or next repetition date was supplied, so it is not counted above.
- Recovery queue: **Repeating and Missing Number** — **SOLVED Tue Jul 28, 9:30–10:30 PM**. Implementation: XOR-based O(n) time / O(1) extra space solution without modifying input. Algorithm: (1) XOR all array elements with 1...n to get `repeating XOR missing`; (2) find rightmost set bit to partition numbers; (3) XOR each partition separately with both array and 1...n; (4) verify which result is in the array (repeating) vs missing. Artifact: `../iOS-Apps/DSA/sprint-01-AI-Software-Foundations.swift` function `findMissingAndRepeatingValue`. **Prior-mistake note:** The Jul 21 LIS submission was a pattern-selection mismatch — chose DP subsequence instead of arrays/hash-map; the mental process jumped to "interesting problem" rather than matching the recovery target. **Bonus:** Also solved **Longest Common Subsequence** (DP, O(m×n) time/space) in same session. Next repetition: ~Aug 11 (14-day interval). The timed two-pointer solve is rescheduled to Wed Jul 29, 5:00–6:00 mixed set.

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
| Jul 21 | None - in-sprint day slip, not a gate | Sprint 1 Monday Jul 20 blocks not completed | Preserve verified domain code. Use Sat Jul 25, 4:30–6:00 for the missing ADR/minimal CI and Mon Jul 27, 9:30–10:30 for Repeating and Missing Number. The displaced safe-async and Swift work use Sat Jul 25 and Sun Jul 26; the unseen arrays/hash problem is absorbed by the Jul 29 mixed set. | Review Jul 24; execution Jul 25–29 | **Partial, verified through Jul 23:** domain code and the 3/4 adapter defense remain accepted. The external Swift artifact at `../iOS-Apps/iOSToAIJourney/Sprint-01-AI-Software-Foundations/TaskListFeature.swift` has only the prior `xcrun swiftc -typecheck TaskListFeature.swift` → exit 0 evidence. The final reviewer confirmed that its implementation is unstaged in the sibling repository and its staged blob is empty, so the evidence is **working-tree-only/non-durable** and proves only the guided state/protocol/fake foundation. Observable model, SwiftUI view, cancellation transition, actor integration, and tests remain scheduled. Repeating and Missing Number is unsolved, its prior-mistake note is missing, and ADR/CI remain incomplete. Sat Jul 25 status unreported as of this update. |
| Jul 22 | None - in-sprint day slip, not a gate | Wednesday FastAPI and DSA blocks were not completed before their windows elapsed | Thu Jul 23 FastAPI replaces the missed flow and minimum contract evidence. Remaining async, Postgres, transaction, and lifecycle depth stays beside its scheduled implementation. Recover DSA through Sun Jul 26 review, Tue Jul 28 timed solve, and Jul 29 repetition/mixed set. | Jul 23–30 | **FastAPI replacement complete and verified Jul 23:** app-owned injection plus 201/200/404/409/422, health/readiness, OpenAPI, and isolation contracts; Ruff format/lint, strict mypy, and 9 tests pass. DSA recovery remains planned. IIT attendance and actual hours remain unreported; Week-2 sequence and the Aug 2 gate are unchanged. |
| Jul 25 | None - in-sprint block slip, not a gate | The Fri Jul 24 B1 block overran its 9:11 PM stop (B1 notes last modified Jul 25, 02:16 IST), consuming the 9:11–10:11 PM weekly-review window | Fold the weekly review's two required outputs - clean-checkout reproduction of the in-memory vertical slice with format/lint/strict-type/test results, and the Week-1 gap list - into the **existing** Fri Jul 31, 2:15–7:30 gate-rehearsal block, which already owns rehearsal. Do not create a third Week-1 replacement block; Week 1's two optional replacements are both already allocated to Sat Jul 25. Actual roadmap hours and Jul 22-23 IIT attendance stay unreported until supplied. | Fri Jul 31 | **Open.** SQL and B1 evidence for Jul 24 is complete and reviewer-verified (B1 17/24); the review itself is marked missed rather than restaged. A Jul 25 working-tree run of `uv run --extra dev pytest -q` returned `9 passed in 0.21s`, matching the Jul 23 record - but that is the existing working tree, **not** the clean-checkout reproduction the review requires, so that item stays outstanding. No hours were inferred. |
| Jul 28 | None — multi-day block slip, not a gate | Sat Jul 25 safe async partial (lab created, notes empty, timeout/cancellation tests missing; ADR/CI not started); Sun Jul 26 entirely missed (Swift concurrency + DSA two-pointer); Mon Jul 27 entirely missed (Postgres adapter, persisted vertical slice, Repeating and Missing Number); Tue Jul 28 daytime blocks missed (transactions/idempotency, Apple architecture) | **Recovery redistribution (Jul 28 evening through Aug 2):** Tue evening: Postgres compose + adapter skeleton (6:00–7:30) + DSA Repeating and Missing Number (9:30–10:30). Wed: Postgres adapter completion + readiness (2:15–4:15), two-pointer repetition (4:30–5:00), transaction/idempotency start (5:00–6:00), IIT (6:00–8:00). Thu: signed webhooks (2:15–4:15), contract/lifecycle/failure tests + ADR (4:30–6:00), IIT (6:00–8:00). Fri: Docker + CI with Postgres (2:15–4:15), gate rehearsal (4:30–6:30), weekly review + evidence close (6:30–7:30). Sun Aug 2: Swift concurrency test (1 hr) + clean-checkout exit gate run + score + PROGRESS.md close (1 hr). **Deferred to Consolidation 1:** Apple SwiftUI observation/state architecture (only the Swift concurrency/cancellation test is retained for exit gate item 9). **Deferred within sprint:** I1 system design — use B1 (17/24, already scored) for exit test item 10. Drop/defer per sprint guide: UI polish, Docker optimization, advanced SQLAlchemy, extra endpoints. Do not drop: Postgres transaction/constraint, signed webhook duplicate behavior, cancellation/timeout test, CI, Apple concurrency test, DSA/design continuity. | Aug 2 | **Partial — Tue Jul 28 evening complete.** Postgres compose + adapter skeleton + migration + readiness endpoint verified. DSA Repeating and Missing Number solved (XOR/O(n)/O(1)) + LCS bonus. Prior-mistake note recorded (pattern-selection mismatch from Jul 21 LIS). Wed Jul 29 onwards continues per plan. |
| Aug 26 | None — multi-week pause, not a failed gate | Execution stopped after the Tue Jul 28 evening session. Four consecutive weeks (Jul 27, Aug 3, Aug 10, Aug 17) recorded no roadmap work, triggering `04-Weekly-Operating-System.md`: "two consecutive weeks below the minimum-viable plan trigger a roadmap pause and a smaller restart gate." Sprint 1 was never closed or scored; 1 of 10 exit-test items proven. Separately, commit `53f549a` shipped an unreachable Postgres adapter and broke the project's own lint/format/type gates, and corrupted `PROGRESS.md` with compressed tool output. | **Schedule revision approved Aug 26 (roadmap change control, user-approved).** Capacity confirmed at the unchanged 20–25 h/week. Every block from Sprint 1 onward shifts **+6 weeks**; readiness target moves Mar 31 → **May 12, 2027**. No outcome, exit gate, prerequisite, weekly budget, or portfolio boundary weakened — dates only. A new **restart gate (Aug 26–30)** is inserted: truthful ledger close, toolchain recheck, stack-snapshot refresh, Apple evidence made durable in a real repository, and repair of `53f549a`. Sprint 1 receives a full repair sprint **Aug 31–Sep 13** running its original unchanged 10-item exit test. The two Jul 28 deferrals — system-design **I1** and the **SwiftUI observation/state architecture** — are **restored**, since the time pressure that justified them was removed by the revision rather than by a scope change. `PROGRESS.md` reconstructed from `79f9f93` with all Jul 28 additions re-applied. | Restart gate scored Aug 30; Sprint 1 gate attempted Sep 13 | **Open.** Restart gate active. Nothing in this row is user-reported except the capacity confirmation; the code and ledger findings were directly verified Aug 26. |

## Application readiness

- Networking starts: December 2026. **Unchanged by the Aug 26 revision.**
- Selective applications start: January 2027. **Unchanged by the Aug 26 revision.**
- **Recorded trade, Aug 26, 2026:** these two dates are market-timed, not
  competency-timed, so they did **not** move with the +6 week shift. The
  consequence is explicit: Sprint 12 (production beta) now closes Feb 28 instead
  of Jan 17, so January applications would carry Phase-2 evidence (agents, voice)
  with Phase 3 (security, GCP deployment, reliability) still in flight. This is
  recorded rather than resolved. Decide at **Consolidation 2 (Dec 28–Jan 3)** from
  actual portfolio evidence, not from a prediction made in August.
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

> Outstanding as of Aug 26, 2026: **no weekly review entry has ever been
> written.** The Week of 2026-07-20 entry was displaced when the Fri Jul 24
> 9:11–10:11 PM window was consumed by the B1 block overrun, and the Fri Jul 31
> replacement block never ran because execution stopped Jul 28. The weeks of
> 2026-07-27, 2026-08-03, 2026-08-10, and 2026-08-17 have no entry either; they
> are recorded as missed under **Weekly hours** with no inferred hours.
>
> No entry is drafted here because the underlying facts were not observed, and
> `skill.md` forbids fabricating hours or evidence. The Week of 2026-07-20 entry
> is produced in the restart gate's Thu Aug 27 block, and the current week's
> entry in the Fri Aug 28 6:30–7:30 PM review. Later weeks may be recorded as a
> single "missed, not observed" entry rather than reconstructed.

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
