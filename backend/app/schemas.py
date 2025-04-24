from datetime import datetime
from pydantic import BaseModel, Field

class VacancyCreate(BaseModel):
    """
    Класс-схема для создания вакансии в API.

    В Pydantic BaseModel описывает структуру и валидацию входящих данных.

    Атрибуты (поля схемы):
      - title (str): заголовок вакансии (обязательное поле).
      - description (str): подробное описание вакансии (обязательное поле).
      - created_by (int): идентификатор студента, создающего вакансию (обязательное).
    """
    # ⁡⁢⁣⁣Каждое поле описывается с помощью Field:⁡
    title: str = Field(
        ..., description="Заголовок вакансии"  # ⁡⁢⁣⁣описание для Swagger UI⁡⁢⁣⁣,⁡ ⁡⁢⁣⁡⁢⁣⁣'...' означает обязательное поле⁡
    )
    description: str = Field(
        ..., description="Описание вакансии"
    )
    created_by: int = Field(
        ..., description="ID создателя вакансии (студент)"
    )

class VacancyOut(BaseModel):
    """
    Схема для вывода данных вакансии из API.

    Поля схемы соответствуют возвращаемому JSON:
      - id (int): уникальный идентификатор вакансии.
      - title (str): заголовок вакансии.
      - description (str): описание вакансии.
      - created_by (int): ID автора вакансии.
    """
    id: int = Field(..., description="Уникальный ID вакансии")
    title: str = Field(..., description="Заголовок вакансии")
    description: str = Field(..., description="Описание вакансии")
    created_by: int = Field(..., description="ID автора вакансии")

class ApplicationCreate(BaseModel):
    """
    Схема для создания заявки на вакансию.

    Поля:
      - user_id (int): ID студента, подающего заявку.
      - vacancy_id (int): ID вакансии, на которую подаётся заявка.
    """
    user_id: int = Field(..., description="ID студента")
    vacancy_id: int = Field(..., description="ID вакансии")

class ApplicationOut(BaseModel):
    """
    Схема для вывода данных заявки из API.

    Поля:
      - id (int): уникальный идентификатор заявки.
      - user_id (int): ID студента, подавшего заявку.
      - vacancy_id (int): ID вакансии.
      - status (str): текущий статус (pending/approved/rejected).
      - applied_at (datetime): дата и время подачи заявки.
    """
    id: int = Field(..., description="Уникальный ID заявки")
    user_id: int = Field(..., description="ID студента-заявителя")
    vacancy_id: int = Field(..., description="ID вакансии")
    status: str = Field(..., description="Статус заявки: pending/approved/rejected")
    applied_at: datetime = Field(..., description="Время подачи заявки")

class ApplicationStatusUpdate(BaseModel):
    """
    Схема для обновления статуса заявки работодателем.

    Поле:
      - status (str): новый статус (approved или rejected).
    """
    status: str = Field(
        ..., description="Новый статус заявки: 'approved' или 'rejected'"
    )