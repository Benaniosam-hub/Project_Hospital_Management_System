from fastapi import APIRouter, Depends
from controllers.patient_controller import register_patient_controller, get_patients_controller
from schemas.patient_schemas import PatientRegisterSchema
from core.dependencies import get_current_user, require_roles

patient_bp = APIRouter(prefix="/patients", tags=["Patients"])


# 1. Require JWT authentication to view patients list
@patient_bp.get('/')
async def get_patients(current_user: dict = Depends(get_current_user)):
    return await get_patients_controller()


# 2. Enforce Role-Based Access Control (RBAC) to register new patients
@patient_bp.post(
    '/register', 
    status_code=201, 
    dependencies=[Depends(require_roles(["admin", "doctor", "receptionist"]))]
)
async def register_patient(
    patient_data: PatientRegisterSchema,
    current_user: dict = Depends(get_current_user)
):
    return await register_patient_controller(patient_data,current_user)