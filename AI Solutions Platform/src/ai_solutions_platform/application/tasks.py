"""Task application use cases and required persistence contract."""

from datetime import UTC, datetime
from typing import Protocol
from uuid import UUID, uuid4

from ai_solutions_platform.domain.tasks import TaskRecord


class TaskRepository(Protocol):
    """Persistence behavior required by the task application service."""

    async def add(self, record: TaskRecord) -> None:
        """Store a task record or raise a domain-specific exception."""
        ...

    async def get_by_id(self, task_id: UUID) -> TaskRecord | None:
        """Return the task with the given ID, or None when it is absent."""
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

    async def read(self, task_id: UUID) -> TaskRecord | None:
        """Return a task by ID, or None when it is absent."""
        return await self._repository.get_by_id(task_id)
