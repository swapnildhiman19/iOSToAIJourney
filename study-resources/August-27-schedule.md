# Thursday, August 27, 2026 — Your Day, In Plain English

> **Where you are:** Day 2 of a 5-day "restart gate" (Aug 26–30). This is not a
> sprint. Nothing new is being taught. You are getting the record straight and
> making the code actually run, so that Monday's restart starts from something real.
>
> **Time today:** 3.5 hours of roadmap work, plus IIT 6:00–8:00 PM.
>
> **Full gate plan:** [`../sprints/Restart-Gate-2026-08-26.md`](../sprints/Restart-Gate-2026-08-26.md)

---

## Words this roadmap uses that nobody else does

| The roadmap says | It means |
|---|---|
| **Ledger** | The file `PROGRESS.md`. That's it. It records what you built and what proves it. |
| **Gate** | A pass/fail checkpoint. You either demonstrate the thing or you don't. |
| **Restart gate** | This week. A small checkpoint after the 4-week break, before restarting Sprint 1. |
| **Evidence** | Something reproducible — a command that runs, a test that passes, a commit SHA. Not "I read it" or "I understand it." |
| **Repair** | You started a sprint, never finished it, and will redo it. Different from "failed," which means you tried the final test and missed. |
| **Vertical slice** | One feature working all the way through — HTTP request → code → database → back out. |

---

## Why today matters for the job you're chasing

This repo exists to make you hireable as an **AI Forward-Deployed Engineer**
(primary target) with **iOS AI** as the backup path.

An FDE shows up at a customer, builds working software fast, and demos it. So the
bar is always: *does it run, and can you prove it runs?*

Right now your backend **does not persist anything.** You wrote a PostgreSQL
adapter in July, but nothing in the app ever calls it — the running API still uses
the in-memory version, so every task disappears on restart. That is the single
most important thing to fix this week. It gets fixed **Friday**.

Today clears the two things standing in the way of Friday:
1. The record of what you've done is wrong in places, and every plan gets made from it.
2. Your project fails its own quality checks, which makes any change harder to trust.

Be straight with yourself about the ratio: **today is ~55 minutes of real
engineering and ~2.5 hours of cleanup.** That's the cost of a 4-week gap. Friday
is 5 hours and mostly building.

---

## The day at a glance

| Time | What you're doing | Real work or cleanup? |
|---|---|---|
| 2:15–2:35 PM | Read 3 lines in `PROGRESS.md`, check I got them right | Cleanup |
| 2:35–3:20 PM | Write down what you can still do after a month off | Cleanup, but useful |
| 3:20–4:15 PM | Fix 13 code-quality errors in your backend | **Real work** |
| 4:15–4:30 PM | Break | — |
| 4:30–6:00 PM | Save your Swift file into a real git repo so it can't be lost | **Real work** |
| 6:00–8:00 PM | IIT KGP | Separate |

**Not today:** wiring up the database (Friday), fixing the health-check endpoint
(Saturday), DSA problems (Saturday), anything from Sprint 2 (not allowed yet).

---

# Block 1 · 2:15–4:15 PM

## Part A — 2:15–2:35 PM · Read three lines. Don't rewrite them.

**What this is:** I already wrote these into `PROGRESS.md` yesterday. You're
checking my work, not doing it. If they're right, you're done in 5 minutes.

**Open `PROGRESS.md` and find these three things:**

**1. In the big table under "Roadmap status"** — the row for Sprint 1 (attempt 1).
It should say **`repair`**.

Why that word and not "fail": you never attempted the final test. "Fail" is
reserved for when you take the test and miss. You didn't take it. Different
problem, different fix — so it gets a different word.

**2. Under "Recovery actions"** — a row dated **Aug 26**.

It should explain: you stopped after July 28, four weeks passed, so everything
moved 6 weeks later (target is now May 12, 2027 instead of March 31), and two
things you'd cut back in July got put back in.

**3. At the very top, under "Current focus"** — it should say you're on the
restart gate right now, not Sprint 1.

**If all three are right:** say so, close the file, move on. Do not spend the
leftover 15 minutes polishing wording. That is the exact habit that ate your
July.

---

## Part B — 2:35–3:20 PM · What can you still do after a month off?

**Skip the jargon:** the roadmap wants a "weekly review." That means a half-page
you're supposed to write every Friday answering seven questions. **You have never
written one — not once since July 16.** That's partly why four missed weeks went
unnoticed.

**You said you did nothing since last month, so what is there to review?** Two
separate answers:

- **The week of July 20 — you did plenty.** FastAPI with proper error handling,
  the SQL work verified against a real Postgres database, and a webhook system
  design that scored 17/24. That week has real content.
- **July 27 through Aug 17 — genuinely nothing.** That's a *one-line* entry. Not
  a report. Literally: "No roadmap work. Life and Walmart. ~1 hour of DSA on
  Aug 22." Done.

### The part that's actually worth your 45 minutes

Forget the retrospective format. Answer **one question honestly**, in writing:

> **After a month away, what can I still build right now without looking anything up?**

Go down this list and mark each **can do / need to look it up / gone**:

- [ ] Set up a FastAPI endpoint that validates input and returns proper 404 / 409 / 422
- [ ] Write a SQLAlchemy async session and use it
- [ ] Write an Alembic migration
- [ ] Explain what `await` actually does in the event loop
- [ ] Explain why a database transaction rolls back
- [ ] Write a `Protocol` in Python and inject a fake implementation for tests
- [ ] Explain the webhook design you scored 17/24 on, out loud, without notes

**This is the single most useful thing you'll write today.** Anything marked "gone"
is what Monday's repair sprint needs to attack first. Anything marked "can do" is
something you can put on a resume honestly.

### Then write it down

In `PROGRESS.md`, scroll to the section **"Weekly review entry template."** Below
the blank template, add a new section:

```markdown
### Week of 2026-07-20

- Planned roadmap hours: ~24
- Actual roadmap hours: not observed — never recorded that week
- What I can now do without a tutorial: [your list from above]
- Strongest evidence: [name the files / commands that prove it]
- Which exit criterion remains unproven: 9 of Sprint 1's 10 items
- What failed, and what kind of failure: life/work disruption — not a skill gap,
  not a broken tool. The roadmap's own fix for this category is a smaller week
  and a scope cut, which is what the Aug 26 six-week shift did.
- Next week's single most important result: a task that actually saves to
  Postgres and is still there after a restart.

### Weeks of 2026-07-27, 08-03, 08-10, 08-17 — missed

No roadmap work recorded. Only activity: ~1 hour of DSA on Sat Aug 22
(0/1 knapsack, committed Aug 26 as `82b2282`). Hours not observed.
```

**On hours: write "not observed." Do not guess a number.** A made-up 24 would
make every future capacity decision wrong. "I don't know" is a real answer.

**Stop at 3:20.** If you only finish the July 20 entry, that's fine — the missed-weeks
entry is the first thing on the drop list.

---

## Part C — 3:20–4:15 PM · Fix the 13 code-quality errors

**This is the real work of the day.**

### What "the debt" actually is

You set up three automatic checkers in your own project. When you committed
`53f549a` on July 28, you didn't run them. Here's what they're saying:

| Tool | What it checks | Complaints |
|---|---|---|
| `ruff format` | Spacing, indentation, line length | 4 files need reformatting |
| `ruff check` | Bug-prone patterns, unused imports, import order | 8 errors |
| `mypy` | Whether your type annotations are correct and complete | 1 error |

**Verified 11:40 PM last night — still exactly this:**

```
health.py:13   B008    Depends() used as a default argument value
health.py:19   B904    raise inside except without "from"
health.py:21   RUF010  use {exc!s} instead of {str(exc)}          [auto-fixable]
database.py:3  I001    imports out of order                       [auto-fixable]
database.py:4  UP035   import AsyncGenerator from collections.abc [auto-fixable]
database.py:13 E501    line is 91 chars, limit is 88
postgres_tasks.py:3  I001  imports out of order                   [auto-fixable]
postgres_tasks.py:4  F401  "select" imported but never used       [auto-fixable]

mypy: health.py:13 — function is missing a return type annotation
```

**Why an FDE cares:** you can't hand a customer a project that fails its own
checks. And these aren't nitpicks — two of them are real design problems, one of
them is a small security leak.

### Step 1 — Let the tools fix what they can (5 min)

```bash
cd "AI Solutions Platform" && uv run ruff format src tests
```

```bash
cd "AI Solutions Platform" && uv run ruff check src tests --fix
```

The formatter handles the long line. `--fix` handles 5 of the 8 errors. That
leaves three that need you to make a decision.

### Step 2 — `B008`: the one worth understanding (20 min)

**Your current code** in `src/ai_solutions_platform/api/routes/health.py`:

```python
async def readiness_probe(session: AsyncSession = Depends(get_db_session)):
```

**What the tool is complaining about:** normally, putting a function call as a
default value is a classic Python bug — the call runs *once* when the file loads,
and every caller shares that one result.

**But here the tool is wrong, and you should know why.** In FastAPI,
`Depends(...)` isn't really a default value. It's a marker that FastAPI reads out
of the function signature to figure out what to hand you. The tool's suggested
fix ("use a module-level singleton") would break dependency injection entirely.

**FastAPI's own answer** is to move the marker out of the default slot and into
the type annotation:

```python
from typing import Annotated

DbSession = Annotated[AsyncSession, Depends(get_db_session)]

async def readiness_probe(session: DbSession) -> dict[str, str]:
```

This satisfies the checker honestly instead of silencing it, and the `DbSession`
alias is reusable by every route that needs a database — which matters tomorrow,
when you wire up the real adapter and suddenly have several.

**Why this is worth 20 minutes and not 2:** being able to say *"the linter is
right about Python in general and wrong about FastAPI specifically, and here's
the framework's own resolution"* is exactly the kind of reasoning an FDE
interview probes for. Anyone can silence a warning.

Adding `-> dict[str, str]` also clears the mypy error. Two birds.

### Step 3 — `B904`: exception chaining, and a small leak (15 min)

**Your current code:**

```python
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Database unready: {str(exc)}",
        )
```

**Two problems in four lines:**

1. **No `from exc`.** Python can't tell the difference between "this error
   happened *while handling* another error" and "my error handler itself crashed."
   The traceback you get at 2 AM in production is worse for it.

2. **You're returning the database error text to whoever called the endpoint.**
   Health-check endpoints are often unauthenticated. A SQLAlchemy connection
   failure message can include your host, port, database name, and sometimes the
   username. Log it; don't return it.

```python
    except Exception as exc:
        logger.warning("Readiness probe failed", exc_info=exc)
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Database unready",
        ) from exc
```

The `RUF010` complaint disappears with this rewrite too.

*(There's a second, bigger security item — a plaintext password committed in
`alembic.ini`. Leave it. It's already logged for the repair sprint. Don't open
that thread today.)*

### Step 4 — Prove it (10 min)

```bash
cd "AI Solutions Platform" && uv run ruff format --check src tests && uv run ruff check src tests && uv run mypy src tests && uv run --extra dev pytest -q
```

**You want:** format clean, 0 ruff errors, 0 mypy errors, **9 tests passed**.

If a test broke, you changed behavior and not just style. Read the failure before
touching anything else.

**Keep the terminal output.** That transcript is your evidence.

### Do not start wiring the database

That's Friday's 4:30–6:30 block and it needs the full two hours. **Stop at 4:15.**

---

# Block 2 · 4:30–6:00 PM · Save your Swift work so it can't be lost

**This is the iOS AI lane — your backup career path. 1.5 hours.**

### The problem, in one command

```
$ git -C ~/Desktop/AI/iOS-Apps log --oneline
fatal: your current branch 'main' does not have any commits yet
```

`~/Desktop/AI/iOS-Apps` is a git repo with **zero commits in it.** Your
`TaskListFeature.swift` has never been committed anywhere. It exists only as a
loose file on your disk.

That means: one bad `git checkout` and it's gone. And more importantly for a job
hunt — **nobody can look at it.** You can't link it, an interviewer can't clone
it, and you can't prove when you wrote it. Uncommitted work doesn't count as
portfolio evidence.

### Part A — 4:30–5:00 · Make a proper repo

```bash
mkdir -p ~/Desktop/AI/iOS-Apps/AppleAILab && cd ~/Desktop/AI/iOS-Apps/AppleAILab && git init
```

Add a `.gitignore` so Xcode's junk doesn't get committed:

```gitignore
.DS_Store
build/
DerivedData/
*.xcuserstate
xcuserdata/
.swiftpm/
```

### Part B — 5:00–5:20 · Move the file and check it still compiles

```bash
mv ~/Desktop/AI/iOS-Apps/iOSToAIJourney/Sprint-01-AI-Software-Foundations/TaskListFeature.swift ~/Desktop/AI/iOS-Apps/AppleAILab/
```

```bash
cd ~/Desktop/AI/iOS-Apps/AppleAILab && xcrun swiftc -typecheck TaskListFeature.swift; echo "EXIT=$?"
```

You want `EXIT=0`. I ran this last night at the old path and got 0 — you're
re-running it at the new path, because your evidence has to describe the file
you're actually committing.

*(Side note for tomorrow, not today: your active Xcode switched from the beta 27
back to stable 26.3 at some point. Nothing's broken. It goes in Friday's
toolchain check.)*

### Part C — 5:20–5:40 · Commit it and write down the SHA

```bash
cd ~/Desktop/AI/iOS-Apps/AppleAILab && git add -A && git commit -m "Apple AI Lab: task list state, protocol, and fake service foundation" && git log --oneline
```

**Copy the SHA into `PROGRESS.md`.** A commit whose SHA you didn't record is the
same problem in a new place.

### Part D — 5:40–6:00 · Update the record honestly

In `PROGRESS.md`, find the sentences describing this Swift file as
"working-tree-only / non-durable." Replace them with the new path and the SHA.
**Keep the note that it used to be non-durable** — that's history, not a mistake
to erase.

**Now the important part: don't oversell what this file is.** I opened it last
night. It's **77 lines**:

| What's in it | What is NOT in it |
|---|---|
| `TaskItem` struct | Any `@Observable` model |
| `TaskListState` — idle, loading, empty, content, error, cancelled | Any SwiftUI `View` |
| `ServiceScenario` — success, empty, failure, slow | Any test |
| `TaskListServiceProtocol` + error type | Actor integration |
| `MockTaskListService` with fake delays | Cancellation handling in UI |

So it's a solid **foundation** — the data model, the protocol, and a fake service
you can test against. It is **not** a working SwiftUI feature. Write it that way.

And that's fine. The roadmap explicitly allows stopping a first Apple session
right here. The view, the observable model, cancellation, and tests were put back
into the repair sprint starting Monday. They're not missing — they're scheduled.

### One warning

**Do not run `git add` or `git commit` in the `~/Desktop/AI/iOS-Apps` parent
folder.** It's in a tangled state — ten of your other projects got accidentally
staged inside it. Untangling that is not this week's job and you could lose real
work. Only touch the new `AppleAILab` folder.

### Stop at 6:00 PM for IIT.

---

# Checklist — tick these before bed

**Block 1A — the three lines**
- [ ] Sprint 1 row says `repair`
- [ ] Aug 26 recovery row is there
- [ ] "Current focus" says restart gate
- [ ] I didn't rewrite anything that was already fine

**Block 1B — what I can still do**
- [ ] Went through the 7-item recall list and marked each honestly
- [ ] Wrote the Week of 2026-07-20 entry
- [ ] Wrote "not observed" for hours instead of guessing
- [ ] Wrote the one-line missed-weeks entry *(droppable)*

**Block 1C — code quality**
- [ ] `ruff format` and `ruff check --fix` run
- [ ] `B008` fixed with `Annotated` — and I can explain why the linter's own
      suggestion was wrong here
- [ ] `B904` fixed with `from exc`, and the DB error text no longer leaks out
- [ ] Return type added, mypy clean
- [ ] **9 tests still passing**
- [ ] Saved the terminal output

**Block 2 — Swift**
- [ ] `AppleAILab` repo created with a `.gitignore`
- [ ] File moved, type-check re-run, `EXIT=0`
- [ ] Committed, SHA written into `PROGRESS.md`
- [ ] Described as a foundation, not a finished feature
- [ ] Parent `iOS-Apps` folder left alone

---

# If the day runs short, drop in this order

1. **Drop first:** the one-line missed-weeks entry. Nobody needs it tonight.
2. **Drop second:** the code-quality fixes — they go back to Friday 4:30, which
   is where they came from. Costs you wiring time tomorrow.
3. **Never drop:** the "what can I still do" list, and the Swift commit. Those
   are the two things today exists for.

---

# What's coming

| Day | Hours | The point of it |
|---|---|---|
| **Fri Aug 28** | 5 | Recheck your tools, reread your Postgres notes, then **make the database actually work** — the big one |
| **Sat Aug 29** | ~3 | Fix the health-check endpoint that currently lies; redo the knapsack problem from scratch + 2 overdue DSA problems |
| **Sun Aug 30** | 2 | Write a real database test, clone the repo fresh and check it starts, then **score this week pass/fail** |
| **Mon Aug 31** | — | Sprint 1 restarts properly. Don't touch it before then. |

---

# How this week gets scored on Sunday

Seven things. All seven have to work.

| # | The test | Where it stands now | Does today move it? |
|---|---|---|---|
| 1 | Fresh clone → Postgres and API start using only the README | Not started | No |
| 2 | `alembic upgrade head` runs clean | Migration exists, worked in July | No |
| 3 | Create a task, read it back, **and see the row in `psql`** | Blocked — adapter isn't wired up | No — Friday |
| 4 | Restart the container, record is still there | Blocked by #3 | No |
| 5 | format / lint / mypy / tests all green | 13 failures | **Yes — Block 1C** |
| 6 | Stop Postgres → health check returns 503, not a false "OK" | Two endpoints, one of them lies | No — Saturday |
| 7 | `PROGRESS.md` claims nothing it can't prove | Mostly true, reviews missing | **Yes — Blocks 1A, 1B, 2D** |

**Two of seven move today.** For 3.5 hours, that's the right amount. Don't try to
do Friday's work tonight.
---

## Closed out — executed Friday, August 28

> This plan ran a day late, on Friday afternoon. Continue at
> [`August-28-evening.md`](August-28-evening.md).

**Verified by re-running the checks, not by taking your word for it:**

| Block | Result |
|---|---|
| 1A · Read three lines in `PROGRESS.md` | Done. Confirmed correct. |
| 1B · What can you still build after a month off? | Done, and honestly — you said up front that you looked things up, which is what made the result usable. |
| 1C · Fix the code-quality errors | **Done.** All four gates green, 9 tests pass. **Exit-test item 5 closed.** |
| 2 · Commit the Swift file | **Done.** `AppleAILab` is a real repo; commit `85b14c1`; type-check exits 0. |

**Two corrections to what this file predicted:**

1. It said "13 errors." The real count was **7 `ruff` findings plus 4 files
   needing reformatting**, and `mypy` was already clean once the formatter ran.
   Nothing was hidden — the estimate was just built from a stale count.
2. It called Block 1B a review. What it actually produced was a **diagnostic**,
   and it found something: four concepts came back intact (Alembic, `await`,
   transaction rollback, `Protocol` + fake), one came back **wrong**
   (SQLAlchemy — `async` was explained as providing atomicity, which it does
   not), and the B1 webhook design **failed** — it came back as a WebSocket.
   That last one is the real result of the day. See
   [`August-28-evening.md`](August-28-evening.md) → *The webhook problem*.

**Still open from today:** the backend fix is uncommitted. First action Friday
evening.
