from datetime import datetime, timedelta

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, exists
from sqlalchemy.orm import defer

from doctor_appointment_api.auth import require_role
from doctor_appointment_api.config import SLOT_DURATION
from doctor_appointment_api.database import db_dependency
from doctor_appointment_api.models import ROLE, Availability, User, Appointment, STATUS
from doctor_appointment_api.schemas import AppointmentRequest

patient_api_router = APIRouter()

@patient_api_router.get("/doctors")
async def get_doctors(db:db_dependency, user = Depends(require_role(ROLE.PATIENT))):
    result = await db.execute(select(User).filter(User.role == ROLE.DOCTOR.value))
    doctors = result.scalars().all()
    doctor_list = []
    for d in doctors:
        doctor_list.append({
            "id": d.id,
            "email": d.email,
            "name": d.name,
            "role": d.role.value
        })
    return doctor_list

@patient_api_router.get("/doctors/{doctor_id}/availability")
async def get_availability(db: db_dependency, doctor_id: int, user = Depends(require_role(ROLE.PATIENT))):
    result = await db.execute(select(Availability).filter(
        Availability.doctor_id == doctor_id,
        Availability.start_time > datetime.now()
    ).order_by(Availability.start_time))
    availabilities = result.scalars().all()

    slots = []
    for avail in availabilities:
        slot_start = avail.start_time
        while slot_start + timedelta(minutes=SLOT_DURATION) <= avail.end_time:
            slot_end = slot_start + timedelta(minutes=SLOT_DURATION)

            booked_result = await db.execute(
                select(Appointment).filter(
                    Appointment.doctor_id == doctor_id,
                    Appointment.start_time == slot_start,
                    Appointment.end_time == slot_end,
                    Appointment.status == STATUS.BOOKED
                )
            )

            if booked_result.scalar_one_or_none() is None:
                slots.append({"start_time": slot_start, "end_time": slot_end})

            slot_start = slot_end

    return slots

@patient_api_router.post("/appointment/{doctor_id}/book")
async def book_appointment(db: db_dependency, request: AppointmentRequest, user = Depends(require_role(ROLE.PATIENT))):
    end_time = request.start_time + timedelta(minutes=SLOT_DURATION)

    availability_result = await db.execute(
        select(Availability).filter(
            Availability.doctor_id == request.doctor_id,
            Availability.start_time <= request.start_time,
            Availability.end_time >= end_time
        )
    )

    availability = availability_result.scalar_one_or_none()
    if not availability:
        raise HTTPException(status_code=400, detail="Slot not available")

    if not is_valid_slot(request.start_time, availability.start_time):
        raise HTTPException(status_code=400, detail="Invalid slot start time")

    booked_result = await db.execute(
        select(Appointment).filter(
            Appointment.doctor_id == request.doctor_id,
            Appointment.start_time == request.start_time,
            Appointment.end_time == end_time,
            Appointment.status == STATUS.BOOKED
        )
    )
    if booked_result.scalar_one_or_none():
        raise HTTPException(status_code=400, detail="Slot already booked")

    appointment = Appointment(
        doctor_id=request.doctor_id,
        patient_id=user.id,
        start_time=request.start_time,
        end_time=end_time,
        status=STATUS.BOOKED
    )
    db.add(appointment)
    await db.commit()
    await db.refresh(appointment)
    return appointment

def is_valid_slot(start_time: datetime, availability_start: datetime) -> bool:
    diff = (start_time - availability_start).total_seconds()
    return diff % (SLOT_DURATION * 60) == 0

@patient_api_router.get("/appointments/my")
async def get_appointments(db: db_dependency, user = Depends(require_role(ROLE.PATIENT))):
    result = await db.execute(select(Appointment).filter(user.id == Appointment.patient_id, Appointment.status == STATUS.BOOKED))
    return result.scalars().all()

@patient_api_router.post("/appointment/{appointment_id}/cancel")
async def cancel_appointment(db: db_dependency, appointment_id: int, user = Depends(require_role(ROLE.PATIENT))):
    result = await db.execute(select(Appointment).filter(
        Appointment.id == appointment_id,
        Appointment.patient_id == user.id,
        Appointment.status == STATUS.BOOKED
    ))
    appointment = result.scalar_one_or_none()
    if not appointment:
        raise HTTPException(status_code=400, detail="Appointment not found")

    appointment.status = STATUS.CANCELLED
    await db.commit()
    await db.refresh(appointment)

    return {"detail": "Appointment has been cancelled",
            "appointment": {
                "id": appointment.id,
                "doctor_id": appointment.doctor_id,
                "patient_id": appointment.patient_id,
                "start_time": appointment.start_time,
                "end_time": appointment.end_time,
                "status": appointment.status.value
            }}