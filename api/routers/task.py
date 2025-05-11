from typing import List

from fastapi import APIRouter

import api.schemas.task as task_schema

router = APIRouter()

@router.get("/tasks", response_model=List[task_schema.Task])
async def list_tasks():
    return [
        task_schema.Task(id=1, title="Pick up dry cleaning", done=False),
        task_schema.Task(id=2, title="Go to the gym", done=True),
    ]

@router.post("/tasks")
async def create_task():
    pass

@router.put("/tasks/{task_id}")
async def update_task():
    pass

@router.delete("/tasks/{task_id}")
async def delete_task():
    pass
