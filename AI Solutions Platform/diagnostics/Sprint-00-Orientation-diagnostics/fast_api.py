from fastapi import FastAPI
from pydantic import BaseModel
from dataclasses import dataclass

app = FastAPI()

@app.get("/health")
def health():
    return {
        "status": "200"
    }

class CreateTaskRequest(BaseModel):
    title: str

class ResponseValidation(BaseModel):
    id: int
    title: str
    status: str

@app.post(
    "/task",
    response_model=ResponseValidation,
)
def handle_post_task(request: CreateTaskRequest):
    return {
        "id": 1234,
        "title": request.title,
        "status": "Created successfully",
        "somerandomString": 123,
    }

tasksLists = []

class TaskService:
    def create(self, request: CreateTaskRequest):
        tasksLists.append(request.title)
        return tasksLists

service = TaskService()

@app.post("/tasks")
def handle_post_tasks(request: CreateTaskRequest):
    return service.create(request)



from fastapi import HTTPException

@dataclass
class TService:
    def create(self, title:str):
        if title == "Study AI":
            raise DuplicateTask()
        
        return {
            "id": 1,
            "title": title,
            "status": "Created Successfully"
        }
new_service = TService()

class DuplicateTask(Exception):
    pass

@app.post(
    "/v2/tasks",
    response_model=ResponseValidation
    )
def handle_v2_post_tasks(request:CreateTaskRequest):
    try :
       return new_service.create(request.title)
    except DuplicateTask:
        raise HTTPException(
            status_code=409,
            detail="This task is already existing"
        )


from fastapi.testclient import TestClient

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {
        "status":"200"
    }

def test_create_task():

    response = client.post(
        "/v2/tasks",
        json={
            "title": "Study AI"
        },
    )

    assert response.status_code == 409