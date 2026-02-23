from sqlalchemy import Column, Integer, String, ForeignKey, Enum as SQLEnum
from sqlalchemy.orm import relationship
from .database import Base
from enum import Enum

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True)
    hashed_password = Column(String(255), nullable=False)

    tasks = relationship("Task", back_populates="owner")

class TaskStatus(str, Enum):
    todo = "todo"
    in_progress = "in_progress"
    completed = "completed"

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(String(500), nullable=True)
    status = Column(SQLEnum(TaskStatus), default=TaskStatus.todo, nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="tasks")