"""Unit tests for the task application service."""

from datetime import UTC
from uuid import UUID

import pytest

from ai_solutions_platform.application.tasks import TaskService
from ai_solutions_platform.domain.tasks import DuplicateTaskTitle
from ai_solutions_platform.persistence.in_memory_tasks import (
    InMemoryTaskRepository,
)


async def test_create_returns_persisted_task_record() -> None:
    repository = InMemoryTaskRepository()
    service = TaskService(repository)
    title = "Prepare architecture"

    record = await service.create(title)

    assert record.title == title
    assert isinstance(record.task_id, UUID)
    assert record.task_id.version == 4
    assert record.created_at.tzinfo is UTC


async def test_create_rejects_duplicate_title() -> None:
    repository = InMemoryTaskRepository()
    service = TaskService(repository)
    title = "Prepare architecture"

    await service.create(title)

    with pytest.raises(DuplicateTaskTitle):
        await service.create(title)
