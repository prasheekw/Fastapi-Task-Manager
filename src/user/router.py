from fastapi import APIRouter, status, Depends, Request
from src.utils.db import get_db
from sqlalchemy.orm import Session
from src.user.dtos import UserCreate, UserResponseSchema, LoginSchema
from src.user import controller


user_router = APIRouter(prefix="/user")

@user_router.post("/register", response_model=UserResponseSchema ,status_code=201)
def register(body:UserCreate, db:Session = Depends(get_db)):
    return controller.register(body, db)

@user_router.post("/login", status_code=200)
def login(body:LoginSchema, db: Session = Depends(get_db)):
    return controller.login(body, db)

@user_router.get("/is_auth", status_code=200)
def is_authenticated(request:Request, db:Session = Depends(get_db), response_model=UserResponseSchema):
    return controller.is_authenticated(request, db)