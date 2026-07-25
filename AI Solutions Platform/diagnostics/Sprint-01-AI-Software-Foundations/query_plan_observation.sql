-- ============================================================
-- PostgreSQL Query Plan Observation Script
-- Sprint-01-AI-Software-Foundations Evidence
-- Compares execution plans with and without indexes using EXPLAIN ANALYZE
-- ============================================================

-- Seed test fixture data
INSERT INTO task (task_id, title, status) VALUES
    ('c0000000-0000-0000-0000-000000000001', 'Alpha task', 'pending'),
    ('c0000000-0000-0000-0000-000000000002', 'Beta task', 'active'),
    ('c0000000-0000-0000-0000-000000000003', 'Gamma task', 'failed'),
    ('c0000000-0000-0000-0000-000000000004', 'Delta task', 'pending'),
    ('c0000000-0000-0000-0000-000000000005', 'Epsilon task', 'completed')
ON CONFLICT DO NOTHING;

-- ------------------------------------------------------------
-- Experiment 1: Query Plan WITH Index (idx_task_status_recent)
-- Access Pattern: "Find tasks by status, newest first"
-- ------------------------------------------------------------
EXPLAIN ANALYZE
SELECT task_id, title, created_at
FROM task
WHERE status = 'pending'
ORDER BY created_at DESC;

/*
Expected Output / Plan Observation:
-----------------------------------
Index Scan Backward using idx_task_status_recent on task
  (cost=0.15..8.20 rows=2 width=556)
  Index Cond: ((status)::text = 'pending'::text)

Observation:
1. PostgreSQL utilizes the B-tree index `idx_task_status_recent`.
2. Scans backward because index is (status, created_at DESC) and query specifies ORDER BY created_at DESC.
3. Does not perform a full table scan.
*/

-- ------------------------------------------------------------
-- Experiment 2: Query Plan WITHOUT Index
-- Drop index temporarily to observe baseline behavior
-- ------------------------------------------------------------
DROP INDEX IF EXISTS idx_task_status_recent;

EXPLAIN ANALYZE
SELECT task_id, title, created_at
FROM task
WHERE status = 'pending'
ORDER BY created_at DESC;

/*
Expected Output / Plan Observation:
-----------------------------------
Sort (cost=1.07..1.08 rows=2 width=556)
  Sort Key: created_at DESC
  -> Seq Scan on task (cost=0.00..1.06 rows=2 width=556)
        Filter: ((status)::text = 'pending'::text)
        Rows Removed by Filter: 3

Observation:
1. Without index, PostgreSQL falls back to a Sequential Scan (Seq Scan).
2. It reads all 5 rows and discards 3 non-matching rows.
3. Requires an explicit extra Sort step in memory.
*/

-- ------------------------------------------------------------
-- Restore Index post-experiment
-- ------------------------------------------------------------
CREATE INDEX idx_task_status_recent
    ON task (status, created_at DESC);
