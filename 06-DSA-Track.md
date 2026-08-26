# DSA Track

Budget: four roadmap hours per week from July 2026 through May 2027
(schedule revised August 26, 2026: +6 weeks).

The goal is not a large solved count. The goal is to recognize patterns, write
correct code under time pressure, explain complexity, test edge cases, and
recover when the first approach is wrong.

## Choose one interview language

Run the orientation diagnostic in both Swift and Python on equivalent problems.

Use Python as the primary language if:

- implementation time is within 20% of Swift;
- standard data structures can be used without repeated syntax lookup; and
- you can explain type/complexity behavior clearly.

Otherwise:

- keep Swift as the primary language through Phase 1;
- solve one short problem per week in Python while backend fluency grows;
- make one language decision during Consolidation 1;
- do not switch languages after that without an actual interview requirement.

Python aligns with AI-FDE work; Swift may initially produce stronger interview
performance. Evidence decides.

## Orientation diagnostic

Complete without preparation:

1. 20 minutes — easy array/hash-map problem.
2. 35 minutes — medium sliding-window or tree problem.
3. 40 minutes — medium graph problem.
4. 15 minutes — explain complexity and test cases for all three.

Record:

- time to recognize the pattern;
- time to a correct implementation;
- hints used;
- syntax failures;
- missed edge cases;
- ability to explain the invariant;
- whether the final solution can be reproduced the next day.

The diagnostic is a baseline, not a pass/fail event.

## Weekly four-hour structure

### Monday home — 1 hour

- Reproduce one due problem without notes.
- Write the invariant and complexity.
- If it fails, stop after 45 minutes and study the gap.

### Tuesday home — 1 hour

- One unseen problem in the current pattern.
- Spend the first five minutes on examples, constraints, and brute force.
- Code only after stating the optimized invariant.

### Wednesday — 1.5 hours

- One timed medium or two related shorter problems.
- Compare alternatives and identify the signal that reveals the pattern.
- On IIT weeks, the last 30 minutes moves to Sunday or begins at 4:00 PM if
  Walmart work allows.

### Weekly repetition/review — 30 minutes

- Schedule repetitions.
- Update the mistake ledger.
- Re-code the smallest failing fragment.
- Review one pattern card from memory.

No session is counted merely because a solution video was watched.

## What “solved” means

A problem is independently solved only when you can:

1. restate the problem and constraints;
2. show a brute-force baseline;
3. identify the pattern and invariant;
4. implement without copying;
5. test normal, boundary, and adversarial cases;
6. state time and space complexity;
7. explain one alternative or variant;
8. reproduce the core solution later.

If editorial code was viewed before a correct implementation, record
“learned,” not “solved.”

## Spaced-repetition policy

### Failed or copied

Repeat after 1, 3, 7, and 21 days.

### Solved with a hint

Repeat after 3, 10, and 30 days.

### Clean independent solve

Repeat after 14 and 45 days, or replace the second repetition with a harder
variant.

Stop repeating when the pattern and invariant are stable. Do not memorize line
order.

## Mistake taxonomy

Tag every failure:

- misunderstood requirement;
- missed constraint;
- wrong pattern;
- correct pattern, wrong invariant;
- data-structure choice;
- off-by-one or boundary;
- mutation/reference error;
- recursion/base case;
- complexity regression;
- syntax/library fluency;
- weak test cases;
- communication or panic;
- time management.

Each Friday, fix the most frequent category, not the most recent emotional
failure.

## Sprint syllabus

### Orientation

- Diagnostic in Swift and Python.
- Establish language and starting pattern.

### Sprint 1

- Arrays, strings, hash maps/sets.
- Frequency maps, prefix/suffix ideas, two pointers.

Exit evidence: two unseen mediums with correct invariants and tests.

### Sprint 2

- Sliding window.
- Monotonic and ordinary stack/queue.
- Binary-search foundations.

Exit evidence: distinguish fixed/variable window and binary search on answer.

### Sprint 3

- Binary search completion.
- Linked lists, fast/slow pointers, reversal, and cycle patterns.

### Sprint 4

- Trees: DFS/BFS, recursion versus iteration, path and subtree patterns.

Phase 1 check: one mixed timed pair without knowing the pattern category.

### Sprint 5

- Binary search trees.
- Tries.
- Heaps/top-k/merge patterns.

### Sprint 6

- Graph representation, BFS/DFS.
- Topological sort, union-find, and shortest-path recognition.

### Sprint 7

- Backtracking.
- Intervals and sweep-line recognition.

### Sprint 8

- One-dimensional dynamic programming.
- Memoization to tabulation and state definition.

Phase 2 check: 75-minute mixed mock with two mediums.

### Sprint 9

- Two-dimensional dynamic programming.
- Grid, subsequence, and knapsack-family recognition.

### Sprint 10

- Greedy proof intuition.
- Bit operations and math patterns relevant to interviews.

### Sprint 11

- Mixed patterns.
- Repair the three highest-frequency mistake tags.

### Sprint 12

- Current company-tagged mediums for target roles.
- Keep at least half the work untagged to avoid memorizing a company list.

Phase 3 check: two 45-minute single-problem mocks in consecutive weeks.

### Sprint 13

- Tagged mediums and one paired mock.
- Focus on verbal clarity and test design.

### Sprint 14

- Timed mixed mediums.
- One mock with interruptions and follow-up constraints.

### Sprint 15

- Two full mock sessions.
- Target only observed weaknesses.

### Sprint 16

- Interview-mode maintenance.
- No new pattern unless a scheduled interview requires it.

Final target: solve a representative medium in 30–35 minutes while narrating,
then handle a follow-up without discarding the whole solution.

## Pattern card template

One screen/page maximum:

- pattern name;
- recognition signals;
- invariant;
- canonical data structure;
- complexity;
- failure traps;
- minimal pseudocode;
- three representative problem links;
- next review date.

Do not create a large theory notebook. The card exists to trigger recall.

## Problem ledger

Record:

- date and link/ID;
- unseen, repeated, or company-tagged;
- pattern;
- language;
- result: independent / hinted / learned / failed;
- recognition and total time;
- complexity;
- mistake tags;
- next repetition;
- one-sentence lesson.

## Mock progression

- Phase 1: open rubric, normal editor, self-review.
- Phase 2: 75-minute paired problems, no pattern label.
- Phase 3: 45-minute interviewer-style medium with follow-ups.
- Phase 4: two mocks per sprint plus real-interview maintenance.

Ask the mock interviewer to evaluate reasoning, communication, code quality,
tests, and recovery—not just the final output.

## Quantity guardrail

A reasonable result is roughly 90–120 well-reviewed unique problems plus
repetitions. This is not a quota. Fewer problems with independent recall beat
300 copied solutions.

Do not use daily streaks as the primary metric. Use:

- clean medium solve rate;
- median time to correct solution;
- repeated mistake frequency;
- mock score;
- ability to reproduce after 2–6 weeks.

## Recovery

If a sprint’s DSA work slips:

1. keep repetitions for failed/copied problems;
2. drop extra new problems;
3. retain one unseen medium;
4. use the consolidation week for the weakest pattern.

Never make up a missed week by solving seven problems on Sunday.
