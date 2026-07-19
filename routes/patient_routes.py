from fastapi import APIRouter
from controllers.patient_controller import register_patient_controller, get_patients_controller

patient_bp = APIRouter()

@patient_bp.post('/register')
async def register_patient():
    return await register_patient_controller()

@patient_bp.get('/')
async def get_patients():
    return await get_patients_controller()