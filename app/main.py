from fastapi import FastAPI
from .database import engine, Base
from . import models
from .routes import auth

app = FastAPI()
app.include_router(auth.router)

Base.metadata.create_all(bind=engine)

@app.get("/")
def hello():
    return {"message": "Hello World"}