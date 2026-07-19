# AI Solutions Platform

> A reusable engine for enterprise AI solutions — text, voice, context, agents,
> tools, evaluations, security, and observability.

## Status

**Sprint 0 — Orientation skeleton.** No production code yet.

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
│       ├── domain/           # Provider-neutral types
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
└── README.md
```

## Quick start

```bash
# Create virtual environment and install dependencies
uv venv
source .venv/bin/activate
uv pip install -e ".[dev]"

# Copy and configure secrets
cp .env.example .env
# Edit .env with your API keys — never commit .env

# Run tests
pytest
```

## Security

- `.env` and all credential files are gitignored at the repo root.
- No Walmart-confidential, proprietary, or real customer data in this repo.
- Model artifacts, database files, and Xcode user data are gitignored.
- Provider API keys go in `.env` or a secret manager, never in source.
