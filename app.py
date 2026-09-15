from fastapi import FastAPI
from src.utils.db import Base, engine
from src.tasks.models import TaskModel
from src.user.models import UserModel
from src.tasks.router import task_router
from src.user.router import user_router

Base.metadata.create_all(engine)

app = FastAPI()

app.include_router(task_router)

app.include_router(user_router)
