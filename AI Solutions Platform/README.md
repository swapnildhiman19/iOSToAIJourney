# AI Solutions Platform

> A reusable engine for enterprise AI solutions — text, voice, context, agents,
> tools, evaluations, security, and observability.

## Status

**Sprint 1 — AI Software Foundations (active July 20–August 2, 2026).**

The typed domain/application boundary and in-memory repository are implemented
and independently verified. FastAPI, Postgres, the architecture decision, and
CI are still in progress; do not infer the Sprint 1 gate from the domain tests.
The dated recovery plan is in
[`Sprint-01-AI-Software-Foundations.md`](../sprints/Sprint-01-AI-Software-Foundations.md).

## Architecture

This is a **modular monolith** in Python/FastAPI. Modules split into services
only when a measured need exists (scaling, isolation, deployment ownership,
blocking workloads, or transport requirements such as real-time media).

See the [Portfolio Architecture](../03-Portfolio-Architecture.md) for the full
system map and module contracts.

## Project structure

```
AI Solutions Platform/
├── src/
│   └── ai_solutions_platform/
│       ├── __init__.py
│       ├── domain/           # Provider-neutral domain records and errors
│       ├── application/      # Use cases and required repository protocols
│       ├── persistence/      # In-memory now; Postgres adapter later
│       ├── model_gateway/    # Gemini + Anthropic adapters
│       ├── context/          # Retrieval strategies
│       ├── memory/           # Working, episodic, semantic, procedural
│       ├── harness/          # Model/tool lifecycle, budgets, approvals
│       ├── agent_runtime/    # ADK 2.0 adapter, MCP client, A2A
│       ├── realtime/         # Voice/streaming, LiveKit adapter
│       ├── tools/            # Reusable tool adapters
│       ├── evals/            # Evaluation framework
│       ├── identity_policy/  # Auth, tenants, PII, audit
│       └── telemetry/        # OpenTelemetry instrumentation
├── tests/
│   ├── unit/
│   ├── integration/
│   └── conftest.py
├── diagnostics/              # Orientation and sprint diagnostic scripts
├── .env.example
├── pyproject.toml
├── uv.lock
└── README.md
```

## Quick start

```bash
# Install the locked project and development dependencies
uv sync --locked --extra dev

# Copy and configure secrets when a task needs them
cp .env.example .env
# Edit .env with your API keys — never commit .env

# Run the current local quality gates
uv run --locked --extra dev ruff format --check src tests
uv run --locked --extra dev ruff check src tests
uv run --locked --extra dev mypy src tests
uv run --locked --extra dev pytest -q
```

## Security

- `.env` and all credential files are gitignored at the repo root.
- No Walmart-confidential, proprietary, or real customer data in this repo.
- Model artifacts, database files, and Xcode user data are gitignored.
- Provider API keys go in `.env` or a secret manager, never in source.
