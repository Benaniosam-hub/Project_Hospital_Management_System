from fastapi import APIRouter
from controllers.auth_controller import register_controller, login_controller, StaffLoginSchema, StaffRegisterSchema

auth_bp = APIRouter()

@auth_bp.post('/register', status_code=201)
async def register(register_data: StaffRegisterSchema):
    return await register_controller(register_data)

@auth_bp.post('/login')
async def login(login_data: StaffLoginSchema):
    return await login_controller(login_data) 
