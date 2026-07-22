"""In-memory persistence adapter for tasks."""

import asyncio

from ai_solutions_platform.domain.tasks import DuplicateTaskTitle, TaskRecord


class InMemoryTaskRepository:
    """Store task records in memory for tests and local exercises."""

    def __init__(self) -> None:
        self._records_by_title: dict[str, TaskRecord] = {}
        self._lock = asyncio.Lock()

    async def add(self, record: TaskRecord) -> None:
        """Store a record unless its title already exists."""
        async with self._lock:
            if record.title in self._records_by_title:
                raise DuplicateTaskTitle(record.title)

            self._records_by_title[record.title] = record
