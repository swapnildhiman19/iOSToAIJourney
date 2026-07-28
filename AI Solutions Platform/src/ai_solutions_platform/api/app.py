"""FastAPI application factory and instance definition."""

from fastapi import FastAPI

from ai_solutions_platform.api.routes.health import router as health_router
from ai_solutions_platform.api.routes.tasks import router as tasks_router
from ai_solutions_platform.application.tasks import TaskRepository
from ai_solutions_platform.persistence.in_memory_tasks import InMemoryTaskRepository


def create_app(repository: TaskRepository | None = None) -> FastAPI:
    """Construct an application with repository state owned by that app."""
    app = FastAPI(
        title="AI Solutions Platform API",
        version="0.1.0",
        docs_url="/docs",
        openapi_url="/openapi.json",
    )
    app.state.task_repository = (
        repository if repository is not None else InMemoryTaskRepository()
    )
    app.include_router(tasks_router)
    app.include_router(health_router)
    return app


app = create_app()