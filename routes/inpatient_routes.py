from fastapi import APIRouter
from controllers.inpatient_controller import add_room_controller, get_rooms_controller, admit_patient_controller

inpatient_bp = APIRouter()

@inpatient_bp.post('/rooms')
async def add_room():
    return await add_room_controller ()
@inpatient_bp.get('/rooms')
async def get_rooms():
    return await get_rooms_controller()
@inpatient_bp.post('/admit')
async def admit_patient():
    return await admit_patient_controller()
