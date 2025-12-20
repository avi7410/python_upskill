from http.client import HTTPException

from fastapi import APIRouter, status, HTTPException
from database import db_dependency
import schemas
import models

api_router = APIRouter()

@api_router.post('/register', status_code=status.HTTP_201_CREATED)
def register(request: schemas.Register, db: db_dependency):
    user = db.query(models.User).filter(models.User.email == request.email).first()
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail = "User with this email already exists"
        )
    user = models.User(**request.model_dump())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@api_router.get('/login', status_code=status.HTTP_200_OK)
def login(request: schemas.Login, db: db_dependency):
    user = db.query(models.User).filter(models.User.email == request.email).first()
    if (not user) or (user.password != request.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email not registered or Incorrect Password"
        )
    return "Login Successful !!!"


