# Sprint 01 — AI Software Foundations

> Dates: Monday, July 20–Sunday, August 2, 2026  
> Required roadmap time: approximately 24–25 hours per week  
> Build outcome: tested FastAPI/Postgres foundation with safe async and webhook
> behavior

## In plain language

Before adding a model, build the reliable shell that will contain it. This
sprint proves that requests are validated, business logic is separated from
HTTP, concurrent work is bounded, data changes are transactional, duplicate
events are safe, and tests can catch failures.

The sprint intentionally contains no real agent framework.

## Prerequisites

- Orientation results recorded.
- Python 3.12+, `uv`, Git, and a working editor.
- Docker/Postgres available by the second week.
- Current Xcode/Swift toolchain recorded.
- Primary DSA language selected or explicitly pending.

If Python typing, async, or HTTP diagnostic scored 0, replace the first matching
build block with the isolated exercise. Do not remove the exit gate.

## Concepts to be able to explain

- domain model versus transport/database model;
- dependency inversion and structural typing with `Protocol`;
- event loop, task, cancellation, timeout, semaphore, and backpressure;
- sync versus async work;
- HTTP method, status, validation, idempotency, and error contract;
- transaction, isolation, unique constraint, index, migration, and rollback;
- unit versus integration versus contract test;
- webhook signing, fast acknowledgement, duplicate delivery, and retries;
- process lifecycle, health, readiness, and graceful shutdown.

## Target repository shape

```text
ai-solutions-platform/
├── pyproject.toml
├── uv.lock
├── .env.example
├── src/ai_solutions_platform/
│   ├── domain/
│   ├── application/
│   ├── api/
│   ├── persistence/
│   ├── integrations/
│   └── telemetry/
├── tests/
│   ├── unit/
│   ├── integration/
│   └── contract/
├── migrations/
├── docs/decisions/
├── compose.yaml
└── .github/workflows/ci.yml
```

The exact number of files is not assessed. Dependency direction is.

## Simple runnable exercise

This exercise shows the boundary before adding Postgres. It is deliberately
small enough to run independently.

### Setup

```bash
mkdir sprint-01-api && cd sprint-01-api
uv init --python 3.12
uv add fastapi uvicorn
uv add --dev pytest httpx
```

Create `app.py`:

```python
"""A small FastAPI service with domain/HTTP separation.

Run:
    uv run uvicorn app:app --reload
Test:
    uv run pytest -q
"""

import asyncio
from dataclasses import dataclass
from datetime import UTC, datetime
from typing import Protocol
from uuid import UUID, uuid4

from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field


# Domain object: it has no FastAPI or Pydantic dependency.
@dataclass(frozen=True)
class TaskRecord:
    task_id: UUID
    title: str
    created_at: datetime


class DuplicateTaskTitle(Exception):
    """Business error raised independently from HTTP."""


class TaskRepository(Protocol):
    """Application-facing persistence contract."""

    async def add(self, record: TaskRecord) -> None:
        ...


class InMemoryTaskRepository:
    """A test/demo adapter. Postgres replaces it later."""

    def __init__(self) -> None:
        self._records_by_title: dict[str, TaskRecord] = {}
        # The lock protects the read-then-write critical section.
        self._lock = asyncio.Lock()

    async def add(self, record: TaskRecord) -> None:
        async with self._lock:
            if record.title in self._records_by_title:
                raise DuplicateTaskTitle(record.title)
            self._records_by_title[record.title] = record


class TaskService:
    """Application logic depends on the protocol, not a database SDK."""

    def __init__(self, repository: TaskRepository) -> None:
        self._repository = repository

    async def create(self, title: str) -> TaskRecord:
        record = TaskRecord(
            task_id=uuid4(),
            title=title,
            created_at=datetime.now(UTC),
        )
        await self._repository.add(record)
        return record


# HTTP models are separate because external contracts evolve differently.
class CreateTaskRequest(BaseModel):
    title: str = Field(min_length=1, max_length=120)


class TaskResponse(BaseModel):
    task_id: UUID
    title: str
    created_at: datetime


app = FastAPI(title="Sprint 01 API")
repository = InMemoryTaskRepository()
service = TaskService(repository)


@app.exception_handler(DuplicateTaskTitle)
async def duplicate_task_handler(
    request: Request,
    error: DuplicateTaskTitle,
) -> JSONResponse:
    del request, error  # The response intentionally exposes no internal detail.
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={
            "code": "duplicate_task_title",
            "message": "A task with this title already exists.",
        },
    )


@app.get("/health")
async def health() -> dict[str, str]:
    # Liveness proves the process responds; readiness is added with Postgres.
    return {"status": "ok"}


@app.post(
    "/tasks",
    response_model=TaskResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_task(body: CreateTaskRequest) -> TaskResponse:
    record = await service.create(body.title)
    return TaskResponse(
        task_id=record.task_id,
        title=record.title,
        created_at=record.created_at,
    )
```

Create `test_app.py`:

```python
from fastapi.testclient import TestClient

from app import app


client = TestClient(app)


def test_create_and_reject_duplicate() -> None:
    title = "unique-title-for-this-test"

    created = client.post("/tasks", json={"title": title})
    assert created.status_code == 201
    assert created.json()["title"] == title

    duplicate = client.post("/tasks", json={"title": title})
    assert duplicate.status_code == 409
    assert duplicate.json()["code"] == "duplicate_task_title"


def test_validation_is_an_http_contract() -> None:
    response = client.post("/tasks", json={"title": ""})
    assert response.status_code == 422
```

Run:

```bash
uv run pytest -q
uv run uvicorn app:app
```

### How the exercise works

```mermaid
flowchart LR
    JSON[JSON request] --> Pydantic[CreateTaskRequest]
    Pydantic --> Route[FastAPI route]
    Route --> Service[TaskService]
    Service --> Protocol[TaskRepository protocol]
    Protocol --> Memory[In-memory adapter]
    Memory --> Service
    Service --> Response[TaskResponse]
    Error[Duplicate domain error] --> Handler[HTTP exception handler]
```

The route translates HTTP into an application call. The service owns the use
case. The repository protocol lets Postgres replace the in-memory adapter
without changing the service. A domain error is translated at the edge rather
than teaching the domain about HTTP status codes.

### Extend the exercise

Before moving on:

- make title comparison case-insensitive without changing the HTTP layer;
- write a concurrent duplicate test;
- add a read operation;
- replace the global dependencies with FastAPI dependency providers;
- explain why the lock is insufficient across multiple processes;
- identify which database constraint must enforce the invariant in production.

## Week 1 — language, async, API, and SQL

### Monday, July 20

#### 2:15–4:15 — Python domain boundaries

- Dataclasses, immutability, enums, protocols, generics, exceptions, and type
  narrowing.
- Implement the isolated service above without copying.
- Add Ruff and mypy/pyright to the platform repository.

#### 4:30–6:30 — repository skeleton and CI

- Initialize `src/` layout and `uv` lockfile.
- Add formatting, lint, type, and test commands.
- Create the first architecture decision:
  “Domain code cannot import model, web, or database SDKs.”
- Add a minimal GitHub Actions workflow.

#### 9:30–10:30 — DSA

Arrays/hash maps: one due/revision problem.

### Tuesday, July 21

#### 2:15–4:15 — safe async

- Event-loop model, coroutine versus task, task groups, cancellation, timeout,
  semaphore, and blocking boundaries.
- Compare bounded and unbounded fake dependency calls.
- Write tests for timeout and cancellation cleanup.
- Orientation adjustment (learning): demonstrate the blocking boundary directly - stall the loop with time.sleep inside one coroutine, show it starves concurrent tasks, then fix with asyncio.sleep / run_in_executor; state which call blocks the event loop and why (closes the async diagnostic's inverted blocking-vs-non-blocking explanation).

#### 4:30–6:30 — Swift Concurrency

- Rebuild the orientation actor example in a Swift package.
- Add task cancellation and one Swift Testing test.
- Identify `MainActor` UI boundaries.

#### 9:30–10:30 — DSA

One unseen arrays/hash-maps problem.

### Wednesday, July 22

#### 2:15–4:15 — FastAPI flow

- Request/response validation, dependency injection, middleware, lifespan, and
  error mapping.
- Implement health, readiness placeholder, create, and read routes.
- Generate and inspect OpenAPI.

#### 4:30–6:00 — DSA

Two pointers: one pattern exercise and one timed problem.

#### 6:00–8:00 — IIT KGP

Move the remaining DSA 30 minutes to Sunday.

### Thursday, July 23

#### 2:15–4:15 — API contracts and tests

- Domain errors versus transport errors.
- Sync and async API tests.
- Validation, boundary, duplicate, timeout, and cancellation cases.
- Refactor global demo dependencies into explicit providers.

#### 4:30–6:00 — SwiftUI state

- Build a small adaptive task list backed by an actor/service.
- Cover loading, empty, content, error, and cancellation states.

#### 6:00–8:00 — IIT KGP

### Friday, July 24

#### 2:15–4:15 — SQL and Postgres

- Model task, incoming event, and processing attempt tables.
- Add primary/foreign/unique constraints and indexes.
- Write one transaction rollback exercise and inspect one query plan.

#### 4:30–6:30 — System design B1

Reliable webhook ingestion. Use the full design template.

#### 6:30–7:30 — review

- Run the in-memory vertical slice from a clean checkout.
- Record Week 1 gaps.
- Cut optional work before Week 2.

### Sunday, July 26

#### Two-hour Apple block

- Add Swift Testing for actor/service behavior.
- Add one cancellation test.
- Complete the moved 30-minute DSA review inside this block.

## Week 2 — Postgres, webhooks, lifecycle, and reliability

### Monday, July 27

#### 2:15–4:15 — async Postgres adapter

- SQLAlchemy async engine/session lifecycle or a small direct `asyncpg`
  adapter.
- Replace the in-memory repository through the same application protocol.
- Add Alembic migration.

#### 4:30–6:30 — persisted vertical slice

- Add Postgres to `compose.yaml`.
- Add readiness check that verifies the required dependency.
- Run integration tests against a clean database.

#### 9:30–10:30 — DSA

Two-pointer repetition.

### Tuesday, July 28

#### 2:15–4:15 — transactions and idempotency

- Enforce the duplicate invariant with a database unique constraint.
- Translate the database conflict into a domain error.
- Implement an idempotency-key record inside the same transaction as the
  intended state change.
- Test rollback.

#### 4:30–6:30 — Apple architecture

- Separate SwiftUI view, feature state, service protocol, and adapter.
- Test the service without rendering a view.

#### 9:30–10:30 — DSA

Unseen two-pointer problem.

### Wednesday, July 29

#### 2:15–4:15 — signed webhooks and background work

Implement an HMAC verifier:

```python
import hashlib
import hmac


def verify_signature(
    *,
    secret: bytes,
    body: bytes,
    supplied_hex_digest: str,
) -> bool:
    """Verify raw request bytes in constant-time comparison."""

    expected = hmac.new(secret, body, hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected, supplied_hex_digest)
```

Then:

- verify the raw body before parsing;
- persist provider event ID under a unique constraint;
- acknowledge after durable acceptance, not after all downstream work;
- process asynchronously;
- make duplicate delivery a successful no-op;
- record failed attempt and retry policy.

Do not log the secret or full sensitive payload.

#### 4:30–6:00 — DSA

Mixed arrays/hash/two-pointer timed set.

#### 6:00–8:00 — IIT KGP

### Thursday, July 30

#### 2:15–4:15 — lifecycle, failure, and concurrency tests

- FastAPI lifespan owns pools/resources.
- Test dependency outage at startup and during request.
- Test ten concurrent creates with duplicate collisions.
- Test cancellation and resource release.
- Distinguish liveness from readiness.

#### 4:30–6:00 — SwiftUI adaptive states

- Add retry and cancellation behavior.
- Inspect concurrency warnings and fix them.
- Record one small Instruments or performance observation if available.

#### 6:00–8:00 — IIT KGP

### Friday, July 31

#### 2:15–4:15 — Docker and CI completion

- Add a non-root application container.
- Run tests with Postgres in CI.
- Add health/readiness and graceful shutdown.
- Verify `.env.example` contains names, never values.
- Run secret scan available in the repository/GitHub settings.

#### 4:30–6:30 — System design I1

Offline-first adaptive iOS feed.

#### 6:30–7:30 — gate rehearsal

- Attempt the failure cases before polishing.
- Record tentative score.
- Assign only gate repairs for the weekend.

### Sunday, August 2

#### Two-hour sprint close

- Apple cancellation/concurrency test.
- Complete DSA pattern card and repetition schedule.
- Run clean setup and exact exit gate.
- Update `PROGRESS.md`.

## Required build outputs

- Typed package with clear dependency direction.
- FastAPI health/readiness, create/read, and signed webhook surfaces.
- Orientation adjustment (build): API tests assert success (201 body: task_id/title/created_at) and error (409 body: code/message) response bodies, with the 409 mapping consolidated into POST /tasks (not a parallel route).
- Postgres migration and transaction.
- Redis is not required in Sprint 1.
- Duplicate/idempotency behavior at the database boundary.
- Unit, API, integration, concurrency, and failure tests.
- Container and CI.
- Swift actor/service sample and adaptive SwiftUI state.
- B1 and I1 system-design notes.
- DSA ledger for arrays/hash/two pointers.

## FDE practice

Write a one-page explanation for a customer engineer:

- why business logic is independent from FastAPI/Postgres;
- what happens when the same webhook arrives twice;
- what the service does when Postgres is unavailable;
- what is intentionally not built yet.

Avoid “clean architecture” jargon unless the reader asks. Explain operational
value.

## Exit test

Run without a tutorial:

1. From a fresh checkout, start Postgres and the API through documented
   commands.
2. Create and read a persisted record.
3. Submit a valid signed webhook twice and prove one downstream effect.
4. Submit an invalid signature and prove no payload is accepted.
5. Force a transaction failure and prove rollback.
6. Force dependency timeout/cancellation and prove cleanup.
7. Run lint, type, unit, API, integration, and concurrency tests in CI.
8. Explain the event loop, transaction, idempotency, and domain/HTTP boundary.
9. Run the Swift concurrency/cancellation test.
10. Present B1 or I1 in 15 minutes and answer one failure challenge.

Score with the five-part sprint rubric. Pass requires at least 11/15, no zero,
and every item above proven.

## Official resources

- [Python typing](https://docs.python.org/3/library/typing.html)
- [Python protocols](https://typing.python.org/en/latest/spec/protocol.html)
- [Python asyncio](https://docs.python.org/3/library/asyncio.html)
- [FastAPI dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/)
- [FastAPI async tests](https://fastapi.tiangolo.com/advanced/async-tests/)
- [Pydantic models](https://docs.pydantic.dev/latest/concepts/models/)
- [SQLAlchemy asyncio](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html)
- [Alembic](https://alembic.sqlalchemy.org/)
- [PostgreSQL transactions](https://www.postgresql.org/docs/current/tutorial-transactions.html)
- [Docker Python guide](https://docs.docker.com/guides/python/)
- [GitHub Actions Python guide](https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python)
- [Swift Concurrency](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/concurrency/)
- [Swift Testing](https://developer.apple.com/documentation/testing/)

## Drop/defer rule

If time is short, drop in this order:

1. UI polish.
2. Docker image optimization.
3. advanced SQLAlchemy abstraction.
4. extra endpoints.

Do not drop:

- Postgres transaction/constraint;
- signed duplicate webhook behavior;
- cancellation and timeout test;
- CI;
- Apple concurrency test;
- DSA/design continuity.
