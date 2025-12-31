from fastapi import HTTPException
from fastapi.params import Depends
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta
from sqlalchemy import select
from doctor_appointment_api.database import db_dependency
from doctor_appointment_api import models

from doctor_appointment_api.config import ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM, SECRET_KEY

pwd_content = CryptContext(schemes=["bcrypt"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

class Hash:
    @staticmethod
    def bcrypt(password: str):
        return pwd_content.hash(password)

    @staticmethod
    def verify(plain_password, hashed_password):
        return pwd_content.verify(plain_password, hashed_password)


def create_access_token(user: models.User):
    to_encode = {
        "sub": str(user.id),
        "exp": datetime.utcnow()+ timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
    }
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str):
    invalid_credentials_exception = HTTPException(status_code=401, detail = "Invalid Credentials")
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id: str = payload.get("sub")
        if id is None:
            raise invalid_credentials_exception
        return id
    except JWTError:
        raise invalid_credentials_exception

async def get_current_user(db: db_dependency, token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(status_code=401, detail = "Could not validate credentials")
    user_id = verify_token(token)
    result = await db.execute(select(models.User).where(models.User.id == user_id))
    user = result.scalar_one_or_none()
    if user is None:
        raise credentials_exception
    return user

def require_role(required_role: models.ROLE):
    def role_check(user: models.User = Depends(get_current_user)):
        if user.role != required_role:
            raise HTTPException(status_code=403, detail = "You do not have permission to perform this action")
        return user
    return role_check