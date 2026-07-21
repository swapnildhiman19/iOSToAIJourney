# Roadmap Validation

> Audit date: July 18, 2026
> Result: **PASS**

This audit checks the rebuilt roadmap against the attached implementation plan.
It validates structure and internal consistency; it does not claim that future
preview APIs will remain unchanged.

## Roadmap coach skill

- [x] [`skill.md`](./skill.md) is the canonical `ai-roadmap-coach` v2.1.0 copy.
- [x] Kiro, Cursor, Claude, and Gemini installation paths are documented in
      `00-FRESH-SYSTEM-CONTEXT.md` and carry identical skill content.
- [x] Multi-intent requests have a deterministic verify → score → record order.
- [x] Task-specific rubrics take precedence over whole-sprint scoring.
- [x] Artifact verification and evidence-safe ledger transactions are explicit.
- [x] The active gate must match the active sprint before sprint assessment.
- [x] Scheduled-sprint authoring preserves dates, prerequisites, weekly budget,
      portfolio boundaries, evidence, exit gates, and drop/defer rules.
- [x] Unscheduled sprints and roadmap sequence changes require approved impact
      analysis.
- [x] `AI-ROADMAP-PROMPT-CONTEXT.md` carries the v2 fallback behavior rules.

## Calendar

- [x] Orientation runs July 16–19, 2026.
- [x] Exactly 16 sprints are present.
- [x] Every sprint is 14 inclusive days, Monday through Sunday.
- [x] Consolidation weeks follow Sprints 4, 8, 12, and 16.
- [x] Every consolidation week is seven days.
- [x] Blocks are contiguous with no gap or overlap.
- [x] Final verification is March 29–31, 2027.
- [x] The active target remains March 31, 2027.

## Weekly budget

Normal weekly calculation:

- AI core/platform: 12 hours.
- Apple: 5.5 hours.
- DSA: 4 hours.
- System design: 2 hours.
- Review/FDE evidence: 1 hour.
- Roadmap total: approximately 24.5 hours.
- IIT KGP: 4 additional hours, tracked separately.

The Wednesday/Thursday 6:00 PM class overlap is handled by ending the rotating
block at 6:00 and moving only 30 minutes. Optional time replaces missed work
instead of raising the baseline.

## Sprint contract

- [x] Every sprint has a stated prerequisite in the master prerequisite chain.
- [x] Every sprint contains theory/competency work.
- [x] Every sprint changes a portfolio or interview artifact.
- [x] Every sprint has a measurable exit gate.
- [x] Every sprint schedules DSA and system design.
- [x] Every sprint specifies public-safe evidence.
- [x] Every sprint has a cut/defer rule.
- [x] Failed prerequisites pause dependent work.

## System-design count

Verified unique case headings:

- AI: 18.
- iOS: 10.
- Backend/distributed: 6.
- Total: 34.

The schedule in the master roadmap matches the catalog. Orientation is an
uncounted diagnostic; Consolidations 1 and 3 contain B2 and I6; Consolidations
2 and 4 repeat weak cases.

## DSA

- [x] Four hours per week.
- [x] Swift/Python primary-language decision uses an orientation diagnostic.
- [x] All required patterns are scheduled.
- [x] Spaced repetition distinguishes failed, hinted, and clean solves.
- [x] Timed mediums, company-tagged work, and mocks progress by phase.
- [x] Quality and recall replace a large solved-count target.

## AI/FDE coverage

- [x] Python, FastAPI, async, SQL/Postgres, Redis, storage, events, and tests.
- [x] Provider-neutral Gemini-primary gateway and current Claude comparator.
- [x] Structured output, tools, multimodal input, streams, cancellation,
      fallback, token/cost accounting, and capability routing.
- [x] Context engineering and a measured choice among SQL/exact search, long
      context, native file search, hybrid retrieval, graph, and agentic
      retrieval.
- [x] Explicit state, memory, harness, eval, and runtime design.
- [x] ADK 2.0 graph workflows, deterministic/model boundaries, durable state,
      approvals, multi-agent patterns, MCP, and A2A.
- [x] LiveKit/WebRTC, cascaded/native voice, turn detection, barge-in, handoff,
      latency, fallback, and voice evaluation.
- [x] Containers, CI/CD, Cloud Run, functions/Eventarc, Agent Runtime, IAM,
      secrets, queues, OpenTelemetry, SLO, load/fault/cost, and scale.
- [x] Tenant isolation, RBAC/policy, audit, quotas, PII, prompt/tool security,
      Agent Identity, Agent Gateway, and Model Armor.
- [x] Working literacy—not a second platform—in Terraform, GKE/Kubernetes, and
      AWS Bedrock.
- [x] Full FDE lifecycle from qualification/discovery to rollout, adoption,
      handoff, no-go decision, and reusable playbook.

## Apple coverage

- [x] Apple AI projects remain independent from the backend platform.
- [x] Foundation Models v2, multimodal input, structured generation, tools,
      streaming, and model availability.
- [x] Dynamic Profiles, Evaluations, Foundation Models Instruments, App
      Intents, Core Spotlight, view annotations, and AppIntentsTesting.
- [x] Core AI generative deployment, traditional Core ML, MLX/SLM,
      quantization, and local/cloud benchmarks.
- [x] Swift 6.4, current Swift Concurrency/Testing, SwiftUI 2027 additions,
      Xcode 27/Device Hub, current design tools, and Metal 4 literacy.
- [x] Beta/preview and hardware-dependent features are labeled.
- [x] Mac-first progress is possible before a physical-device/developer-account
      checkpoint.

## Portfolio separation

- [x] AI Solutions Platform has provider, context, memory, harness, agents,
      realtime, eval, policy, integration, and telemetry boundaries.
- [x] Flutter is a thin text/voice demonstration client.
- [x] Apple AI Lab is a standalone Foundation Models/App Intents project.
- [x] Local AI Workbench is a standalone Core AI/Core ML/MLX project.
- [x] Synthetic/public scenarios replace Walmart data.
- [x] Four case studies map directly to measured platform/FDE evidence.

## Currentness and archive isolation

- [x] Complete old Week 1, project placeholders, post drafts, and personal
      legacy notes are under `archive/pre-WWDC26/source/`.
- [x] The active index does not navigate to the legacy schedule.
- [x] Legacy Gemini 2.5, Xcode 16, and Vertex Agent Engine assumptions remain
      only inside the archive or are named explicitly as retired terminology.
- [x] The July 16 stack snapshot uses Gemini 3.x/3.5, Gemini Embedding 2,
      ADK 2.0, Gemini Enterprise Agent Platform/Agent Runtime, current stable
      MCP with the July 28 candidate flagged, and WWDC26 APIs.
- [x] Stable/preview status and phase-boundary refreshes are explicit.

## Detailed horizon

- [x] Orientation has exact sessions, diagnostics, official sources, runnable
      Python/Swift exercises, outputs, and an exit gate.
- [x] Sprint 1 has exact sessions, an independently runnable FastAPI exercise,
      platform/Apple/DSA/design/FDE outputs, official sources, and an exit test.
- [x] Sprint 2 has exact sessions, independently runnable provider/context
      exercises, two-provider/tool/stream/failure requirements, official
      sources, and an exit test.
- [x] Later sprints remain outcome-level and are expanded at the prior
      consolidation checkpoint.

## Executable sample checks

- [x] The bounded-async orientation Python sample ran successfully on Python
      3.12.
- [x] The provider-neutral stream sample ran and emitted its required terminal
      usage event.
- [x] The deterministic context-budget sample selected the expected items.
- [x] The Sprint 1 FastAPI create/validation/duplicate flow ran successfully on
      Python 3.12 with current FastAPI/Pydantic.
- [ ] Live Gemini/Claude and Apple model samples intentionally remain
      orientation/Sprint 2 checks because they require the user’s credentials,
      budget, SDK, hardware, and availability state.

## Measurability

- [x] Sprint score and pass/partial/fail rules exist.
- [x] Initial schema, retrieval, agent, text, voice, reliability, security, and
      Apple targets exist.
- [x] Monthly portfolio audits and phase gates exist.
- [x] Minimum-viable week and failure-specific recovery actions exist.
- [x] `PROGRESS.md` tracks evidence, hours, scores, stack refreshes, blockers,
      recovery, portfolio milestones, and interview readiness.

## Known time-sensitive assumptions

Recheck rather than silently trust:

- model IDs, pricing, region availability, and provider capability;
- the MCP `2026-07-28` final publication/migration;
- ADK/Agent Runtime and LiveKit APIs;
- OpenTelemetry GenAI semantic-convention stability;
- Xcode 27/OS 27 release status and Apple beta API signatures;
- physical-device and paid-developer-account availability.

These assumptions have dated checkpoints and do not invalidate the durable
competency sequence.
