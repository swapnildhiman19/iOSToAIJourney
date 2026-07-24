"""HTTP contract tests for the task API."""

from typing import Any, cast
from uuid import UUID, uuid4

from httpx import ASGITransport, AsyncClient, Response

from ai_solutions_platform.api.app import create_app
from ai_solutions_platform.persistence.in_memory_tasks import InMemoryTaskRepository


def _client(
    repository: InMemoryTaskRepository | None = None,
) -> AsyncClient:
    app = create_app(repository=repository)
    return AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test",
    )


def _json_object(response: Response) -> dict[str, Any]:
    return cast(dict[str, Any], response.json())


async def test_health_and_readiness_contracts() -> None:
    async with _client() as client:
        health_response = await client.get("/health")
        readiness_response = await client.get("/ready")

    assert health_response.status_code == 200
    assert health_response.json() == {"status": "ok"}
    assert readiness_response.status_code == 200
    assert readiness_response.json() == {"status": "ready"}


async def test_create_then_read_uses_the_injected_repository() -> None:
    repository = InMemoryTaskRepository()
    async with _client(repository) as client:
        create_response = await client.post(
            "/tasks",
            json={"title": "Learn FastAPI boundaries"},
        )
        create_body = _json_object(create_response)
        read_response = await client.get("/tasks/" + create_body["task_id"])

    assert create_response.status_code == 201
    assert set(create_body) == {"task_id", "title", "created_at"}
    assert create_body["title"] == "Learn FastAPI boundaries"
    task_id = UUID(create_body["task_id"])
    assert task_id.version == 4
    assert isinstance(create_body["created_at"], str)
    assert read_response.status_code == 200
    assert read_response.json() == create_body

    stored_record = await repository.get_by_id(task_id)
    assert stored_record is not None
    assert stored_record.title == "Learn FastAPI boundaries"


async def test_read_unknown_task_returns_stable_404_contract() -> None:
    async with _client() as client:
        response = await client.get(f"/tasks/{uuid4()}")

    assert response.status_code == 404
    assert response.json() == {
        "code": "task_not_found",
        "message": "Task not found.",
    }


async def test_duplicate_title_returns_stable_409_contract() -> None:
    async with _client() as client:
        first_response = await client.post(
            "/tasks",
            json={"title": "Unique task"},
        )
        duplicate_response = await client.post(
            "/tasks",
            json={"title": "Unique task"},
        )

    assert first_response.status_code == 201
    assert duplicate_response.status_code == 409
    assert duplicate_response.json() == {
        "code": "duplicate_task_title",
        "message": "A task with this title already exists.",
    }


async def test_empty_title_returns_fastapi_validation_contract() -> None:
    async with _client() as client:
        response = await client.post("/tasks", json={"title": ""})

    assert response.status_code == 422
    body = _json_object(response)
    detail = body["detail"]
    assert isinstance(detail, list)
    assert detail[0]["loc"] == ["body", "title"]
    assert detail[0]["type"] == "string_too_short"


async def test_openapi_documents_success_and_error_contracts() -> None:
    async with _client() as client:
        response = await client.get("/openapi.json")

    assert response.status_code == 200
    schema = _json_object(response)
    post_responses = schema["paths"]["/tasks"]["post"]["responses"]
    read_responses = schema["paths"]["/tasks/{task_id}"]["get"]["responses"]

    assert post_responses["201"]["content"]["application/json"]["schema"] == {
        "$ref": "#/components/schemas/TaskResponse"
    }
    assert post_responses["409"]["content"]["application/json"]["schema"] == {
        "$ref": "#/components/schemas/ErrorResponse"
    }
    assert post_responses["422"]["content"]["application/json"]["schema"] == {
        "$ref": "#/components/schemas/HTTPValidationError"
    }
    assert read_responses["200"]["content"]["application/json"]["schema"] == {
        "$ref": "#/components/schemas/TaskResponse"
    }
    assert read_responses["404"]["content"]["application/json"]["schema"] == {
        "$ref": "#/components/schemas/ErrorResponse"
    }
    assert read_responses["422"]["content"]["application/json"]["schema"] == {
        "$ref": "#/components/schemas/HTTPValidationError"
    }


async def test_app_factories_do_not_share_repository_state() -> None:
    async with _client() as first_client, _client() as second_client:
        first_response = await first_client.post(
            "/tasks",
            json={"title": "Same title"},
        )
        second_response = await second_client.post(
            "/tasks",
            json={"title": "Same title"},
        )

    assert first_response.status_code == 201
    assert second_response.status_code == 201
