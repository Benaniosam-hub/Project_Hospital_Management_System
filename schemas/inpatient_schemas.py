from datetime import date
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field, field_validator

class RoomAssignSchema(BaseModel):
    patient_id: int = Field(..., gt=0, description="Valid patient ID")
    room_number: str = Field(
        ..., min_length=1, max_length=20, description="Room designation"
    )
    admission_date: date= Field(..., description="Admission date (YYYY-MM-DD)")
    discharge_date: Optional[date] = Field(
        None, description="Discharge date if applicable"
    )

    @field_validator("discharge_date")
    @classmethod
    def validate_discharge(cls, value: Optional[date], info) -> Optional[date]:
        admission = info.date.get("admission_date")
        if value and admission and value < admission:
            raise ValueError("Discharge date cannot be earlier than admission date")
        return value
    
    model_config = ConfigDict(extra="forbid")


class DischargePatientSchema(BaseModel):
    discharge_date: date = Field(
        ..., description="Actual discharge date (YYYY-MM-DD)"
    )

    model_config = ConfigDict(extra="forbid")