"""Domain concepts for tasks."""

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass(frozen=True)
class TaskRecord:
    """An immutable record of a task created by the application."""

    task_id: UUID
    title: str
    created_at: datetime


class DuplicateTaskTitle(Exception):
    """Raised when a task title violates the uniqueness invariant."""
