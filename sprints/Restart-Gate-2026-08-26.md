# Restart Gate — August 26–30, 2026

> Dates: Wednesday, August 26–Sunday, August 30, 2026
> Required roadmap time: approximately 10.5 hours, plus Saturday as replacement
> capacity
> Outcome: a truthful ledger and a foundation that actually runs
> Status when authored: active

> **Revision 1 — 11:45 PM, Wednesday August 26, 2026.** Thursday's 2:15–4:15
> block was re-planned after checking its own work: three of its four items were
> already recorded in `PROGRESS.md` when this guide was written at 18:59 IST.
> The freed ~55 minutes absorb the lint/format/type cleanup that had opened
> Friday's 4:30–6:30 repair block, so Friday now has two uninterrupted hours for
> wiring `PostgresTaskRepository`. **Total required hours, every exit-test item,
> every date, and the drop/defer order are unchanged** — this moves work earlier
> within the gate, it does not add, remove, or weaken any of it. A per-day
> executable version of Thursday lives at
> [`../study-resources/August-27-schedule.md`](../study-resources/August-27-schedule.md).

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

> **Revised 11:45 PM, Wednesday August 26.** The 2:15–4:15 block was authored
> before its own work was checked. Three of its four items — the Sprint 1
> `repair` scoring, the Aug 26 recovery row, and the Current focus / Active
> sprint gate update — were **already written into `PROGRESS.md`** when this gate
> was authored at 18:59 IST. Only the weekly review is genuinely outstanding.
> The freed ~55 minutes are reallocated **inside the same two-hour block** to the
> lint/format/type cleanup that was Friday's first repair item. No hours are
> added, no exit-test item changes, and Friday keeps a full two hours for the
> wiring itself — the highest-risk work in this gate.
>
> Executable detail for the day:
> [`../study-resources/August-27-schedule.md`](../study-resources/August-27-schedule.md).

Roadmap time today: 3.5 hours (2:15–4:15, 4:30–6:00), matching the Thursday
budget in `04-Weekly-Operating-System.md`. IIT KGP runs 6:00–8:00 PM. No home
block is required.

> **Executed Friday, August 28 — one day late.** Every block below ran on Friday
> afternoon instead of Thursday. **Done and reviewer-verified:** the four quality
> gates are green (16:37 IST), closing exit-test item 5; `AppleAILab` is a real
> repository with commit `85b14c1`, closing the Apple durability output. **Not
> clean:** the backend fix is still uncommitted, and the unaided B1 re-test
> failed — webhook ingestion came back as a WebSocket, so a **conceptual gap** is
> now open (`PROGRESS.md` → System-design ledger, Recovery actions). The cost of
> the slip is Friday's own 2:15–4:15 block, which elapsed unexecuted and moves
> once to Saturday.

#### 2:15–4:15 PM — Ledger truth pass, part 2, then clear the quality debt (2 hours)

##### 2:15–2:35 PM — Read three lines in `PROGRESS.md`; do not rewrite them (20 minutes)

- **Stage:** Evidence.
- **Topic:** confirm what is already recorded instead of writing it twice.
- **Check these three in `PROGRESS.md` and correct only what is actually wrong:**
  1. **Roadmap status** → the Sprint 1 (attempt 1) row reads **`repair`**, with
     "1 of 10 exit-test items proven (item 10, B1 17/24)".
     `08-Assessment-and-Recovery.md` reserves `fail` for an *attempted* gate;
     this one was never attempted, so `repair` is the correct status.
  2. **Recovery actions** → a row dated **Aug 26** covering the pause, this gate,
     the +6 week shift, and the restoration of the two Jul 28 deferrals.
  3. **Current focus** and **Active sprint gate** → both point at this restart
     gate and its seven-item exit test.
- If all three hold, that *is* the finding. Write nothing and move on.
- **Evidence:** none produced. This is a verification step, not a recording step.

##### 2:35–3:20 PM — Write down what you can still do after a month off (45 minutes)

- **Stage:** Evidence. This is the one part of the original block that is real
  outstanding work: **no weekly review has ever been written.**
- **In plain language:** a "weekly review" is half a page you are meant to write
  every Friday. You have never written one. A month-late retrospective is low
  value, so the block is pointed at the one question that is *not* stale:
  **after four weeks away, what can you still build without looking it up?**
  Go down the Sprint 1 competency list and mark each item *can do / need to look
  it up / gone*. Whatever comes back "gone" is what Monday's repair sprint
  attacks first. Write that list down first; the entry below is its container.
- **Build:**
  1. Write the **Week of 2026-07-20** entry using the seven questions in
     `04-Weekly-Operating-System.md` → *Weekly review template*, appended under
     `PROGRESS.md` → **Weekly review entry**. Keep the blank template in place
     and add a real dated `### Week of 2026-07-20` section beneath it.
  2. Question 4 asks what failed and in which category. Answer it against the
     recovery decision tree in `08-Assessment-and-Recovery.md`: this is
     **Life/work disruption**, whose prescribed action is the 9.5-hour
     minimum-viable week plus a scope cut — which is exactly what the Aug 26
     revision applied. Naming the category correctly is what makes it repairable
     rather than shameful.
  3. Then write **one combined entry** for the weeks of 2026-07-27, 2026-08-03,
     2026-08-10, and 2026-08-17: recorded as missed and **not observed**. Do not
     reconstruct hours you never recorded. "Not observed" is a complete and
     honest answer; an invented number is not.
- **Evidence:** at least one complete seven-question review in `PROGRESS.md`.
- **Stop:** append only. Do not rewrite any historical score or evidence.

##### 3:20–4:15 PM — Fix the 13 code-quality errors in the backend (55 minutes)

- **Stage:** Independent build. **Pulled forward from Friday 4:30–6:30, item 1**,
  into the time freed above. Friday's block is correspondingly reduced.
- **Assumed prerequisite:** none beyond running the project's own tools. This is
  deliberately mechanical work placed at the end of a recording block.
- **Topic:** `53f549a` landed without running the gates the project already
  defines. **Re-verified 11:40 PM Aug 26 — unchanged:** 8 `ruff check` errors, 4
  files failing `ruff format --check`, and 1 `mypy` error, every one of them in a
  file that commit introduced.
- **Build, in this order:** `ruff format` first (it absorbs the `E501` in
  `database.py`), then `ruff check --fix` (5 of the 8 are autofixable), then the
  three that need a decision from you — `B008` and `B904` in
  `api/routes/health.py`, and the missing return annotation `mypy` reports on the
  same function. **`B008` is real design feedback, not noise:** FastAPI's own
  answer is `Annotated[AsyncSession, Depends(get_db_session)]`, not the
  module-level singleton Ruff's generic message suggests.
- **Evidence:** `ruff format --check src tests`, `ruff check src tests`,
  `mypy src tests`, and `uv run --extra dev pytest -q` all green in one
  transcript, with pytest still at **9 passed**.
- **Do not** start wiring `PostgresTaskRepository` in this block. That is
  Friday's work and it needs the full two hours.

#### 4:30–6:00 PM — Commit the Swift file so it cannot be lost (1.5 hours)

- **Stage:** Evidence.
- **Assumed prerequisite:** Git. **No Swift authoring in this block.**
- **Topic:** the Apple lane's evidence currently does not exist in any commit.
  **Re-verified 11:30 PM Aug 26:** `~/Desktop/AI/iOS-Apps` is a repository on
  branch `main` with **zero commits** — `git log` answers "your current branch
  'main' does not have any commits yet" — so `TaskListFeature.swift` is
  working-tree-only and proves nothing reproducible.
- **Build:**
  1. Create `~/Desktop/AI/iOS-Apps/AppleAILab/` as its **own** git repository,
     matching the pattern the other ten projects in that folder already use.
  2. Move `iOS-Apps/iOSToAIJourney/Sprint-01-AI-Software-Foundations/TaskListFeature.swift`
     into it. Add a `.gitignore` (Xcode, `DerivedData`, `.DS_Store`).
  3. Re-run `xcrun swiftc -typecheck TaskListFeature.swift` **from the new
     location** and capture the exit code. (Coach-verified exit **0** at 11:42 PM
     Aug 26 against the *pre-move* path on Xcode 26.3; the point of re-running is
     that the evidence must describe the file at the path you are committing.)
  4. Commit. Capture the SHA.
  5. In `PROGRESS.md`, replace the "working-tree-only / non-durable" language for
     this artifact with the new repo path and SHA. Keep the historical note that
     it *was* non-durable — that is evidence history, not a mistake to erase.
- **What the artifact actually is — do not overstate it when you rewrite the
  ledger line.** Verified Aug 26: the file is **77 lines** containing
  `TaskItem`, a six-case `TaskListState`, a `ServiceScenario` enum, the
  `TaskListServiceProtocol`, `TaskServiceError`, and `MockTaskListService`.
  There is **no `@Observable` model, no SwiftUI view, and no test**. This block
  changes only its *durability*. It remains the guided state/protocol/fake
  foundation that `04-Weekly-Operating-System.md` → *Apple block* explicitly
  permits stopping at; observation, the view, actor integration, cancellation UI,
  and tests are restored into the Sprint 1 repair sprint.
- **Noticed Aug 26, record Friday, do not chase today:** `xcode-select -p` now
  returns `/Applications/Xcode.app/Contents/Developer` (Xcode **26.3**, build
  17C519), while the July 16 baseline in `PROGRESS.md` records Xcode-beta 27
  beta 3 as the active developer directory. `Xcode-beta.app` is still installed.
  This belongs in Friday's toolchain-recheck row, not in this block.
- **Evidence:** `git -C ../iOS-Apps/AppleAILab log --oneline` shows a real commit
  containing the artifact; `PROGRESS.md` cites the SHA.
- **Do not** stage, commit, or clean the `iOS-Apps` parent repository. It has ten
  nested repos accidentally staged as gitlinks (`git status --short` shows the
  `AD`/`Am` entries); untangling it is not this gate's work and risks real data.
- **Stop at 6:00 PM** for IIT KGP (6:00–8:00).

### Friday, August 28

#### 2:15–4:15 PM — Toolchain recheck and context reload (2 hours) — ELAPSED, MOVED TO SATURDAY

> **Revised 4:40 PM, Friday August 28.** This window elapsed unexecuted because
> Thursday's blocks ran in it. Per `08-Assessment-and-Recovery.md` it gets **one**
> replacement and no more: Saturday, as the new Replacement block C. Friday
> evening is **not** extended to absorb it — the 4:30–6:30 wiring block is the
> highest-risk item in this gate and is not shortened for a recheck.
>
> One consequence to carry into tonight: item 3 below was the context reload for
> the wiring block. You are now wiring without having re-read the 2,208-line
> Postgres notes. **Do not fix that by reading them front to back at 4:40 PM** —
> that spends the block on reading. Open the file beside the editor and search it
> when you get stuck on session lifetime or engine construction. The Aug 28
> recall check says the concepts you need here — `await`, transactions, `Protocol`
> injection — are still intact.

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
- **Topic:** make the persistence adapter reachable.
- **Revised Aug 26:** the lint/format/type cleanup that opened this block moved to
  **Thursday 3:20–4:15 PM**. It was executed Fri Aug 28 and all four gates are
  green (verified 16:37 IST), so this block does not re-do it.
- **Revised again 4:40 PM, Fri Aug 28.** The gates are confirmed green, so step 0
  of the previous revision is already satisfied. **Do this first, and it is not
  optional:**

  ```bash
  git add -A "AI Solutions Platform" && git commit -m "fix: restore ruff/mypy gates broken by 53f549a"
  ```

  The repair currently exists only as four modified files in the working tree.
  That is the **exact** non-durability that left the July Swift artifact
  unprovable for five weeks, and you are about to edit the composition root on
  top of it. Commit the clean, isolated fix before the risky change, not after.
  Two minutes.
- **Build:**
  1. **The main event:** wire `PostgresTaskRepository` into the application.
     `api/app.py` and `api/dependencies.py` currently make
     `InMemoryTaskRepository` the only reachable adapter. Choose the composition
     point deliberately, keep the in-memory adapter available for tests, and do
     not let a SQLAlchemy type escape into `domain/` or `application/`.
  2. Verify by observation, not by assumption: start the API, `POST /tasks`, then
     confirm the row in `psql` — not just in the HTTP response.
  3. With the spare capacity this block now has, re-run all four gates plus the
     existing 9 tests against the wired application before you stop. A green
     suite that only ever exercised the in-memory adapter is not the same result.
- **Evidence:** all four gates green; a `psql` transcript showing the row.
- **Stop at 6:30 PM.**

> **DONE — verified 7:07 PM, Fri Aug 28.** The wiring works. Composition moved into the per-request
> dependency; create → read → row in `psql`; record survived a container restart; 409/404 exercised
> against the real unique constraint; readiness returns 503 during an outage. **Exit-test items 3, 4
> and 6 closed on top of item 5 — the gate is 4/7.** Three design findings and the coverage gap are
> recorded in `PROGRESS.md` → AI Solutions Platform milestones. **The block overran its 6:30 stop**,
> so the 6:30–7:30 review + B1 hour did not run and moves to Saturday.

#### 6:30–7:30 PM — Verify the reviews, then repair the B1 gap (1 hour)

> **Revised 4:40 PM, Fri Aug 28.** The two overdue weekly review entries — Week of
> 2026-07-20, and the four dead weeks as one combined entry — are **already
> written** into `PROGRESS.md` from Friday's recall exercise, which supplied their
> substance. Both leave *Actual roadmap hours* as **not observed**, because they
> never were. That frees most of this block for the conceptual gap the recall
> exercise exposed, which matters more than a retrospective.

- **Stage:** Evidence, then repair.
- **6:30–6:50 — verify, do not rewrite (20 min).** Read the two appended entries.
  You are the only one who can confirm they are true. Supply actual hours **only**
  where you genuinely remember them; leave *not observed* everywhere else. A
  guessed number is worse than a blank, because it silently recalibrates every
  plan built on top of it.
- **6:50–7:10 — repair the B1 recall failure (20 min).** Moved here from Saturday
  so it lands the same day it was found. Re-read **only** the critical-flow trace
  and the HMAC/dedup sections of
  `notes/sprint-01-AI-Software-Foundations-notes-02-b1-*.md` — not the whole
  document. Then close the notes and write, from memory:
  1. one sentence on why a webhook is an ordinary one-shot HTTP `POST` and **not**
     a persistent connection;
  2. the four failure modes the design exists to survive — unverified sender,
     slow consumer, duplicate delivery, permanent consumer failure — and the one
     mechanism you chose for each.
  This is **not** a redesign and B1 is **not** rescored; 17/24 stands. If it does
  not hold, tag it and it becomes the first block of I1 in the repair sprint.
- **7:10–7:30 — buffer.** If the wiring block overran, this is where it lands.
  Overrunning past 7:30 is what consumed the July 24 review; do not repeat it.

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
   **No longer hypothetical — demonstrated Fri Aug 28, 7:07 PM:** with Postgres stopped,
   `/healthz/ready` returned 503 while `/ready` returned 200 `{"status":"ready"}` in the same
   outage. A live false green. Item 6's evidence stands on `/healthz/ready`, but this gate should
   not close while the lying endpoint is still routable.
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

#### Replacement block D (~1 hour) — The displaced review hour and the B1 repair

> **Added 7:10 PM, Fri Aug 28.** Friday's 6:30–7:30 block did not run — the wiring overran, which
> was the right trade. It moves here intact: 20 min verifying the two written weekly reviews and
> supplying real hours, 20 min on the webhook/WebSocket repair. Do this **first** on Saturday, before
> the build blocks, because it is the part that gets dropped when a day runs long.

#### Replacement block C (~2 hours) — Toolchain recheck and stack refresh

> **Added 4:40 PM, Fri Aug 28**, holding the Friday 2:15–4:15 block that elapsed
> when Thursday ran late. This is that block's **one** permitted replacement.

- **Stage:** Evidence.
- **Build:** exactly the three items written under Friday 2:15–4:15 PM — the
  environment re-baseline against the July 16 snapshot, the
  `09-Current-Stack-Snapshot.md` refresh (Gemini model line, MCP spec status now
  that `2026-07-28` has passed, Xcode 27 / OS 27 stable-versus-preview), and the
  Postgres notes re-read.
- **Why it is not dropped:** "`09-Current-Stack-Snapshot.md` refreshed and dated"
  is a **required output** of this gate, and the snapshot is now six weeks stale
  and self-marked as such.
- **Evidence:** a dated **Stack refreshes** row in `PROGRESS.md`; updated
  `09-Current-Stack-Snapshot.md`.

#### Replacement block B (~1 hour) — Overdue DSA repetitions — DROPPED to the repair sprint

> **Dropped 4:40 PM, Fri Aug 28.** Saturday cannot hold Replacement A, the
> displaced two-hour toolchain block, **and** this. This is **item 2 of this
> gate's own drop/defer order**, invoked in sequence after item 1 (the extra
> weekly reviews) was banked by writing them early — not an ad-hoc cut. The
> repetitions move into the repair sprint's DSA hours, which start Monday
> Aug 31. The knapsack re-derivation stays first in that queue and is still
> recorded as `learned`, not `solved`. **If Saturday runs long, this stays
> dropped** — do not restore it by shortening Replacement A.

**Original text, retained for the repair sprint — start with the knapsack
re-derivation.** Wednesday's memoisation was
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
