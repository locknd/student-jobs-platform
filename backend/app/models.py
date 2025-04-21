from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, UTC
from app.database import Base

# ⁡⁢⁣⁣Модель вакансии: содержит заголовок, описание и ID создателя⁡
class Vacancy(Base):
    __tablename__ = "vacancies"

    id = Column(Integer, primary_key=True, index=True)

    # ⁡⁢⁣⁣Название вакансии⁡
    title = Column(String, nullable=False)

    # ⁡⁢⁣⁣Подробности вакансии⁡
    description = Column(Text, nullable=False)

    # ⁡⁢⁣⁣ID пользователя, создавшего вакансию⁡
    created_by = Column(Integer, nullable=False)

    # ⁡⁢⁣⁣Связь с таблицей заявок⁡
    applications = relationship("Application", back_populates="vacancy")

# ⁡⁢⁣⁣Модель заявки: пользователь подаёт заявку на конкретную вакансию⁡
class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)

    # ⁡⁢⁣⁣ID пользователя, подавшего заявку⁡
    user_id = Column(Integer, nullable=False)

    # ⁡⁢⁣⁣Вакансия, на которую подана заявка⁡
    vacancy_id = Column(Integer, ForeignKey("vacancies.id"), nullable=False)

    # ⁡⁢⁣⁣Статус заявки (по умолчанию "pending")⁡
    status = Column(String, default="pending", nullable=False)         

    # ⁡⁢⁣⁣Дата подачи заявки⁡
    applied_at = Column(DateTime, default=lambda: datetime.now(UTC))
    
    # ⁡⁢⁣⁣Связь с моделью вакансии⁡
    vacancy = relationship("Vacancy", back_populates="applications")