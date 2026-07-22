from fastapi import HTTPException
from schemas.auth_schemas import StaffLoginSchema, StaffRegisterSchema
from services.auth_services import AuthService

auth_service = AuthService()


async def register_controller(register_data: StaffRegisterSchema):
  data = register_data.model_dump()
  result, status_code = await auth_service.register_user(data)

  if status_code >= 400:
    raise HTTPException(
        status_code=status_code,
        detail=result.get("error", "Registration failed"),
    )
  return result


async def login_controller(login_data: StaffLoginSchema):
  # Extract directly from validated Pydantic object
  result, status_code = await auth_service.login_user(
      login_data.username, login_data.password
  )

  if status_code >= 400:
    raise HTTPException(
        status_code=status_code, detail=result.get("error", "Login failed")
    )
  return result