import sqlalchemy.orm as Session
from fastapi import HTTPException
from starlette import status
from ..crud import task as task_crud
from ..crud import user as user_crud
from .. import models

def create_new_task(db: Session, title: str, description: str, owner_id: int):
    user = db.query(models.User).filter(models.User.id == owner_id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    return task_crud.create_task(db, title, description, owner_id)

def list_tasks(db: Session, user_id: int):
    return task_crud.get_tasks_by_user(db, user_id)

def remove_task(db: Session, task_id: int, current_user: models.User):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()

    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")

    if task.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to delete this task"
        )

    db.delete(task)
    db.commit()

    return {"message": "Task deleted successfully"}

    return task
