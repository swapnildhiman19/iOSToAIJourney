"""FastAPI dependency providers for task use cases."""

from typing import Annotated, cast

from fastapi import Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession

from ai_solutions_platform.application.tasks import TaskRepository, TaskService
from ai_solutions_platform.persistence.database import get_db_session
from ai_solutions_platform.persistence.postgres_tasks import PostgresTaskRepository

DbSession = Annotated[AsyncSession, Depends(get_db_session)]


def get_task_repository(request: Request, session: DbSession) -> TaskRepository:
    """Build a Postgres-backed repository from the per-request session."""
    stored = cast(TaskRepository | None, request.app.state.task_repository)

    if stored is not None:
        return stored  # ← test path: use injected InMemoryRepo

    return PostgresTaskRepository(session)  # ← production path: build with session


def get_task_service(
    repository: Annotated[TaskRepository, Depends(get_task_repository)],
) -> TaskService:
    """Build a task service from the repository selected at composition time."""
    return TaskService(repository=repository)
