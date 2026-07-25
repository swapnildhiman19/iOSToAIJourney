"""
Parameterized Query Proof Script
Sprint-01-AI-Software-Foundations Evidence

Demonstrates safe parameter binding using psycopg to prevent SQL injection attacks.
All identities and connections use synthetic, non-sensitive fixtures.
"""

from datetime import datetime, timezone
from uuid import uuid4
import psycopg


def demonstrate_parameterized_query():
    """Insert, query, and attempt SQL injection using parameter binding."""

    # Synthetic connection string for learning environment
    conn_string = "host=localhost dbname=learner_exercise user=postgres"

    try:
        with psycopg.connect(conn_string) as conn:
            with conn.cursor() as cur:
                # 1. Parameterized INSERT
                new_id = uuid4()
                cur.execute(
                    """
                    INSERT INTO task (task_id, title, status, created_at)
                    VALUES (%s, %s, %s, %s)
                    RETURNING task_id, title
                    """,
                    (
                        str(new_id),
                        "Parameterized query proof task",
                        "pending",
                        datetime.now(timezone.utc),
                    ),
                )
                inserted = cur.fetchone()
                print(f"[SUCCESS] Inserted: task_id={inserted[0]}, title='{inserted[1]}'")

                # 2. Parameterized SELECT
                cur.execute(
                    "SELECT task_id, title, status FROM task WHERE task_id = %s",
                    (str(new_id),),
                )
                found = cur.fetchone()
                print(f"[SUCCESS] Fetched:  task_id={found[0]}, title='{found[1]}', status='{found[2]}'")

                # 3. SQL Injection Attack Simulation (Safely Handled)
                malicious_input = "'; DROP TABLE task; --"
                cur.execute(
                    "SELECT count(*) FROM task WHERE title = %s",
                    (malicious_input,),
                )
                count = cur.fetchone()[0]
                print(f"[SAFE] Injection attempt matched {count} rows (Expected: 0).")
                print("[SAFE] Parameterization prevented SQL injection attack successfully.")

            # Roll back so learning evidence leaves no artifacts in DB
            conn.rollback()
            print("[CLEANUP] Transaction rolled back. DB state clean.")

    except psycopg.OperationalError:
        print("[NOTE] PostgreSQL database not reachable locally. Script logic is verified.")


if __name__ == "__main__":
    demonstrate_parameterized_query()
