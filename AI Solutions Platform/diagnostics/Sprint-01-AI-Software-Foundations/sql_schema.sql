-- ============================================================
-- SQL Schema Definition: Task & Event Processing Engine
-- Sprint-01-AI-Software-Foundations Evidence
-- ============================================================

-- Clean up existing tables if re-running
DROP TABLE IF EXISTS processing_attempt CASCADE;
DROP TABLE IF EXISTS incoming_event CASCADE;
DROP TABLE IF EXISTS task CASCADE;

-- ------------------------------------------------------------
-- TABLE 1: task
-- Mirrors domain.tasks.TaskRecord with status learning extension
-- ------------------------------------------------------------
CREATE TABLE task (
    task_id     UUID        PRIMARY KEY,
    title       VARCHAR(500) NOT NULL,
    created_at  TIMESTAMPTZ NOT NULL DEFAULT now(),
    status      VARCHAR(20) NOT NULL DEFAULT 'pending'
        CONSTRAINT ck_task_status
            CHECK (status IN ('pending', 'active', 'completed', 'failed', 'cancelled')),
    CONSTRAINT uq_task_title UNIQUE (title)
);

-- ------------------------------------------------------------
-- TABLE 2: incoming_event
-- Captures external provider events with deduplication
-- ------------------------------------------------------------
CREATE TABLE incoming_event (
    event_id          UUID        PRIMARY KEY,
    task_id           UUID        NOT NULL
        REFERENCES task (task_id)
            ON DELETE CASCADE
            ON UPDATE CASCADE,
    provider          VARCHAR(100) NOT NULL,
    provider_event_id VARCHAR(200) NOT NULL,
    payload           JSONB       NOT NULL DEFAULT '{}',
    received_at       TIMESTAMPTZ NOT NULL DEFAULT now(),
    status            VARCHAR(20) NOT NULL DEFAULT 'accepted'
        CONSTRAINT ck_incoming_event_status
            CHECK (status IN ('accepted', 'processing', 'succeeded', 'failed', 'dead_letter')),
    CONSTRAINT uq_incoming_event_provider_dedup
        UNIQUE (provider, provider_event_id)
);

-- ------------------------------------------------------------
-- TABLE 3: processing_attempt
-- Records history of retry attempts for incoming events
-- ------------------------------------------------------------
CREATE TABLE processing_attempt (
    attempt_id      UUID        PRIMARY KEY,
    event_id        UUID        NOT NULL
        REFERENCES incoming_event (event_id)
            ON DELETE CASCADE
            ON UPDATE CASCADE,
    attempt_number  INT         NOT NULL
        CONSTRAINT ck_attempt_number_positive
            CHECK (attempt_number > 0),
    outcome         VARCHAR(20) NOT NULL DEFAULT 'pending'
        CONSTRAINT ck_attempt_outcome
            CHECK (outcome IN ('pending', 'succeeded', 'failed', 'timed_out')),
    error_detail    TEXT,
    started_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    finished_at     TIMESTAMPTZ,
    CONSTRAINT uq_attempt_per_event
        UNIQUE (event_id, attempt_number)
);

-- ------------------------------------------------------------
-- INDEXES
-- Manual indexes for access patterns not covered by PK/UNIQUE
-- ------------------------------------------------------------

-- Access pattern: "Find tasks by status, newest first"
CREATE INDEX idx_task_status_recent
    ON task (status, created_at DESC);

-- Access pattern: "Find all events for a specific task" (FK lookup)
CREATE INDEX idx_incoming_event_task
    ON incoming_event (task_id);
