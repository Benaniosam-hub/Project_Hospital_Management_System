from fastapi import APIRouter
from controllers.patient_controller import register_patient_controller, get_patients_controller, PatientRegisterSchema

patient_bp = APIRouter(prefix="/patients", tags=["Patients"])

@patient_bp.post('/register',status_code=201)
async def register_patient(patient_data: PatientRegisterSchema):
    return await register_patient_controller(patient_data)

@patient_bp.get('/')
async def get_patients():
    return await get_patients_controller()