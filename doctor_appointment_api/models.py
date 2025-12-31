from sqlalchemy import Column, Integer, String, Enum, DateTime, ForeignKey
from doctor_appointment_api.database import Base
import enum

class ROLE(enum.Enum):
    DOCTOR = "DOCTOR"
    PATIENT = "PATIENT"

class STATUS(enum.Enum):
    BOOKED = "BOOKED"
    CANCELLED = "CANCELLED"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)
    role = Column(Enum(ROLE), nullable=False)
    name = Column(String(100), nullable=False)

class Availability(Base):
    __tablename__ = "availability"
    id = Column(Integer, primary_key=True)
    doctor_id = Column(Integer, ForeignKey("users.id"))
    start_time = Column(DateTime)
    end_time = Column(DateTime)

class Appointment(Base):
    __tablename__ = "appointments"
    id = Column(Integer, primary_key=True)
    doctor_id = Column(Integer, ForeignKey("users.id"))
    patient_id = Column(Integer, ForeignKey("users.id"))
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    status = Column(Enum(STATUS))