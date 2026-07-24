"""HTTP route handlers for task operations and system status."""

from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from ai_solutions_platform.api.dependencies import get_task_service
from ai_solutions_platform.api.schemas import (
    CreateTaskRequest,
    ErrorResponse,
    TaskResponse,
)
from ai_solutions_platform.application.tasks import TaskService
from ai_solutions_platform.domain.tasks import DuplicateTaskTitle

router = APIRouter()


@router.get("/health", status_code=status.HTTP_200_OK)
async def health_check() -> dict[str, str]:
    """Report whether the web process is alive."""
    return {"status": "ok"}


@router.get("/ready", status_code=status.HTTP_200_OK)
async def readiness_check() -> dict[str, str]:
    """Report placeholder readiness until external dependencies are added."""
    return {"status": "ready"}


@router.post(
    "/tasks",
    status_code=status.HTTP_201_CREATED,
    response_model=TaskResponse,
    responses={
        409: {
            "model": ErrorResponse,
            "description": "Duplicate task title conflict",
        },
    },
)
async def create_task(
    request: CreateTaskRequest,
    service: Annotated[TaskService, Depends(get_task_service)],
) -> TaskResponse | JSONResponse:
    """Create a task, translating a domain uniqueness error to HTTP 409."""
    try:
        record = await service.create(request.title)
    except DuplicateTaskTitle:
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={
                "code": "duplicate_task_title",
                "message": "A task with this title already exists.",
            },
        )

    return TaskResponse(
        task_id=record.task_id,
        title=record.title,
        created_at=record.created_at,
    )


@router.get(
    "/tasks/{task_id}",
    status_code=status.HTTP_200_OK,
    response_model=TaskResponse,
    responses={
        404: {
            "model": ErrorResponse,
            "description": "Task not found",
        },
    },
)
async def read_task(
    task_id: UUID,
    service: Annotated[TaskService, Depends(get_task_service)],
) -> TaskResponse | JSONResponse:
    """Return a task by ID or a stable HTTP 404 error contract."""
    record = await service.read(task_id)
    if record is None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "code": "task_not_found",
                "message": "Task not found.",
            },
        )

    return TaskResponse(
        task_id=record.task_id,
        title=record.title,
        created_at=record.created_at,
    )
