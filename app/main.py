from fastapi import FastAPI
from .database import engine, Base
from . import models
from .routes import auth, tasks

app = FastAPI()
app.include_router(auth.router)
app.include_router(tasks.router)

Base.metadata.create_all(bind=engine)

@app.get("/")
def hello():
    return {"message": "Hello World"}