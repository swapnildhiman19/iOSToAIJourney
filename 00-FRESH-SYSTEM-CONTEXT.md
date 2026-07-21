# Fresh-System Context and Handoff

> Portable bootstrap document for the AI FDE + iOS AI journey  
> Context snapshot: July 16, 2026  
> Target readiness date: March 31, 2027

## Purpose

Keep this file with the complete `iOSToAIJourney/` directory when:

- moving the roadmap to another computer;
- starting a fresh AI session;
- resuming after a long break;
- losing access to the original planning conversation.

All links are relative so the directory can move safely.

Routine questions such as "What should I study today?", "Where do I record
this?", "What is my score?", or "Create the next detailed sprint" are handled
by `ai-roadmap-coach` **v2.1.0**.

The canonical copy is [`skill.md`](./skill.md). These global installations are
distribution copies:

- **Antigravity IDE**: `~/.gemini/config/skills/ai-roadmap-coach/SKILL.md`
- **Kilo IDE (Cursor)**: `~/.cursor/skills-cursor/ai-roadmap-coach/SKILL.md`
- **Kilo CLI (Claude)**: `~/.claude/skills/ai-roadmap-coach/SKILL.md`
- **KIRO IDE / KIRO CLI**: `~/.kiro/skills/ai-roadmap-coach/SKILL.md`

All distributed `SKILL.md` files must remain byte-equivalent to the canonical
copy after skill maintenance. Ask directly; no attachment is required. If
skills are unavailable, attach
[`AI-ROADMAP-PROMPT-CONTEXT.md`](./AI-ROADMAP-PROMPT-CONTEXT.md) instead.

This file is the broader machine/session handoff.

## Resume in five steps

1. Open [`PROGRESS.md`](./PROGRESS.md) and identify the active block.
2. Open the matching guide under [`sprints/`](./sprints/).
3. Find today's dated sessions.
4. Check [`09-Current-Stack-Snapshot.md`](./09-Current-Stack-Snapshot.md) if it
   is stale or a phase boundary passed.
5. Continue from the active gate; do not restart or redesign automatically.

At the time this snapshot was created, Orientation was ready to start.
`PROGRESS.md` overrides that statement after execution begins.

## Bootstrap prompt for a fresh AI assistant

```text
You are helping me execute my AI FDE + iOS AI roadmap.

Read these files first:
1. 00-FRESH-SYSTEM-CONTEXT.md
2. AI-ROADMAP-PROMPT-CONTEXT.md
3. PROGRESS.md
4. the active sprint file identified by PROGRESS.md
5. 09-Current-Stack-Snapshot.md when current APIs/models matter

PROGRESS.md is the status source of truth. The active sprint is the daily
instruction source. Do not reactivate archive/pre-WWDC26, redesign the whole
roadmap, or expand future sprints unless I explicitly request it.

Keep required roadmap work within 20–25 hours per week. IIT KGP classes are
separate. Failed gates require repair or consolidation, not silent completion.

Explain new concepts first in plain language, then technically. Use focused
runnable examples, comments, diagrams, official sources, and connections to the
current portfolio project.

The primary goal is production AI Engineer / Forward-Deployed AI Engineer
readiness by March 31, 2027. Modern iOS and Apple AI are the secondary
differentiator. Preserve the separation among the AI Solutions Platform, Apple
AI Lab, and Local AI Workbench.
```

## User and goal

- Background: experienced iOS engineer.
- Primary target: production AI Engineer and Forward-Deployed AI Engineer.
- Preparation level: Walmart/MAANG-level and advanced US/global AI-FDE roles.
- Deadline: March 31, 2027.
- Primary emphasis: universal production AI systems and full FDE ownership.
- Secondary emphasis: current iOS, Apple Intelligence, and on-device AI.
- ML theory: IIT KGP program, not duplicated here.
- Roadmap budget: 20–25 hours weekly.
- IIT KGP: Wednesday and Thursday, 6:00–8:00 PM.
- DSA: four hours weekly.
- System design: one weekly case, followed by later mocks.
- Public evidence: four substantial engineering case studies.
- Networking begins December 2026.
- Selective applications begin January 2027.

## Source-of-truth order

1. The user's newest correction or completion report.
2. [`PROGRESS.md`](./PROGRESS.md) for current status and evidence.
3. The active guide under [`sprints/`](./sprints/) for daily work.
4. [`08-Assessment-and-Recovery.md`](./08-Assessment-and-Recovery.md) for
   scoring and repair.
5. [`09-Current-Stack-Snapshot.md`](./09-Current-Stack-Snapshot.md) for current
   technology.
6. [`02-Master-Roadmap-Jul2026-Mar2027.md`](./02-Master-Roadmap-Jul2026-Mar2027.md)
   for sequence and dates.
7. [`01-Competency-Map.md`](./01-Competency-Map.md) for skill depth.
8. [`03-Portfolio-Architecture.md`](./03-Portfolio-Architecture.md) for project
   boundaries.

Everything under [`archive/pre-WWDC26/`](./archive/pre-WWDC26/) is historical
only.

## File map

- [`README.md`](./README.md) — navigation.
- [`AI-ROADMAP-PROMPT-CONTEXT.md`](./AI-ROADMAP-PROMPT-CONTEXT.md) — manual
  fallback context when the `ai-roadmap-coach` Cursor skill is unavailable.
- [`PROGRESS.md`](./PROGRESS.md) — status, evidence, scores, and blockers.
- [`01-Competency-Map.md`](./01-Competency-Map.md) — required/working/deferred
  skills.
- [`02-Master-Roadmap-Jul2026-Mar2027.md`](./02-Master-Roadmap-Jul2026-Mar2027.md)
  — complete dated roadmap.
- [`03-Portfolio-Architecture.md`](./03-Portfolio-Architecture.md) — projects
  and technical boundaries.
- [`04-Weekly-Operating-System.md`](./04-Weekly-Operating-System.md) — weekly
  timetable.
- [`05-System-Design-Track.md`](./05-System-Design-Track.md) — 34 cases.
- [`06-DSA-Track.md`](./06-DSA-Track.md) — four-hour weekly DSA method.
- [`07-FDE-Track.md`](./07-FDE-Track.md) — discovery-to-handoff practice.
- [`08-Assessment-and-Recovery.md`](./08-Assessment-and-Recovery.md) — gates,
  targets, and recovery.
- [`09-Current-Stack-Snapshot.md`](./09-Current-Stack-Snapshot.md) — dated
  model/framework/API choices.
- [`VALIDATION.md`](./VALIDATION.md) — structural validation.
- [`sprints/`](./sprints/) — current executable sprint guides.

Only Orientation and Sprints 1–2 were initially expanded. Later guides are
written shortly before execution so fast-moving APIs stay current.

## Daily execution rule

At any time, there is one active block.

1. Read the active sprint.
2. Find today's date.
3. Complete only today's sessions.
4. Produce code, tests, evals, measurements, design scores, or stated evidence.
5. Do not add unrelated technology.
6. Stop when the block ends.
7. Update `PROGRESS.md` during Friday review and the sprint gate.

The master roadmap is not a daily checklist.

## Normal weekly timetable

### Monday

- 2:15–4:15 PM: current AI/backend competency.
- 4:30–6:30 PM: AI Solutions Platform.
- 9:30–10:30 PM: DSA repetition.

### Tuesday

- 2:15–4:15 PM: current AI/backend competency.
- 4:30–6:30 PM: Apple AI Lab or Local AI Workbench.
- 9:30–10:30 PM: unseen DSA problem.

### Wednesday

- 2:15–4:15 PM: current AI/backend competency.
- 4:30–6:00 PM: DSA.
- 6:00–8:00 PM: IIT KGP.

### Thursday

- 2:15–4:15 PM: current AI/backend competency.
- 4:30–6:00 PM: Apple project.
- 6:00–8:00 PM: IIT KGP.

### Friday

- 2:15–4:15 PM: integration, tests, evals, or repair.
- 4:30–6:30 PM: system design.
- 6:30–7:30 PM: review and `PROGRESS.md`.

### Weekend

- Saturday: recovery/replacement only.
- Sunday: two-hour Apple deep-work block.

Roadmap total: approximately 24.5–25 hours. IIT adds four separate hours.

## Complete phase sequence

### Orientation — July 16–19, 2026

Environment, Python/backend, Apple, DSA, system-design, and FDE diagnostics.

### Phase 1

- Sprint 1, July 20–August 2: Python/FastAPI/backend.
- Sprint 2, August 3–16: provider-neutral model API and context.
- Sprint 3, August 17–30: knowledge/retrieval decision.
- Sprint 4, August 31–September 13: state, memory, harness, and evals.
- Consolidation 1, September 14–20.

### Phase 2

- Sprint 5, September 21–October 4: ADK 2.0 workflows.
- Sprint 6, October 5–18: multi-agent, MCP/A2A, and durable execution.
- Sprint 7, October 19–November 1: voice foundations.
- Sprint 8, November 2–15: production multi-text/multi-voice agents.
- Consolidation 2, November 16–22.

### Phase 3

- Sprint 9, November 23–December 6: security and tenant controls.
- Sprint 10, December 7–20: GCP deployment and events.
- Sprint 11, December 21–January 3: reliability, telemetry, scale, latency, and
  cost.
- Sprint 12, January 4–17: LoRA experiment and production beta.
- Consolidation 3, January 18–24.

### Phase 4

- Sprint 13, January 25–February 7: FDE discovery/pilot/integration.
- Sprint 14, February 8–21: public release and portfolio.
- Sprint 15, February 22–March 7: interview loops.
- Sprint 16, March 8–21: final FDE simulation.
- Consolidation 4, March 22–28.
- Final verification, March 29–31.

## Portfolio 1 — AI Solutions Platform

Primary flagship proving transferable AI/FDE engineering:

- Python/FastAPI;
- Gemini primary and Claude comparator/fallback;
- structured output, tools, multimodal input, and streams;
- context, SQL/search, retrieval, memory, and evals;
- ADK 2.0, MCP, A2A, and durable workflows;
- LiveKit/WebRTC text and multi-voice agents;
- identity, tenancy, security, audit, PII, and quotas;
- OpenTelemetry, SLOs, load/fault tests, latency, cost, and scale;
- Cloud Run, functions/Eventarc, queues, and Agent Runtime;
- thin Flutter text/voice demonstration client.

Reference scenarios use synthetic/public data:

1. Knowledge and research.
2. Operations triage with approved actions.
3. Developer workflow with a GitHub-style integration.

## Portfolio 2 — Apple AI Lab

Separate SwiftUI project:

- Foundation Models v2;
- system-model availability and fallback;
- text/image input, structured output, tools, and streaming;
- Dynamic Profiles;
- Apple Evaluations and Foundation Models Instruments;
- App Intents, Siri-facing actions, Core Spotlight, and AppIntentsTesting;
- current SwiftUI, concurrency, testing, and accessibility.

## Portfolio 3 — Local AI Workbench

Separate Mac-first project:

- Core AI custom generative-model deployment;
- one traditional Core ML model;
- MLX/MLX-LM local SLM;
- quantization, local tool use, and one LoRA experiment;
- Core AI/Core ML/MLX/cloud benchmark;
- quality, startup, first token, speed, memory, energy, privacy, and cost.

Core AI begins in Phase 3, not during Orientation or Sprint 1.

## Initial technical direction

Always verify current details in `09-Current-Stack-Snapshot.md`.

- Python 3.12+ and FastAPI.
- Gemini/GCP primary.
- Claude as a real comparator/fallback.
- ADK 2.0 primary agent framework.
- MCP for tools and A2A for independent agents.
- LiveKit/WebRTC for voice.
- Postgres durable state and Redis ephemeral state/cache.
- OpenTelemetry for observability.
- Cloud Run default; Agent Runtime where justified.
- Foundation Models v2 and Core AI with beta/device fallbacks.
- Kubernetes, Terraform, and AWS Bedrock at working-literacy depth.

Do not freeze model IDs or preview APIs for the entire roadmap.

## Context/RAG rule

RAG is one context strategy.

Use this order:

1. deterministic code or SQL;
2. exact/filtered search;
3. native file search or cached long context;
4. hybrid lexical+dense retrieval and reranking;
5. graph retrieval for measured relationship failures;
6. agentic retrieval for genuinely iterative research.

Compare quality, latency, freshness, authorization, and cost.

## Assessment and recovery

A normal sprint is scored 0–3 across:

1. conceptual depth;
2. implementation correctness;
3. tests/evaluation;
4. production/security behavior;
5. communication/evidence.

Maximum: 15.

- Pass: at least 11/15, all explicit gates satisfied, no zero.
- Partial: at least 8/15 with a precise noncritical repair.
- Fail: below 8/15, missing prerequisite, or critical security/data failure.
- Blocked: external dependency with substitute and recheck documented.

Rules:

- evidence, not hours, proves completion;
- failed prerequisites pause dependent work;
- failed gates trigger repair/consolidation;
- optional blocks replace missed work;
- never create time debt or borrow sleep;
- do not fabricate scores or evidence.

## Security and privacy

- Never publish Walmart code, architecture, screenshots, identifiers, metrics,
  prompts, customer information, or internal data.
- Use synthetic or public fixtures.
- Never commit credentials, `.env`, model weights, database files, or Xcode
  user state.
- Tool authorization occurs outside the model.
- Use least privilege, tenant-scoped data, audit, quotas, PII controls,
  retention, and deletion.

## Fresh-machine setup

Install only what the active sprint requires.

### Orientation and Sprint 1

- Git.
- Python 3.12+.
- `uv`.
- Docker or reachable Postgres.
- Xcode and Swift.

### Sprint 2

- Google Gen AI credentials and budget.
- Anthropic credentials and budget, or a documented blocker.

### Later

- `gcloud` and production GCP resources.
- Flutter.
- ADK.
- LiveKit.
- Terraform/Kubernetes tooling.
- MLX/Core AI conversion tools.
- AWS account/CLI.

## Transfer checklist

- [ ] Copy/clone the complete repository with Git history.
- [ ] Preserve the relative directory structure.
- [ ] Keep `archive/pre-WWDC26/` archived.
- [ ] Do not transfer credentials or large model assets through Git.
- [ ] Recreate secrets securely.
- [ ] Read `PROGRESS.md` and identify the active sprint.
- [ ] Verify only the active sprint's tools.
- [ ] Re-run current setup/tests.
- [ ] Repair broken external evidence links.
- [ ] Refresh the stack snapshot when stale.
- [ ] Record new hardware, OS, Xcode, Python, Docker, and cloud versions.
- [ ] Continue from the current gate rather than restarting automatically.

## Final destination

By March 31, 2027, evidence should include:

- production-grade AI Solutions Platform;
- evaluated multi-text and multi-voice agents;
- secure and observable GCP deployment;
- complete FDE discovery-to-handoff simulation;
- Apple AI Lab;
- Core AI/Core ML/MLX Local AI Workbench;
- four deep case studies;
- 18 AI, 10 iOS, and 6 backend system designs;
- sustained DSA and interview mocks;
- resume claims linked to reproducible evidence.

On a fresh system, always resume from `PROGRESS.md`, not from this final list.
