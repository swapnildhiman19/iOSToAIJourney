# Weekly Operating System

The previous plan confused available time with sustainable time. This schedule
keeps the existing daily anchors but limits required roadmap work to 25 hours.
The IIT KGP program is an additional four hours.

## Fixed daily anchors

| Time | Commitment |
|---|---|
| 7:30–8:30 AM | Meditation |
| 10:00 AM–12:00 PM | Walmart work block 1 |
| 12:00–12:30 PM | Lunch |
| 12:30–2:00 PM | Walmart work block 2 |
| 2:00–3:15 PM | Buffer — work overrun, food, rest. **Not roadmap capacity.** |
| 3:15–3:30 PM | Walk and context switch |
| 3:30–5:30 PM | AI core block |
| 5:30–5:45 PM | Break |
| 5:45–7:45 PM | Rotating track block (Mon/Tue/Fri). IIT 6:00–8:00 replaces it Wed/Thu. |
| 7:45–8:45 PM | Optional/review block — required only on Friday |
| 9:30–10:30 PM | Home block — Mon, Tue, Wed, Thu |

> **Revised Friday, August 28, 2026 (approved roadmap change).** The weekday start moved
> **2:15 PM → 3:30 PM**. The 2:15 start was not working in practice; 3:30 is the earliest
> sustainable start, so the plan moves rather than pretending otherwise. Everything shifts
> +1h15m. **Mon/Tue/Fri lose nothing** — they end later instead. The entire cost lands on
> **Wed/Thu**, where the 6:00 PM IIT start is a hard wall that cannot be pushed. Those two
> days gain the 9:30–10:30 PM home block, which Mon/Tue already used. **2:00–3:15 PM is
> now explicitly not study capacity** and must not be reclaimed by a future daily plan.

Sleep, meals, commute, exercise, family, and recovery remain real constraints.
The roadmap does not claim unassigned time as study capacity.

## Learning-stage calibration

Every generated daily plan and every newly authored or materially revised
learning block must be labeled **Learn**, **Guided practice**, **Independent
build**, or **Evidence**. Before assigning work, inspect the latest artifact and
`PROGRESS.md`; do not infer mastery from job seniority, a related technology, or
one diagnostic.

- For a new or weak competency, spend roughly the first third on explanation and
  a worked micro-example, the second third on guided implementation, and the final
  third on a small independent variation plus evidence.
- For a practiced competency, use the normal build-heavy loop below.
- Do not combine an unfamiliar framework, a new architecture pattern, all UI
  states, cancellation, and tests into one block. Preserve the sprint outcome by
  spreading those stages across the already scheduled lane.
- A partial guided artifact is valid evidence of progress; record its exact stage
  and continue from it instead of calling the whole outcome failed.

## Required weekly rotation

### Monday — platform depth

- 3:30–5:30: current AI competency.
- 5:45–7:45: apply it to the AI Solutions Platform.
- 9:30–10:30: DSA repetition.

Required total: 5 hours.

### Tuesday — Apple track

- 3:30–5:30: current AI competency.
- 5:45–7:45: Apple AI Lab or Local AI Workbench.
- 9:30–10:30: DSA repetition.

Required total: 5 hours.

### Wednesday — AI core + IIT

- 3:30–5:30: current AI competency.
- 6:00–8:00: IIT KGP ML program. **Not roadmap hours.**
- 9:30–10:30: DSA.

Roadmap total: 3 hours. IIT: 2 additional hours.

### Thursday — AI core + IIT

- 3:30–5:30: current AI competency.
- 6:00–8:00: IIT KGP ML program. **Not roadmap hours.**
- 9:30–10:30: DSA.

Roadmap total: 3 hours. IIT: 2 additional hours.

### Friday — design and review

- 3:30–5:30: current AI competency or sprint integration.
- 5:45–7:45: one system-design case.
- 7:45–8:45: weekly review, evidence links, and next-week selection.

Required total: 5 hours.

### Weekend

- Saturday: no required study. It is recovery or a replacement block for work
  missed during the week.
- Sunday: 2 hours of Apple deep work. During an Apple-light sprint, this becomes
  platform shipping or FDE simulation.
- Optional weekend work replaces a missed required block; it does not raise the
  weekly target.

Required total: 2 hours.

## Honest weekly totals

The Wednesday/Thursday IIT overlap makes the exact total vary slightly.

- AI core and platform: **12 hours** — unchanged.
- Apple AI: **4 hours** — reduced from 5.5–6.
- DSA: **4 hours** — unchanged.
- System design: 2 hours — unchanged.
- Review/evidence: 1 hour — unchanged.
- Required roadmap total: **approximately 23 hours** (was 24.5–25).
- IIT KGP program: 4 additional hours.

**Where the 1.5 hours went, recorded Aug 28, 2026.** The later start costs about
1.5 hours a week and all of it lands on Wednesday and Thursday, because IIT at
6:00 PM cannot move. That loss was assigned deliberately rather than spread:
**AI core, platform, DSA, design, and review are all held at their previous
hours, and Apple AI absorbs the entire cut.** AI FDE is the primary target and
Apple is the declared backup, so the reduction belongs on the backup track; DSA
is protected because it serves both targets and already carries a backlog.
Thursday is therefore no longer an Apple day — Apple is now Tuesday's block plus
Sunday. **23 hours stays inside the 20–25 band, so no outcome, gate, date, or
prerequisite moves.** Revisit at Consolidation 1 if Apple evidence falls behind.

If IIT homework appears, it replaces an AI theory reading block where topics
overlap. It does not automatically expand the week.

## What each block is for

### AI core block

Use a two-hour loop:

1. 10 minutes — state the competency and exit evidence.
2. 35 minutes — official documentation or first-principles lesson.
3. 60 minutes — code, experiment, or debug.
4. 15 minutes — tests, measurements, and notes.

Watching a video without producing notes, code, or a decision is not a completed
block.

### Platform block

Only:

- vertical-slice implementation;
- tests/evals;
- incident or performance investigation;
- deployment/operations;
- architecture decision backed by evidence.

Do not spend it reorganizing folders, changing themes, or comparing tools
without a decision question.

### Apple block

Use this order:

1. official WWDC session/API documentation;
2. isolated runnable experiment;
3. integration into Apple AI Lab or Local AI Workbench;
4. Swift tests/evaluations;
5. Instruments/benchmark evidence.

A learner who has not demonstrated SwiftUI state architecture may stop the first
Apple block after the state model, protocol, and fake adapter. Observation, the
view, actor integration, cancellation UI, and tests continue in later Apple
blocks; the sprint outcome remains unchanged.

### DSA block

- 20 minutes: recall the pattern from memory.
- 70 minutes: one or two unseen/timed problems.
- 20 minutes: compare alternatives and complexity.
- 10 minutes: schedule repetitions and record the mistake.

### System-design block

- 5 minutes: clarify requirements.
- 5 minutes: estimates and SLOs.
- 10 minutes: API/events and data model.
- 20 minutes: high-level design and critical flows.
- 10 minutes: failure, security, and operations.
- 5 minutes: scale/cost trade-offs.
- 5 minutes: self-critique and evidence update.

The first attempts may use notes. By Phase 4, the same structure must be
delivered without notes in 45 minutes.

## Sprint rhythm

### First Monday

- Read the sprint outcome and exit gate.
- Select no more than three required build slices.
- Create evidence placeholders in `PROGRESS.md`.
- Confirm dependencies and cloud budget.

### First Friday

- Review the first system-design case.
- Run the smallest end-to-end demo.
- Remove scope that does not serve the exit gate.

### Second Monday

- Stop broad reading.
- Focus on integration, tests, evals, failure handling, and measurement.

### Second Friday

- Attempt the exit gate before polishing.
- Record pass/partial/fail and evidence.
- A partial gate becomes the first consolidation task.

### Sunday after the sprint

- Complete Apple milestone evidence.
- Record DSA repetitions.
- Decide what not to carry forward.

## Optional-block policy

Optional blocks are replacement capacity.

Valid uses:

- replace a missed required block;
- finish a test/eval already needed for the exit gate;
- prepare a demo when all core work is complete;
- rest when energy is low.

Invalid uses:

- start the next sprint early;
- add a new framework/provider/database;
- compensate for unrealistic scope;
- exceed 25 roadmap hours repeatedly.

No more than two optional blocks may be used in one normal week. If more are
needed, reduce scope or use consolidation.

## Minimum-viable week

For illness, a Walmart incident, or personal emergency:

- two AI core blocks: 4 hours;
- one Apple block: 2 hours;
- one DSA block: 2 hours;
- one system-design outline: 1 hour;
- one 30-minute review.

Total: 9.5 hours.

Rules:

- Keep the current sprint; do not start a replacement plan.
- Mark work as missed, not completed.
- Defer polish and optional evidence.
- Use the next consolidation week for the oldest failed gate.

## Recovery and no-time-debt rules

- Never borrow from sleep or meditation.
- Never schedule two deep blocks into one future slot to “catch up.”
- A missed block is either replaced once, deferred, or removed.
- Two consecutive weeks above 25 roadmap hours trigger a mandatory scope cut.
- Two consecutive weeks below the minimum-viable plan trigger a roadmap pause
  and a smaller restart gate.
- Consolidation weeks repair competence, not calendar guilt.

## Weekly review template

Answer on Friday:

1. What can I now do without a tutorial?
2. What evidence proves it?
3. Which exit criterion remains unproven?
4. What failed, and what category of failure was it?
5. Did I measure quality, latency, cost, security, or reliability where
   relevant?
6. Which scheduled item created no value and should be removed?
7. What is the single most important result for next week?

Update `PROGRESS.md` during this block. Memory of progress is not evidence.
