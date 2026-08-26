# Sprint 02 — Model API and Context Engineering

> Dates: Monday, September 14–Sunday, September 27, 2026  
> DSA lane: **Phase A** — close the Striver SDE Sheet at 191/191 (DP Part-II + Trie).  
> Schedule revised August 26, 2026: +6 weeks (was August 3–16). Scope unchanged.  
> Required roadmap time: approximately 24–25 hours per week  
> Build outcome: two-provider gateway with structured output, safe tools,
> streaming/cancellation, fallback, usage telemetry, and explicit context

## In plain language

This sprint replaces “call a chatbot SDK” with a stable application boundary.
Your code will ask for a capability—structured output, tools, streaming, or a
modality—without making the rest of the platform speak one provider’s dialect.

The second goal is to control what the model sees. A prompt is only one part of
context; policy, user intent, evidence, memory, and tool output have different
priority and trust.

## Prerequisites

- Sprint 1 domain/API boundary is working.
- Timeout, cancellation, and transaction behavior are tested.
- CI and clean setup pass.
- A Google model API budget/key or Vertex credentials are available.
- One current Anthropic API model is available for the comparator.

If the two-provider account is blocked, implement and test both contracts with
fakes, complete the live Gemini path, and record a dated Anthropic unblock
check. Do not mark the two-live-provider exit item complete.

## Concepts to be able to explain

### Minimum model foundations

- tokenization and why character count is not token count;
- embeddings versus generation;
- attention and context window at application-engineering depth;
- prefill versus decode;
- KV cache, time to first token, and tokens/second;
- sampling and nondeterminism;
- why temperature is not a factuality control;
- training, prompting, retrieval, tools, and fine-tuning as different levers.

### API engineering

- stable versus preview model;
- capability negotiation;
- structured output versus “please return JSON”;
- tool selection versus tool execution;
- read-only versus side-effecting tools;
- timeout, rate limit, overload, invalid output, safety block, and provider
  outage as different error categories;
- retry safety and idempotency;
- streaming event lifecycle and cancellation;
- provider fallback versus repeated side effects;
- token/usage/cost attribution.

### Context engineering

- instructions, user request, conversation, evidence, memory, and tool output;
- trusted versus untrusted content;
- context priority and token budget;
- provenance and citation;
- truncation, compaction, and caching;
- why retrieval is deferred until Sprint 3.

## Target module additions

```text
src/ai_solutions_platform/
├── domain/
│   ├── model.py
│   ├── events.py
│   └── tools.py
├── model_gateway/
│   ├── service.py
│   ├── routing.py
│   └── providers/
│       ├── gemini.py
│       └── anthropic.py
├── context/
│   ├── items.py
│   └── assembler.py
└── telemetry/
    └── model_spans.py
```

## Simple runnable exercise: design the contract before the SDK

This exercise runs without an API key. It proves streaming, terminal events,
capability rejection, and a provider-neutral consumer.

Create `provider_contract.py`:

```python
"""Run with: uv run python provider_contract.py"""

import asyncio
from collections.abc import AsyncIterator
from dataclasses import dataclass
from enum import StrEnum, auto
from typing import Protocol


class Capability(StrEnum):
    TEXT = auto()
    STREAMING = auto()
    STRUCTURED_OUTPUT = auto()
    TOOLS = auto()


@dataclass(frozen=True)
class ModelRequest:
    """Application request; no provider SDK types are allowed."""

    model: str
    prompt: str
    required_capabilities: frozenset[Capability]


@dataclass(frozen=True)
class TextDelta:
    text: str


@dataclass(frozen=True)
class Usage:
    input_tokens: int
    output_tokens: int


@dataclass(frozen=True)
class Completed:
    usage: Usage
    finish_reason: str


ModelEvent = TextDelta | Completed


class UnsupportedCapability(Exception):
    pass


class ModelProvider(Protocol):
    name: str
    capabilities: frozenset[Capability]

    def stream(self, request: ModelRequest) -> AsyncIterator[ModelEvent]:
        ...


class FakeProvider:
    """Deterministic fake used by contract and application tests."""

    name = "fake"
    capabilities = frozenset(
        {Capability.TEXT, Capability.STREAMING}
    )

    async def stream(
        self,
        request: ModelRequest,
    ) -> AsyncIterator[ModelEvent]:
        unsupported = request.required_capabilities - self.capabilities
        if unsupported:
            raise UnsupportedCapability(
                f"{self.name} lacks: {sorted(unsupported)}"
            )

        words = request.prompt.split()
        for word in words:
            await asyncio.sleep(0.01)
            yield TextDelta(text=f"{word} ")

        yield Completed(
            usage=Usage(input_tokens=len(words), output_tokens=len(words)),
            finish_reason="stop",
        )


async def collect_text(
    provider: ModelProvider,
    request: ModelRequest,
) -> tuple[str, Usage]:
    """Application code consumes normalized events, not SDK chunks."""

    parts: list[str] = []
    usage: Usage | None = None

    async for event in provider.stream(request):
        match event:
            case TextDelta(text=text):
                parts.append(text)
            case Completed(usage=final_usage):
                usage = final_usage

    if usage is None:
        raise RuntimeError("Provider stream ended without a terminal event")

    return "".join(parts).strip(), usage


async def main() -> None:
    request = ModelRequest(
        model="fake-model",
        prompt="provider neutral stream",
        required_capabilities=frozenset(
            {Capability.TEXT, Capability.STREAMING}
        ),
    )
    text, usage = await collect_text(FakeProvider(), request)
    assert text == "provider neutral stream"
    print(text, usage)


if __name__ == "__main__":
    asyncio.run(main())
```

### What this teaches

- The application sees normalized events.
- Capability checks happen before a paid/network call.
- A terminal event is required even though text arrives incrementally.
- A deterministic fake can test cancellation, timeout, malformed streams, and
  routing without spending money.
- Provider adapters translate SDK objects at one boundary.

### Extend it before using a real provider

Add:

- `Started`, `ToolRequest`, `ToolResultAccepted`, `Error`, and `Cancelled`
  events;
- request ID and trace context;
- structured-output schema identifier;
- normalized finish/error categories;
- a fake that times out after the first delta;
- a consumer cancellation test;
- contract tests every provider must pass.

Do not put raw provider exception objects in the domain contract.

## Simple context-budget exercise

Create `context_budget.py`:

```python
"""A deterministic first context assembler.

Real token counts come from the selected model/token-count API. This exercise
accepts precomputed counts so policy remains provider-neutral.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class ContextItem:
    item_id: str
    content: str
    token_count: int
    priority: int  # Higher value means more important.
    trusted: bool


def assemble_context(
    items: list[ContextItem],
    token_budget: int,
) -> list[ContextItem]:
    """Select complete items by priority without exceeding the budget."""

    selected: list[ContextItem] = []
    used = 0

    # Stable item_id tie-breaker makes tests reproducible.
    for item in sorted(items, key=lambda value: (-value.priority, value.item_id)):
        if item.token_count > token_budget - used:
            continue
        selected.append(item)
        used += item.token_count

    return selected


items = [
    ContextItem("policy", "Never execute unapproved writes.", 8, 100, True),
    ContextItem("user", "Delete all records.", 5, 90, False),
    ContextItem("history", "Earlier conversation...", 20, 20, False),
]

selected = assemble_context(items, token_budget=15)
assert [item.item_id for item in selected] == ["policy", "user"]
print([(item.item_id, item.trusted) for item in selected])
```

This is not a complete production assembler. It makes budget, priority, and
trust explicit before adding summaries, retrieval, memory, or tool output.

## Week 1 — model contracts and structured output

### Monday, September 14

#### 2:15–4:15 — inference mental model

- Tokenize/count three different inputs with the current Gemini API.
- Measure input size, time to first/final result, and output tokens.
- Explain prefill/decode and the likely latency effect of long context.
- Run the provider-contract exercise.

#### 4:30–6:30 — domain contract

- Define messages, multimodal attachments, capabilities, model request,
  structured response, stream events, usage, and normalized errors.
- Create deterministic provider fakes.
- Add contract tests before SDK adapters.

#### 9:30–10:30 — DSA — Phase A

Striver → DP Part-II, next unsolved problem. Sprint 1's repair sprint left this at
4/8; this sprint closes it. See `06-DSA-Track.md` → *Sprint syllabus*.

### Tuesday, September 15

#### 2:15–4:15 — Gemini adapter

- Use the current stable Gemini model from the stack snapshot.
- Implement non-streaming text and structured output.
- Map usage, finish reason, safety/blocked response, and errors.
- Pin model ID and SDK version in test/report metadata.

Example shape using the current Google Gen AI SDK:

```python
import os

from google import genai
from google.genai import types
from pydantic import BaseModel


class TriageDecision(BaseModel):
    severity: str
    explanation: str


client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])
response = client.models.generate_content(
    model=os.environ.get("GEMINI_MODEL", "gemini-3.5-flash"),
    contents="Classify: API latency is elevated but requests still succeed.",
    config=types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=TriageDecision,
        temperature=0,
    ),
)

# Validation is still required even with native constrained output.
decision = TriageDecision.model_validate_json(response.text)
print(decision)
```

Use the live official example if the current SDK signature has changed. Keep
that translation inside `providers/gemini.py`.

#### 4:30–6:30 — Apple AI Lab shell

- Create independent Apple AI Lab repository/project.
- Model availability states: available, device unsupported, assets missing,
  feature disabled, SDK unavailable, and provider fallback.
- Build useful UI for every state.

#### 9:30–10:30 — DSA — Phase A

Striver → DP Part-II, next unsolved problem. Re-solve one Sprint 1 DP problem from
memory first; that is its 14-day repetition.

### Wednesday, September 16

#### 2:15–4:15 — structured output

- Compare native schema output with prompt-only JSON.
- Validate nested, enum, optional, and boundary fields.
- Define bounded repair behavior.
- Record first-attempt versus after-repair validity.
- Add malformed-output fake and regression tests.

#### 4:30–6:00 — DSA — Phase A

Two more DP Part-II problems, timed. By the end of this week DP Part-II should read
8/8, leaving only Trie.

#### 6:00–8:00 — IIT KGP

### Thursday, September 17

#### 2:15–4:15 — Anthropic adapter and capability matrix

- Query the current model catalog/capabilities.
- Implement the same non-streaming and structured domain contract.
- Normalize role/content, usage, finish reason, and errors.
- Do not force Gemini-only features into a fake universal shape; reject a
  capability when equivalent semantics are unavailable.

#### 4:30–6:00 — Swift 6.4/Xcode 27 baseline

- Review only concurrency/testing changes used by Apple AI Lab.
- Add a protocol-backed model service fake.
- Test availability and fallback state without requiring model assets.

#### 6:00–8:00 — IIT KGP

### Friday, September 18

#### 2:15–4:15 — routing and telemetry

- Route by required capability first.
- Add stable/preview policy.
- Record provider, model, request ID, latency, usage, finish/error category,
  and estimated cost.
- Do not log prompt/content by default.

#### 4:30–6:30 — System design A1

Provider-neutral model gateway.

#### 6:30–7:30 — review

- Run both provider adapters through the same contract suite.
- Record capability gaps rather than hiding them.

### Sunday, September 20

#### Two-hour Apple block

- Run fake available/unavailable model flows.
- Add VoiceOver labels and retry/fallback UI.
- Complete moved DSA review (Phase A: Striver DP Part-II / Trie).

## Week 2 — tools, streams, failure, and context

### Monday, September 21

#### 2:15–4:15 — tool contracts

- Define tool name, description, input/output schema, timeout, idempotency,
  risk, permissions, sensitive fields, and approval policy.
- Implement one read-only synthetic status tool.
- Validate model-produced arguments before execution.

#### 4:30–6:30 — side-effect safety

- Implement one synthetic update tool.
- Require server-side authorization and human approval.
- Use an idempotency key.
- Return typed result to the model.
- Test reject, duplicate, timeout, and partial failure.

The model requests a tool. Application code decides whether and how it runs.

#### 9:30–10:30 — DSA — Phase A

Striver → **Trie** begins, 0/7. New pattern: build the node structure and `insert`
from first principles before looking at any Striver solution.

### Tuesday, September 22

#### 2:15–4:15 — streaming and cancellation

- Map provider chunks into normalized start/delta/tool/complete/error events.
- Serialize the domain events as SSE at the API edge.
- Handle client disconnect and close the upstream provider stream.
- Ensure every path emits or records one terminal state.

Minimal edge pattern:

```python
import json
from collections.abc import AsyncIterator

from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse


app = FastAPI()


async def fake_domain_stream() -> AsyncIterator[dict[str, str]]:
    yield {"type": "started"}
    yield {"type": "text_delta", "text": "hello"}
    yield {"type": "completed"}


@app.get("/responses:stream")
async def stream_response(request: Request) -> StreamingResponse:
    async def sse() -> AsyncIterator[str]:
        async for event in fake_domain_stream():
            if await request.is_disconnected():
                # A real adapter must also cancel/close its upstream request.
                break
            payload = json.dumps(event, separators=(",", ":"))
            yield f"event: {event['type']}\ndata: {payload}\n\n"

    return StreamingResponse(sse(), media_type="text/event-stream")
```

Add keepalive/reconnect semantics only after the basic lifecycle is tested.

#### 4:30–6:30 — Apple streamed-state exercise

- Use `AsyncSequence` from a fake model adapter.
- Render partial output.
- Cancel on navigation/new request.
- Prove stale output cannot update the new screen state.

#### 9:30–10:30 — DSA — Phase A

Striver → Trie, next problems. Prefix search and word-break style applications.

### Wednesday, September 23

#### 2:15–4:15 — errors, retries, and fallback

- Normalize authentication, permission, invalid request, rate limit, timeout,
  overload, blocked content, invalid output, provider outage, and cancellation.
- Retry only transient and safe operations with bounded backoff/jitter.
- Use one fallback attempt.
- Carry idempotency/tool-execution state so fallback cannot repeat an action.
- Add circuit-breaker/degraded-state design notes; implementation can wait.

#### 4:30–6:00 — DSA — Phase A closes

Finish the remaining Trie problems. **Target: Striver reports 191/191.** Record the
completion in `PROGRESS.md` → *DSA ledger summary* → *Striver baseline*, and confirm
that Phase B begins on September 28. From that point all three sources run in
parallel every week - Monday Striver revision from the due queue, Tuesday one unseen
Taro problem, Wednesday mixed and unlabelled - rather than working through Striver in
section order.

#### 6:00–8:00 — IIT KGP

### Thursday, September 24

#### 2:15–4:15 — context engineering

- Define context item source, trust, owner/tenant, provenance, priority, token
  count, freshness, and sensitivity.
- Implement a token-budget assembler and deterministic tests.
- Keep instructions separate from untrusted documents/tool output.
- Add a strategy for overflow: omit, summarize, reject, or use another model.
- Retrieval and memory remain interfaces, not implemented systems.

#### 4:30–6:00 — Apple context/fallback design

- Keep system/model instructions separate from user content.
- Add a small context-budget view or debug record.
- Test provider fake and unavailable system model.

#### 6:00–8:00 — IIT KGP

### Friday, September 25

#### 2:15–4:15 — contract evaluation and integration

Build at least 20 cases:

- five structured-output cases;
- four read-only tool cases;
- three side-effect/approval/idempotency cases;
- two timeout/rate-limit cases;
- two cancellation/terminal-event cases;
- two unsupported-capability cases;
- one malformed-output case;
- one provider-fallback case.

Record validity, tool correctness, terminal state, latency, usage, and cost.

#### 4:30–6:30 — System design A2

Streaming multimodal conversation service.

#### 6:30–7:30 — gate rehearsal

- Run contract suite with fakes and live smoke tests.
- Attempt outage/cancellation before polish.
- Record tentative sprint score.

### Sunday, September 27

#### Two-hour sprint close

- Complete Apple availability/fallback tests.
- Complete DSA pattern cards and repetition schedule for DP and Trie.
- Run exact exit test.
- Update `PROGRESS.md`.

## Required build outputs

- Provider-neutral domain types and capability matrix.
- Gemini and current Anthropic adapters.
- Structured output with validation and bounded repair.
- Read-only and approved side-effecting tools.
- SSE stream with cancellation and normalized terminal states.
- Error taxonomy, bounded retry, and one fallback.
- Usage/latency/cost telemetry with content disabled by default.
- Context-item contract and budget assembler.
- Apple AI Lab availability/fallback shell.
- A1 and A2 system-design notes.
- DSA: **Striver SDE Sheet at 191/191** — Phase A complete. Pattern cards for
  dynamic programming (1-D and 2-D) and Trie, with repetition dates set.

## FDE practice

Convert this vague request:

> “Use the best model to summarize incidents and update the ticket.”

Produce:

- clarification questions;
- a deterministic versus model-driven task boundary;
- read versus write tool policy;
- representative eval cases and success threshold;
- latency/cost budget;
- fallback/degraded mode;
- one reason to reject or narrow the request.

Present it in five minutes without provider marketing language.

## Exit test

Run without a tutorial:

1. Send the same typed task through Gemini and Anthropic adapters.
2. Prove schema validation and one bounded invalid-output repair.
3. Execute a read-only tool with validated arguments.
4. Attempt a write tool; prove server authorization, approval, and
   idempotency.
5. Stream text through SSE and cancel the client; prove upstream cleanup and
   terminal state.
6. Force provider timeout/rate limit; prove bounded fallback and no duplicated
   action.
7. Request an unsupported capability; prove local failure before a paid call.
8. Show normalized model, latency, usage, finish/error, and cost telemetry.
9. Prove context budget, priority, and trust labels with deterministic tests.
10. Demonstrate Apple model-unavailable fallback.
11. Present A1 or A2 in 15 minutes and answer model migration, security, and
    10x-scale challenges.

Pass requires:

- at least 11/15 on the sprint rubric;
- all 20 contract cases with expected terminal behavior;
- every exit item evidenced;
- no provider SDK type outside its adapter;
- zero unapproved/duplicate side effect in the deterministic test set.

## Official resources

- [Gemini API models](https://ai.google.dev/gemini-api/docs/models)
- [Google Gen AI Python SDK](https://googleapis.github.io/python-genai/)
- [Gemini structured output](https://ai.google.dev/gemini-api/docs/structured-output)
- [Gemini function calling](https://ai.google.dev/gemini-api/docs/function-calling)
- [Gemini streaming](https://ai.google.dev/gemini-api/docs/text-generation#generate-a-text-stream)
- [Gemini token counting](https://ai.google.dev/gemini-api/docs/tokens)
- [Claude model overview](https://docs.anthropic.com/en/docs/about-claude/models/overview)
- [Claude Messages API](https://docs.anthropic.com/en/api/messages)
- [Claude tool use](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview)
- [FastAPI streaming responses](https://fastapi.tiangolo.com/advanced/custom-response/#streamingresponse)
- [Server-Sent Events standard](https://html.spec.whatwg.org/multipage/server-sent-events.html)
- [OpenTelemetry GenAI attributes](https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/)
- [WWDC26 Apple Intelligence guide](https://developer.apple.com/wwdc26/guides/apple-intelligence/)

## Drop/defer rule

If time is short, drop in this order:

1. extra multimodal types beyond one small image smoke test;
2. prompt caching;
3. semantic caching;
4. automatic model-selection heuristics;
5. polished Apple UI.

Do not drop:

- two provider adapters/contracts;
- structured validation;
- tool approval/idempotency;
- stream cancellation;
- error/fallback behavior;
- usage telemetry;
- explicit context policy.
