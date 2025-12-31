from pydantic import BaseModel, EmailStr
from datetime import datetime
from doctor_appointment_api.models import ROLE

class Register(BaseModel):
    email: EmailStr
    password: str
    role: ROLE
    name: str
    class Config:
        from_attributes = True
        use_enum_values = True

class ForgotPassword(BaseModel):
    email: EmailStr
    class Config:
        from_attributes = True

class UserPublic(BaseModel):
    email: EmailStr
    role: ROLE
    name: str
    class Config:
        from_attributes = True
        use_enum_values = True

class AppointmentCreateDto(BaseModel):
    start_datetime: datetime
    end_datetime: datetime

class AppointmentRequest(BaseModel):
    doctor_id: int
    start_time: datetime