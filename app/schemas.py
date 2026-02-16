from typing import Optional
from pydantic import BaseModel, EmailStr

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
    owner_id: int

class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    owner_id: int

    class Config:
        from_attributes = True