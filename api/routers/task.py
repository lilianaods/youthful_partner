from typing import List

from fastapi import APIRouter, Depends

import api.schemas.task as task_schema

import api.cruds.task as task_crud
from api.db import get_db

from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()

@router.get("/tasks", response_model=List[task_schema.Task])
async def list_tasks():
    return [
        task_schema.Task(id=1, title="Pick up dry cleaning", done=False),
        task_schema.Task(id=2, title="Go to the gym", done=True),
    ]

@router.post("/tasks", response_model=task_schema.TaskCreateResponse)
async def create_task(task_body: task_schema.TaskCreate, db: AsyncSession = Depends(get_db)):
    return await task_crud.create_task(db, task_body)

@router.put("/tasks/{task_id}")
async def update_task(task_id: int, task_body: task_schema.TaskCreate):
    return task_schema.TaskCreateResponse(id=task_id, **task_body.dict())

@router.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    return
