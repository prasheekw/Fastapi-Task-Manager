from fastapi import APIRouter, Depends, HTTPException, status
from src.tasks import controller
from src.tasks.dtos import TaskDTO
from src.utils.db import get_db
from sqlalchemy.orm import Session
from src.utils.helper import is_authenticated
from src.user.models import UserModel

task_router = APIRouter(prefix="/tasks")

@task_router.post("/create",status_code=201)
def create_task(body: TaskDTO, db:Session = Depends(get_db), user:UserModel = Depends(is_authenticated)):
    return controller.create_task(body, db, user)

@task_router.get("/get_tasks", status_code=200)
def get_all_tasks(db = Depends(get_db), user:UserModel = Depends(is_authenticated)):
    return controller.get_all_tasks(db, user)

@task_router.get("/get_one_task/{task_id}", status_code=200)
def get_one_task(task_id: int, db:Session = Depends(get_db), user:UserModel = Depends(is_authenticated)):
    return controller.get_one_task(task_id, db, user)

@task_router.put("/update_task/{task_id}", status_code=200)
def update_task(task_id:int, body: TaskDTO, db:Session = Depends(get_db), user:UserModel = Depends(is_authenticated)):
    return controller.update_task(task_id, db, body, user)

@task_router.delete("/delete_task/{task_id}", status_code=204)
def delete_task(task_id: int, db:Session = Depends(get_db), user:UserModel = Depends(is_authenticated)):
    return controller.delete_task(task_id, db, user)