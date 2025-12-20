from fastapi.params import Depends
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from typing import Annotated

url = "mysql+pymysql://root:ttn@127.0.0.1:3306/python_upskill"

engine = create_engine(url)
local_session = sessionmaker(autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = local_session()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]