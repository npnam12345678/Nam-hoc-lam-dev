# app/routers/todo_routers.py

from fastapi import APIRouter

router = APIRouter()

@router.get("/todos")
def get_todos():
    return [
        {"id": 1, "title": "Learn Python"},
        {"id": 2, "title": "Learn FastAPI"}
    ]