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
- **Restart-gate progress, verified Fri Aug 28, 16:37 IST (reviewer-run, not
  user-reported):** exit-test item 5 is **closed** — `ruff format --check`,
  `ruff check`, `mypy src tests`, and `pytest -q` all pass, and the seven `ruff`
  findings introduced by `53f549a` are gone. `AppleAILab` is now a real
  repository with commit `85b14c1`, ending five weeks of working-tree-only Swift
  evidence. **Two things did not go to plan.** Thursday's blocks executed on
  Friday afternoon, consuming Friday's own 2:15–4:15 toolchain-recheck window;
  and the unaided re-test of the B1 webhook design **failed** — it came back as a
  WebSocket (see System-design ledger). **The backend repair is still
  uncommitted** in the working tree, which is the identical non-durability that
  cost the Swift artifact five weeks. Exit-test items 1, 2, 3, 4 and 6 remain
  unproven and every one of them depends on wiring `PostgresTaskRepository`.
- **Superseded the same evening, 19:07 IST (reviewer-verified).** `PostgresTaskRepository` is wired and the persisted vertical slice works: create → read → row visible in `psql`, surviving a container restart, with 409/404 exercised against the real unique constraint. **Restart-gate items 3, 4, 5 and 6 are closed — the gate moved from 1/7 to 4/7 in one evening.** The line that had been true since July — "the running API persists nothing" — is no longer true. Remaining: item 1 (clean-checkout reproduction, Sunday), item 2 (`alembic upgrade head` proven from a fresh checkout; it is currently at `0001 (head)` on an already-migrated database), and item 7 (ledger truth, scored Aug 30). Item 6's evidence holds but the placeholder `/ready` still returns a false green during an outage and is deleted Saturday.
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
- [x] 3. `POST /tasks` then `GET /tasks/{task_id}` returns the record, **and** the row is visible in `psql`. **Closed Fri Aug 28, 19:06 IST — reviewer-verified against the running service, not user-reported.** `uvicorn` on port 8111 against container `task_postgres` (healthy, migration at `0001 (head)`): `POST /tasks {"title":"psql-proof-aug28"}` → **201** with `task_id` `086d56ee-85fe-4155-bd22-6b484338efef`; `docker exec task_postgres psql -U postgres -d task_db -c 'select task_id, title, created_at from tasks;'` shows that exact row; `GET /tasks/{id}` → **200** with matching payload. Two error contracts were exercised against the **real** constraint, not a fake: a second `POST` of the same title → **409** `duplicate_task_title` (so the `IntegrityError` → `DuplicateTaskTitle` translation works against live Postgres), and an unknown UUID → **404** `task_not_found`. Swapnil had independently proven the same path first — rows `proof`, `Unique task`, and `restart-gate-done` are stamped 18:51–19:04 IST, before he submitted the work.
- [x] 4. The record survives a container restart. **Closed Fri Aug 28, 19:07 IST — reviewer-verified.** `docker stop task_postgres`, then `docker start` and wait for `healthy`; `GET /tasks/086d56ee-85fe-4155-bd22-6b484338efef` → **200** with the identical `created_at`. The first request after restart succeeded — the SQLAlchemy pool recovered without a stale-connection failure, which was not assumed and was checked twice.
- [x] 5. `ruff format --check`, `ruff check`, `mypy src tests`, and `pytest -q` are all green. **Closed Fri Aug 28, 16:37 IST — reviewer-verified, not user-reported.** The four commands were run in sequence against the working tree: `29 files already formatted`, `All checks passed!`, `Success: no issues found in 29 source files`, `9 passed in 0.34s`. The `B008`, `B904`, `RUF010`, two `I001`, `UP035`, and `F401` findings from `53f549a` are all cleared, and `health.py` now uses the `Annotated[AsyncSession, Depends(get_db_session)]` form rather than a call in an argument default. **Caveat carried:** the repair exists only as uncommitted working-tree modifications to four files, so this evidence is non-durable. Item 5 is re-run from a clean checkout at the Aug 30 gate.
- [x] 6. With Postgres stopped, the readiness endpoint returns 503 rather than a false green. **Closed Fri Aug 28, 19:07 IST — reviewer-verified.** With `task_postgres` stopped, `GET /healthz/ready` → **503** `{"detail":"Database unready"}`. **The contradiction is now demonstrated rather than argued:** in the same outage `GET /ready` returned **200** `{"status":"ready"}` — a live false green, with `tests/api/test_tasks.py` still asserting that behaviour. Deleting the placeholder and its test is Saturday's Replacement block A; item 6 is scored on `/healthz/ready`, which is correct, but the gate is not closed while the lying endpoint is still routable.
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

**Revised Aug 28, 2026 (approved):** the weekday start moved 2:15 PM → 3:30 PM, so the required week is now **~23 hours**, down from 24.5-25. Still inside the 20-25 band. The 1.5-hour reduction was assigned entirely to **Apple AI (5.5-6 h → 4 h)**; AI core/platform (12 h), DSA (4 h), design (2 h) and review (1 h) are all held. See `04-Weekly-Operating-System.md` and the Aug 28 schedule row under Recovery actions.

| Week of | AI/platform | Apple | DSA | Design | Review/FDE | Roadmap total | IIT | Note |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Jul 13 | - | - | - | - | - | - | - | Orientation |
| Jul 20 | plan | plan | plan | plan | plan | plan 24-25 | unreported | FastAPI replacement verified Jul 23; Fri Jul 24 SQL and B1 complete and reviewer-verified Jul 25 (B1 17/24). The external Swift foundation has only a prior type-check from a working-tree-only/non-durable sibling artifact; Swift concurrency continues Sun. Safe async and ADR/minimal CI remain the two Sat replacements, unreported as of Jul 25. **The Jul 24 review did not run, so actual roadmap hours and Jul 22–23 IIT attendance are still unreported and are not inferred here**; the Fri Jul 31 review is now the recording point. |
| Jul 27 | ~2.5 hrs (Tue eve) | 0 | ~1 hr (Tue eve) | 0 | 0 | ~3.5 hrs (Tue Jul 28 evening) | unreported | **Jul 27–28 daytime missed**: Mon and Tue daytime blocks not attempted. **Tue Jul 28 evening executed**: 6:00–7:30 PM Postgres setup (compose, adapter, migration, readiness) + 9:30–10:30 PM DSA (Repeating/Missing Number XOR solution + LCS bonus). Recovery redistribution recorded Jul 28 under Recovery actions. Remaining Week-2 work continues Wed–Sun. Fill complete actuals at Aug 2 close. |
| Aug 3 | 0 | 0 | 0 | 0 | 0 | **0 - missed** | unreported | No recorded roadmap work. Recorded Aug 26; hours are not inferred. |
| Aug 10 | 0 | 0 | 0 | 0 | 0 | **0 - missed** | unreported | No recorded roadmap work. Recorded Aug 26; hours are not inferred. |
| Aug 17 | 0 | 0 | ~1 hr (Sat Aug 22) | 0 | 0 | **~1 hr - missed** | unreported | Only recorded activity in the window: `DSA6.swift` (0/1 knapsack, recursive only) modified Aug 22 in `../iOS-Apps/DSA`; committed Aug 26 as `82b2282`. See DSA ledger. |
| Aug 24 | not reported | not reported | 0 | 0 | not reported | **not reported** | unreported | Restart gate opened Wed Aug 26; the Wed 2:15-4:15 and 4:30-6:30 blocks had already elapsed when the gate was authored at 18:59 IST. **Thu Aug 27: nothing reported.** **Fri Aug 28: Thursday's blocks executed a day late**, in the afternoon — backend quality gates repaired and verified green at 16:37, `AppleAILab` created and committed (`85b14c1`, 16:30:59), unaided-recall re-test completed with one failure recorded (B1). Friday's own 2:15-4:15 toolchain-recheck block elapsed unexecuted and moves once to Sat Aug 29. **Actual hours are not reported and are not inferred here** — fill at the Aug 30 gate close. **Fri Aug 28 evening block executed and verified:** `PostgresTaskRepository` wired, persisted vertical slice proven in `psql`, restart survival and readiness-under-outage confirmed. Gate went 1/7 → 4/7. The block ran past its 6:30 PM stop — the review/B1 hour was displaced and moves to Saturday. |

Two consecutive roadmap weeks above 25 hours require a scope cut.

## AI Solutions Platform milestones

- [/] Repository and CI foundation. Skeleton exists at `AI Solutions Platform/`; `src/`, `uv.lock`, `.python-version`, pyproject configuration, formatting, lint, strict type-check, and test commands were verified Jul 22. The required architecture decision and `.github/workflows/ci.yml` are absent; the Sat Jul 25 replacement block was not executed. Separately, `async_boundary_lab.py` (staged, not committed) demonstrates bounded/unbounded fan-out and blocking boundary as Sprint 1 async evidence; its companion notes file is empty. ADR and CI remain scheduled for Thu Jul 30 and Fri Jul 31 respectively. Milestone remains partial.
- [x] Sprint 1 domain-boundary exercise checkpoint. Frozen domain record, domain duplicate exception, repository `Protocol`, injected application service, in-memory adapter, and create/duplicate tests were verified Jul 22. Targeted and full pytest each passed 2 tests; Ruff format/lint and strict mypy passed; the domain/application forbidden-SDK scan returned zero matches. Swapnil's independent adapter-swap defense was reviewed Jul 22 at 3/4 and accepted with corrections: add `PostgresTaskRepository` rather than rewrite the memory adapter, switch the composition/provider, and translate the exact unique-constraint failure inside the Postgres adapter to `DuplicateTaskTitle`. This closes the local exercise checkpoint, not the Aug 2 sprint gate.
- [/] FastAPI/Postgres vertical slice. The in-memory HTTP boundary is verified Jul 23: app-owned repository composition, create/read, health/readiness placeholder, stable 404/409 bodies, default 422 validation, generated OpenAPI, and app-isolation evidence. Locked Ruff format/lint and strict mypy passed; full pytest passed 9 tests. **Tue Jul 28 evening (6:00–7:30 PM):** Postgres 16 container via `docker compose up -d` (compose.yaml with health check and named volume); `PostgresTaskRepository` implements `TaskRepository` protocol with `IntegrityError` → `DuplicateTaskTitle` translation; async session provider via `database.py`; first Alembic migration (`0001_create_tasks_table.py`) applied against live Postgres; `/healthz/ready` endpoint returns 200 when DB connected, 503 when unavailable. Dependencies added: `alembic>=1.18.5`, `asyncpg>=0.31.0`, `sqlalchemy[asyncio]>=2.0`. Learning notes: `notes/sprint-01-AI-Software-Foundations-notes-04-postgreSQL-connection-understanding.md` (comprehensive AsyncEngine/Session/Pool/Alembic lifecycle understanding). Clean-database integration tests remain scheduled for Wed Jul 29. **Correction recorded Aug 26, 2026 (verified, not user-reported):** the sentence above overstates what shipped. `PostgresTaskRepository` is referenced exactly once in the repository - its own class definition at `persistence/postgres_tasks.py:10`. Nothing imports it; `api/app.py` composes `InMemoryTaskRepository()` as the only reachable adapter, so the running API persists nothing and exit-test items 1-2 were never achievable from this commit. `/healthz/ready` exists but has zero test coverage, while `/ready` in `api/routes/tasks.py` returns ready unconditionally and `tests/api/test_tasks.py` asserts that placeholder behavior. The commit also landed without running the project's own gates: `ruff check src tests` reports 8 errors, `ruff format --check` 4 files, and `mypy src tests` 1 error, all in files introduced by `53f549a`. The migration file itself is real, applied, and correct. Repair is scheduled in the restart gate (Aug 28-30). This milestone stays **partial**. **Closed Fri Aug 28, 2026, 19:06 IST — reviewer-verified end to end.** `PostgresTaskRepository` is reachable and the slice persists. Swapnil moved the composition point out of app startup and into the per-request dependency — `api/app.py` now stores whatever repository it is given (`None` in production), and `get_task_repository(request, session: DbSession)` returns the injected repository when one exists and otherwise constructs `PostgresTaskRepository(session)` from the per-request session. This is the correct resolution of the lifetime mismatch (app-lifetime fake vs request-lifetime adapter) and it is what the 3/4 adapter-swap review on Jul 22 asked for. Both constraints held: `InMemoryTaskRepository` still serves all 9 tests, and no SQLAlchemy type entered `domain/` or `application/`. Evidence under **Active sprint gate** items 3, 4, 6. **Three findings recorded, none blocking, none repaired here.** (a) *Implicit default:* `create_app()` with no argument now means "use Postgres", inverting its previous meaning; the only thing preventing a future no-argument test from hitting a real database is the `or InMemoryTaskRepository()` added to the test helper. (b) *The fake path still builds a session:* `get_task_repository` declares `session: DbSession` unconditionally, so FastAPI resolves `get_db_session` on every request including in-memory ones; it passes only because a SQLAlchemy session opens no connection until first use, which couples the test path to database configuration for no benefit. (c) *The adapter owns the transaction:* `PostgresTaskRepository.add` calls `commit()` itself, so a future service operation needing two writes in one transaction — create task **plus** outbox event, which is the Sprint 1 webhook pattern — cannot get atomicity. **The real gap is coverage:** all 9 tests still exercise only the in-memory adapter, so everything above was proven by hand and nothing protects it from regression. Integration tests are Sunday's block. **Partial repair verified Fri Aug 28, 16:37 IST:** the gate failures are fixed — all four commands green, 9 tests passing — and the two findings that were real design feedback rather than noise were fixed correctly: `B008` by hoisting the dependency into an `Annotated` type alias (the FastAPI-native form, not the linter's suggested module-level singleton, which would break FastAPI's signature inspection), and `B904` by chaining with `from exc` **and** removing the interpolated exception text from the HTTP response body, which had been leaking the database host, port, and name from an unauthenticated endpoint. The adapter itself is still unreachable and the fix is still uncommitted, so the milestone remains **partial**.
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

**Durable evidence recorded Fri Aug 28, 2026 (reviewer-verified).** `AppleAILab` is a real Git
repository at `../iOS-Apps/AppleAILab`, commit **`85b14c1`** — "Apple AI Lab: task list state,
protocol, and fake service foundation", 2026-08-28 16:30:59 +0530 — holding `TaskListFeature.swift`
(77 lines) and a 6-line `.gitignore`; working tree clean; `xcrun swiftc -typecheck
TaskListFeature.swift` exits 0. This closes the restart gate's "AppleAILab exists as a repository
with a real commit" required output and supersedes the working-tree-only/non-durable status the
artifact had carried since Jul 23. **No milestone above is ticked by it.** The file is a guided
foundation — task model, state enum, repository protocol, fake service — with no SwiftUI view, no
observable model, no cancellation transition, and no tests. Those remain scheduled in the Sprint 1
repair sprint, where the SwiftUI observation/state architecture was restored on Aug 26.

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
- **Unaided recall re-test, Fri Aug 28, 2026 — failed. The 17/24 score is unchanged; this records retention, not design quality.** Asked to defend B1 out loud without notes, Swapnil described a **WebSocket**: a persistent "live listener" attached to the server, an opening handshake authenticating both parties, continuous two-way conversation (Gemini Live API given as the example), then TCP vs UDP vs QUIC ordering guarantees. None of that is webhook ingestion and none of it appears in B1. A webhook is an ordinary one-shot HTTP `POST` that the provider sends to your URL; the connection closes with the response like any other request. **Zero of the six mechanisms actually scored came back:** per-request HMAC signature verification, durable-accept-then-process-async, deduplication under at-least-once delivery, full-jitter retry with dead-letter, day-range partitioning, and the 500 → 5,000 → 50,000 RPS ladder. Classification per `08-Assessment-and-Recovery.md`: **conceptual gap.** Repair scheduled Fri Aug 28, 6:50–7:10 PM; see Recovery actions. **Prerequisite consequence — satisfied Aug 28, ~19:35 IST.** The webhook/WebSocket distinction now holds under a closed-notes answer, so I1 is no longer blocked. **Carried into the repair sprint's design hours, as a 10-minute opener rather than a block:** the two mechanisms that did not return — *durable accept then process asynchronously* as the answer to a slow consumer (retry was misapplied there), and *dead-lettering* as the answer to a permanently broken one. Both are specific and small; neither is a prerequisite for I1.
- **Test conditions, recorded so this result is not over-read (Aug 28):** the re-test was not uniform. The six competency items were re-tested *after* a same-session revision pass in Antigravity, so recall there was primed even where the unaided answer was written first. B1 had **no revision pass at all** and was the oldest material in the set — five weeks cold. It was therefore the harshest item in an uneven test, and the gap between it and the other six overstates the difference between them.

**Recorded objection, Swapnil, Aug 28, 2026 — partly upheld.** Swapnil's position: the 17/24 may itself be too generous; what he produced on Aug 28 *is* his real level; and expecting a defensible webhook design this early is unfair, since the roadmap is barely started.

**Upheld:** the two numbers measure different things and must not be read against each other. 17/24 scored a **written artifact** — one that was independently arithmetic-checked and found correct. It never claimed to predict unaided recall five weeks later, and this ledger already recorded why: the design was *unchallenged and solo*, which is exactly why the self-assessed 24/24 was rejected. A cold-recall failure is therefore not evidence that the artifact score was inflated. The expectation point is also correct and already recorded: the Phase-1 bar is **≥12/24 with no zero**; 17/24 clears it; the 20/24 bar belongs to the Phase-4 March-2027 mock. One correction of fact: B1 was not pre-Sprint-1 — it was a Sprint 1 week-1 deliverable, Jul 24.

**Not upheld:** the score is not changed. Rewriting a historical score downward from later recall is the same error as inflating it upward — both replace what was measured with what someone felt afterwards. 17/24 stands as the artifact score, with the Aug 28 recall failure recorded beside it as a separate fact. Both are true; neither overwrites the other.

**The finding this actually exposes — a roadmap gap, not a personal one.** The DSA track has explicit spaced repetition: a problem ledger, dated repetition intervals, and a rule that a repetition is solved from memory and re-scheduled. **The system-design track has no equivalent.** A case is designed once, scored once, and never revisited. Under that design, decay was the expected outcome, not a surprising one. Adding repetition to the design track is a **roadmap change** requiring impact analysis and approval; it is recorded here as an open proposal, to be decided before the design hours in the Sprint 1 repair sprint. **Not implemented.**

Next scheduled case: **I1 — Offline-first adaptive feed** (Sprint 1, Week 2, Fri Jul 31).

## DSA ledger summary

### Problem sources — registered Aug 26, 2026

Before this date the roadmap named **no** DSA problem source; selection was ad hoc,
which produced the recorded Jul 21 pattern-selection mismatch. Full selection rules
and the four-phase sequence are in `06-DSA-Track.md` -> *Problem sources* and
*Sprint syllabus*.

| Source | Role |
|---|---|
| [Striver SDE Sheet](https://takeuforward.org/dsa/strivers-sde-sheet-top-coding-interview-problems) | Pattern spine; authoritative for what is done and due (Phases A-B) |
| [Taro Top 75](https://www.jointaro.com/interviews/taro-75/) | Timed/unseen practice, minus Striver overlap (Phase B, Tuesdays) |
| [Taro - Google](https://www.jointaro.com/interviews/companies/google/) | Company-tagged, weighted from January (Phase B) |

Per-problem notes (Notion, Swift solutions + recognition signals):
[DSA](https://app.notion.com/p/vibedin/DSA-2c39b3ea0f2983edb48b81b3b2062918) |
[Taro Google](https://app.notion.com/p/vibedin/Taro-LeetCode-Google-Interview-Questions-2669b3ea0f2980a69bdac1ca6df2f4b3) |
[Taro Top 75](https://app.notion.com/p/vibedin/Taro-Top-75-LeetCode-Question-2669b3ea0f29804ca16ff9725ad087ad)

### Striver baseline - read Aug 26, 2026 from the live dashboard

**172 / 191 complete.** Easy 25/25, Medium 85/93, Hard 62/73. Every topic is at 100%
except three: **Dynamic Programming 3/7**, **Dynamic Programming Part-II 0/8**, and
**Trie 0/7**. All 19 unsolved problems sit in two patterns.

This is directly observed from the source's own progress dashboard, not user-reported.
It is evidence of *prior completion*, **not** of current recall - the track's eight-point
definition of "solved" requires reproduction, and Swapnil reports being out of touch with
the sheet. Phase B exists to convert one into the other. Corroborating signal: every
self-selected session since Jul 21 has been DP (Jul 21 LIS, Jul 28 LIS + LCS, Aug 22 0/1
knapsack).

**Syllabus re-sequenced Aug 26** on this evidence: the original order would have
re-covered arrays/trees/graphs (all 100%) through November while leaving Trie until Nov 2
and DP until Dec 14. Work now runs Phase A (complete the 19 gaps, Aug 31-Sep 27) ->
Phase B (Sep 28-Apr 4) -> Phase C (maintenance, Apr 5-May 9).

**Phase B is interleaved, revised the same day.** The first version worked through
Striver section by section, which means the section heading tells you the pattern before
you start - and pattern selection is the current most-frequent recorded mistake tag.
All three sources now run in parallel every week: Monday is Striver revision from the
due queue (any topic), Tuesday is one unseen Taro problem, Wednesday is mixed and
unlabelled. Phase A stays deliberately blocked because those 19 problems are first
exposure, and focused blocks beat interleaving for initial acquisition. No pattern was
dropped; see the coverage map in `06-DSA-Track.md`.

- Primary language: Swift (interview-primary through Phase 1; Python one problem/week; re-decide at Consolidation 1). See the 06-DSA-Track.md language rule.
- Unique independent solves: 1 (Maximum Product Subarray, medium DP, Swift; derivation in iOS-Apps/DSA/Sprint-Orientation-00.swift).
- Learned/hinted: 0.
- Failed: 0.
- Repetitions completed: 0.
- Current clean medium solve rate: not yet measured (Sprint 1 starts timed array/hash + two-pointer mediums).
- Median independent medium time: not measured (the orientation solve was untimed).
- Most frequent mistake tag: pattern-selection mismatch (1). Added Aug 26 from the
  knapsack session: `syntax/library fluency` (1), `recursion/base case` (1), `weak test
  cases` (1). Too few data points to name a dominant category yet; revisit at the first
  Friday review with a full week of tags. Original note follows: pattern-selection mismatch - the Jul 21 LIS submission did not match the required arrays/hash-map revision; no timed-solve mistake tag is recorded yet.
- Most recent mock score: not measured.
- Next due repetition: Maximum Product Subarray ~Aug 3 (clean-solve 14-day interval), or replace with a harder DP variant.
- **Wed Aug 26 evening session — 0/1 knapsack, recorded as `learned` not `solved`.**
  Continuation of the Aug 22 attempt. Swapnil wrote the memoisation and a tabulation
  pass; **it did not compile** — `swiftc -typecheck DSA6.swift` exited 1 with six
  errors: `memo` referenced four times but never declared, the memo helper declared
  `-> Int` with no return, `let dp` mutated in the tabulation loop, and an `else`
  placed outside the `for j` loop. One real logic defect beyond the mechanics: in the
  memo version the `weights[n-1] > capacity` branch assigned to the table without
  returning, so execution fell through and computed `include` with a negative
  capacity — the early return present in his own recursive version was lost in
  translation. Boundary defect: `for j in 1...capacity` traps at capacity 0.
  **Correct on the conceptual points that matter:** the memo key is `[n][capacity]`
  (correctly excluding the invariant `weights`/`values`), `-1` chosen as the sentinel
  because 0 is a legitimate answer, and the recurrence itself right in all three
  approaches.
  **Repair authored by the assistant at Swapnil's request**, so per
  `06-DSA-Track.md` -> *What "solved" means* ("if editorial code was viewed before a
  correct implementation, record 'learned', not 'solved'") this counts as **learned**.
  It does **not** increment unique independent solves.
  Artifact: `../iOS-Apps/DSA/DSA6.swift`, commit **`5290285`**. Verified by executing
  all three approaches (recursive, memoised, tabulated) against the same eight cases —
  classic, capacity 0, n 0, item too heavy, exact fit, all fit, must-skip-heaviest,
  empty arrays — by switching which helper `knapsack01` returns; all three agree on
  all eight, and `swiftc -typecheck` exits 0.
  **Mistake tags:** `syntax/library fluency`, `recursion/base case`, `weak test cases`.
  **Still owed by Swapnil, not yet demonstrated:** an independent re-derivation, and a
  spoken statement of why memoisation turns O(2^n) into O(n x capacity). The complexity
  figures now in the file were written by the assistant, not derived by him.
  **Repetitions (copied-work interval 1/3/7/21):** first re-derivation **Sat Aug 29**
  in the existing restart-gate DSA block, then **Wed Sep 2**, then **Wed Sep 16**. The
  1-day interval is skipped because Thursday Aug 27 has no DSA block; creating one
  would be time debt, which `04-Weekly-Operating-System.md` forbids.
- **Overdue as of Aug 26:** Maximum Product Subarray (due ~Aug 3, 23 days overdue)
  and Repeating and Missing Number (due ~Aug 11, 15 days overdue). Both are
  scheduled into the restart gate's Saturday Aug 29 replacement block. Repetition
  is repair, not new content.
- **Sat Aug 22 session — recorded Aug 26, now durable.** `../iOS-Apps/DSA/DSA6.swift`,
  +44/-19 lines, committed Aug 26 as **`82b2282`** in the `iOS-Apps/DSA` repository.
  **Correction to the first Aug 26 entry:** it claimed "recursive, then memoized." The
  file was inspected line by line before committing and **the memoization was never
  written** — `//approach 2 : memoization` is followed by an empty comment on line 51.
  What exists is the recursive include/exclude solution with base cases, exponential
  time and O(n) recursion depth. The state parameters that vary (capacity, n) are named
  in the comment but no memo table or lookup exists. Result: **incomplete**, not solved.
  No timing, accepted run, or mistake tag was supplied, so none is claimed. This is the
  only recorded activity in the Jul 29 - Aug 25 window, and finishing the memoisation is
  the first Phase A task.
- Jul 21 Sprint 1 submission review (verified Jul 22): `../iOS-Apps/DSA/sprint-01-AI-Software-Foundations.swift` is an untracked Longest Increasing Subsequence solution, not an arrays/hash-map revision. It type-checks with one trailing-closure warning; the active `firstIndex` search makes it O(n^2) time and O(n) space. No accepted run, timing, due-item provenance, mistake reflection, or next repetition date was supplied, so it is not counted above.
- Recovery queue: **Repeating and Missing Number** — **SOLVED Tue Jul 28, 9:30–10:30 PM**. Implementation: XOR-based O(n) time / O(1) extra space solution without modifying input. Algorithm: (1) XOR all array elements with 1...n to get `repeating XOR missing`; (2) find rightmost set bit to partition numbers; (3) XOR each partition separately with both array and 1...n; (4) verify which result is in the array (repeating) vs missing. Artifact: `../iOS-Apps/DSA/sprint-01-AI-Software-Foundations.swift` function `findMissingAndRepeatingValue`. **Prior-mistake note:** The Jul 21 LIS submission was a pattern-selection mismatch — chose DP subsequence instead of arrays/hash-map; the mental process jumped to "interesting problem" rather than matching the recovery target. **Bonus:** Also solved **Longest Common Subsequence** (DP, O(m×n) time/space) in same session. Next repetition: ~Aug 11 (14-day interval). The timed two-pointer solve is rescheduled to Wed Jul 29, 5:00–6:00 mixed set.

**Record boundary (Aug 26, 2026).** Three places, no duplication:

- **Striver site** - authoritative for which problems are done and due for revision.
- **Notion** - the per-problem notebook (statement, recognition signal, Swift solution,
  and going forward: date, result, timings, mistake tag, next repetition).
- **This section** - aggregate only: counts by source, weakest patterns, mistake-tag
  frequency, next repetitions, and mock scores.

Do not copy per-problem detail into `PROGRESS.md`. Two ledgers drift, and the one that
drifts is the one nobody trusts.

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
| Aug 28 | None — retention failure on already-scored material, not a failed gate | Asked to defend B1 (17/24, Jul 24) from memory, Swapnil described a WebSocket — persistent connection, opening handshake, continuous two-way conversation, TCP/UDP/QUIC ordering — instead of webhook ingestion. Zero of the six mechanisms he was scored on returned. Classification: **conceptual gap** per `08-Assessment-and-Recovery.md`, not a life/work disruption. Read narrowly: the material was five weeks cold, had no revision pass (unlike the six competency items re-tested the same day), and the design track schedules no repetition at all — so this measures the absence of a review loop at least as much as it measures Swapnil. The one part that is not about scheduling is the substitution of a **persistent bidirectional connection** for a **one-shot HTTP POST**, which is a factual error worth 20 minutes regardless of any score. | **20 minutes, Fri Aug 28, 6:50–7:10 PM**, inside the weekly-review block freed by writing the overdue entries early — moved off Saturday so it lands the same day it was found, and because Saturday is already absorbing a displaced two-hour block. Re-read only the critical-flow trace and the HMAC/dedup sections of `notes/sprint-01-AI-Software-Foundations-notes-02-b1-*.md` — not the whole document. Then, notes closed, write: (a) one sentence on why a webhook is an ordinary HTTP POST and not a persistent connection; (b) the four failure modes the design exists to survive — unverified sender, slow consumer, duplicate delivery, permanent consumer failure — and the one mechanism answering each. Not a redesign; B1 is **not** rescored. If it does not hold Aug 29, it becomes the first block of the I1 case in the repair sprint. | Fri Aug 28 | **Half done, still open.** Swapnil re-read the B1 write-up on the evening of Aug 28 (~19:20 IST), user-reported; the file itself is unmodified since Jul 25, consistent with a read rather than an edit. **The closed-notes recall step has not been attempted, so the repair is not closed.** Reading the document back is explicitly not the evidence this row asks for — the whole finding is that Swapnil had already written all 52 KB of it and still lost the model, so re-reading proves the same thing it proved in July. Closes only on the two-question answer given with the notes shut. **CLOSED same evening, ~19:35 IST — the conceptual gap is repaired; a narrower carry remains.** Closed-notes answer given. **The WebSocket model is gone**, which was the whole reason this row existed: the webhook is now described as an event notification pushed by the provider ("Stripe sends payment successful") into service → repository → database, with no persistent connection anywhere in the answer. Of the four mechanisms: **(a) sender authenticity — strong.** Signature sent with the request, timestamp checked, hash recomputed and compared, and the correct motivation given unprompted (the endpoint is publicly reachable). The timestamp/replay detail is more than the row asked for. **(c) duplicate delivery — mechanism right, vocabulary wrong.** Check-then-skip idempotency with a fast path and a database fallback, matching the design's Redis-with-Postgres-fallback; but he called the fast path a "connection pool", which holds database connections, not dedup keys. **(b) slow consumer — missed.** Answered with retry and exponential backoff, which is the answer to (d), not (b); the durable-accept-then-process-async mechanism from his own design did not return, and one mechanism was made to cover two failure modes. **(d) permanently broken consumer — thin.** "Time off after specific period" reaches giving up but not **dead-lettering**, so the event is lost rather than parked for inspection and replay. **Ruling: 2 of 4 solid, 1 misapplied, 1 incomplete — but the classification changes.** This is no longer a *conceptual gap*; the wrong mental model is corrected. What is left is ordinary incomplete recall of two specific mechanisms, which is a smaller and differently-treated thing. **B1 is not rescored; 17/24 stands untouched.** |
| Aug 28 | None — sustainable-capacity correction, not a failed gate | The 2:15 PM weekday roadmap start was not working in practice. Swapnil reported 3:30 PM as the earliest he can genuinely begin. Recorded as a capacity fact, not a preference: a start time nobody meets is not a schedule, and four silent weeks in Jul-Aug are what an unmet schedule looks like. | **Schedule revision approved Aug 28 (roadmap change control, user-approved after impact analysis).** All weekday blocks shift +1h15m: 3:30-5:30 AI core, 5:45-7:45 rotating track, 7:45-8:45 review (Fri), 9:30-10:30 home block now on **Mon/Tue/Wed/Thu**. 2:00-3:15 PM is explicitly marked **not roadmap capacity** so no future daily plan reclaims it. Mon/Tue/Fri lose nothing; the whole ~1.5 h/week cost lands on Wed/Thu because IIT at 6:00 PM cannot move. **The cut was assigned, not spread:** Apple AI absorbs all of it (5.5-6 h → 4 h), since AI FDE is primary and Apple is the declared backup; AI core/platform, DSA, design and review are held at previous hours, DSA protected because it serves both targets and carries a backlog. Thursday is no longer an Apple day. **No outcome, exit gate, prerequisite, sprint date, portfolio boundary, or readiness date changed** — 23 h stays inside the 20-25 band. Files updated: `04-Weekly-Operating-System.md` (authority), `AI-ROADMAP-PROMPT-CONTEXT.md`, `00-FRESH-SYSTEM-CONTEXT.md`, and supersede banners on the Sprint 01/02 guides, whose in-body clock times are left intact as a record of what was planned. `skill.md` needed no edit: it hardcodes no clock times and reads the operating-system file. | Review at Consolidation 1 if Apple evidence falls behind | **Applied Aug 28.** In force from Mon Aug 31, the first day of the Sprint 1 repair sprint. |
| Aug 28 | None — block slip, not a gate | Thursday's 2:15–6:00 blocks executed a day late, on Friday afternoon, consuming Friday's own 2:15–4:15 toolchain-recheck and stack-snapshot window. | Move the environment re-baseline and the `09-Current-Stack-Snapshot.md` refresh **once**, into Saturday Aug 29 replacement capacity — Saturday exists for exactly this and this is its first claim. Friday evening is **not** extended to absorb it: the 4:30–6:30 wiring block is the gate's highest-risk item and is not shortened. To keep Saturday inside a sane budget, the Saturday DSA repetitions are dropped to the repair sprint's DSA hours — item 2 of this gate's own drop/defer order, invoked in sequence. | Sat Aug 29 | **Open.** |

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
> **Updated Fri Aug 28, 2026.** The first two entries are now written, below the
> template. Hours are left as *not observed* in both, because they never were —
> `skill.md` forbids inferring them. The four dead weeks are recorded as one
> honest combined entry rather than four reconstructions, since reconstructing
> them from memory five weeks later would be fabrication. The current week's
> entry (Week of 2026-08-24) is written at the Aug 30 gate close, not before,
> because the gate result is part of it.

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
---

### Week of 2026-07-20 — written Fri Aug 28, 2026 (five weeks late)

- Planned roadmap hours: 24–25.
- Actual roadmap hours: **not observed.** Never recorded at the time; not inferred here.
- IIT hours: **not observed.**
- Result I can now produce without a tutorial: measured Fri Aug 28 by unaided recall
  against the Sprint 1 competency list, stated before any lookup.
  **Holds (4):** Alembic's purpose — version control for the database schema, the same
  way Git versions code; what `await` does — it yields while waiting on I/O so the
  thread serves other work instead of blocking; why a transaction rolls back — a
  constraint violation or an error before `COMMIT` discards the whole unit; `Protocol`
  plus a fake adapter for tests — matching method signatures let the service take
  either implementation, which is what makes the injection work.
  **Partial (1):** SQLAlchemy — the translator role and the transaction/key vocabulary
  returned, but `async` was explained as the mechanism providing atomicity. That is
  **wrong**: atomicity comes from the transaction (`BEGIN`/`COMMIT`/`ROLLBACK`); `async`
  only stops the thread blocking while the network round-trip completes. Two unrelated
  ideas fused during the gap. Corrected in the repair sprint's first Postgres block.
  **Not demonstrated (1):** FastAPI 404/409/422 — no unaided answer was attempted
  before the lookup, so it is unproven in either direction and is re-tested cold.
  **Failed (1):** the B1 webhook design — see the System-design ledger.
- Strongest evidence: SQL/Postgres learning evidence, reviewer-verified Jul 25 against
  live PostgreSQL 16.14; B1 scored 17/24 on Jul 24.
- Failed or partial gate: no gate was attempted. The Fri Jul 24 9:11–10:11 PM review
  window was consumed by the B1 block overrunning to 02:16 IST.
- Root cause: a single artifact overran its stop, the review that would have caught the
  drift was the thing it displaced, and four weeks of silence followed.
- Quality/latency/cost/security/reliability measurement: B1's own estimates — 43.2 M
  events/day, 3.708 TB over 30-day retention, ingest p95 <20 ms. Produced, then not
  retained five weeks later.
- DSA pattern and mistake: pattern-selection mismatch, recorded Jul 28 (LIS, Jul 21).
- System-design case and score: B1 — Reliable webhook ingestion, 17/24.
- Apple evidence: `TaskListFeature.swift` type-checked Jul 23 but left uncommitted for
  five weeks; made durable Aug 28 as `85b14c1`.
- FDE/customer-delivery evidence: none.
- Scope removed: I1 and the SwiftUI observation/state architecture were deferred Jul 28;
  both were **restored** Aug 26 when the +6 week shift removed the time pressure that
  had justified cutting them.
- Recovery action: the Aug 26 row (+6 weeks, restart gate) and the Aug 28 B1 row.
- Next week's single most important result: **a task record that survives a container
  restart.** It was the answer in July and it is still unproven.

### Weeks of 2026-07-27, 2026-08-03, 2026-08-10, 2026-08-17 — one combined entry, written Fri Aug 28, 2026

- Planned roadmap hours: 20–25 per week.
- Actual roadmap hours: **not observed.** Recorded as missed under **Weekly hours**;
  no hours inferred for any of the four weeks.
- IIT hours: **not observed.**
- Only recorded activity in the entire window: `DSA6.swift` — 0/1 knapsack, recursive
  solution only — modified Sat Aug 22 in `../iOS-Apps/DSA`, committed Aug 26 as
  `82b2282`. Recorded Aug 26 as learned, not solved.
- Result producible without a tutorial: measured Aug 28; see the entry above.
- Root cause: **not diagnosed from evidence, because no evidence exists.** Classified
  Aug 26 under `08-Assessment-and-Recovery.md` as a life/work disruption, and the
  remedy that taxonomy prescribes — minimum-viable week plus scope cut — was applied as
  the +6 week shift rather than as a reduction in any outcome.
- System-design case and score: none.
- Apple evidence: none.
- Scope removed: none in-window. Scope was re-timed on Aug 26, not cut.
- Recovery action: the Aug 26 row.
- Next week's single most important result: closing the restart gate honestly.
- **Why this is one entry and not four:** reconstructing four weekly retrospectives from
  memory five weeks after the fact would be fabrication, which `README.md` rule 9 and the
  evidence protocol both forbid. One truthful combined entry is the record.
