from sqlalchemy.orm import Session
from ..crud import user as user_crud
from ..security import hash_password
from fastapi import HTTPException

def register_user(db: Session, email: str, password: str):
    existing_user = user_crud.get_user_by_email(db, email)

    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    hashed_pw = hash_password(password)

    return user_crud.create_user(db, email, hashed_pw)