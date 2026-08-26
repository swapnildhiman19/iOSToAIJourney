# Restart Gate — August 26–30, 2026

> Dates: Wednesday, August 26–Sunday, August 30, 2026
> Required roadmap time: approximately 10.5 hours, plus Saturday as replacement
> capacity
> Outcome: a truthful ledger and a foundation that actually runs
> Status when authored: active

## In plain language

You stopped after Tuesday July 28 and four weeks passed. Two things broke in
that time, and they are different kinds of broken.

The **record** stopped being true. `PROGRESS.md` still says "Wed Jul 29 onwards
continues per plan." No weekly review has ever been written. Four weeks are
unaccounted for. A ledger that overstates reality is worse than no ledger,
because every later decision is made from it.

The **code** never worked. Commit `53f549a` is titled "Postgres foundation," but
`PostgresTaskRepository` is imported by nothing — `api/app.py` still hardcodes
the in-memory adapter, so the running API persists nothing at all. The same
commit also broke the project's own quality gates.

This gate fixes both, and adds nothing. It is deliberately not a sprint: there
is no new competency, no new framework, and no new scope. It exists because
`04-Weekly-Operating-System.md` says two consecutive weeks below the
minimum-viable plan trigger a roadmap pause and a smaller restart gate. Four
occurred.

Failing this gate is an acceptable outcome. It is recorded, and the Sprint 1
repair sprint absorbs the residue.

## Prerequisites

- Orientation passed (July 20, 2026).
- Docker, `uv`, Python 3.12+, and Git available.
- Access to the sibling repositories under `~/Desktop/AI/iOS-Apps/`.

## What is deliberately not here

- **No system-design case.** A gate does not carry lane quotas, the same way a
  consolidation week does not. I1 is restored into the Sprint 1 repair sprint
  starting August 31, where it was always scheduled.
- **No new DSA pattern.** Only the two overdue spaced repetitions, which are
  repair, not new content. Full 4 h/week DSA resumes August 31.
- **No Sprint 2 material.** Reading ahead is not permitted by the optional-block
  policy and is not permitted here.

---

## Dated sessions

### Wednesday, August 26

Blocks 2:15–4:15 and 4:30–6:30 have elapsed. IIT KGP runs 6:00–8:00 PM.

#### 9:30–10:30 PM — Ledger truth pass, part 1 (1 hour)

- **Stage:** Evidence.
- **Assumed prerequisite:** none. This is recording, not building — correct work
  for a low-energy first hour back.
- **Topic:** make the record match reality before touching any code.
- **Build:**
  1. In `~/Desktop/AI/iOS-Apps/DSA`, commit the uncommitted `DSA6.swift`
     (0/1 knapsack, recursive only — the memoisation was started and left as an
     empty comment). **Done Aug 26: commit `82b2282`**, and the ledger row now
     records the session as incomplete rather than "recursive, then memoized."
     Durable first, cited second.
  2. Open the [Striver SDE Sheet](https://takeuforward.org/dsa/strivers-sde-sheet-top-coding-interview-problems)
     and confirm the baseline recorded on your behalf: **172/191** — Easy 25/25,
     Medium 85/93, Hard 62/73, with **DP 3/7**, **DP Part-II 0/8**, and **Trie 0/7**
     as the only incomplete topics. If any number has moved, correct
     `PROGRESS.md` → **DSA ledger summary** → *Striver baseline*. A baseline you have
     not looked at yourself is not a baseline.
  3. Skim `06-DSA-Track.md` → *Problem sources* and *Sprint syllabus*. The four-phase
     sequence (complete the 19 gaps → revise all 191 → Taro lists → maintenance) is
     what the next eight months of DSA follow. If the phase order does not match how
     you actually want to work, say so now rather than in October.
- **Already recorded for you, verify rather than redo:** the four missed weeks in
  **Weekly hours**, the overdue repetitions, and the Aug 22 session are already in
  `PROGRESS.md`. Your job tonight is the SHA and the two confirmations above.
- **Evidence:** a DSA commit SHA in the ledger, and a personally-verified Striver
  baseline.
- **Stop at 10:30 PM.** Do not start scoring Sprint 1 tonight.

### Thursday, August 27

#### 2:15–4:15 PM — Ledger truth pass, part 2 (2 hours)

- **Stage:** Evidence.
- **Topic:** close the first Sprint 1 attempt honestly and reconstruct the
  missing reviews.
- **Build:**
  1. Score the July 20–August 2 Sprint 1 attempt against its **real** exit test
     (`sprints/Sprint-01-AI-Software-Foundations.md` → *Exit test*). The honest
     count is 1 of 10 items proven (item 10, B1 at 17/24). Set the Roadmap status
     row to **`repair`**, not `fail` — the gate was never attempted, and
     `08-Assessment-and-Recovery.md` reserves `fail` for an attempted gate.
  2. Add a **Recovery actions** row dated Aug 26 describing the pause, this gate,
     the +6 week shift, and the restoration of the two July 28 deferrals.
  3. Write the overdue **Weekly review entry** for the week of Jul 20 using the
     seven questions in `04-Weekly-Operating-System.md`. Answer question 4
     ("what failed, and what category of failure was it?") against the
     `08-Assessment-and-Recovery.md` taxonomy — this one is *life/work
     disruption*, and naming it correctly is what makes it repairable.
  4. Update **Current focus** and **Active sprint gate** to this restart gate.
- **Evidence:** Sprint 1 row reads `repair` with the 1/10 count; a dated recovery
  row; at least one written weekly review.
- **Stop:** do not rewrite any historical score or evidence. Append only.

#### 4:30–6:00 PM — Apple evidence durability (1.5 hours)

- **Stage:** Evidence.
- **Assumed prerequisite:** Git. No Swift authoring in this block.
- **Topic:** the Apple lane's evidence currently does not exist in any commit.
  `~/Desktop/AI/iOS-Apps` is a repository on branch `main` with **zero commits**,
  so `TaskListFeature.swift` is working-tree-only and proves nothing reproducible.
- **Build:**
  1. Create `~/Desktop/AI/iOS-Apps/AppleAILab/` as its **own** git repository,
     matching the pattern the other ten projects in that folder already use.
  2. Move `iOS-Apps/iOSToAIJourney/Sprint-01-AI-Software-Foundations/TaskListFeature.swift`
     into it. Add a `.gitignore` (Xcode, `DerivedData`, `.DS_Store`).
  3. Re-run `xcrun swiftc -typecheck TaskListFeature.swift` and capture the exit
     code. The previous exit-0 result was never re-verified.
  4. Commit. Capture the SHA.
  5. In `PROGRESS.md`, replace the "working-tree-only / non-durable" language for
     this artifact with the new repo path and SHA. Keep the historical note that
     it *was* non-durable — that is evidence history, not a mistake to erase.
- **Evidence:** `git -C ../iOS-Apps/AppleAILab log --oneline` shows a real commit
  containing the artifact; `PROGRESS.md` cites the SHA.
- **Do not** stage, commit, or clean the `iOS-Apps` parent repository. It has ten
  nested repos accidentally staged as gitlinks; untangling it is not this gate's
  work and risks real data.
- **Stop at 6:00 PM** for IIT KGP (6:00–8:00).

### Friday, August 28

#### 2:15–4:15 PM — Toolchain recheck and context reload (2 hours)

- **Stage:** Learn (reload), then Evidence.
- **Topic:** six weeks of drift, and your own notes have gone cold.
- **Build:**
  1. Re-run the environment baseline: `python3 -V`, `uv --version`,
     `docker --version`, `docker compose version`, `swift --version`,
     `xcodebuild -version`, `xcrun simctl list runtimes`. Compare against the
     July 16 baseline in `PROGRESS.md` and record every change.
  2. Refresh `09-Current-Stack-Snapshot.md`. It is dated July 16 and explicitly
     marked stale. Recheck at minimum: the current Gemini model line (the
     snapshot pins `gemini-2.5-pro` while a newer 3.x line was already flagged),
     the MCP specification status (the `2026-07-28` candidate has now passed its
     date), and Xcode 27 / OS 27 release status. Record stable versus preview.
  3. Re-read `notes/sprint-01-AI-Software-Foundations-notes-04-postgreSQL-connection-understanding.md`.
     This is the AsyncEngine / Session / Pool / Alembic material you will need in
     the next block, and it is 2,208 lines you wrote and have not seen in a month.
- **Evidence:** a dated stack-refresh row in `PROGRESS.md` → **Stack refreshes**;
  updated `09-Current-Stack-Snapshot.md`.

#### 4:30–6:30 PM — Repair `53f549a`, part 1 (2 hours)

- **Stage:** Independent build.
- **Assumed prerequisite:** the adapter-swap defense reviewed at 3/4 on July 22.
  That review told you exactly what to do here; this is you doing it.
- **Topic:** make the persistence adapter reachable, and restore the quality gates.
- **Build:**
  1. Clear the lint and type debt first — it is mechanical and it unblocks
     everything after it. `ruff check src tests` reports 8 errors,
     `ruff format --check` 4 files, `mypy src tests` 1 error, all in
     `persistence/database.py`, `persistence/postgres_tasks.py`,
     `api/routes/health.py`, and `api/app.py`. Note what each error was actually
     telling you; `B008` and `B904` in `health.py` are real design feedback, not
     noise.
  2. **The main event:** wire `PostgresTaskRepository` into the application.
     `api/app.py` and `api/dependencies.py` currently make
     `InMemoryTaskRepository` the only reachable adapter. Choose the composition
     point deliberately, keep the in-memory adapter available for tests, and do
     not let a SQLAlchemy type escape into `domain/` or `application/`.
  3. Verify by observation, not by assumption: start the API, `POST /tasks`, then
     confirm the row in `psql` — not just in the HTTP response.
- **Evidence:** all four gates green; a `psql` transcript showing the row.
- **Stop at 6:30 PM.**

#### 6:30–7:30 PM — Weekly review (1 hour)

- **Stage:** Evidence.
- Answer the seven review questions for this week. Record actual hours — the real
  ones. This is the first honest hours entry since July 20 and it calibrates
  everything that follows.
- Write the remaining overdue weekly reviews if time allows.

### Saturday, August 29

Saturday carries no required study. It is replacement capacity, and this gate has
work to replace.

#### Replacement block A (~2 hours) — Repair `53f549a`, part 2

- **Stage:** Independent build.
- **Build:**
  1. Resolve the readiness contradiction. `GET /ready` in `api/routes/tasks.py`
     returns ready unconditionally — its own docstring admits it is a placeholder
     — and `tests/api/test_tasks.py` asserts that behavior, locking the lie in.
     `GET /healthz/ready` in `api/routes/health.py` does the real `SELECT 1` and
     has zero coverage. Keep one. Delete the other and the test that protects it.
  2. Fix `.env.example`: `DATABASE_URL` currently reads
     `postgresql://localhost:5432/ai_solutions` — wrong database name, no
     credentials, and no `+asyncpg` driver. `compose.yaml`, `alembic.ini`, and
     `database.py` all agree on
     `postgresql+asyncpg://postgres:postgrespassword@localhost:5432/task_db`.
  3. Note for the repair sprint, do not fix now: `alembic.ini` is tracked in git
     with a plaintext password. Acceptable for local dev, but it belongs in the
     Sprint 1 security discussion.
- **Evidence:** one readiness endpoint, tested against a **stopped** database and
  proven to return 503.

#### Replacement block B (~1 hour) — Overdue DSA repetitions

**Added Aug 26: start with the knapsack re-derivation.** Wednesday's memoisation was
repaired by the assistant, so it is recorded as `learned`, not `solved`, and the
independent solve is still owed. Open a blank file — do **not** open
`DSA6.swift` — and rebuild the memoised version from the recurrence. Then answer
aloud, without checking: *why does memoisation turn O(2^n) into O(n x capacity)?*
If either part needs the file, tag it `learned` again and repeat Sep 2.

- **Stage:** Evidence.
- Both scheduled repetitions are overdue: Maximum Product Subarray (~Aug 3) and
  Repeating and Missing Number (~Aug 11). Solve from memory, time them, and
  record the result and next interval in Notion, per the record boundary in
  `06-DSA-Track.md` → *Problem ledger*. Repetition is repair, not new content.
- Both are useful calibration for Phase A, which starts Monday: Maximum Product
  Subarray **is** dynamic programming, so how it goes is an early read on the
  pattern you are about to spend four weeks on.

### Sunday, August 30

#### 2 hours — Prove it, then score the gate

- **Stage:** Evidence.
- **Build:**
  1. Add real fixtures to `tests/conftest.py`. It is currently a one-line
     docstring named "Shared test fixtures" that defines zero fixtures. You need
     a database fixture with per-test rollback.
  2. Write the first integration test that actually touches Postgres.
     `tests/integration/` contains only `.gitkeep`, and all 9 existing tests
     exercise the in-memory adapter.
  3. **Run the clean-checkout reproduction** — outstanding since July 24. Clone
     to a fresh directory, follow only the documented README commands, and record
     the exact transcript. If the README is wrong, the README is the bug.
  4. Score this gate. Record the result in `PROGRESS.md` whichever way it lands.
- **Stop:** do not begin Sprint 1 repair work. It starts Monday.

---

## Required outputs

- `PROGRESS.md` reflects the missed period, the Sprint 1 `repair` status, the
  Aug 26 recovery action, the Aug 22 DSA session, the Apple repo SHA, and at
  least one written weekly review.
- `09-Current-Stack-Snapshot.md` refreshed and dated.
- `AppleAILab` exists as a repository with a real commit.
- `AI Solutions Platform` passes format, lint, strict type check, and tests.
- A persisted task record demonstrated in `psql`.
- A clean-checkout transcript.

## Exit test

Run without a tutorial:

1. From a fresh checkout, start Postgres and the API through the documented
   commands only.
2. `alembic upgrade head` applies cleanly.
3. `POST /tasks` then `GET /tasks/{task_id}` returns the record, **and** the row
   is visible in `psql`.
4. Restart the container; the record is still there.
5. `ruff format --check`, `ruff check`, `mypy src tests`, and `pytest -q` are all
   green.
6. Stop Postgres; the readiness endpoint returns 503 rather than a false green.
7. `PROGRESS.md` contains no claim stronger than its evidence, and the four
   missed weeks are marked missed with no inferred hours.

**Pass:** items 1–7 all hold.
**Partial:** the ledger items hold but the vertical slice does not; the residue
moves into the Sprint 1 repair sprint's first block and is recorded as carried.
**Fail:** the ledger is still untrue on August 30. Repair before any new content —
`README.md` non-negotiable rule 9.

This gate is scored pass/partial/fail only. It does **not** use the five-part
`/15` sprint rubric; that belongs to the September 13 sprint close.

## What this gate closes

Sprint 1 exit-test items **1** and **2**, and part of item **5**. Items 3, 4, 6,
7, 8, and 9 remain for the repair sprint. Item 10 already passed.

## Official resources

- [SQLAlchemy asyncio](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html)
- [Alembic](https://alembic.sqlalchemy.org/)
- [FastAPI dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/)
- [FastAPI async tests](https://fastapi.tiangolo.com/advanced/async-tests/)
- [pytest fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html)
- [Ruff rules](https://docs.astral.sh/ruff/rules/)
- [mypy strict mode](https://mypy.readthedocs.io/en/stable/command_line.html#cmdoption-mypy-strict)

## Drop/defer order

If time runs short, drop in this order:

1. The second and third overdue weekly reviews (keep the week of Jul 20).
2. The Saturday DSA repetitions — reschedule into the repair sprint's DSA hours.
3. The integration test — but only if the `psql` demonstration succeeded.

Do not drop:

- the truthful ledger close;
- wiring `PostgresTaskRepository` into the application;
- the readiness-endpoint resolution;
- the Apple repository commit;
- the clean-checkout reproduction.
