from typing import Optional
from pydantic import BaseModel, EmailStr

from app.models import TaskStatus


class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    status: TaskStatus = TaskStatus.todo

class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: TaskStatus
    owner_id: int

    class Config:
        from_attributes = True