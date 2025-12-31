## Doctor Appointment API


## Setup

1) Database
- Ensure MySQL is running and a database exists (`doctor_appointment_db`).
- Set your DB credentials in `doctor_appointment_api/config.py` (`DB_URL`).

2) Install dependencies (from one level above the `doctor_appointment_api` folder)

# go to the project root (one directory above the package folder)
cd /path/to/project/root

pip install --upgrade pip
pip install fastapi uvicorn sqlalchemy passlib python-jose aiomysql pydantic


3) Run the API (from the same directory — one level above the package)

uvicorn doctor_appointment_api.main:app --reload


- Swagger UI: http://127.0.0.1:8000/docs
- OpenAPI JSON: http://127.0.0.1:8000/openapi.json

On first run, tables are created automatically.

---

## Authentication & RBAC
- Register with: email, password, role (`DOCTOR` or `PATIENT`), name.
- Login at `POST /auth/login` to get `{ access_token, token_type }`.
- Use `Authorization: Bearer <token>` on protected endpoints.
- RBAC: routes enforce the required role (Doctor-only or Patient-only).

---

## Endpoints

Auth (open)
- POST `/auth/register` — Create a user.
- POST `/auth/login` — Login, returns JWT.
- POST `/auth/forgot-password` — Mock reset.

Doctor (requires DOCTOR)
- POST `/doctors/availability` — Set a working availability window.
- GET `/appointments` — List your booked appointments.

Patient (requires PATIENT)
- GET `/doctors` — List all doctors.
- GET `/doctors/{doctor_id}/availability` — View 30-min availability slots.
- POST `/appointment/{doctor_id}/book` — Book a slot.
- GET `/appointments/my` — List your booked appointments.
- POST `/appointment/{appointment_id}/cancel` — Cancel your appointment.

---

## Example Flow
1) Register a doctor and a patient via `/auth/register`.
2) Doctor logs in, sets availability via `POST /doctors/availability`.
3) Patient logs in, lists doctors, then checks `/doctors/{id}/availability`.
4) Patient books a slot with `POST /appointment/{doctor_id}/book`.
5) Doctor checks `GET /appointments` to see bookings.
6) Patient checks `GET /appointments/my` or cancels with `POST /appointment/{appointment_id}/cancel`.



