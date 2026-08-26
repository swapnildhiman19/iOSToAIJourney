# DSA Track

Budget: four roadmap hours per week from July 2026 through May 2027
(schedule revised August 26, 2026: +6 weeks).

The goal is not a large solved count. The goal is to recognize patterns, write
correct code under time pressure, explain complexity, test edge cases, and
recover when the first approach is wrong.

## Problem sources

Recorded August 26, 2026. Before this date the track named **no** problem source,
and problem selection was ad hoc every week. That gap produced a recorded defect:
the July 21 submission was tagged *pattern-selection mismatch* because the session
chose an interesting problem instead of the assigned pattern. Each weekly slot now
has exactly one authoritative source.

| Source | Role | Used in |
|---|---|---|
| [Striver SDE Sheet](https://takeuforward.org/dsa/strivers-sde-sheet-top-coding-interview-problems) | **The pattern spine.** Authoritative for what is done and what is due; it has its own Revision tab. | Phases A and B |
| [Taro Top 75](https://www.jointaro.com/interviews/taro-75/) | Timed and unseen practice, **minus** anything already in Striver. | Phase C |
| [Taro — Google](https://www.jointaro.com/interviews/companies/google/) | Company-tagged practice. | Phase C, weighted late |

Company-tagged work stays weighted to Phases C and D so that at least half of all
practice remains untagged. Memorising a company list is not preparation.

### Overlap rule

The three lists overlap heavily — roughly **79%** of the Taro Top 75 index is already
in Striver (Two Sum, Merge Intervals, Trapping Rain Water, 3Sum, Kadane's, Number of
Islands, Rotting Oranges, Valid Parentheses, LRU Cache, Median of Two Sorted Arrays,
Search in Rotated Sorted Array, Generate Parentheses, House Robber, and more).

**A problem is counted and revised once**, against Striver wherever it appears there.
The Taro lists contribute only their genuinely new problems. Treating the three lists
as additive triple-counts the work and inflates the schedule by roughly 30 hours.

### Baseline — Striver SDE Sheet, read August 26, 2026

**172 / 191 complete.** Easy 25/25, Medium 85/93, Hard 62/73.

Every topic is at 100% except three:

| Topic | State |
|---|---|
| Dynamic Programming | **3 / 7** |
| Dynamic Programming Part-II | **0 / 8** |
| Trie | **0 / 7** |

All 19 unsolved problems sit in two patterns. This is the first recorded evidence of
an actual DSA baseline, and it is corroborated by every recent self-selected session
being DP: July 21 (LIS), July 28 (LIS + LCS), August 22 (0/1 knapsack).

**A ticked checkbox is not a solve.** The sheet records that a problem was once
completed, not that it can be reproduced today. Phase B exists for exactly that
reason. See *What "solved" means* below, which is the standard that governs.

### Where records live

Three places, with no duplication between them:

- **Striver site** — authoritative for which problems are done and which are due for
  revision. Use its Revision tab; do not rebuild that state elsewhere.
- **Notion** — the per-problem notebook. Already close to the *pattern card* spec
  below: each entry carries a recognition signal and a full Swift solution.
  - [DSA](https://app.notion.com/p/vibedin/DSA-2c39b3ea0f2983edb48b81b3b2062918)
  - [Taro — Google interview questions](https://app.notion.com/p/vibedin/Taro-LeetCode-Google-Interview-Questions-2669b3ea0f2980a69bdac1ca6df2f4b3)
  - [Taro — Top 75](https://app.notion.com/p/vibedin/Taro-Top-75-LeetCode-Question-2669b3ea0f29804ca16ff9725ad087ad)
- **`PROGRESS.md` → DSA ledger summary** — aggregate only: counts by source, weakest
  patterns, mistake-tag frequency, next repetitions, and mock scores.

**Never duplicate per-problem detail into `PROGRESS.md`.** Two ledgers drift, and the
one that drifts is the one nobody trusts.

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
- **Source:** the spaced-repetition queue — whatever is due, from any list.

### Tuesday home — 1 hour

- One unseen problem in the current pattern.
- Spend the first five minutes on examples, constraints, and brute force.
- Code only after stating the optimized invariant.
- **Source:** the current phase — Striver in Phases A and B, Taro in Phase C.
  Do not substitute a more interesting problem; that is the exact mistake tagged
  on July 21.

### Wednesday — 1.5 hours

- One timed medium or two related shorter problems.
- Compare alternatives and identify the signal that reveals the pattern.
- **Source:** Striver in Phases A and B; Taro Top 75 and the Taro Google list in
  Phase C.
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

Revised August 26, 2026 from the Striver baseline above. The original syllabus
sequenced patterns Sprint 1 to 16 as if starting from zero. That would have spent
September through November re-covering arrays, trees, and graphs — all already at
100% — while leaving Trie until November 2 and dynamic programming until December 14,
the only two patterns actually missing.

The work now runs in four phases. **No pattern was dropped**; see the coverage map.

### Phase A — complete the sheet

**Sprint 1 (repair) and Sprint 2, August 31 – September 27, approximately 16 hours**

Finish the 19 unsolved Striver problems and take the sheet to 191/191:

- Dynamic Programming, the remaining 4 of 7.
- Dynamic Programming Part-II, all 8.
- Trie, all 7.

This is genuinely new material, not revision, so it is paced at roughly 50 minutes per
problem. Memoisation to tabulation, state definition, grid/subsequence/knapsack
recognition, and prefix-tree construction and search all belong here.

Exit evidence: Striver reports 191/191, and two of the DP problems are re-solved from
memory a week later without notes.

### Phase B — revise everything

**Sprints 3 to 8, September 28 – December 27, approximately 48 hours**

All 191 problems, in Striver's own topic order. Depth varies by recall, which is what
makes 191 problems fit inside 48 hours:

1. Read the problem statement.
2. Give yourself **60 seconds** to state the pattern and the invariant aloud.
3. Instant and correct — tick it and move on.
4. Blank, vague, or wrong — re-solve it fully and tag the mistake.

Nothing is skipped; only the time per problem varies. A problem you genuinely know does
not cost the same as one you have lost, and pretending otherwise is how a revision plan
quietly becomes unfinishable.

| Sprint | Dates | Striver topics | Problems |
|---|---|---|---:|
| Sprint 3 | Sep 28 – Oct 11 | Arrays I–IV, String I–II | 36 |
| Sprint 4 | Oct 12 – 25 | Linked List I–II, LL and Arrays, Stack and Queue I–II | 35 |
| Sprint 5 | Nov 2 – 15 | Binary Search, Heaps, Greedy, Recursion | 26 |
| Sprint 6 | Nov 16 – 29 | Binary Tree I–III, Binary Trees [Misc] | 33 |
| Sprint 7 | Nov 30 – Dec 13 | BST I–II, Recursion and Backtracking, Graph I–II | 39 |
| Sprint 8 | Dec 14 – 27 | Dynamic Programming I–II, Trie | 22 |
| | | **Total** | **191** |

Sprint 8 revisits the Phase A material after roughly three months — the longest and
most informative repetition interval in the schedule. Treat a failure there as signal,
not as wasted work.

Phase 1 check, during Sprint 4: one mixed timed pair without knowing the pattern
category.

Phase 2 check, during Sprint 8: 75-minute mixed mock with two mediums.

### Phase C — interview practice

**Sprints 9 to 14, January 4 – April 4, approximately 35 hours**

Only now do the Taro lists open, and only for their genuinely new problems:

- Taro Top 75 — the roughly 30 not already covered by Striver.
- Taro Google list — company-tagged mediums for the target roles.
- Timed mixed mediums; mocks with follow-ups and interruptions.
- Repair the three highest-frequency mistake tags from Phase B.

Keep at least half the work untagged. A company list is a sample of what was asked
once, not a syllabus.

Phase 3 check, Sprints 12 to 13: two 45-minute single-problem mocks in consecutive
weeks.

### Phase D — maintenance

**Sprints 15 to 16, April 5 – May 2, approximately 12 hours**

- Two full mock sessions per sprint, targeting only observed weaknesses.
- No new pattern unless a scheduled interview requires it.

Final target, unchanged: solve a representative medium in 30–35 minutes while
narrating, then handle a follow-up without discarding the whole solution.

### Coverage map

Every pattern in the original syllabus still has a home:

| Pattern | Now covered in |
|---|---|
| Arrays, strings, hash maps, prefix/suffix, two pointers | Phase B, Sprint 3 |
| Sliding window | Phase B, Sprint 3 (Striver Arrays and String) |
| Stack, queue, monotonic stack | Phase B, Sprint 4 |
| Linked lists, fast/slow pointers, reversal, cycles | Phase B, Sprint 4 |
| Binary search, including binary search on answer | Phase B, Sprint 5 |
| Heaps, top-k, merge patterns | Phase B, Sprint 5 |
| Greedy | Phase B, Sprint 5 |
| Recursion | Phase B, Sprint 5 |
| Trees, DFS/BFS, path and subtree patterns | Phase B, Sprint 6 |
| Binary search trees | Phase B, Sprint 7 |
| Backtracking | Phase B, Sprint 7 |
| Graphs, topological sort, union-find, shortest path | Phase B, Sprint 7 |
| **Trie** | **Phase A** (new), revised in Phase B Sprint 8 |
| **1-D and 2-D dynamic programming** | **Phase A** (new), revised in Phase B Sprint 8 |
| Intervals and sweep-line | Phase B Sprint 3 (Merge Intervals), extended in Phase C |
| Bit operations and interview maths | **Phase C.** Striver has no dedicated section for these, so they must be picked deliberately from the Taro lists rather than assumed covered. |
| Company-tagged mediums | Phase C |
| Mocks | Phases B, C, and D |

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

This record lives in **Notion**, one entry per problem — not in `PROGRESS.md`.

The existing Notion pages already carry the hardest parts: a recognition signal per
problem (for example, *"Subarray Sum Equals k: prefix-sum hashmap, check whether
prefixSum[i] − target was seen before"*) and a full Swift solution. Four fields are
missing and should be added going forward:

1. date, and whether the attempt was unseen, repeated, or company-tagged;
2. result — independent / hinted / learned / failed;
3. recognition time and total time;
4. mistake tag and next repetition date.

`PROGRESS.md` carries only the aggregate: counts by source, weakest patterns,
mistake-tag frequency, next repetitions, and mock scores.

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

**Accepted deviation, recorded August 26, 2026.** The three chosen sources come to
roughly **260 unique problems** — more than double the guardrail above. This was
decided deliberately, not by oversight, and it is defensible for three reasons:

1. Striver's 172 are **revision**, not first exposure. The guardrail is about how
   many problems can be learned well, and re-recognising a solved problem is a
   different and much cheaper operation.
2. The 60-second recall test in Phase B enforces the guardrail's actual intent —
   independent recall — rather than its headline number.
3. Only about 50 problems across the three lists are genuinely new: the 19 Striver
   gaps plus roughly 30 unique Taro problems. That figure sits **inside** the
   90–120 range.

If Phase B shows recall failing on more than roughly a third of the 172, this
deviation stops being defensible: the sheet is then first exposure rather than
revision, and scope must be cut back toward the guardrail. Re-check at
Consolidation 2 (December 28 – January 3).

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
