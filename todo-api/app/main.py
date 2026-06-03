from fastapi import FastAPI
from app.routers.todo_routers import router

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API is running"}

app.include_router(router)

@app.get("/")
def home():
    return {"message": "Hello FastAPI"}
