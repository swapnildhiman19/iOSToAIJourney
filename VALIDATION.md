# Roadmap Validation

> Audit date: July 23, 2026 (structural)
> Last evidence verification: July 25, 2026 — see *July 24 evidence verification*
> Last schedule revision: August 26, 2026 — see *August 26 schedule revision*
> Result: **PASS** (structure); see the August 26 section for two open defects

This audit checks the rebuilt roadmap against the attached implementation plan.
It validates structure and internal consistency; it does not claim that future
preview APIs will remain unchanged.

## Roadmap coach skill

- [x] [`skill.md`](./skill.md) is the canonical `ai-roadmap-coach` v2.2.0 copy.
- [x] Kiro, Cursor, Claude, and Gemini installation paths are documented in
      `00-FRESH-SYSTEM-CONTEXT.md` and carry identical skill content.
- [x] Multi-intent requests have a deterministic verify → score → record order.
- [x] Task-specific rubrics take precedence over whole-sprint scoring.
- [x] Artifact verification and evidence-safe ledger transactions are explicit.
- [x] The daily-plan workflow requires calibration from demonstrated evidence and
      Learn, Guided practice, Independent build, or Evidence labels. This audit
      applies that check to the materially revised July 23 FastAPI and July 26,
      July 28, and July 30 Apple sessions; it does not claim untouched Sprint 1
      sessions have migrated to the newer metadata format.
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
- [x] ~~Final verification is March 29–31, 2027.~~ **Superseded August 26, 2026:**
      final verification is **May 10–12, 2027**. Re-verified below.
- [x] ~~The active target remains March 31, 2027.~~ **Superseded August 26, 2026:**
      the active target is **May 12, 2027** (+6 weeks). Re-verified below.

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
- [x] The materially revised July 23 FastAPI, July 26 Apple, July 28 Apple,
      and July 30 SwiftUI sessions separate end-of-sprint outcomes from current
      evidence with focused sources, per-stage timing, exit evidence, and explicit
      stop/defer boundaries. Untouched Sprint 1 sessions are outside this migration
      claim.
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

## Evidence boundary

- The external Swift artifact at
  `../iOS-Apps/iOSToAIJourney/Sprint-01-AI-Software-Foundations/TaskListFeature.swift`
  had a prior `xcrun swiftc -typecheck TaskListFeature.swift` result of exit 0.
  The final reviewer found its implementation only in the sibling repository's
  unstaged working tree, with an empty staged blob. This is working-tree-only,
  non-durable evidence and proves only the guided state/protocol/fake foundation,
  not a complete SwiftUI feature or Apple milestone.
- This recovery did not rerun that Swift check or mutate the sibling repository.

## July 23 bounded recovery consistency review

- [x] One bounded pass reviewed the target diff against Tasks 1–2 and the
      recovered findings; no broad redesign or untouched-session migration was
      started.
- [x] The revised July 23 FastAPI session now uses the canonical Learn, Guided
      practice, Independent build, and Evidence labels, with per-stage timing
      and exit evidence totaling the original two-hour block.
- [x] Focused roadmap assertions found one official Apple Observation link, one
      official SwiftUI link, one FastAPI additional-response link, five focused-
      source blocks, zero misplaced resource bullets, and all four required
      revised-session headings exactly once.
- [x] Ruff format check reported 26 files formatted; Ruff lint passed; strict
      mypy passed 26 source files; pytest passed 9 tests in 0.17 seconds.
- [x] Canonical `skill.md` and the four documented distribution copies shared
      SHA-256
      `f346a404dc782f45ad8a45a4f7931265e5b965baeeab2afb1d995db80c5347f3`.
- [x] `git diff --check`, `git diff --cached --check`, and
      `git diff HEAD --check` reported no whitespace errors before this record.
- [x] `PROGRESS.md`, this validation file, and the Sprint 1 notes all retain
      working-tree-only and non-durable labels for the sibling Swift evidence.

Remaining unverified boundaries are unchanged: the Swift implementation is not
reproducible from a durable sibling revision; its prior type-check was not rerun;
Postgres persistence, real readiness/lifespan behavior, outage/concurrency depth,
and untouched Sprint 1 sessions remain outside this pass; actual roadmap hours
and IIT attendance remain unreported. The sibling repository was not edited,
staged, committed, or otherwise mutated.

## July 24 evidence verification — recorded July 25, 2026

This pass verified the Friday July 24 SQL and B1 artifacts and recorded the
outcome. It did not re-run the July 23 structural audit above, and it did not
re-verify the sibling Swift artifact.

- [x] All five SQL artifacts were **executed**, not merely read. Server:
      PostgreSQL 16.14 in container `orientation-pg`, database
      `learner_exercise`, driven by
      `docker exec -i orientation-pg psql -U postgres -d learner_exercise -v ON_ERROR_STOP=1 < <file>`.
      Schema applied clean (3 tables, 8 indexes). Rollback proof returned
      `before_count 0 → INSERT 0 1 → row visible in transaction → ROLLBACK →
      0 rows → after_count 0`. The plan script ran both the indexed and
      un-indexed variants.
- [x] `parameterized_query_proof.py` executed successfully in an **ephemeral**
      environment (`uv run --no-project --with "psycopg[binary]"`, `PGPORT=5433`,
      password supplied), inserting, fetching, matching 0 rows against a
      `'; DROP TABLE task; --` payload, leaving `to_regclass('task')` intact, and
      rolling back. `psycopg` is **not** a dependency of
      `AI Solutions Platform/pyproject.toml`, so this script cannot run in the
      project environment as committed; adding it belongs to July 27.
- [x] Four artifact claims were found inaccurate and are recorded as corrections
      rather than silently edited: the index split is 6 automatic + 2 manual, not
      5 + 3; the plan is a forward `Index Scan`, not `Index Scan Backward`, and
      the stated reason is inverted; the printed costs and `rows=2` estimate do
      not match the server; and at 5 rows the un-indexed plan was faster
      (0.025 ms vs 0.051 ms), leaving index value unproven at fixture scale.
- [x] The `sql_evidence_package.md` fixture-hygiene claim was **false** when
      written: `Sprint-00-Orientation-diagnostics/test_insert.sql` still contained
      a real personal email address. It now inserts `learner@example.invalid`,
      and the two anti-pattern rows in the SQL notes no longer name a real
      personal address or a real employer domain. A repository scan for those
      strings returns no remaining hits outside the pre-existing orientation
      notes.
- [x] B1 was scored against the correct rubric — `05-System-Design-Track.md`
      eight dimensions, 0–3, /24 — not the whole-sprint /15 rubric. Reviewer
      **17/24**; the artifact's self-assessed 24/24 is preserved in place and is
      not the recorded outcome, per the track rule that the score is diagnostic
      and must never be inflated. The B1 numeric derivations were independently
      rechecked and are arithmetically correct.
- [x] The hand-drawn diagram at `notes/WhatsApp Image 2026-07-24 at 23.53.37.jpeg`
      was inspected and independently supports the ingest flow and the
      500 → 5,000 → 50,000 RPS scaling analysis. It carries placeholder alt text
      and no caption, which is noted as an evidence-quality gap.
- [x] The missed July 24 weekly review is recorded as missed and folded once into
      the existing July 31 gate-rehearsal block. No third Week-1 replacement
      block was created, no deep block was merged, and the August 2 gate,
      Week-2 sequence, and Saturday July 25 replacements are unchanged.
- [x] `uv run --extra dev pytest -q` returned `9 passed in 0.21s` on July 25,
      matching the July 23 record. This ran in the **existing working tree**, so
      it confirms the suite is unbroken but does **not** satisfy the review's
      clean-checkout reproduction requirement, which remains outstanding.
- [x] The edited orientation fixture was re-executed against a throwaway
      database (orientation `schema.sql` then `test_insert.sql`), inserting
      `learner@example.invalid` / `Learner One` successfully; the scratch
      database was dropped afterwards and the original `diag` database was not
      mutated.
- [x] No hours were inferred. Actual roadmap hours and July 22–23 IIT attendance
      remain unreported in `PROGRESS.md`.
- [x] Evidence was recorded only in `PROGRESS.md` ledger sections, the existing
      per-sprint notes files, the active sprint guide's override, and this file.
      No new per-diagnostic tracking file was created.

Remaining unverified after this pass: the Saturday July 25 safe-async and
ADR/CI blocks (unreported), the clean-checkout reproduction of the in-memory
vertical slice, Postgres persistence and lifespan depth, the sibling Swift
implementation's durability, and the Repeating and Missing Number solve.

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


## August 26 schedule revision

A four-week pause (July 29–August 25, 2026) triggered the
`04-Weekly-Operating-System.md` restart rule. Under roadmap change control this
revision was analyzed, approved by the user, and applied. **Scope, outcomes, exit
gates, prerequisites, the 20–25 hour weekly budget, and portfolio boundaries are
unchanged. Only dates moved, plus one inserted restart gate.**

### Calendar — re-verified by computation, not by reading

Every block was parsed from the master calendar table and checked against real
dates:

- [x] 16 sprints present.
- [x] Every sprint is exactly 14 inclusive days, Monday through Sunday.
- [x] 4 consolidation weeks, each exactly 7 days, Monday through Sunday.
- [x] Consolidation weeks still follow Sprints 4, 8, 12, and 16.
- [x] Blocks are contiguous with no gap or overlap from August 26, 2026 onward.
- [x] Final verification is **May 10–12, 2027** (Monday–Wednesday).
- [x] Orientation is unchanged at July 16–19, 2026.
- [x] The gap between Orientation and the restart gate is **intentional and
      recorded**: Sprint 1's first attempt (Jul 20–Aug 2) plus the unworked pause
      (Aug 3–25). It is a truthful record of elapsed time, not a scheduling error.

### Scope preservation

- [x] The Sprint 1 ten-item exit test is byte-identical to its original.
- [x] Sprint 1's July 20–August 2 sessions are preserved verbatim as history; the
      repair sprint was **appended**, not substituted.
- [x] The two deferrals recorded July 28 — system-design **I1** and the **SwiftUI
      observation/state architecture** — are **restored** into the repair sprint.
      The revision therefore reduced deferred scope; it did not add any.
- [x] Weekly budget unchanged at approximately 24.5–25 hours; IIT separate.
- [x] Networking (December 2026) and selective applications (January 2027) were
      deliberately **not** shifted. The consequence — Sprint 12's beta landing
      February 28 rather than January 17 — is recorded in `PROGRESS.md` →
      *Application readiness* with a decision point at Consolidation 2.
- [x] `04-Weekly-Operating-System.md`, `03-Portfolio-Architecture.md`, and the
      system-design/FDE tracks required no edits; they reference sprints by number
      and phase, not by absolute date.

### Ledger integrity — a defect was found and repaired

- [x] **`PROGRESS.md` was corrupted in commit `53f549a` (July 28).** A compressed
      tool *read* of the file had been written back over the file itself: line 1
      became the literal tool header `PROGRESS.md [332L]`, and **134 lines across
      23 sections** were replaced by 61 `[lean-ctx: omitted N lines]` markers. The
      heaviest losses were the Roadmap status table (16 lines), the July 16
      environment baseline (13), platform milestones (12), and the DSA and FDE
      ledgers (9 each). The corruption was committed and pushed.
- [x] Repaired August 26 by reconstruction, not by hand-editing: the last clean
      revision (`79f9f93`, 332 lines, 0 markers) was taken as the base, and all
      **eight** genuine July 28 additions were re-applied by unique-line anchor —
      the two header lines, the Recovery-override schedule paragraph, the `Jul 27`
      weekly-hours row, the repository/CI and FastAPI/Postgres milestone bullets,
      the DSA recovery-queue solve, and the `Jul 28` recovery row.
- [x] Verified by set difference: exactly the seven intended lines from the clean
      base were replaced and nothing else was dropped. Zero omission markers
      remain. All four July 28 fact probes survived.
- [x] No historical score, evidence row, or attempt was rewritten. All August 26
      changes are additions or explicitly-marked supersessions.

### Truthfulness of the new record

- [x] The four missed weeks are recorded as **missed** with **no inferred hours**.
- [x] Sprint 1's first attempt is recorded as `repair`, not `fail` — its gate was
      never attempted, and `08-Assessment-and-Recovery.md` reserves `fail` for an
      attempted gate.
- [x] The one piece of real work inside the pause — `DSA6.swift`, 0/1 knapsack,
      modified August 22 — is recorded, and explicitly labelled working-tree-only
      until it is committed.
- [x] The July 28 platform-milestone claim was **corrected in place by appended
      note rather than deletion**: `PostgresTaskRepository` is referenced exactly
      once repo-wide (its own definition), `api/app.py` composes only
      `InMemoryTaskRepository`, and the running API persists nothing. Exit-test
      items 1–2 were never achievable from that commit.
- [x] `ruff check src tests` (8 errors), `ruff format --check` (4 files), and
      `mypy src tests` (1 error) were **executed**, not assumed. Every failure is
      in a file introduced by `53f549a`.
- [x] `study-resources/July-29-schedule.md` carries a SUPERSEDED banner. Its only
      working-tree change had been a cosmetic markdown reflow (164 insertions, 3
      real deletions, zero checkboxes ticked); that reflow was reverted so the
      record shows the file as authored.

### Open defects — not repaired by this pass

- [ ] **The Cursor distribution copy of the coach skill does not exist.**
      `00-FRESH-SYSTEM-CONTEXT.md` documents
      `~/.cursor/skills-cursor/ai-roadmap-coach/SKILL.md`, and the *Roadmap coach
      skill* section above asserts that Kiro, Cursor, Claude, and Gemini paths all
      carry identical content. Verified August 26: the canonical `skill.md` and
      the Gemini, Claude, and Kiro copies all share SHA-256
      `f346a404dc782f45ad8a45a4f7931265e5b965baeeab2afb1d995db80c5347f3`, but the
      Cursor path is absent — `~/.cursor/` has no `skills-cursor` directory.
      Either restore the copy or remove the claim; do not leave the assertion
      standing while it is false.
- [ ] `AI Solutions Platform/alembic.ini` is tracked in git with a plaintext
      database password. Acceptable for local development, but it belongs in the
      Sprint 1 security discussion rather than passing unremarked.
- [ ] `notes/sprint-01-...-notes-02-b1-...md` still refers to "the Phase-4 March
      2027 mock." Left unchanged deliberately: it is dated learning evidence, and
      evidence is not retro-edited.

### Filename

`02-Master-Roadmap-Jul2026-Mar2027.md` retains its name although the window now
ends in May 2027. `skill.md` resolves the roadmap root by that literal string, and
three distribution copies must stay byte-identical; renaming would require six
markdown edits plus a synchronized skill release, and any stale copy would break
root resolution silently. The document's own title and header record the true
window. This is a lagging label, not a weakened gate.
