from sqlalchemy import Column, String, Integer
from database import Base

class User(Base):
    __tablename__ = "users"
    email = Column(String(50), unique=True, primary_key=True)
    full_name = Column(String(50))
    age = Column(Integer)
    password = Column(String(50))
