from fastapi import HTTPException, status
from src.tasks.dtos import TaskDTO
from sqlalchemy.orm import Session
from src.tasks.models import TaskModel
from src.user.models import UserModel

def create_task(body: TaskDTO, db:Session, user: UserModel):
    data = body.model_dump()
    new_task = TaskModel(
        title = data["title"],
        description = data["description"],
        is_completed = data["is_completed"],
        user_id = user.id
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task


def get_all_tasks(db:Session, user:UserModel):
    tasks = db.query(TaskModel).filter(TaskModel.user_id == user.id).all()
    return {"data": tasks}

def get_one_task(task_id:int, db: Session, user:UserModel):
    
    task:TaskModel = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="task not found")
    if task.user_id != user.id:
        raise HTTPException(status_code=401, detail="you are unauthorize")
    return task


def update_task(task_id: int, db: Session, body: TaskDTO, user:UserModel):
    task = db.get(TaskModel,task_id)

    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="task not found")

    if task.user_id != user.id:
        raise HTTPException(status_code=401, detail="you are not authorized")

    task.title = body.title
    task.description = body.description
    task.is_completed = body.is_completed

    db.commit()
    db.refresh(task)
    return task

def delete_task(task_id: int, db:Session, user:UserModel):
    task = db.get(TaskModel, task_id)

    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="task not found")
    if task.user_id != user.id:
        raise HTTPException(status_code=401, detail="you are unauthorize")
    
    db.delete(task)
    db.commit()

    return None
