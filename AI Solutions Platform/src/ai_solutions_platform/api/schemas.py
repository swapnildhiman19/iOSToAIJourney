"""Pydantic request and response schemas for the task API."""

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field


class CreateTaskRequest(BaseModel):
    """Payload accepted when creating a task."""

    title: str = Field(min_length=1, description="Unique title of the task")


class TaskResponse(BaseModel):
    """Public HTTP representation of a task."""

    task_id: UUID
    title: str
    created_at: datetime


class ErrorResponse(BaseModel):
    """Stable HTTP representation of an application error."""

    code: str
    message: str
