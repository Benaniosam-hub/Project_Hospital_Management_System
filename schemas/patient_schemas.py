from datetime import date
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field, field_validator


class PatientRegisterSchema(BaseModel):
  first_name: str = Field(
      ..., min_length=2, max_length=50, description="First name must be 2-50 chars"
  )
  last_name: str = Field(
      ..., min_length=2, max_length=50, description="Last name must be 2-50 chars"
  )
  gender: str = Field(..., description="Gender must be Male, Female, or Other")
  date_of_birth: date = Field(..., description="Date of birth (YYYY-MM-DD)")
  phone: str = Field(..., description="10-digit phone number")
  blood_group: Optional[str] = Field(
      None, description="e.g., A+, O-, etc."
  )
  patient_type: Optional[str] = Field(
      None, description="e.g., Inpatient or Outpatient"
  )

  @field_validator("gender")
  @classmethod
  def validate_gender(cls, value: str) -> str:
    allowed = ["Male", "Female", "Other"]
    if value.title() not in allowed:
      raise ValueError(f"Gender must be one of {allowed}")
    return value.title()

  model_config = ConfigDict(extra="forbid")