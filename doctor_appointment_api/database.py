from fastapi import Depends
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base
from typing import Annotated
from doctor_appointment_api.config import DB_URL

engine = create_async_engine(DB_URL, echo=True)
local_session = async_sessionmaker(autoflush=False, bind=engine, expire_on_commit=False)
Base = declarative_base()

async def get_db():
    async with local_session() as db:
        yield db

db_dependency = Annotated[AsyncSession, Depends(get_db)]