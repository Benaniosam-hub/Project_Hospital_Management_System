from fastapi import HTTPException
from pydantic import BaseModel, EmailStr
from typing import Optional
from services.auth_services import AuthService

auth_service = AuthService()

class StaffRegisterSchema(BaseModel):
    first_name: str
    last_name: str
    username: str
    password: str
    email: EmailStr
    role: str  # e.g., 'admin', 'doctor', 'nurse', etc.
    specialization: Optional[str] = None

class StaffLoginSchema(BaseModel):
    username: str
    password: str

async def register_controller(register_data: StaffRegisterSchema):
    data = register_data.model_dump()
    result, status_code = await auth_service.register_user(data)

    if status_code >= 400:
        raise HTTPException(status_code=status_code, detail=result.get("error","Registration failed"))
    return result

async def login_controller(login_data: StaffLoginSchema):
    result, status_code = await auth_service.login_user(
        login_data.username,
        login_data.password
    )
    if status_code >= 400:
        raise HTTPException(status_code=status_code, detail=result.get("error", "Login failed"))
    
    return result