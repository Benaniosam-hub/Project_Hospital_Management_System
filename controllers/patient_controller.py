from fastapi import HTTPException
from pydantic import BaseModel
from typing import Optional
from services.patient_services import PatientService

patient_service = PatientService()

class PatientRegisterSchema(BaseModel):
    first_name: str
    last_name: str
    gender: str
    date_of_birth: str
    phone: str
    blood_group: Optional[str] = None
    patient_type: Optional[str] = None


async def register_patient_controller(patient_data: PatientRegisterSchema):
    data = patient_data.model_dump() 
    result, status_code = await patient_service.register_patient(data)

    if status_code >= 400:
        raise HTTPException(status_code=status_code, detail=result.get("error","Failed to register patient"))
    return result

async def get_patients_controller():
    result, status_code = await patient_service.list_patients()

    if status_code >= 400:
        raise HTTPException(status_code=status_code, detail=result.get("error", "Failed to retrieve patients"))
    return result