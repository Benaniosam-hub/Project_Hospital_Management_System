from fastapi import APIRouter
from controllers.appointment_controller import book_appointment_controller, get_doctor_schedule_controller

appointment_bp = APIRouter()

@appointment_bp.post('/book')
async def book_appointment_controller():
    return await book_appointment_controller()

@appointment_bp.get('/doctor/{doctor_id}')
async def get_doctor_schedule_controller(doctor_id: int):
    return await get_doctor_schedule_controller(doctor_id)