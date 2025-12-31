from fastapi import FastAPI
from doctor_appointment_api.database import engine, Base
from doctor_appointment_api.models import User, Appointment, Availability
from doctor_appointment_api.routers.auth import auth_api_router
from doctor_appointment_api.routers.doctor import doctor_api_router
from doctor_appointment_api.routers.patient import patient_api_router

app = FastAPI()

app.include_router(auth_api_router, prefix="/auth")
app.include_router(doctor_api_router)
app.include_router(patient_api_router)

@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        print("Tables created!")