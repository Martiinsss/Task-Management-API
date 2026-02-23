from fastapi import HTTPException, status as http_status
from sqlalchemy.orm import Session
from .. import models
from ..models import TaskStatus


def create_task(db: Session, title: str, description: str, owner_id: int):
    task = models.Task(
        title=title,
        description=description,
        owner_id=owner_id
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def get_tasks_by_user(db: Session, user_id: int):
    return db.query(models.Task).filter(models.Task.owner_id == user_id).all()

def get_task_by_id(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()

def update_task_status(db: Session, task_id: int, status: TaskStatus, current_user_id: int):
    task = get_task_by_id(db, task_id)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    if task.owner_id != current_user_id:
        raise HTTPException(status_code=403, detail="Not enough permissions")

    task.status = status
    db.commit()
    db.refresh(task)

    return task

def delete_task(db: Session, task_id: int):
    task = get_task_by_id(db, task_id)
    if task:
        db.delete(task)
        db.commit()
    return task