from pydantic import BaseModel
from datetime import datetime

class VacancyCreate(BaseModel):
    title: str
    description: str
    created_by: int

class VacancyOut(VacancyCreate):
    id: int
    class Config:
        from_attributes = True

class ApplicationCreate(BaseModel):
    user_id: int
    vacancy_id: int

class ApplicationOut(ApplicationCreate):
    id: int
    status: str
    applied_at: datetime
    class Config:
        from_attributes = True

class ApplicationStatusUpdate(BaseModel):
    status: str

    class Config:
        schema_extra = {
            "example": {"status": "approved"}
        }