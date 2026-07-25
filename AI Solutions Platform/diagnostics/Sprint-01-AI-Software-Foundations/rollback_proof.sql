-- ============================================================
-- Transaction Rollback Proof
-- Sprint-01-AI-Software-Foundations Evidence
-- Demonstrates ACID Atomicity by verifying rollback removes uncommitted rows
-- ============================================================

-- Step 1: Record row count before starting
SELECT count(*) AS before_count FROM task;

-- Step 2: Begin explicit transaction
BEGIN;

-- Step 3: Insert test task inside transaction
INSERT INTO task (task_id, title, status)
VALUES (
    'a0000000-0000-0000-0000-000000000001',
    'Transaction Rollback Proof Task',
    'pending'
);

-- Step 4: Verify task IS visible within active transaction connection
SELECT task_id, title, status 
FROM task 
WHERE task_id = 'a0000000-0000-0000-0000-000000000001';

-- Step 5: Roll back the transaction (simulate failure / abort)
ROLLBACK;

-- Step 6: Prove row is completely removed and table state is restored
SELECT task_id, title, status 
FROM task 
WHERE task_id = 'a0000000-0000-0000-0000-000000000001';

SELECT count(*) AS after_count FROM task;
