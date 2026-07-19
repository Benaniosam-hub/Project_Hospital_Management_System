from fastapi import APIRouter
from controllers.auth_controller import register_controller, login_controller

auth_bp = APIRouter()

@auth_bp.post('/register')
async def register():
    return await register_controller()

@auth_bp.post('/login')
async def login():
    return await login_controller() 