from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..models import TaskStatus
from ..security import get_current_user
from .. import models

from ..database import SessionLocal
from ..schemas import TaskCreate, TaskResponse
from ..services.task_service import *

router = APIRouter(prefix="/tasks", tags=["Tasks"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=TaskResponse)
def create_task(
        task: TaskCreate,
        db: Session = Depends(get_db),
        current_user: models.User = Depends(get_current_user)
    ):
    return create_new_task(db, task.title, task.description, current_user.id)

@router.get("/", response_model=list[TaskResponse])
def get_all_tasks(db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    return list_tasks(db, current_user.id)

@router.patch("/tasks/{task_id}/update")
def update_task_status(task_id: int, status: TaskStatus, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    return update_task_status(db, task_id, status, current_user.id)

@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    return remove_task(db, task_id, current_user)