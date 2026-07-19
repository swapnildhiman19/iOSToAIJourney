# Sprint 00 — Orientation and Diagnostics

> Dates: Thursday, July 16–Sunday, July 19, 2026  
> Roadmap time: approximately 13–15 hours  
> Outcome: an honest baseline and a runnable environment for Sprint 1

## In plain language

This is a health check, not a setup marathon. You will prove what already works,
record what does not, and install only what Sprint 1 needs. A weak diagnostic is
useful because it prevents the next eight months from being built on an
assumption.

Do not study before a diagnostic. Do not turn a poor score into a judgment about
your career.

## Required outputs

- Completed diagnostic rows in `PROGRESS.md`.
- Primary DSA language decision or a dated decision checkpoint.
- Current Mac/Xcode/Apple Intelligence availability record.
- Python/FastAPI/Postgres prerequisites verified.
- Provider API budget and secret-handling plan.
- AI Solutions Platform repository/skeleton location selected.
- Sprint 1 scope adjustment of no more than 20%.

## Before the first session

Read:

1. [Master index](../README.md).
2. [Competency map](../01-Competency-Map.md).
3. [Weekly operating system](../04-Weekly-Operating-System.md).
4. [Assessment and recovery](../08-Assessment-and-Recovery.md).
5. [Current stack snapshot](../09-Current-Stack-Snapshot.md).

Do not read all remaining roadmap files during orientation.

## Schedule

### Thursday, July 16

#### 2:15–4:15 — roadmap and environment baseline

1. Record current versions without upgrading:

   ```bash
   git --version
   python3 --version
   uv --version
   docker --version
   gcloud --version
   swift --version
   xcodebuild -version
   ```

2. Record “not installed” rather than stopping to install every missing tool.
3. Create or select a dedicated public-safe repository for the AI Solutions
   Platform.
4. Confirm `.env`, credentials, model artifacts, Xcode user data, and local
   databases are ignored.
5. Set a provider/GCP monthly budget before making paid calls.

Required now:

- Git;
- Python 3.12+;
- `uv`;
- Docker or an available Postgres installation;
- Xcode/Swift for the Apple diagnostic.

Can wait:

- Terraform;
- Kubernetes tooling;
- AWS;
- LiveKit CLI;
- Flutter;
- model-conversion tools.

#### 4:30–6:00 — Apple hardware and toolchain diagnostic

Record:

```bash
system_profiler SPHardwareDataType
xcodebuild -version
xcrun simctl list devices available
swift --version
```

In a tiny SwiftUI app or package:

- build one screen;
- run one Swift Testing test;
- run one actor/async function;
- record the available OS 27 SDK and simulator status;
- record `SystemLanguageModel` availability where the current SDK supports it.

Do not require a physical iPhone during orientation.

#### 6:00–8:00 — IIT KGP class

This is tracked separately. No roadmap home block.

### Friday, July 17

#### 2:15–4:15 — Python and async diagnostic

Create a temporary `diagnostics/python_baseline.py` and run the exercise below.
First complete the `TODO` without looking at the answer pattern.

```python
"""Run with: uv run python diagnostics/python_baseline.py"""

import asyncio
from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class WorkItem:
    """Immutable input at the domain boundary."""

    item_id: str
    delay_seconds: float


class Processor(Protocol):
    """A structural contract; implementations need not inherit from it."""

    async def process(self, item: WorkItem) -> str:
        ...


class FakeProcessor:
    async def process(self, item: WorkItem) -> str:
        await asyncio.sleep(item.delay_seconds)
        return f"processed:{item.item_id}"


async def process_bounded(
    items: list[WorkItem],
    processor: Processor,
    max_concurrency: int = 2,
) -> list[str]:
    """Process concurrently without allowing unbounded fan-out."""

    semaphore = asyncio.Semaphore(max_concurrency)

    async def run_one(item: WorkItem) -> str:
        async with semaphore:
            # A dependency that exceeds the budget fails this item.
            async with asyncio.timeout(0.25):
                return await processor.process(item)

    # TODO before reading docs:
    # Run all items concurrently while preserving input-order results.
    tasks = [asyncio.create_task(run_one(item)) for item in items]
    return await asyncio.gather(*tasks)


async def main() -> None:
    items = [
        WorkItem("a", 0.05),
        WorkItem("b", 0.10),
        WorkItem("c", 0.05),
    ]
    results = await process_bounded(items, FakeProcessor())
    assert results == ["processed:a", "processed:b", "processed:c"]
    print(results)


if __name__ == "__main__":
    asyncio.run(main())
```

Explain aloud:

- why `Processor` is useful;
- what the semaphore bounds;
- what gets cancelled on timeout;
- how blocking `time.sleep` would differ from `asyncio.sleep`;
- whether `gather` is the best failure policy for independent production work.

Score 0–3 for Python structure and 0–3 for async reasoning.

#### 4:30–6:30 — system-design diagnostic

Without the design template, spend 45 minutes on:

> Design an enterprise AI assistant with a mobile client, company documents,
> and one action tool.

Record the result. Then read the method in
[the system-design track](../05-System-Design-Track.md) and score the attempt.
Do not redraw it yet.

#### 6:30–7:30 — first progress review

- Enter all evidence links in `PROGRESS.md`.
- List only concrete blockers.
- Identify the one prerequisite most likely to block Sprint 1.

### Saturday, July 18

Use one three-hour orientation block. This is an exception to the normal
recovery Saturday.

#### Hour 1 — FastAPI/HTTP diagnostic

Without a tutorial, create:

- `GET /health`;
- `POST /tasks` with a validated request and response;
- a domain error mapped to a non-200 HTTP response;
- one test using `TestClient` or `httpx`.

Score:

- 0: cannot start;
- 1: happy path only;
- 2: validation and test pass;
- 3: domain/HTTP boundary and error test are clear.

#### Hour 2 — SQL/Postgres diagnostic

Explain and then demonstrate:

- table, primary key, foreign key, unique constraint, and index;
- transaction commit and rollback;
- parameterized query;
- why an index can hurt writes;
- one query plan using `EXPLAIN`.

If Postgres is unavailable, complete the conceptual diagnostic and make its
installation the first Sprint 1 task. Do not substitute SQLite evidence for
Postgres behavior.

#### Hour 3 — model API diagnostic

With `GOOGLE_API_KEY` stored outside source control:

```python
"""Run after: uv add google-genai"""

import os

from google import genai
from pydantic import BaseModel


class DiagnosticResult(BaseModel):
    summary: str
    risk: str


client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])

# Keep the model configurable because IDs change over the roadmap.
model_id = os.environ.get("GEMINI_MODEL", "gemini-3.5-flash")
response = client.models.generate_content(
    model=model_id,
    contents="Explain one risk of letting an AI call a refund tool.",
    config={
        "response_mime_type": "application/json",
        "response_json_schema": DiagnosticResult.model_json_schema(),
    },
)

result = DiagnosticResult.model_validate_json(response.text)
print(result.model_dump())
```

If the current SDK uses a typed config object instead of the shown mapping,
adapt from the current official structured-output example and record the exact
SDK version. The diagnostic is about reading the current API, validating the
result, and handling a failure—not memorizing one call signature.

Record:

- model ID and stable/preview state;
- SDK version;
- latency and token/usage data if returned;
- schema-validation result;
- one forced invalid-output or missing-key failure.

### Sunday, July 19

#### 90 minutes — DSA language diagnostic

- Solve equivalent array/hash problems in Swift and Python.
- Record time, syntax lookup, correctness, tests, and explanation.
- Apply the language rule in [the DSA track](../06-DSA-Track.md).

#### 90 minutes — Apple concurrency diagnostic

Run this as a Swift executable target:

```swift
import Foundation

actor ResultStore {
    // Actor isolation protects this mutable array from concurrent access.
    private var values: [String] = []

    func append(_ value: String) {
        values.append(value)
    }

    func snapshot() -> [String] {
        values
    }
}

@main
struct ConcurrencyDiagnostic {
    static func main() async {
        let store = ResultStore()

        await withTaskGroup(of: Void.self) { group in
            for id in 1...3 {
                group.addTask {
                    // A real task should check cancellation before expensive work.
                    guard !Task.isCancelled else { return }
                    await store.append("item-\(id)")
                }
            }
        }

        let values = await store.snapshot()
        precondition(Set(values) == Set(["item-1", "item-2", "item-3"]))
        print(values.sorted())
    }
}
```

Explain:

- why the store is an actor;
- what isolation does and does not guarantee;
- how child tasks relate to the group;
- where cancellation should be observed;
- what belongs on `MainActor` in a SwiftUI application.

#### 60 minutes — FDE diagnostic

Use the synthetic prompt:

> “Our operations team reads incident alerts, searches several documents and
> dashboards, and posts a recommendation. Add AI so this is faster.”

Spend 20 minutes asking written discovery questions, 20 minutes proposing a
pilot, and 20 minutes identifying data/risk/adoption blockers. Score with the
[FDE rubric](../07-FDE-Track.md).

#### 60 minutes — close orientation

- Finish `PROGRESS.md`.
- Select the primary DSA language.
- Confirm Sprint 1 prerequisites.
- Adjust at most one Sprint 1 learning item and one build item.
- Preserve the original Sprint 1 exit gate.

## Official resources

Use only the sections needed to complete a diagnostic:

- [Python tutorial](https://docs.python.org/3/tutorial/)
- [Python asyncio](https://docs.python.org/3/library/asyncio.html)
- [uv documentation](https://docs.astral.sh/uv/)
- [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/)
- [Pydantic models](https://docs.pydantic.dev/latest/concepts/models/)
- [pytest documentation](https://docs.pytest.org/)
- [PostgreSQL tutorial](https://www.postgresql.org/docs/current/tutorial.html)
- [Google Gen AI SDK](https://googleapis.github.io/python-genai/)
- [Gemini structured output](https://ai.google.dev/gemini-api/docs/structured-output)
- [Swift Concurrency](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/concurrency/)
- [Swift Testing](https://developer.apple.com/documentation/testing/)
- [WWDC26 Apple Intelligence guide](https://developer.apple.com/wwdc26/guides/apple-intelligence/)

## Orientation exit gate

- [ ] Every diagnostic has a score/result and evidence.
- [ ] Missing Sprint 1 prerequisites are installed or scheduled in the first
      block.
- [ ] No credential or Walmart-confidential information is in the repository.
- [ ] Provider and cloud budgets/alerts are recorded.
- [ ] DSA language is selected or the Consolidation 1 decision is explicit.
- [x] Apple hardware, SDK, simulator, and system-model availability are
      recorded in [PROGRESS.md](file:///Users/swapnildhiman/Desktop/AI/iOSToAIJourney/PROGRESS.md#L37-L61).
- [ ] Sprint 1 has no more than a 20% evidence-based adjustment.

If the gate fails, begin Sprint 1 with the oldest prerequisite. Do not expand
orientation into a second setup week.
