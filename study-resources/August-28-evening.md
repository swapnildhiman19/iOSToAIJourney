# Friday, August 28, 2026 — from 4:40 PM

> Written 4:40 PM Friday. Thursday's plan ran today instead of yesterday. This
> picks up from where that left off and answers the two things you asked about.
>
> Companion files: [`August-27-schedule.md`](August-27-schedule.md) (what you just
> finished) and
> [`../sprints/Restart-Gate-2026-08-26.md`](../sprints/Restart-Gate-2026-08-26.md)
> (the whole 5-day gate).

---

## First, what actually landed today

I re-ran everything myself rather than taking your word for it. Both of these are
**verified**, not reported:

| What | Result |
|---|---|
| `ruff format --check` / `ruff check` / `mypy` / `pytest` | All four green. 9 tests pass. **Restart-gate item 5 is closed.** |
| `AppleAILab` repository | Real repo, commit `85b14c1`, 77-line Swift file + `.gitignore`, clean tree, type-check exits 0. |

That's the first durable Apple evidence in the whole roadmap. For five weeks
`TaskListFeature.swift` was a loose file nobody could verify existed. Now it has
a SHA. That genuinely counts.

**And it's committed** — `41a4e97`, four files, at 4:52 PM. Both pieces of
today's work are now durable. Nothing is sitting in a working tree waiting to be
lost.

**One honest note on scale.** File timestamps put the whole of today's execution
between **4:20 and 4:31 PM** — about eleven minutes of actual editing. That is
not a criticism; the work genuinely was small once you sat down. It's worth
seeing because it means the 55-minute and 90-minute estimates in the Thursday
plan were badly wrong, and because **today's roadmap budget is almost entirely
still in front of you.**

---

## Tonight — two blocks

### 5:00–6:30 PM · Wire the database in (the big one)

> Ninety minutes, not the scheduled two — the block opened at 4:30 and it's 5:00.
> **The scope does not shrink to match.** If it isn't done at 6:30, you stop, and
> Saturday's Replacement block A picks it up. Overrunning is what ate July 24.

The commit is already done, so go straight at it. Right now `api/app.py` does
this:

```python
app.state.task_repository = repository or InMemoryTaskRepository()
```

One repository object, created once, living for the whole life of the app. Every
request shares it. That works perfectly for the in-memory one — it's just two
dictionaries.

**Here is the wall you are going to hit, and I'm telling you now so you don't
lose 30 minutes to it.** Look at your Postgres adapter:

```python
class PostgresTaskRepository:
    def __init__(self, session: AsyncSession):
```

It needs a **session**. And a session is *per-request* — it opens, runs your
queries, commits or rolls back, and closes, for one single request. That's the
whole point of `get_db_session` being a generator with `async with`.

So the two adapters have **different lifetimes**:

| | Lives for | Holds |
|---|---|---|
| `InMemoryTaskRepository` | the whole app | two dictionaries |
| `PostgresTaskRepository` | one request | one database session |

Which means you **cannot** just swap the class name in `app.py`. There is no
session available at app-startup time — there's no request yet. The composition
point has to move somewhere that runs per-request.

I'm deliberately not giving you the answer. You defended this exact swap at 3/4
on July 22 and the reviewer's correction told you what to do. Look at
`api/dependencies.py` — `get_task_repository` already runs once per request, and
`health.py` already shows you how to ask for a session inside a dependency. The
answer is in the shape of those two files.

**Two rules you don't get to break:**

1. The in-memory adapter must still work, because all 9 tests use it. Don't
   delete it, don't break it.
2. No SQLAlchemy type may leak into `domain/` or `application/`. Those layers
   must not know a database exists. That's the entire point of the `Protocol`.

**How you know you're done — and it is not "the tests pass":**

```bash
# start the API, then:
curl -X POST localhost:8000/tasks -H 'content-type: application/json' -d '{"title":"proof"}'
# then look in the actual database:
docker exec -it <container> psql -U postgres -d task_db -c "select * from tasks;"
```

If the row is in `psql`, you've done it. An HTTP 201 proves nothing — the
in-memory adapter returns 201 too. **See the row.**

**Stop at 6:30 even if it isn't finished.** Saturday has a block for part 2.
Overrunning is what ate July 24.

### 6:30–7:30 PM · Check my work, then fix the webhook thing

- **6:30–6:50 — read the two weekly reviews I wrote.** They're at the bottom of
  `PROGRESS.md`. I wrote them from today's recall exercise, which supplied the
  content. You're checking them, not writing them. Both say **"Actual roadmap
  hours: not observed"** — because they weren't. Fill in a real number only if
  you actually remember one. A guessed number is worse than a blank; every plan
  after it silently inherits the lie.
- **6:50–7:10 — the webhook repair.** See below. This is the most important
  20 minutes of the evening.
- **7:10–7:30 — buffer.** If the wiring overran, it lands here.

---

## The thing you asked about: `Annotated[...]` and `Depends`

You wrote the correct fix. Here's what you actually wrote.

### `Depends(get_db_session)`

It means: **"FastAPI — before you run my function, call `get_db_session()` and
hand me whatever it produces."** That's it. You're not calling the function
yourself; you're telling the framework to call it for you and pass the result in.

### Why the linter complained about the old version

The old code was:

```python
async def readiness_probe(session: AsyncSession = Depends(get_db_session)):
```

That looks like a **default value**. And in normal Python, a default value is
evaluated **once, when the file is imported**, and that one object is reused
forever. That's the classic bug ruff's `B008` exists to catch:

```python
def add_item(item, basket=[]):   # the list is created ONCE
    basket.append(item)          # every call shares the SAME list
```

So ruff sees a function call in the default slot and warns you.

**But ruff is wrong here, and knowing why is the interview answer.** FastAPI
never lets that default reach your function. It *reads the signature*, sees a
`Depends` marker, and calls `get_db_session()` **fresh for every request**. So
the bug B008 warns about cannot happen. B008 is right about Python and wrong
about FastAPI.

The wrong move would have been to silence the warning. You didn't.

### `Annotated[X, Y]`

Read it as: **"the type is `X`, and here's some extra baggage `Y` stapled to it
for anyone who cares."**

- **mypy** looks at `X` and ignores the baggage. So it still type-checks as a
  plain `AsyncSession`.
- **FastAPI** looks at the baggage and finds the `Depends`.

So:

```python
Annotated[AsyncSession, Depends(get_db_session)]
```

reads as: *"This is an `AsyncSession`. To get one, call `get_db_session`."*

The dependency now lives **inside the type annotation** instead of in the
default-value slot. Ruff stops complaining. FastAPI still finds it. Nothing is
suppressed. This is FastAPI's own recommended form, not a workaround.

### And the alias

```python
DbSession = Annotated[AsyncSession, Depends(get_db_session)]

async def readiness_probe(session: DbSession) -> dict[str, str]:
```

`DbSession` is just a **named shortcut** so you don't retype that mouthful in
every route. `session: DbSession` and the full `Annotated[...]` are identical to
Python. Your `dependencies.py` already used this pattern — you matched the
codebase.

### The other fix, which mattered more than the linter did

You changed:

```python
detail=f"Database unready: {str(exc)}"   # before
detail="Database unready"                # after
```

That wasn't cosmetic. When a database connection fails, the exception text
usually contains **the connection string** — host, port, database name,
sometimes the username. And `/healthz/ready` is normally **unauthenticated**,
because load balancers have to hit it without credentials.

So the old code meant: *break the database, and anyone who runs `curl` against
your health endpoint gets your infrastructure layout.*

`from exc` keeps the full detail in your **server logs**, where you want it. The
caller gets four words. That's the correct split, and it's a good thing to be
able to explain out loud.

---

## The webhook problem — read this part twice

I asked you to explain your B1 design (scored 17/24 in July) from memory. What
came back was **a WebSocket**, not a webhook. I need to be direct about this
because it's the most important finding of the day.

### What you said, and what's actually true

| You said | Reality |
|---|---|
| "a live listener attached to the server" | No. Nothing stays attached. |
| "we need that connection permanently" | No. It closes after each event. |
| "first a handshake to configure that both parties are authentic" | No opening handshake. Each request is signed individually. |
| "to and fro conversation, like Gemini Live API" | That's a **WebSocket**. Different tool, different problem. |
| "TCP vs UDP vs QUIC, packet ordering" | Real networking, but one layer below, and **not in your B1 design at all**. |

### What a webhook actually is

You give a provider — Stripe, GitHub, Slack — a URL. When something happens on
their side, **their server sends an ordinary HTTP POST to your URL.** Connection
opens, they send the event, you reply `200`, connection closes. Done.

That's the entire idea. It's a normal HTTP request where **they're the client and
you're the server** — the exact reverse of you calling their API. Nothing
persistent. No session. No handshake.

A **WebSocket** is the thing you described: one connection held open, both sides
talking whenever they want. That's for live chat and streaming audio. Genuinely
useful — genuinely a different problem.

### How much should you actually worry about this? — revised

You pushed back on this, and you were mostly right. Recording the correction.

**Your point stands:** the 17/24 scored a *written design document*. Today
measured *cold recall five weeks later*. Those are two different things, and one
does not invalidate the other. Today's result is **not** evidence the 17/24 was
inflated. Your ledger already said the design was "unchallenged and solo" — that
was the reason your own 24/24 self-score was rejected back in July.

**And the test wasn't even fair.** The six other topics were re-tested right
after you'd revised them in Antigravity. B1 got no revision pass at all, and it
was the oldest material in the set. It was the hardest question in an uneven
test.

**One correction of fact:** B1 wasn't before Sprint 1 — it was a Sprint 1 week-1
deliverable, July 24. But your larger point about expectations holds: the
Phase-1 bar is **≥12/24 with no zero**. You cleared it. The 20/24 bar is the
Phase-4 mock in March 2027, seven months away.

**What I'm not changing:** the score. Marking it down now because recall faded
would be the same mistake as marking it up because it felt good — both replace
what was measured with a later feeling. 17/24 stands, and the recall failure is
recorded next to it as a separate fact.

**What this actually exposed, and it isn't about you.** Your DSA track has real
spaced repetition — a problem ledger, dated intervals, solve-from-memory rules.
Your **system-design track has none**. Design a case, score it once, never see it
again. Under that design, forgetting was the *expected* outcome. That's a gap in
the roadmap, and it's the useful finding of the day. Changing it is a roadmap
change, so it needs your approval — I've recorded it as an open proposal to
decide before the design hours in the repair sprint, not made the change.

**Why it's still worth 20 minutes tonight:** swapping a persistent two-way
connection for a one-shot HTTP POST is a plain factual error, independent of any
score. And webhook integration is common in FDE delivery work, so it's cheap to
fix now and awkward to fix in front of a customer later.

### Your B1 design, as four questions

This is the whole thing. Four questions, four mechanisms. You had all of them in
July.

1. **"How do I know this POST really came from Stripe and not an attacker?"**
   → **HMAC signature.** They sign the request body with a shared secret; you
   recompute it and compare. **Per request, every request.** ← *This is the
   "authentic parties" you half-remembered — but it's a signature check on each
   message, not a one-time handshake.*
2. **"What if my processing is slow?"**
   → **Accept durably, process later.** Write the raw event to storage, return
   `200` immediately, handle it asynchronously. If you're slow, the provider
   times out and retries — and now you have duplicates *and* a backlog.
3. **"What if the same event arrives twice?"**
   → **It will.** Delivery is *at-least-once*: providers retry on timeout, and a
   retry sent after you already succeeded looks identical to a first delivery.
   So **deduplicate on the event ID** and make processing idempotent.
4. **"What if my consumer stays broken?"**
   → **Retry with backoff, then give up loudly.** Yours: full jitter, base 2s,
   cap 1 hour, 5 attempts, then **dead-letter** — so it's neither lost nor
   retried forever.

Everything else in that design — day-range partitioning, Redis for dedup, the
500 → 5,000 → 50,000 RPS ladder, S3 offload above 8 KB — is *how you make those
four survive scale*.

### Tonight's 20 minutes

1. Open `notes/sprint-01-AI-Software-Foundations-notes-02-b1-*.md`. Read **only**
   the critical-flow trace and the HMAC/dedup sections. Not the whole document —
   it's long and reading all of it is how this becomes an hour.
2. **Close the file.**
3. Write, from memory: one sentence on why a webhook is a plain one-shot HTTP
   POST, then the four failure modes above and the one mechanism you chose for
   each.

**B1 is not being rescored.** 17/24 stands — you earned it on the artifact and
the artifact hasn't changed. This is about whether it's still in your head.

---

## Where the gate stands after tonight

| # | Restart-gate exit test | Status |
|---|---|---|
| 1 | Fresh clone → Postgres + API start from the README only | Not started — Sunday |
| 2 | `alembic upgrade head` runs clean | Migration exists; unproven since July |
| 3 | Create a task, read it back, **see the row in `psql`** | **Tonight** |
| 4 | Restart the container, record survives | Tonight or Saturday |
| 5 | format / lint / mypy / tests green | ✅ **Closed today** (re-run Sunday from a clean clone) |
| 6 | Stop Postgres → readiness returns 503, not a false OK | Saturday |
| 7 | `PROGRESS.md` claims nothing it can't prove | ✅ Reviews written; verify at 6:30 |

**Saturday now holds:** the readiness/`.env` cleanup, plus the toolchain and
stack-snapshot refresh that got displaced when Thursday ran late. The DSA
repetitions moved to the repair sprint — that's item 2 of this gate's own
drop order, used in sequence, not an ad-hoc cut.
---

## Resources — in the order you should reach for them

**Tonight's wiring problem (first three are the ones that matter):**

1. **Your own notes** —
   `notes/sprint-01-AI-Software-Foundations-notes-04-postgreSQL-connection-understanding.md`.
   2,208 lines you wrote in July on AsyncEngine / Session / Pool / Alembic
   lifecycle. **Search it, don't read it.** You wrote it; you need three answers
   from it, not a re-read.
2. **Your own code**, in this order — `api/dependencies.py` (how a per-request
   dependency is built today), `api/routes/health.py` (how a dependency asks for
   a session), `api/app.py` (the composition point you're changing),
   `persistence/postgres_tasks.py` (what the adapter needs handed to it).
3. **FastAPI — "Dependencies with yield"**:
   <https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/>
   This is *the* page for tonight. It explains why `get_db_session` is written as
   a generator and exactly when the session opens and closes around your request.
   If you read one external page, read this one.
4. **FastAPI — Dependencies**:
   <https://fastapi.tiangolo.com/tutorial/dependencies/> — background for the
   `Annotated` / `Depends` material above.
5. **SQLAlchemy asyncio**:
   <https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html> — reference
   only. Dense. Go here when something specific breaks, not to learn from.

**For the 20-minute webhook repair:**

6. **Your B1 write-up** —
   `notes/sprint-01-AI-Software-Foundations-notes-02-b1-reliable-webhook-system-design-deep-teaching.md`,
   critical-flow trace and HMAC/dedup sections **only**.
7. **Stripe's webhook documentation**: <https://docs.stripe.com/webhooks> — the
   clearest plain-English writing on webhooks anywhere, and it's written from the
   receiving side, which is your side. Skim the delivery-and-retry section: it
   states at-least-once delivery outright and tells you to make your handler
   idempotent. That's mechanism 3 from your own design, in someone else's words.

**Not tonight** — the stack snapshot, model-line and Xcode-version rechecks, and
your `09-Current-Stack-Snapshot.md` refresh all moved to Saturday. Don't open
them today.
