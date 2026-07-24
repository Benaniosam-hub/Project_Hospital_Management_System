from fastapi import HTTPException
from services.patient_services import PatientService
from schemas.patient_schemas import PatientRegisterSchema

patient_service = PatientService()

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