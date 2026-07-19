from fastapi import APIRouter
from controllers.inpatient_controller import (
    add_room_controller, 
    get_rooms_controller, 
    admit_patient_controller,
    RoomCreateSchema,
    PatientAdmitSchema
)

inpatient_bp = APIRouter()

@inpatient_bp.post('/rooms', status_code=201)
async def add_room(room_data: RoomCreateSchema):
    return await add_room_controller(room_data)

@inpatient_bp.get('/rooms')
async def get_rooms():
    return await get_rooms_controller()

@inpatient_bp.post('/admit', status_code=201)
async def admit_patient(admission_data: PatientAdmitSchema):
    return await admit_patient_controller(admission_data)