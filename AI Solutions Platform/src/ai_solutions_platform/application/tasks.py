"""Task application use cases and required persistence contract."""

from datetime import UTC, datetime
from typing import Protocol
from uuid import uuid4

from ai_solutions_platform.domain.tasks import TaskRecord


class TaskRepository(Protocol):
    """Persistence behavior required by the task application service."""

    async def add(self, record: TaskRecord) -> None:
        """Store a task record or raise a domain-specific exception."""
        ...


class TaskService:
    """Coordinate task-related application use cases."""

    def __init__(self, repository: TaskRepository) -> None:
        self._repository = repository

    async def create(self, title: str) -> TaskRecord:
        """Create, persist, and return a new task record."""
        record = TaskRecord(
            task_id=uuid4(),
            title=title,
            created_at=datetime.now(UTC),
        )
        await self._repository.add(record)
        return record
