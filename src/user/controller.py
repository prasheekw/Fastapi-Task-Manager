from fastapi import HTTPException, Request
from src.user.models import UserModel
from src.user.dtos import UserCreate, LoginSchema
from sqlalchemy.orm import Session
from pwdlib import PasswordHash
from src.utils.settings import settings
from datetime import timedelta, datetime, timezone
from jwt.exceptions import InvalidTokenError
import jwt

password_hash = PasswordHash.recommended()

def get_password_hash(password):
    return password_hash.hash(password)

def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)

def register(body:UserCreate, db:Session):

    is_username = db.query(UserModel).filter(UserModel.username == body.username).first()
    if is_username:
        raise HTTPException(status_code=404, detail="Username Already Exists")

    is_email = db.query(UserModel).filter(UserModel.email == body.email).first()
    if is_email:
        raise HTTPException(status_code=404, detail="Email Alredy Exists")

    hash_password = get_password_hash(body.password)

    new_user = UserModel(
        name = body.name,
        username = body.username,
        email = body.email,
        hashed_password = hash_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

def login(body:LoginSchema, db:Session):

    is_username = db.query(UserModel).filter(UserModel.username == body.username).first()
    if not is_username:
        raise HTTPException(status_code=401, detail="username is incorrect")

    valid_password = verify_password(body.password, is_username.hashed_password)

    if not valid_password:
        raise HTTPException(status_code=401, detail="password is incorrect")

    exp_time = datetime.now(timezone.utc) + timedelta(settings.EXP_TIME)

    token = jwt.encode({"_id":str(is_username.id), "exp": exp_time.timestamp()},settings.SECRET_KEY, algorithm=settings.ALGORITHM)

    return token

def is_authenticated(request:Request, db:Session):
    try:
        jwt_token = request.headers.get("authorization")
        if not jwt_token:
            raise HTTPException(status_code=401, detail="you are Unauthorized")
        token = jwt_token.split(" ")[-1]

        data = jwt.decode(jwt_token, settings.SECRET_KEY, settings.ALGORITHM)

        user_id = data.get("_id")
        exp_time = data.get("exp")

        current_time = datetime.now().timestamp()

        if exp_time is None:
            raise HTTPException(status_code=401, detail="Token expiration is missing")

        if current_time > exp_time:
            raise HTTPException(status_code=401, detail="you are Unauthorized")

        user = db.query(UserModel).filter(UserModel.id == user_id).first()
        if not user:
            raise HTTPException(status_code=401, detail="you are unauthorized")
    except InvalidTokenError:
        raise HTTPException(status_code=401, detail="You are unauthorized")
    return None