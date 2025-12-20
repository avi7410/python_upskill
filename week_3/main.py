from fastapi import FastAPI
from api import api_router
import models
from database import engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(api_router, prefix="/api")
