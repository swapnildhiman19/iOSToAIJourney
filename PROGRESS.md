PROGRESS.md [332L]
# Progress Ledger
> Last roadmap update: July 28, 2026 (evening session complete)
> Current block: Sprint 1 (Orientation passed Jul 20) — active
... [lean-ctx: omitted 2 lines]
checkbox requires an evidence link, command, score, recording, or reproducible
... [lean-ctx: omitted 1 lines]
## Current focus
- Block: Sprint 1 - AI Software Foundations (Jul 20-Aug 2).
... [lean-ctx: omitted 2 lines]
- Current blocker: none - all Sprint 1 prerequisites confirmed Jul 20 (Python 3.14.6, uv 0.9.28, Git 2.50.1, Docker 29.6.1 / Postgres 16, Swift 6.2.4, DSA language selected).
... [lean-ctx: omitted 1 lines]
- Carry-forward from orientation (fold into Sprint 1, no scope growth): (1) FastAPI 409 consolidation and response-body evidence closed Jul 23 with the in-memory HTTP contract tests; (2) SQL — **closed Jul 24, verified Jul 25**: `ROLLBACK` and a Python parameterized query both demonstrated against live PostgreSQL 16.14; (3) Model API - forced-failure branch + latency/usage capture (Sprint 2, where the model lands); (4) synthetic test fixture identity — **closed Jul 25**: `test_insert.sql` line 4 still contained a real personal email after the Jul 24 hygiene step claimed completion; it now inserts `learner@example.invalid` / `Learner One`.
- Schedule (authoritative recovery override recorded Wed Jul 22): the domain checkpoint and adapter-swap defense are reviewed. The Thu Jul 23 FastAPI replacement is verified through per-app injection, stable 404/409 contracts, default 422 validation, OpenAPI, and 9 passing tests. The Fri Jul 24 SQL and B1 blocks are complete and reviewer-verified Jul 25 (SQL artifacts executed against live Postgres; B1 scored 17/24 against the eight-dimension track rubric). The **Fri Jul 24 9:11–10:11 PM weekly review did not happen** — the B1 write-up overran its 9:11 PM stop (`notes/sprint-01-AI-Software-Foundations-notes-02-*.md` last modified Jul 25, 02:16 IST) — so the clean-checkout reproduction and Week-1 gap list move once, into the existing Fri Jul 31 gate-rehearsal block. No third Week-1 replacement block is created. The external Jul 23 Swift artifact at `../iOS-Apps/iOSToAIJourney/Sprint-01-AI-Software-Foundations/TaskListFeature.swift` has only the prior `xcrun swiftc -typecheck TaskListFeature.swift` exit-0 evidence. Its implementation was unstaged in the sibling repository when reviewed, so this is working-tree-only/non-durable evidence of a guided state/protocol/fake foundation, not a complete SwiftUI feature. **Repeating and Missing Number** remains selected but unsolved, with its prior-mistake note still missing. **Sat Jul 25 safe async block — partial**: `async_boundary_lab.py` created and staged (`AI Solutions Platform/diagnostics/Sprint-01-AI-Software-Foundations/async_boundary_lab.py`), demonstrating unbounded fan-out (peak = 50), semaphore-bounded fan-out (peak = 5), and the blocking boundary (`time.sleep` starvation vs `asyncio.to_thread` fix); the companion notes file (`notes/sprint-01-AI-Software-Foundations-notes-03-python-asyncio-complete-understanding.md`) was created but remains **empty**; timeout and cancellation-cleanup tests were not written. **Sat Jul 25 ADR/minimal CI block — not started.** **Sun Jul 26 through Tue Jul 28 afternoon — entirely missed**: Swift concurrency + DSA two-pointer review (Sun), async Postgres adapter + persisted vertical slice + Repeating and Missing Number DSA (Mon), transactions/idempotency + Apple architecture (Tue 2:15–6:30) were all not attempted. The sprint has 5 days remaining (Tue Jul 28 evening through Sun Aug 2) with significant Week-2 backlog; a recovery redistribution is recorded under Recovery actions. IIT and actual roadmap hours for both weeks remain unreported.
## Orientation diagnostics
| Diagnostic | Score/result | Evidence | Action |
... [lean-ctx: omitted 3 lines]
| FastAPI/HTTP | 2.5/3 — Validation, `/health` test, and a clear `DuplicateTask` → HTTP 409 boundary with a passing error test; the clean boundary lives in a parallel `/v2/tasks` route rather than consolidated into `POST /tasks`, and success/error bodies are not asserted | `AI Solutions Platform/diagnostics/Sprint-00-Orientation-diagnostics/fast_api.py`; `uv run --extra dev pytest "diagnostics/Sprint-00-Orientation-diagnostics/fast_api.py" -q` → 2 passed (verified Jul 18) | Sprint 1 cleanup: consolidate the 409 mapping into `POST /tasks` and assert success/error bodies |
| SQL/Postgres | 3/3 — PK, FK, UNIQUE, CHECK, and FK index defined; transaction `COMMIT` persisted; `EXPLAIN` shows Bitmap Index Scan on `idx_orders_customer_id`; `ROLLBACK`, parameterized query, and index write-cost explained in notes | `diagnostics/Sprint-00-Orientation-diagnostics/schema.sql`, `.../test_insert.sql`, `notes/sprint-00-Orientation-notes.md`; demonstrated on Postgres 16 in Docker (container `orientation-pg`, db `diag`) — `\dt`, row selects, and `EXPLAIN` verified Jul 18 | **Closed Jul 25.** `ROLLBACK` and the Python parameterized query are both demonstrated live on PostgreSQL 16.14 (db `learner_exercise`); see the SQL evidence row under AI Solutions Platform milestones |
| Model API | 2/3 — Structured output via `response_json_schema` + Pydantic `model_validate_json`, configurable model ID, `.env`-based key handling; no forced invalid-output/missing-key failure and no latency/usage capture | `diagnostics/Sprint-00-Orientation-diagnostics/gemini_model_api_diagnostic.py`; google-genai 2.12.1 (GA), model `gemini-2.5-pro` (stable/GA; newer Gemini 3.x line exists); successful run user-reported, not independently executed (paid call) | Sprint 1: add a forced-failure branch and record latency/token usage |
| Git/Docker/CI | Partial: Git available; Docker verified Jul 18 and used to run a Postgres 16 container (`orientation-pg`) for the SQL diagnostic; `.env` confirmed git-ignored; CI still untested | July 16 environment baseline below; Jul 18 terminal output (`docker --version`, `docker compose version`, `docker ps`, `git check-ignore`) | Configure CI in Sprint 1 (repository ignores verified) |
... [lean-ctx: omitted 5 lines]
| System design | 14/24 — RAG architecture, RBAC, async processing; gaps in quantification, failure handling, context window management | Handwritten diagram Jul 17; chat interview transcript; rubric scores: Requirements 2/3, Estimates 1/3, Contracts 2/3, Architecture 2/3, AI depth 2/3, Failure handling 1/3, Security 2/3, Communication 2/3 | Study context window mgmt, re-ranking, quantification before Sprint 1 |
| FDE discovery | Baseline 15/24 (orientation diagnostic - not a gate; the 20/24 bar is the Phase-4 Mar-2027 capstone target). Strong qualification, architecture, and security; grow communication structure and quantified baseline+threshold | notes/sprint-00-Orientation-notes.md (FDE discovery diagnostic section) | Sprint 1 embedded FDE one-pager: explain provider-neutral architecture to a non-AI engineer |
### Environment baseline — July 16, 2026 (revised)
Source: direct version, hardware, and simulator commands run from the roadmap
root in the active `(base)` shell. Hardware and simulator data corrected after
... [lean-ctx: omitted 5 lines]
| uv | 0.9.28 (0e1351e40 2026-01-29) | Available |
| Docker | 29.6.1, build 8900f1d; Compose v5.3.0 | **Available** — verified Jul 18; ran Postgres 16 container `orientation-pg` for the SQL diagnostic |
| Google Cloud CLI | 574.0.0; core 2026.06.22 | CLI available; GCP project `easyaiwithswapnil` confirmed |
... [lean-ctx: omitted 1 lines]
| Swift | 6.2.4 (swiftlang-6.2.4.1.4 clang-1700.6.4.2); target `arm64-apple-macosx26.0` | Available |
... [lean-ctx: omitted 1 lines]
| Xcode (beta) | 27 beta 3 at `/Applications/Xcode-beta.app` | Active developer directory (`xcode-select`) |
| Simulators | iOS 26.0, 26.2, and **27.0** (24A5380i) runtimes verified | iOS 27.0 simulator and OS 27 SDK confirmed ✅ |
... [lean-ctx: omitted 6 lines]
Primary DSA language decision: **Swift** (interview-primary through Phase 1; Python maintained one problem/week for AI-FDE fluency; firm re-decision at Consolidation 1)
## Roadmap status
Allowed status: `not-started`, `active`, `blocked`, `gate`, `partial`, `passed`,
or `repair`.
| Block | Dates | Status | Score /15 | Exit evidence | Repair |
... [lean-ctx: omitted 1 lines]
| Orientation | Jul 16–19 | passed | — | Passed Jul 20 (checklist gate): all diagnostics scored + evidenced (Python 2.5, Async 2.5, FastAPI 2.5, SQL 3, Model API 2, System design 14/24, Swift + Concurrency, DSA-Swift independent solve, FDE 15/24); DSA language = Swift; Sprint 1 adjusted within 20%, exit gate preserved | — |
... [lean-ctx: omitted 1 lines]
| Sprint 2 | Aug 3–16 | not-started | — | — | — |
... [lean-ctx: omitted 2 lines]
| Consolidation 1 | Sep 14–20 | not-started | — | — | — |
... [lean-ctx: omitted 4 lines]
| Consolidation 2 | Nov 16–22 | not-started | — | — | — |
... [lean-ctx: omitted 4 lines]
| Consolidation 3 | Jan 18–24 | not-started | — | — | — |
... [lean-ctx: omitted 4 lines]
| Consolidation 4 | Mar 22–28 | not-started | — | — | — |
| Final verification | Mar 29–31 | not-started | — | — | — |
## Active sprint gate
Sprint 1 (Jul 20-Aug 2) is the active block. It uses the five-part sprint rubric (/15); pass requires at least 11/15, no zero, and every item in the Sprint 1 Exit test proven. See sprints/Sprint-01-AI-Software-Foundations.md -> Exit test. The score is recorded at the Aug 2 sprint close.
### Orientation exit gate - CLOSED, passed Jul 20
- [x] Every diagnostic has a score/result and evidence - Python 2.5, Async 2.5, FastAPI 2.5, SQL/Postgres 3, Model API 2, System design 14/24, Swift + Concurrency done, DSA in Swift (independent solve), FDE 15/24. DSA in Python deferred by design (Swift primary; first Python solve in Sprint 1).
... [lean-ctx: omitted 1 lines]
- [x] No credential or confidential information in the repository - .env git-ignored (verified git check-ignore Jul 18). Carry-forward hygiene: replace the real personal email in test_insert.sql with a synthetic identity at the first Sprint 1 SQL touch.
... [lean-ctx: omitted 3 lines]
- [x] Sprint 1 has no more than a 20% evidence-based adjustment - one learning item (blocking vs non-blocking / event-loop offload) and one build item (assert success + error response bodies) added; the exit gate is preserved.
... [lean-ctx: omitted 1 lines]
## Weekly hours
Target roadmap hours: 20-25. IIT is tracked separately.
| Week of | AI/platform | Apple | DSA | Design | Review/FDE | Roadmap total | IIT | Note |
... [lean-ctx: omitted 2 lines]
| Jul 20 | plan | plan | plan | plan | plan | plan 24-25 | unreported | FastAPI replacement verified Jul 23; Fri Jul 24 SQL and B1 complete and reviewer-verified Jul 25 (B1 17/24). The external Swift foundation has only a prior type-check from a working-tree-only/non-durable sibling artifact; Swift concurrency continues Sun. Safe async and ADR/minimal CI remain the two Sat replacements, unreported as of Jul 25. **The Jul 24 review did not run, so actual roadmap hours and Jul 22–23 IIT attendance are still unreported and are not inferred here**; the Fri Jul 31 review is now the recording point. |
| Jul 27 | ~2.5 hrs (Tue eve) | 0 | ~1 hr (Tue eve) | 0 | 0 | ~3.5 hrs (Tue Jul 28 evening) | unreported | **Jul 27–28 daytime missed**: Mon and Tue daytime blocks not attempted. **Tue Jul 28 evening executed**: 6:00–7:30 PM Postgres setup (compose, adapter, migration, readiness) + 9:30–10:30 PM DSA (Repeating/Missing Number XOR solution + LCS bonus). Recovery redistribution recorded Jul 28 under Recovery actions. Remaining Week-2 work continues Wed–Sun. Fill complete actuals at Aug 2 close. |
... [lean-ctx: omitted 1 lines]
## AI Solutions Platform milestones
- [/] Repository and CI foundation. Skeleton exists at `AI Solutions Platform/`; `src/`, `uv.lock`, `.python-version`, pyproject configuration, formatting, lint, strict type-check, and test commands were verified Jul 22. The required architecture decision and `.github/workflows/ci.yml` are absent; the Sat Jul 25 replacement block was not executed. Separately, `async_boundary_lab.py` (staged, not committed) demonstrates bounded/unbounded fan-out and blocking boundary as Sprint 1 async evidence; its companion notes file is empty. ADR and CI remain scheduled for Thu Jul 30 and Fri Jul 31 respectively. Milestone remains partial.
- [x] Sprint 1 domain-boundary exercise checkpoint. Frozen domain record, domain duplicate exception, repository `Protocol`, injected application service, in-memory adapter, and create/duplicate tests were verified Jul 22. Targeted and full pytest each passed 2 tests; Ruff format/lint and strict mypy passed; the domain/application forbidden-SDK scan returned zero matches. Swapnil's independent adapter-swap defense was reviewed Jul 22 at 3/4 and accepted with corrections: add `PostgresTaskRepository` rather than rewrite the memory adapter, switch the composition/provider, and translate the exact unique-constraint failure inside the Postgres adapter to `DuplicateTaskTitle`. This closes the local exercise checkpoint, not the Aug 2 sprint gate.
- [/] FastAPI/Postgres vertical slice. The in-memory HTTP boundary is verified Jul 23: app-owned repository composition, create/read, health/readiness placeholder, stable 404/409 bodies, default 422 validation, generated OpenAPI, and app-isolation evidence. Locked Ruff format/lint and strict mypy passed; full pytest passed 9 tests. **Tue Jul 28 evening (6:00–7:30 PM):** Postgres 16 container via `docker compose up -d` (compose.yaml with health check and named volume); `PostgresTaskRepository` implements `TaskRepository` protocol with `IntegrityError` → `DuplicateTaskTitle` translation; async session provider via `database.py`; first Alembic migration (`0001_create_tasks_table.py`) applied against live Postgres; `/healthz/ready` endpoint returns 200 when DB connected, 503 when unavailable. Dependencies added: `alembic>=1.18.5`, `asyncpg>=0.31.0`, `sqlalchemy[asyncio]>=2.0`. Learning notes: `notes/sprint-01-AI-Software-Foundations-notes-04-postgreSQL-connection-understanding.md` (comprehensive AsyncEngine/Session/Pool/Alembic lifecycle understanding). Clean-database integration tests remain scheduled for Wed Jul 29.
- [x] Sprint 1 relational-modelling and SQL learning evidence (Fri Jul 24, reviewer-verified Sat Jul 25). Artifacts: `AI Solutions Platform/diagnostics/Sprint-01-AI-Software-Foundations/{sql_schema.sql, rollback_proof.sql, parameterized_query_proof.py, query_plan_observation.sql, sql_evidence_package.md}`; teaching record in `notes/sprint-01-AI-Software-Foundations-notes-01-sql-postgresql-deep-learning.md` with a dated reviewer appendix holding the executed transcripts. Verified on PostgreSQL **16.14** (container `orientation-pg`, db `learner_exercise`) via `docker exec -i orientation-pg psql -U postgres -d learner_exercise -v ON_ERROR_STOP=1 < <file>`: schema applies clean (3 tables, 8 indexes — **6 automatic + 2 manual**, correcting the evidence package's "5 + 3"); rollback proof returns `before_count 0 → INSERT 0 1 → visible in transaction → ROLLBACK → 0 rows → after_count 0`; the parameterized-query script inserts, fetches, matches 0 rows for a `'; DROP TABLE task; --` payload, leaves `to_regclass('task')` intact, and rolls back clean. Three claim corrections are recorded rather than silently fixed: the real plan is a forward `Index Scan using idx_task_status_recent`, not `Index Scan Backward` (a DESC index satisfies `ORDER BY … DESC` on a forward read); the printed costs and `rows=2` estimate do not match the server (`0.14..8.16`, Seq Scan `0.00..11.62`, estimate `rows=1` because the table was never `ANALYZE`d); and at 5 rows the un-indexed plan was **faster** (0.025 ms vs 0.051 ms), so index value is unproven at fixture scale. Known gap carried to Jul 27: `psycopg` is not a dependency of `AI Solutions Platform/pyproject.toml`, so the proof script runs only in an ephemeral environment, and its `except psycopg.OperationalError` branch prints "Script logic is verified" for a run that never connected. This is learning evidence for the Jul 27 adapter, not the persisted vertical slice.
... [lean-ctx: omitted 1 lines]
- [ ] Streaming, structured output, tools, approval, and cancellation.
... [lean-ctx: omitted 5 lines]
- [ ] Native-audio comparator and multi-agent voice handoff.
... [lean-ctx: omitted 3 lines]
- [ ] LoRA experiment and adopt/reject decision.
... [lean-ctx: omitted 3 lines]
## Apple AI Lab milestones
- [ ] Availability/fallback shell.
- [ ] Foundation Models v2 text/image and structured generation.
... [lean-ctx: omitted 2 lines]
- [ ] Evaluations and Instruments evidence.
... [lean-ctx: omitted 1 lines]
- [ ] Core Spotlight and safe private retrieval.
... [lean-ctx: omitted 1 lines]
- [ ] Physical-device checkpoint recorded.
## Local AI Workbench milestones
- [ ] Current SLM selection with license/hardware rationale.
- [ ] MLX local run and compatible endpoint.
- [ ] Quantization comparison.
... [lean-ctx: omitted 3 lines]
- [ ] Core AI/Core ML/MLX/cloud benchmark.
... [lean-ctx: omitted 2 lines]
## System-design ledger
Required: 18 AI, 10 iOS, 6 backend.
- AI complete: **1/18** (Orientation diagnostic)
... [lean-ctx: omitted 3 lines]
- Two most recent scores: **17/24 (B1, Jul 24)**, 14/24 (Orientation, Jul 17)
- Lowest current dimension: no dimension below 2/3 in the most recent case. Both orientation repair targets moved — Estimates and budgets **1/3 → 3/3**, Failure handling **1/3 → 2/3**. Weakest remaining: operational alerting (thresholds, SLO burn-rate, paging path) and document communication structure.
... [lean-ctx: omitted 1 lines]
- AI: Orientation diagnostic (Enterprise AI Assistant with RAG)
... [lean-ctx: omitted 2 lines]
### B1 — Reliable webhook ingestion (Fri Jul 24, scored Jul 25)
- Rubric: `05-System-Design-Track.md` → **Scoring rubric**, eight dimensions 0–3, **/24**. Phase-1 expectation is ≥12/24 with no zero in requirements or critical flow; the 20/24 bar belongs to the Phase-4 Mar-2027 mock and is not applied here.
... [lean-ctx: omitted 2 lines]
- Evidence: `notes/sprint-01-AI-Software-Foundations-notes-02-b1-reliable-webhook-system-design-deep-teaching.md` (design + dated evidence note + critical-flow trace + self-rubric, with a dated reviewer-scoring appendix) and the hand-drawn architecture at `notes/WhatsApp Image 2026-07-24 at 23.53.37.jpeg` (provider → HMAC gateway → durable accept + dedup → async Postgres, partition by day range, Redis-dedup substitution, the 500 → 5,000 → 50,000 RPS ladder with single-Postgres rejected, Kafka overflow, and S3 offload above 8 KB).
- Quantified where orientation was weakest: 500 avg / 5,000 peak RPS, 2 KB avg / 64 KB max payload, 43.2 M events/day, 82.4 GB/day raw → 123.6 GB/day with overhead → 3.708 TB over 30-day active retention, 2.225 TB over 90-day cold retention, ingest p95 <20 ms / p99 <50 ms, end-to-end p95 <500 ms / p99 <2 s, 99.99% availability, RTO <15 min, RPO 0, full-jitter backoff (base 2 s, cap 3600 s, 5 attempts then dead-letter), and a per-component monthly cost table. Arithmetic independently rechecked and correct.
- Recorded defects, not repaired here: the worker-lease sweeper filters on `locked_until`, which `raw_webhook_event` never declares; the critical-flow trace annotates `[00.019 ms]` as "19ms" and has a worker polling 26 µs after acknowledgement; seven metrics are defined with no thresholds, burn-rate alert, or paging path; the cost table prices AWS while the platform target is GCP; and the document carries an off-topic pasted chat block plus a duplicated summary section.
... [lean-ctx: omitted 2 lines]
## DSA ledger summary
- Primary language: Swift (interview-primary through Phase 1; Python one problem/week; re-decide at Consolidation 1). See the 06-DSA-Track.md language rule.
... [lean-ctx: omitted 6 lines]
- Most frequent mistake tag: pattern-selection mismatch - the Jul 21 LIS submission did not match the required arrays/hash-map revision; no timed-solve mistake tag is recorded yet.
... [lean-ctx: omitted 1 lines]
- Next due repetition: Maximum Product Subarray ~Aug 3 (clean-solve 14-day interval), or replace with a harder DP variant.
- Jul 21 Sprint 1 submission review (verified Jul 22): `../iOS-Apps/DSA/sprint-01-AI-Software-Foundations.swift` is an untracked Longest Increasing Subsequence solution, not an arrays/hash-map revision. It type-checks with one trailing-closure warning; the active `firstIndex` search makes it O(n^2) time and O(n) space. No accepted run, timing, due-item provenance, mistake reflection, or next repetition date was supplied, so it is not counted above.
- Recovery queue: **Repeating and Missing Number** — **SOLVED Tue Jul 28, 9:30–10:30 PM**. Implementation: XOR-based O(n) time / O(1) extra space solution without modifying input. Algorithm: (1) XOR all array elements with 1...n to get `repeating XOR missing`; (2) find rightmost set bit to partition numbers; (3) XOR each partition separately with both array and 1...n; (4) verify which result is in the array (repeating) vs missing. Artifact: `../iOS-Apps/DSA/sprint-01-AI-Software-Foundations.swift` function `findMissingAndRepeatingValue`. **Prior-mistake note:** The Jul 21 LIS submission was a pattern-selection mismatch — chose DP subsequence instead of arrays/hash-map; the mental process jumped to "interesting problem" rather than matching the recovery target. **Bonus:** Also solved **Longest Common Subsequence** (DP, O(m×n) time/space) in same session. Next repetition: ~Aug 11 (14-day interval). The timed two-pointer solve is rescheduled to Wed Jul 29, 5:00–6:00 mixed set.
... [lean-ctx: omitted 2 lines]
## FDE evidence
- [x] Opportunity qualification.
- [ ] Current-state workflow map.
- [ ] Two discovery simulations.
... [lean-ctx: omitted 2 lines]
- [ ] Explicit no-go recommendation.
... [lean-ctx: omitted 2 lines]
- [ ] Deployment and rollback presentation.
... [lean-ctx: omitted 5 lines]
Current FDE rubric: baseline 15/24 (orientation diagnostic; the 20/24 pass bar applies to the Phase-4 capstone simulation, not this Week-0 baseline). See notes/sprint-00-Orientation-notes.md.
## Public case studies
| Case study | Target | Status | Evidence/data | Public link |
... [lean-ctx: omitted 2 lines]
| Reliable ADK 2.0 workflows | Phase 2 | not-started | — | — |
| Production voice latency/reliability | Phase 3 | not-started | — | — |
| Discovery-to-production FDE pilot | Phase 4 | not-started | — | — |
## Stack refreshes
| Checkpoint | Due | Completed | Material changes | Migration/eval |
... [lean-ctx: omitted 1 lines]
| Orientation | Jul 19 | Jul 16 snapshot; google-genai 2.12.1 confirmed Jul 18 | google-genai SDK GA (2.12.1); `gemini-2.5-pro` GA with a newer Gemini 3.x line now available | Pending contract setup; re-evaluate model choice (2.5-pro vs 3.x) in Sprint 1 |
| Consolidation 1 | Sep 20 | — | — | — |
... [lean-ctx: omitted 3 lines]
## Device and account gates
- Apple Silicon Mac: MacBook Pro (`Mac16,8`), M4 Pro, 12 cores (8P + 4E), 24 GB memory.
... [lean-ctx: omitted 1 lines]
  are installed; iOS 26.0, 26.2, and **27.0** simulators available.
... [lean-ctx: omitted 1 lines]
- Apple Intelligence system-model availability: FoundationModels availability probe added (CheckFoundationModels.swift, Sprint-00-Orientation); record the concrete availability result in Sprint 1.
- Supported physical iPhone/iPad: pending Consolidation 3 checkpoint.
... [lean-ctx: omitted 1 lines]
- GCP project: `easyaiwithswapnil` (ID: easyaiwithswapnil, number: 377345686823, no organization).
... [lean-ctx: omitted 1 lines]
## Cloud cost and teardown
- Monthly budget: **pay-as-you-go** (GCP project `easyaiwithswapnil`); funds added per requirement.
... [lean-ctx: omitted 1 lines]
- Active billable resources: none yet.
... [lean-ctx: omitted 2 lines]
- Unexpected cost incident: none.
## Blockers
| Opened | Blocker | Type | Evidence | Substitute | Recheck | Owner | Status |
... [lean-ctx: omitted 1 lines]
| Jul 17 | Docker not installed | Prerequisite | Environment baseline Jul 16; resolved Jul 18 (`docker --version` 29.6.1, `docker compose version` v5.3.0) | Could use managed Postgres (Cloud SQL) but local preferred for Sprint 1 | Before Sat diagnostic | Swapnil | **Closed Jul 18** |
## Recovery actions
Detailed dated execution is authoritative in `sprints/Sprint-01-AI-Software-Foundations.md` under **Recovery override — recorded Wednesday, July 22**.
... [lean-ctx: omitted 2 lines]
| Jul 21 | None - in-sprint day slip, not a gate | Sprint 1 Monday Jul 20 blocks not completed | Preserve verified domain code. Use Sat Jul 25, 4:30–6:00 for the missing ADR/minimal CI and Mon Jul 27, 9:30–10:30 for Repeating and Missing Number. The displaced safe-async and Swift work use Sat Jul 25 and Sun Jul 26; the unseen arrays/hash problem is absorbed by the Jul 29 mixed set. | Review Jul 24; execution Jul 25–29 | **Partial, verified through Jul 23:** domain code and the 3/4 adapter defense remain accepted. The external Swift artifact at `../iOS-Apps/iOSToAIJourney/Sprint-01-AI-Software-Foundations/TaskListFeature.swift` has only the prior `xcrun swiftc -typecheck TaskListFeature.swift` → exit 0 evidence. The final reviewer confirmed that its implementation is unstaged in the sibling repository and its staged blob is empty, so the evidence is **working-tree-only/non-durable** and proves only the guided state/protocol/fake foundation. Observable model, SwiftUI view, cancellation transition, actor integration, and tests remain scheduled. Repeating and Missing Number is unsolved, its prior-mistake note is missing, and ADR/CI remain incomplete. Sat Jul 25 status unreported as of this update. |
| Jul 22 | None - in-sprint day slip, not a gate | Wednesday FastAPI and DSA blocks were not completed before their windows elapsed | Thu Jul 23 FastAPI replaces the missed flow and minimum contract evidence. Remaining async, Postgres, transaction, and lifecycle depth stays beside its scheduled implementation. Recover DSA through Sun Jul 26 review, Tue Jul 28 timed solve, and Jul 29 repetition/mixed set. | Jul 23–30 | **FastAPI replacement complete and verified Jul 23:** app-owned injection plus 201/200/404/409/422, health/readiness, OpenAPI, and isolation contracts; Ruff format/lint, strict mypy, and 9 tests pass. DSA recovery remains planned. IIT attendance and actual hours remain unreported; Week-2 sequence and the Aug 2 gate are unchanged. |
| Jul 25 | None - in-sprint block slip, not a gate | The Fri Jul 24 B1 block overran its 9:11 PM stop (B1 notes last modified Jul 25, 02:16 IST), consuming the 9:11–10:11 PM weekly-review window | Fold the weekly review's two required outputs - clean-checkout reproduction of the in-memory vertical slice with format/lint/strict-type/test results, and the Week-1 gap list - into the **existing** Fri Jul 31, 2:15–7:30 gate-rehearsal block, which already owns rehearsal. Do not create a third Week-1 replacement block; Week 1's two optional replacements are both already allocated to Sat Jul 25. Actual roadmap hours and Jul 22-23 IIT attendance stay unreported until supplied. | Fri Jul 31 | **Open.** SQL and B1 evidence for Jul 24 is complete and reviewer-verified (B1 17/24); the review itself is marked missed rather than restaged. A Jul 25 working-tree run of `uv run --extra dev pytest -q` returned `9 passed in 0.21s`, matching the Jul 23 record - but that is the existing working tree, **not** the clean-checkout reproduction the review requires, so that item stays outstanding. No hours were inferred. |
| Jul 28 | None — multi-day block slip, not a gate | Sat Jul 25 safe async partial (lab created, notes empty, timeout/cancellation tests missing; ADR/CI not started); Sun Jul 26 entirely missed (Swift concurrency + DSA two-pointer); Mon Jul 27 entirely missed (Postgres adapter, persisted vertical slice, Repeating and Missing Number); Tue Jul 28 daytime blocks missed (transactions/idempotency, Apple architecture) | **Recovery redistribution (Jul 28 evening through Aug 2):** Tue evening: Postgres compose + adapter skeleton (6:00–7:30) + DSA Repeating and Missing Number (9:30–10:30). Wed: Postgres adapter completion + readiness (2:15–4:15), two-pointer repetition (4:30–5:00), transaction/idempotency start (5:00–6:00), IIT (6:00–8:00). Thu: signed webhooks (2:15–4:15), contract/lifecycle/failure tests + ADR (4:30–6:00), IIT (6:00–8:00). Fri: Docker + CI with Postgres (2:15–4:15), gate rehearsal (4:30–6:30), weekly review + evidence close (6:30–7:30). Sun Aug 2: Swift concurrency test (1 hr) + clean-checkout exit gate run + score + PROGRESS.md close (1 hr). **Deferred to Consolidation 1:** Apple SwiftUI observation/state architecture (only the Swift concurrency/cancellation test is retained for exit gate item 9). **Deferred within sprint:** I1 system design — use B1 (17/24, already scored) for exit test item 10. Drop/defer per sprint guide: UI polish, Docker optimization, advanced SQLAlchemy, extra endpoints. Do not drop: Postgres transaction/constraint, signed webhook duplicate behavior, cancellation/timeout test, CI, Apple concurrency test, DSA/design continuity. | Aug 2 | **Partial — Tue Jul 28 evening complete.** Postgres compose + adapter skeleton + migration + readiness endpoint verified. DSA Repeating and Missing Number solved (XOR/O(n)/O(1)) + LCS bonus. Prior-mistake note recorded (pattern-selection mismatch from Jul 21 LIS). Wed Jul 29 onwards continues per plan. |
## Application readiness
- Networking starts: December 2026.
- Selective applications start: January 2027.
... [lean-ctx: omitted 6 lines]
- Consecutive passing AI system-design mocks: 0/2.
... [lean-ctx: omitted 1 lines]
- Complete FDE simulation: not-started.
## Weekly review entry template
> Outstanding: the **Week of 2026-07-20** entry has not been written. The Fri
> Jul 24 9:11–10:11 PM review window was consumed by the B1 block overrun, and
... [lean-ctx: omitted 2 lines]
> were not observed. It is produced at the Fri Jul 31 gate-rehearsal block
... [lean-ctx: omitted 1 lines]
### Week of YYYY-MM-DD
- Planned roadmap hours:
... [lean-ctx: omitted 2 lines]
- Result I can now produce without a tutorial:
- Strongest evidence:
... [lean-ctx: omitted 2 lines]
- Quality/latency/cost/security/reliability measurement:
... [lean-ctx: omitted 1 lines]
- System-design case and score:
... [lean-ctx: omitted 1 lines]
- FDE/customer-delivery evidence:
... [lean-ctx: omitted 2 lines]
- Next week’s single most important result:


