from datetime import date, time
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field, field_validator

class AppointmentCreateSchema(BaseModel):
    patient_id: int = Field(..., gt=0, description="Valid patient ID")
    doctor_id: int = Field(..., gt=0,description="Valid doctor/staff ID")
    appointment_date: date = Field(..., description="Date (YYYY-MM-DD)")
    appointment_time: time = Field(..., description="Time (HH:MM:SS or HH:MM)")
    status: Optional[str] = Field("Scheduled", description="Appointment status")
    reason: Optional[str] = Field(
        None, max_length=255, description="Brief reason for visit"
    )

    @field_validator("appointment_date")
    @classmethod
    def validate_future_date(cls, value: date) -> date:
        if value < date.today():
            raise ValueError("Appointment date cannot be in the past")
        return value
    
    model_config = ConfigDict(extra="forbid")

class AppointmentUpdateStatusSchema(BaseModel):
    status: str = Field(..., description="Scheduled, Completed, or Cancelled")

    @field_validator("status")
    @classmethod
    def validate_status(cls, value: str) -> str:
        allowed = ["Scheduled", "Completed", "Cancelled"]
        if value.title() not in allowed:
            raise ValueError(f"Status must be one of {allowed}")
        return value.title()
    
    model_config = ConfigDict(extra="forbid")
    