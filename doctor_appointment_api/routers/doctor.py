from datetime import datetime

from fastapi import HTTPException, Depends
from sqlalchemy import select, String, cast

from doctor_appointment_api.auth import require_role
from doctor_appointment_api.routers.auth import APIRouter
from doctor_appointment_api.database import db_dependency
from doctor_appointment_api.models import User, ROLE, Appointment, Availability, STATUS
from doctor_appointment_api.schemas import AppointmentCreateDto

doctor_api_router = APIRouter()

@doctor_api_router.post("/doctors/availability")
async def set_availability(db:db_dependency, request: AppointmentCreateDto, user = Depends(require_role(ROLE.DOCTOR))):
    if request.start_datetime >= request.end_datetime:
        raise HTTPException(status_code=400,detail="start_time must be before end_time")
    if request.start_datetime < datetime.now():
        raise HTTPException(status_code=400,detail="start_time must be in the future")
    result = await db.execute(select(Availability).filter(
        Availability.doctor_id == user.id,
        Availability.start_time < request.end_datetime,
        Availability.end_time > request.start_datetime
    ))
    availablity = result.scalar_one_or_none()
    if availablity:
        raise HTTPException(status_code=409,detail="Overlap in new availability with existing availability timing")
    slot = Availability(
        doctor_id = user.id,
        start_time = request.start_datetime,
        end_time = request.end_datetime
    )
    db.add(slot)
    await db.commit()
    await db.refresh(slot)
    return {
        "message": "Availability set successfully",
        "availability_id": slot.id,
        "start_time": slot.start_time,
        "end_time": slot.end_time,
    }

@doctor_api_router.get("/appointments")
async def get_appointments(db: db_dependency, user = Depends(require_role(ROLE.DOCTOR))):
    result = await db.execute(select(Appointment).filter(user.id == Appointment.doctor_id, Appointment.status == STATUS.BOOKED))
    return result.scalars().all()