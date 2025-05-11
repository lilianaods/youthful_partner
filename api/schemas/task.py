from typing import Optional

from pydantic import BaseModel, Field

class Task(BaseModel):
    id: int
    title: Optional[str] = Field(None, example="Pick up dry cleaning")
    done: bool = Field(False, description="Whether the task is done or not")