from fastapi import APIRouter
from controllers.appointment_controller import book_appointment_controller, get_doctor_schedule_controller,AppointmentCreateSchema

appointment_bp = APIRouter()

@appointment_bp.post('/book', status_code=201)
async def book_appointment(appointment_data: AppointmentCreateSchema):
    return await book_appointment_controller(appointment_data)

@appointment_bp.get('/doctor/{doctor_id}')
async def get_doctor_schedule_controller(doctor_id: int):
    return await get_doctor_schedule_controller(doctor_id)