from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from sqlalchemy.sql import crud

from .. import models, schemas
from ..database import SessionLocal
from ..security import *
from ..services.user_service import register_user

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register", response_model=schemas.UserResponse)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return register_user(db, user.email, user.password)

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == form_data.username).first()

    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    if not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    access_token = create_access_token(data={"sub": str(user.id)})

    return {"access_token": access_token, "token_type": "bearer"}