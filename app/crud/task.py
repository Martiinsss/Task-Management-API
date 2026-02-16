from sqlalchemy.orm import Session
from .. import models

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

def get_tasks(db: Session):
    return db.query(models.Task).all()

def get_task_by_id(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()

def delete_task(db: Session, task_id: int):
    task = get_task_by_id(db, task_id)
    if task:
        db.delete(task)
        db.commit()
    return task