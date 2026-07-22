from typing import Optional
from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator


class StaffRegisterSchema(BaseModel):
  first_name: str = Field(
      ..., min_length=2, max_length=50, description="First name (2-50 chars)"
  )
  last_name: str = Field(
      ..., min_length=2, max_length=50, description="Last name (2-50 chars)"
  )
  username: str = Field(
      ..., min_length=3, max_length=30, description="Unique username"
  )
  password: str = Field(
      ..., min_length=6, max_length=100, description="Minimum 6 characters"
  )
  email: EmailStr = Field(..., description="Valid email address")
  role: str = Field(
      ..., description="Role: admin, doctor, nurse, receptionist, etc."
  )
  specialization: Optional[str] = Field(
      None, max_length=100, description="Doctor specialization if applicable"
  )

  @field_validator("role")
  @classmethod
  def validate_role(cls, value: str) -> str:
    allowed = ["admin", "doctor", "nurse", "receptionist", "patient"]
    clean_role = value.lower().strip()
    if clean_role not in allowed:
      raise ValueError(f"Role must be one of {allowed}")
    return clean_role

  model_config = ConfigDict(extra="forbid")


class StaffLoginSchema(BaseModel):
  username: str = Field(..., description="Staff username")
  password: str = Field(..., description="Staff password")

  model_config = ConfigDict(extra="forbid")