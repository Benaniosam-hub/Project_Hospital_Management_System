from fastapi import HTTPException
from pydantic import BaseModel
from services.inpatient_services import InpatientService

inpatient_service = InpatientService()

class RoomCreateSchema(BaseModel):
    room_number: str
    type: str
    total_beds: int
    price_per_day: float

class PatientAdmitSchema(BaseModel):
    patient_id: int
    room_id: int
    reason: str

async def add_room_controller(room_data: RoomCreateSchema):
    data = room_data.model_dump()
    result, status_code = await inpatient_service.add_room(data)
    
    if status_code >= 400:
        raise HTTPException(
            status_code=status_code, 
            detail=result.get("error", "Failed to add room")
        )
    return result

async def get_rooms_controller():
    result, status_code = await inpatient_service.list_rooms()
    
    if status_code >= 400:
        raise HTTPException(
            status_code=status_code, 
            detail=result.get("error", "Failed to retrieve rooms")
        )
    return result

async def admit_patient_controller(admission_data: PatientAdmitSchema):
    data = admission_data.model_dump()
    result, status_code = await inpatient_service.admit_patient(data)
    
    if status_code >= 400:
        raise HTTPException(
            status_code=status_code, 
            detail=result.get("error", "Failed to admit patient")
        )
    return result