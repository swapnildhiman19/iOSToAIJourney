"""PostgreSQL persistence adapter for task records"""

from uuid import UUID

from sqlalchemy import text
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from ai_solutions_platform.domain.tasks import DuplicateTaskTitle, TaskRecord


class PostgresTaskRepository:
    """Store task records in a PostgreSQL database."""

    def __init__(self, session: AsyncSession):
        self._session = session

    async def add(self, record: TaskRecord) -> None:
        """Persist a task record, catching unique constraint variations"""
        query = text(
            """
            INSERT INTO tasks (task_id, title, created_at)
            VALUES (:task_id, :title, :created_at)
            """
        )
        try:
            await self._session.execute(
                query,
                {
                    "task_id": record.task_id,
                    "title": record.title,
                    "created_at": record.created_at,
                },
            )
            await self._session.commit()
        except IntegrityError as exc:
            await self._session.rollback()
            # Translate SQL constraint violation to Domain Exception
            raise DuplicateTaskTitle(record.title) from exc

    async def get_by_id(self, task_id: UUID) -> TaskRecord | None:
        """Retrieve a task record by its UUID."""
        query = text(
            """
            SELECT task_id, title, created_at
            FROM tasks
            WHERE task_id = :task_id
            """
        )
        result = await self._session.execute(query, {"task_id": task_id})
        row = result.mappings().first()
        if row is None:
            return None
        return TaskRecord(
            task_id=row["task_id"],
            title=row["title"],
            created_at=row["created_at"],
        )
