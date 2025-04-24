from datetime import datetime, UTC  # ⁡⁢⁣⁣импорт для установки значений по умолчанию⁡
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey 
from sqlalchemy.orm import relationship  # ⁡⁢⁣⁣импорт для задания отношений между моделями⁡
from app.database import Base  # ⁡⁢⁣⁣базовый класс для моделей SQLAlchemy⁡

class Employer(Base):
    __tablename__ = "employers"  # ⁡⁢⁣⁣имя таблицы в БД⁡
    id = Column(Integer, primary_key=True, index=True)  # ⁡⁢⁣⁣первичный ключ-идентификатор работодателя⁡
    name = Column(String, nullable=False)  # ⁡⁢⁣⁣имя или название работодателя⁡

    # ⁡⁢⁣⁣связь: один работодатель может иметь множество вакансий⁡
    vacancies = relationship("Vacancy", back_populates="employer")

class Department(Base):
    __tablename__ = "departments"  # ⁡⁢⁣⁣имя таблицы для подразделений⁡
    id = Column(Integer, primary_key=True, index=True)  # ⁡⁢⁣⁣PK отдела⁡
    name = Column(String, nullable=False)  #⁡⁢⁣⁣ название отдела⁡

    # ⁡⁢⁣⁣связь: один отдел предлагает множество вакансий⁡
    vacancies = relationship("Vacancy", back_populates="department")

class Location(Base):
    __tablename__ = "locations"  # ⁡⁢⁣⁣имя таблицы для локаций⁡
    id = Column(Integer, primary_key=True, index=True)  # ⁡⁢⁣⁣PK локации⁡
    city = Column(String, nullable=False)  # ⁡⁢⁣⁣город⁡
    state = Column(String, nullable=False)  # ⁡⁢⁣⁣область или регион⁡

    # ⁡⁢⁣⁣связь: одна локация содержит множество вакансий⁡
    vacancies = relationship("Vacancy", back_populates="location")

class Vacancy(Base):
    __tablename__ = "vacancies"  # ⁡⁢⁣⁣имя таблицы вакансий⁡
    id = Column(Integer, primary_key=True, index=True)  # ⁡⁢⁣⁣PK вакансии⁡
    title = Column(String, nullable=False)  # ⁡⁢⁣⁣заголовок вакансии⁡
    description = Column(Text, nullable=False)  # ⁡⁢⁣⁣описание вакансии⁡
    created_by = Column(Integer, ForeignKey("students.id"), nullable=False)  # ⁡⁢⁣⁣студент, создавший вакансию⁡
    department_id = Column(Integer, ForeignKey("departments.id"), nullable=True)  # ⁡⁢⁣⁣FK на отдел⁡
    location_id = Column(Integer, ForeignKey("locations.id"), nullable=True)  # ⁡⁢⁣⁣FK на локацию⁡
    employer_id = Column(Integer, ForeignKey("employers.id"), nullable=True)  # ⁡⁢⁣⁣FK на работодателя⁡

    # ⁡⁢⁣⁣связи для получения связанных объектов⁡
    employer = relationship("Employer", back_populates="vacancies")  # ⁡⁢⁣⁣работодатель вакансии⁡
    department = relationship("Department", back_populates="vacancies")  #⁡⁢⁣⁣ отдел вакансии⁡
    location = relationship("Location", back_populates="vacancies")  # ⁡⁢⁣⁣локация вакансии⁡
    applications = relationship("Application", back_populates="vacancy")  # ⁡⁢⁣⁣заявки на эту вакансию⁡

class Student(Base):
    __tablename__ = "students"  # ⁡⁢⁣⁣имя таблицы студентов⁡
    id = Column(Integer, primary_key=True, index=True)  # ⁡⁢⁣⁣PK студента⁡
    name = Column(String, nullable=False)  # ⁡⁢⁣⁣имя студента⁡

    # ⁡⁢⁣⁣связь: студент может иметь резюме⁡
    resume = relationship("Resume", uselist=False, back_populates="student")
    # ⁡⁢⁣⁣связь: студент может подавать множество заявок⁡
    applications = relationship("Application", back_populates="student")
    # ⁡⁢⁣⁣связь: история статусов работы⁡
    job_statuses = relationship("JobStatus", back_populates="student")

class Resume(Base):
    __tablename__ = "resumes"  # ⁡⁢⁣⁣имя таблицы резюме⁡
    id = Column(Integer, primary_key=True, index=True)  # ⁡⁢⁣⁣PK резюме⁡
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)  # ⁡⁢⁣⁣FK на студента⁡

    student = relationship("Student", back_populates="resume")  # ⁡⁢⁣⁣связь с владельцем резюме⁡

class Application(Base):
    __tablename__ = "applications"  # ⁡⁢⁣⁣имя таблицы заявок⁡
    id = Column(Integer, primary_key=True, index=True)  # ⁡⁢⁣⁣PK заявки⁡
    user_id = Column(Integer, ForeignKey("students.id"), nullable=False)  # ⁡⁢⁣⁣студент, подавший заявку⁡
    vacancy_id = Column(Integer, ForeignKey("vacancies.id"), nullable=False)  # ⁡⁢⁣⁣вакансия⁡
    status = Column(String, nullable=False, default="pending")  # ⁡⁢⁣⁣текущий статус заявки⁡
    applied_at = Column(DateTime, default=lambda: datetime.now(UTC))  # ⁡⁢⁣⁣время подачи заявки UTC⁡

    student = relationship("Student", back_populates="applications")  # ⁡⁢⁣⁣связь с автором⁡
    vacancy = relationship("Vacancy", back_populates="applications")  # ⁡⁢⁣⁣связь с вакансией⁡
    statuses = relationship("ApplicationStatus", back_populates="application")  # ⁡⁢⁣⁣история изменений статуса⁡
    skills = relationship("ApplicationSkill", back_populates="application")  #⁡⁢⁣⁣ требуемые навыки⁡

class JobStatus(Base):
    __tablename__ = "job_statuses"  # ⁡⁢⁣⁣имя таблицы для статусов работы студентов⁡
    id = Column(Integer, primary_key=True, index=True)  # ⁡⁢⁣⁣PK записи статуса⁡
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)  # ⁡⁢⁣⁣студент⁡
    status = Column(String, nullable=False)  # ⁡⁢⁣⁣значение статуса⁡
    changed_at = Column(DateTime, default=lambda: datetime.now(UTC))  # ⁡⁢⁣⁣время изменения UTC

    student = relationship("Student", back_populates="job_statuses")  # ⁡⁢⁣⁣связь с студентом⁡

class ApplicationStatus(Base):
    __tablename__ = "application_statuses"  # ⁡⁢⁣⁣имя таблицы истории статуса заявок⁡
    id = Column(Integer, primary_key=True, index=True)  # ⁡⁢⁣⁣PK записи⁡
    application_id = Column(Integer, ForeignKey("applications.id"), nullable=False)  # ⁡⁢⁣⁣заявка⁡
    status = Column(String, nullable=False)  # ⁡⁢⁣⁣значение статуса⁡
    changed_at = Column(DateTime, default=lambda: datetime.now(UTC))  # ⁡⁢⁣⁣время изменения UTC

    application = relationship("Application", back_populates="statuses")  # ⁡⁢⁣⁣связь с заявкой⁡

class Skill(Base):
    __tablename__ = "skills"  # ⁡⁢⁣⁣имя таблицы навыков⁡
    id = Column(Integer, primary_key=True, index=True)  # ⁡⁢⁣⁣PK навы⁡⁢⁣⁣ка⁡
    name = Column(String, nullable=False)  # ⁡⁢⁣⁣название навыка⁡

    applications = relationship("ApplicationSkill", back_populates="skill")  # ⁡⁢⁣⁣заявки, требующие этот навык⁡

class ApplicationSkill(Base):
    __tablename__ = "application_skills"  # ⁡⁢⁣⁣имя связующей таблицы заявок и навыков⁡
    id = Column(Integer, primary_key=True, index=True)  # ⁡⁢⁣⁣PK записи⁡
    application_id = Column(Integer, ForeignKey("applications.id"), nullable=False)  # ⁡⁢⁣⁣заявка⁡
    skill_id = Column(Integer, ForeignKey("skills.id"), nullable=False)  # ⁡⁢⁣⁣навык⁡

    application = relationship("Application", back_populates="skills")  # ⁡⁢⁣⁣связь с заявкой⁡
    skill = relationship("Skill", back_populates="applications")  # ⁡⁢⁣⁣связь с навыком⁡