from fastapi import HTTPException, APIRouter
from fastapi.params import Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import select

from doctor_appointment_api.database import db_dependency
from doctor_appointment_api.models import User
from doctor_appointment_api.auth import create_access_token, Hash
from doctor_appointment_api.schemas import Register, ForgotPassword, UserPublic

auth_api_router = APIRouter()

@auth_api_router.post("/login")
async def login(db:db_dependency, request:OAuth2PasswordRequestForm = Depends()):
    result = await db.execute(select(User).filter(User.email == request.username))
    user = result.scalar_one_or_none()
    if (user is None) or (not Hash.verify(request.password, user.password_hash)) :
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = create_access_token(user)
    return {"access_token" : access_token, "token_type": "bearer"}

@auth_api_router.post("/register")
async def register(db:db_dependency, request: Register):
    result = await db.execute(select(User).filter(User.email == request.email))
    user = result.scalar_one_or_none()
    if user:
        raise HTTPException(status_code=400, detail = "User with this email already exists")
    user = User(
        email=request.email,
        password_hash=Hash.bcrypt(request.password),
        role=request.role,
        name=request.name
    )
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return UserPublic.model_validate(user, from_attributes=True)

@auth_api_router.post("/forgot-password")
async def forgot_password(db:db_dependency, request: ForgotPassword):
    result = await db.execute(select(User).filter(User.email == request.email))
    user = result.scalar_one_or_none()
    if user:
        #async password reset email with token
        pass
    return "If the email exists, a reset link was sent"