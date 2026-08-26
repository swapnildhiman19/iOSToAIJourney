# Wednesday, July 29, 2026 — Complete Study Schedule

> # ⛔ SUPERSEDED — NOT EXECUTED
>
> **Recorded August 26, 2026.** This day was never worked. Execution stopped after
> the Tuesday July 28 evening session; all 27 checkboxes below remain unticked and
> no evidence was produced against this plan. It is retained as a record of what
> was scheduled, not as guidance.
>
> Do not execute this file. The active schedule is
> [`../sprints/Restart-Gate-2026-08-26.md`](../sprints/Restart-Gate-2026-08-26.md)
> (Aug 26–30), followed by the Sprint 1 repair sprint (Aug 31–Sep 13) in
> [`../sprints/Sprint-01-AI-Software-Foundations.md`](../sprints/Sprint-01-AI-Software-Foundations.md).
>
> Two assumptions stated below as verified were **not** true and are corrected in
> `PROGRESS.md`: the Postgres adapter was written but never wired into the
> application, and the project's own lint/format/type gates were failing when this
> plan was authored.

> **Sprint:** Sprint 1 — AI Software Foundations (Jul 20–Aug 2)
> **Status:** Recovery Week 2, Day 3 — Building on Tue evening foundation — **never started**
> **Sprint Outcome:** Tested FastAPI/Postgres foundation with safe async and webhook behavior

---

## Daily Overview

| Time Block | Focus | Type | Primary Outcome |
|------------|-------|------|-----------------|
| 2:15–4:15 PM | Postgres Adapter Completion + Integration Tests | Independent Build + Evidence | Adapter passes all integration tests against live Postgres |
| 4:30–5:00 PM | Two-Pointer Pattern Repetition | Review | Solidify two-pointer mental model |
| 5:00–6:00 PM | Transaction/Idempotency Start + Mixed DSA | Independent Build + Evidence | Unique constraint + idempotency record foundation |
| 6:00–8:00 PM | IIT KGP | Fixed Commitment | Tracked separately |

---

## Block 1: 2:15–4:15 PM — Postgres Adapter Completion + Integration Tests

### Learning Stage: Independent Build → Evidence

### Assumed Prerequisites (Verified Tue Jul 28)
- ✅ Postgres 16 running via `docker compose up -d`
- ✅ `PostgresTaskRepository` skeleton with `IntegrityError` → `DuplicateTaskTitle` translation
- ✅ `database.py` with `AsyncSessionLocal` and `get_db_session()` dependency
- ✅ Alembic migration `0001_create_tasks_table.py` applied
- ✅ `/healthz/ready` endpoint responding

### Session Goals
1. Complete the Postgres adapter with full CRUD operations
2. Wire the adapter into FastAPI dependency injection
3. Write and run integration tests against live Postgres
4. Verify readiness endpoint behavior when DB is unavailable

---

### Part A: 2:15–2:45 PM — Complete the Postgres Adapter

#### What You Need to Understand

**Plain Language:** Your `PostgresTaskRepository` currently has `add()` and `get_by_id()`. The in-memory adapter also has these methods plus any additional ones required by `TaskRepository` protocol. Your job is to ensure the Postgres adapter fully satisfies the protocol contract.

**Technical Details:**
- The `TaskRepository` protocol in `application/tasks.py` defines the contract
- Both adapters must implement the exact same methods
- The key difference: Postgres uses SQL while in-memory uses Python dict

#### Code Changes Required

**File:** `src/ai_solutions_platform/persistence/postgres_tasks.py`

Your current implementation is correct for `add()` and `get_by_id()`. Let's verify and potentially add a `list_all()` method if the protocol requires it.

First, check the protocol definition:

```python
# In application/tasks.py - verify the TaskRepository protocol
class TaskRepository(Protocol):
    async def add(self, record: TaskRecord) -> None: ...
    async def get_by_id(self, task_id: UUID) -> TaskRecord | None: ...
```

If only `add` and `get_by_id` are required, your adapter is complete. If `list_all()` is needed, add:

```python
async def list_all(self) -> list[TaskRecord]:
    """Retrieve all task records."""
    query = text("SELECT task_id, title, created_at FROM tasks ORDER BY created_at DESC")
    result = await self._session.execute(query)
    rows = result.mappings().all()
    return [
        TaskRecord(
            task_id=row["task_id"],
            title=row["title"],
            created_at=row["created_at"],
        )
        for row in rows
    ]
```

---

### Part B: 2:45–3:15 PM — Wire Postgres Adapter into FastAPI

#### What You Need to Understand

**Plain Language:** Currently your `app.py` uses `InMemoryTaskRepository()` as default. For production/integration testing, you need to swap this with `PostgresTaskRepository`. FastAPI's dependency injection lets you do this cleanly.

**Technical Details:**
- `app.state.task_repository` currently holds the in-memory adapter
- For Postgres, you need a session per request (not a global session)
- Use FastAPI's `Depends()` to inject a fresh session for each request
- The repository is constructed with that session

#### Code Changes Required

**Option 1: Session-per-request pattern (Recommended)**

Create a new file `src/ai_solutions_platform/api/dependencies.py`:

```python
"""FastAPI dependency providers for the AI Solutions Platform."""

from typing import AsyncGenerator
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from ai_solutions_platform.persistence.database import get_db_session
from ai_solutions_platform.persistence.postgres_tasks import PostgresTaskRepository
from ai_solutions_platform.persistence.in_memory_tasks import InMemoryTaskRepository
from ai_solutions_platform.application.tasks import TaskRepository, TaskService


async def get_postgres_repository(
    session: AsyncSession = Depends(get_db_session),
) -> PostgresTaskRepository:
    """Provide a PostgresTaskRepository with request-scoped session."""
    return PostgresTaskRepository(session)


async def get_task_service(
    repository: PostgresTaskRepository = Depends(get_postgres_repository),
) -> TaskService:
    """Provide a TaskService with injected repository."""
    return TaskService(repository)
```

**Update routes to use dependency injection:**

In `src/ai_solutions_platform/api/routes/tasks.py`, change from using `request.app.state.task_repository` to using `Depends()`:

```python
from fastapi import APIRouter, Depends, HTTPException, status
from ai_solutions_platform.api.dependencies import get_task_service
from ai_solutions_platform.application.tasks import TaskService

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_task(
    body: CreateTaskRequest,
    service: TaskService = Depends(get_task_service),
) -> TaskResponse:
    record = await service.create(body.title)
    return TaskResponse(
        task_id=record.task_id,
        title=record.title,
        created_at=record.created_at,
    )
```

#### Key Concept: Dependency Injection Flow

```
HTTP Request arrives
       ↓
FastAPI sees Depends(get_task_service)
       ↓
get_task_service needs Depends(get_postgres_repository)
       ↓
get_postgres_repository needs Depends(get_db_session)
       ↓
get_db_session creates AsyncSession from pool
       ↓
PostgresTaskRepository constructed with that session
       ↓
TaskService constructed with that repository
       ↓
Route handler executes
       ↓
Request completes → session returned to pool
```

---

### Part C: 3:15–3:55 PM — Write Integration Tests

#### What You Need to Understand

**Plain Language:** Integration tests verify your code works with real Postgres, not just the in-memory fake. They're slower but catch real database issues like constraint violations, SQL syntax errors, and connection problems.

**Technical Details:**
- Use `pytest-asyncio` for async test support
- Create a test database or use transactions that rollback
- Test the full request → response cycle with real DB

#### Test File: `tests/integration/test_postgres_tasks.py`

```python
"""Integration tests for PostgreSQL task persistence."""

import pytest
from uuid import uuid4
from datetime import datetime, UTC
from httpx import AsyncClient, ASGITransport

from ai_solutions_platform.api.app import create_app
from ai_solutions_platform.domain.tasks import TaskRecord, DuplicateTaskTitle
from ai_solutions_platform.persistence.postgres_tasks import PostgresTaskRepository
from ai_solutions_platform.persistence.database import AsyncSessionLocal, engine


@pytest.fixture
async def db_session():
    """Provide a database session that rolls back after each test."""
    async with AsyncSessionLocal() as session:
        yield session
        await session.rollback()


@pytest.fixture
async def postgres_repo(db_session):
    """Provide a PostgresTaskRepository with test session."""
    return PostgresTaskRepository(db_session)


class TestPostgresTaskRepository:
    """Test PostgresTaskRepository against live Postgres."""

    @pytest.mark.asyncio
    async def test_add_and_retrieve_task(self, postgres_repo, db_session):
        """Verify a task can be added and retrieved."""
        task_id = uuid4()
        record = TaskRecord(
            task_id=task_id,
            title="Integration Test Task",
            created_at=datetime.now(UTC),
        )
        
        await postgres_repo.add(record)
        
        retrieved = await postgres_repo.get_by_id(task_id)
        assert retrieved is not None
        assert retrieved.task_id == task_id
        assert retrieved.title == "Integration Test Task"

    @pytest.mark.asyncio
    async def test_duplicate_title_raises_domain_error(self, postgres_repo, db_session):
        """Verify unique constraint translates to DuplicateTaskTitle."""
        record1 = TaskRecord(
            task_id=uuid4(),
            title="Duplicate Title Test",
            created_at=datetime.now(UTC),
        )
        record2 = TaskRecord(
            task_id=uuid4(),
            title="Duplicate Title Test",  # Same title
            created_at=datetime.now(UTC),
        )
        
        await postgres_repo.add(record1)
        
        with pytest.raises(DuplicateTaskTitle):
            await postgres_repo.add(record2)

    @pytest.mark.asyncio
    async def test_get_nonexistent_returns_none(self, postgres_repo):
        """Verify get_by_id returns None for missing task."""
        result = await postgres_repo.get_by_id(uuid4())
        assert result is None


class TestAPIWithPostgres:
    """Test API endpoints with real Postgres backend."""

    @pytest.fixture
    async def client(self):
        """Provide an async test client."""
        app = create_app()
        transport = ASGITransport(app=app)
        async with AsyncClient(transport=transport, base_url="http://test") as client:
            yield client

    @pytest.mark.asyncio
    async def test_create_task_persists_to_postgres(self, client):
        """Verify POST /tasks creates a record in Postgres."""
        unique_title = f"API Test Task {uuid4()}"
        
        response = await client.post("/tasks", json={"title": unique_title})
        
        assert response.status_code == 201
        data = response.json()
        assert data["title"] == unique_title
        assert "task_id" in data

    @pytest.mark.asyncio
    async def test_readiness_returns_healthy_when_db_up(self, client):
        """Verify /healthz/ready returns 200 when Postgres is available."""
        response = await client.get("/healthz/ready")
        
        assert response.status_code == 200
        assert response.json()["status"] == "healthy"
```

#### Running the Tests

```bash
# Ensure Postgres is running
docker compose up -d

# Wait for healthy status
docker compose ps  # Should show "healthy"

# Run integration tests
cd "AI Solutions Platform"
uv run --extra dev pytest tests/integration/ -v

# Run all tests including unit tests
uv run --extra dev pytest -v
```

---

### Part D: 3:55–4:15 PM — Verify Readiness Behavior

#### What You Need to Understand

**Plain Language:** The `/healthz/ready` endpoint should return 503 when Postgres is unavailable. This tells load balancers to stop sending traffic to this instance.

**Technical Details:**
- Stop Postgres: `docker compose stop postgres`
- Hit the endpoint: should return 503
- Start Postgres: `docker compose start postgres`
- Hit the endpoint: should return 200

#### Manual Verification Steps

```bash
# 1. Verify healthy state
curl http://localhost:8000/healthz/ready
# Expected: {"status":"healthy","database":"connected"}

# 2. Stop Postgres
docker compose stop postgres

# 3. Verify unhealthy state
curl http://localhost:8000/healthz/ready
# Expected: 503 with {"detail":"Database unready: ..."}

# 4. Restart Postgres
docker compose start postgres

# 5. Wait for health check
sleep 10

# 6. Verify recovery
curl http://localhost:8000/healthz/ready
# Expected: {"status":"healthy","database":"connected"}
```

### Evidence Checklist for Block 1

- [ ] `PostgresTaskRepository` fully implements `TaskRepository` protocol
- [ ] FastAPI routes use dependency injection for Postgres adapter
- [ ] Integration test: add and retrieve task passes
- [ ] Integration test: duplicate title raises `DuplicateTaskTitle`
- [ ] Integration test: missing task returns `None`
- [ ] Readiness endpoint returns 200 when DB is up
- [ ] Readiness endpoint returns 503 when DB is down
- [ ] All tests pass: `uv run --extra dev pytest -v`

### Recording Destination
`PROGRESS.md` → AI Solutions Platform milestones (FastAPI/Postgres vertical slice)

---

## Block 2: 4:30–5:00 PM — Two-Pointer Pattern Repetition

### Learning Stage: Review + Pattern Solidification

### What You Need to Understand

**Plain Language:** Two-pointer is a technique where you use two indices (pointers) that move through an array, often from opposite ends or at different speeds, to solve problems efficiently without nested loops.

**Technical Details:**
- **Opposite ends pattern:** One pointer at start, one at end, move toward each other
- **Same direction pattern:** Both start at beginning, one moves faster (fast/slow)
- **Key insight:** Reduces O(n²) nested loop to O(n) single pass

### Core Two-Pointer Patterns

#### Pattern 1: Opposite Ends (Most Common)

```swift
func twoSum(_ numbers: [Int], _ target: Int) -> [Int] {
    var left = 0
    var right = numbers.count - 1
    
    while left < right {
        let sum = numbers[left] + numbers[right]
        if sum == target {
            return [left + 1, right + 1]  // 1-indexed
        } else if sum < target {
            left += 1  // Need larger sum, move left pointer right
        } else {
            right -= 1  // Need smaller sum, move right pointer left
        }
    }
    return []
}
```

**When to use:** Sorted array, finding pairs, container problems

#### Pattern 2: Fast and Slow (Tortoise and Hare)

```swift
func hasCycle(_ head: ListNode?) -> Bool {
    var slow = head
    var fast = head
    
    while fast != nil && fast?.next != nil {
        slow = slow?.next
        fast = fast?.next?.next
        
        if slow === fast {
            return true  // They met → cycle exists
        }
    }
    return false
}
```

**When to use:** Cycle detection, finding middle, detecting duplicates in O(1) space

#### Pattern 3: Sliding Window Variant

```swift
func minSubArrayLen(_ target: Int, _ nums: [Int]) -> Int {
    var left = 0
    var sum = 0
    var minLen = Int.max
    
    for right in 0..<nums.count {
        sum += nums[right]
        
        while sum >= target {
            minLen = min(minLen, right - left + 1)
            sum -= nums[left]
            left += 1
        }
    }
    
    return minLen == Int.max ? 0 : minLen
}
```

**When to use:** Subarray problems, window-based problems

### Practice Problem: Container With Most Water

**Problem:** Given n non-negative integers representing heights, find two lines that together with x-axis form a container that holds the most water.

```swift
func maxArea(_ height: [Int]) -> Int {
    var left = 0
    var right = height.count - 1
    var maxWater = 0
    
    while left < right {
        let width = right - left
        let h = min(height[left], height[right])
        maxWater = max(maxWater, width * h)
        
        // Move the shorter line inward (greedy choice)
        if height[left] < height[right] {
            left += 1
        } else {
            right -= 1
        }
    }
    
    return maxWater
}
```

**Why move the shorter line?**
- Width always decreases when we move a pointer
- To potentially increase area, we need a taller line
- Moving the taller line can only decrease or maintain height
- Moving the shorter line might find a taller line

### Mental Model Card

```
TWO-POINTER PATTERN RECOGNITION:
┌─────────────────────────────────────────────────┐
│ TRIGGER: "sorted array" OR "pairs" OR "cycle"   │
│                                                 │
│ OPPOSITE ENDS:                                  │
│   - Sorted array + target sum                   │
│   - Palindrome check                            │
│   - Container/area problems                     │
│                                                 │
│ FAST/SLOW:                                      │
│   - Cycle detection                             │
│   - Find middle of linked list                  │
│   - Find duplicate in O(1) space                │
│                                                 │
│ COMPLEXITY: O(n) time, O(1) space              │
└─────────────────────────────────────────────────┘
```

### Evidence Target
- Review the Repeating/Missing Number solution from yesterday (uses partitioning similar to two-pointer thinking)
- Write out the pattern card in notes
- Do NOT start a new problem — that's for 5:00–6:00 block

---

## Block 3: 5:00–6:00 PM — Transaction/Idempotency Start + Mixed DSA

### Split: 5:00–5:30 PM Transaction/Idempotency, 5:30–6:00 PM DSA

---

### Part A: 5:00–5:30 PM — Transaction and Idempotency Foundation

### Learning Stage: Learn → Guided Practice

### What You Need to Understand

**Plain Language:**  
- **Transaction:** A group of database operations that either ALL succeed or ALL fail together. Think of it like transferring money: debit and credit must both happen or neither happens.
- **Idempotency:** Running the same operation multiple times produces the same result. If you click "Pay" twice, you should only be charged once.

**Technical Details:**

#### Transactions in PostgreSQL

```sql
BEGIN;
  INSERT INTO tasks (task_id, title, created_at) VALUES (...);
  INSERT INTO idempotency_keys (key, created_at) VALUES (...);
COMMIT;
-- If either INSERT fails, ROLLBACK undoes both
```

In SQLAlchemy:
```python
async with session.begin():
    # All operations here are in one transaction
    await session.execute(insert_task)
    await session.execute(insert_idempotency_key)
    # Implicit commit on success, rollback on exception
```

#### Idempotency Key Pattern

When a client sends a request, they include a unique key (like a UUID). The server:
1. Checks if this key exists in the database
2. If yes: return the cached result (don't process again)
3. If no: process the request, store the key + result, return result

```python
class IdempotencyKey:
    """Track processed requests to prevent duplicate processing."""
    key: str  # Unique identifier from client
    result: str  # JSON serialized result
    created_at: datetime
```

### Migration for Idempotency Keys

Create `alembic/versions/0002_create_idempotency_keys.py`:

```python
"""create_idempotency_keys_table

Revision ID: 0002
Revises: 0001
Create Date: 2026-07-29
"""

from typing import Sequence, Union
import alembic.op as op
import sqlalchemy as sa

revision: str = '0002'
down_revision: Union[str, None] = '0001'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'idempotency_keys',
        sa.Column('key', sa.String(length=255), nullable=False, primary_key=True),
        sa.Column('response_body', sa.Text(), nullable=False),
        sa.Column('status_code', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    )


def downgrade() -> None:
    op.drop_table('idempotency_keys')
```

Run migration:
```bash
uv run alembic upgrade head
```

### Evidence Target (Partial — Continue Thu)
- [ ] Understand transaction boundaries in SQLAlchemy
- [ ] Create idempotency_keys migration
- [ ] Apply migration successfully

---

### Part B: 5:30–6:00 PM — Mixed DSA Timed Set

### Learning Stage: Evidence (Timed Independent Solve)

### Problem Selection

**Primary:** Arrays/Hash-Map problem (recovers Jul 21 unseen requirement)

**Suggested Problem:** Two Sum (if not already done) or Group Anagrams

#### Two Sum — Classic Hash-Map

```swift
func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
    var seen: [Int: Int] = [:]  // value -> index
    
    for (i, num) in nums.enumerated() {
        let complement = target - num
        if let j = seen[complement] {
            return [j, i]
        }
        seen[num] = i
    }
    return []
}
```

**Complexity:** O(n) time, O(n) space
**Pattern:** Hash-map for O(1) lookup of complement

#### Group Anagrams — Hash-Map with Sorted Key

```swift
func groupAnagrams(_ strs: [String]) -> [[String]] {
    var groups: [String: [String]] = [:]
    
    for str in strs {
        let key = String(str.sorted())  // "eat" -> "aet"
        groups[key, default: []].append(str)
    }
    
    return Array(groups.values)
}
```

**Complexity:** O(n * k log k) where k is max string length
**Pattern:** Normalize input to create grouping key

### Timed Execution Protocol

1. **Set timer:** 20 minutes
2. **Read problem carefully:** 2 minutes
3. **Plan approach:** 3 minutes (write pseudocode)
4. **Implement:** 12 minutes
5. **Test edge cases:** 3 minutes

### Record After Solving

```markdown
## DSA Log — Jul 29

**Problem:** [Name]
**Time:** XX minutes (target: 20)
**Approach:** [One sentence]
**Complexity:** Time O(...), Space O(...)
**Mistake/Learning:** [What tripped you up or key insight]
**Next repetition:** ~Aug 12
```

### Evidence Target
- [ ] One arrays/hash-map problem solved independently
- [ ] Time recorded
- [ ] Complexity proven
- [ ] Pattern tag recorded

### Stop Point: 6:00 PM Sharp
Do not continue DSA into IIT time. Rest your mind for the class.

---

## Block 4: 6:00–8:00 PM — IIT KGP

Fixed commitment. Tracked separately from roadmap hours.

---

## Evening Reflection (After IIT, Optional)

If you have 15–20 minutes before bed:
- Review today's commit and verify everything is staged
- Skim tomorrow's Thu Jul 30 schedule in the sprint guide
- Do NOT start new work

---

## Done-for-Today Checklist

### Block 1: Postgres Adapter Completion
- [ ] Integration tests pass against live Postgres
- [ ] Dependency injection wired correctly
- [ ] Readiness endpoint verified (200 up, 503 down)
- [ ] Changes committed

### Block 2: Two-Pointer Review
- [ ] Pattern card written/reviewed
- [ ] Mental model solidified

### Block 3A: Transaction/Idempotency
- [ ] idempotency_keys migration created
- [ ] Migration applied
- [ ] Transaction boundary understood

### Block 3B: DSA
- [ ] One arrays/hash problem solved
- [ ] Time and complexity recorded

### Block 4: IIT
- [ ] Attended (tracked separately)

---

## Files Changed/Created Today

### Expected New Files
- `tests/integration/test_postgres_tasks.py` — Integration tests
- `src/ai_solutions_platform/api/dependencies.py` — Dependency providers
- `alembic/versions/0002_create_idempotency_keys.py` — Idempotency migration

### Expected Modified Files
- `src/ai_solutions_platform/api/routes/tasks.py` — Use Depends()
- `PROGRESS.md` — Record evidence

---

## Quick Reference: Commands

```bash
# Start Postgres
docker compose up -d

# Check health
docker compose ps

# Run migrations
uv run alembic upgrade head

# Run all tests
uv run --extra dev pytest -v

# Run integration tests only
uv run --extra dev pytest tests/integration/ -v

# Format and lint
uv run ruff format .
uv run ruff check . --fix

# Type check
uv run mypy src/

# Start the API
uv run uvicorn ai_solutions_platform.api.app:app --reload
```

---

## Remaining Sprint Week

| Day | Blocks | Focus |
|-----|--------|-------|
| **Thu Jul 30** | 2:15–4:15, 4:30–6:00, IIT 6:00–8:00 | Signed webhooks + duplicate handling; contract/lifecycle/failure tests + ADR |
| **Fri Jul 31** | 2:15–4:15, 4:30–6:30, 6:30–7:30 | Docker + CI with Postgres; gate rehearsal; weekly review + evidence close |
| **Sun Aug 2** | 2 hours | Swift concurrency test (1 hr) + clean-checkout exit gate + score + PROGRESS.md close |

---

## Exit Gate Items Status (10 Items)

| # | Item | Status | Evidence |
|---|------|--------|----------|
| 1 | Fresh checkout start Postgres and API | 🟡 In Progress | compose.yaml verified Tue |
| 2 | Create and read persisted record | 🟡 In Progress | Adapter ready, tests Wed |
| 3 | Valid signed webhook twice → one effect | 🔴 Not Started | Thu Jul 30 |
| 4 | Invalid signature rejected | 🔴 Not Started | Thu Jul 30 |
| 5 | Transaction failure → rollback | 🟡 Started | Migration Wed, test Thu |
| 6 | Dependency timeout/cancellation → cleanup | 🔴 Not Started | Thu Jul 30 |
| 7 | CI with lint/type/unit/API/integration/concurrency | 🔴 Not Started | Fri Jul 31 |
| 8 | Explain event loop, transaction, idempotency, domain/HTTP | 🟡 Learning | Notes complete |
| 9 | Swift concurrency/cancellation test | 🔴 Not Started | Sun Aug 2 |
| 10 | Present B1 (17/24) + answer failure challenge | ✅ Complete | B1 scored Jul 25 |
