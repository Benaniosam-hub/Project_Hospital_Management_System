# controllers/appointment_controller.py
from fastapi import HTTPException
from pydantic import BaseModel
from typing import Optional
from services.appointment_services import AppointmentService

appointment_service = AppointmentService()

class AppointmentCreateSchema(BaseModel):
    patient_id: int
    doctor_id: int
    appointment_date: str
    reason: Optional[str] = None


async def book_appointment_controller(appointment_date: AppointmentCreateSchema):
    
    data = appointment_date.model_dump()

    result,status_code = await appointment_service.create_appointment(data)

    if status_code >= 400:
        raise HTTPException(status_code=status_code, detail=result.get("error", "failed to book appointment"))
    return result

async def get_doctor_schedule_controller(doctor_id: int):
    
    result, status_code = await appointment_service.list_doctor_schedule(doctor_id)

    if status_code >= 400:
        raise HTTPException(status_code=status_code, detail=result.get("error", "Doctor schedule not found"))
    
    return result