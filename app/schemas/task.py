from pydantic import BaseModel, Field


class TaskBase(BaseModel):
    title: str | None = Field(None, example="task 1")


class TaskCreate(TaskBase):
    pass


class TaskCreateResponse(TaskCreate):
    id: int

    class Config:
        orm_mode = True


class Task(TaskBase):
    id: int
    done: bool = Field(False, example="task flag")

    class Config:
        orm_mode = True
