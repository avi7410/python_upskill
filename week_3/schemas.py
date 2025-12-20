from pydantic import BaseModel, EmailStr

class Register(BaseModel):
    email: EmailStr
    full_name: str
    age: int
    password: str

    class Config:
        orm_mode = True

class Login(BaseModel):
    email: EmailStr
    password: str

    class Config:
        orm_mode = True