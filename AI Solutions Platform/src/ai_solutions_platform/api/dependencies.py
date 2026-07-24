"""FastAPI dependency providers for task use cases."""

from typing import Annotated, cast

from fastapi import Depends, Request

from ai_solutions_platform.application.tasks import TaskRepository, TaskService


def get_task_repository(request: Request) -> TaskRepository:
    """Resolve the repository owned by the current FastAPI application."""
    return cast(TaskRepository, request.app.state.task_repository)


def get_task_service(
    repository: Annotated[TaskRepository, Depends(get_task_repository)],
) -> TaskService:
    """Build a task service from the repository selected at composition time."""
    return TaskService(repository=repository)
