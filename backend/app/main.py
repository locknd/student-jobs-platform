from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware

# ⁡⁢⁣⁣Создание таблиц при старте
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Student Jobs API",
    version="1.0.0",
    openapi_tags=[
        {"name": "Вакансии", "description": "Операции с вакансиями"},
        {"name": "Заявки", "description": "Операции с заявками"},
    ]
)

# ⁡⁢⁣⁣Добавление CORS middleware для доступа с frontend (React)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Разрешаем запросы с локального фронта
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ⁡⁢⁣⁣Подключение к БД
# ⁡⁢⁣⁣Функция-генератор создаёт сессию на время запроса и закрывает её после

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ⁡⁢⁣⁣---------- ВАКАНСИИ ----------

@app.get("/api/v1/vacancies", response_model=list[schemas.VacancyOut], tags=["Вакансии"])
def read_vacancies(db: Session = Depends(get_db)):
    return db.query(models.Vacancy).all()

@app.get("/api/v1/vacancies/{vacancy_id}", response_model=schemas.VacancyOut, tags=["Вакансии"])
def read_vacancy(vacancy_id: int, db: Session = Depends(get_db)):
    vacancy = db.get(models.Vacancy, vacancy_id)  # современный способ вместо query.get()
    if not vacancy:
        raise HTTPException(status_code=404, detail="Вакансия не найдена")
    return vacancy

@app.post("/api/v1/vacancies", response_model=schemas.VacancyOut, status_code=201, tags=["Вакансии"])
def create_vacancy(vacancy: schemas.VacancyCreate, db: Session = Depends(get_db)):
    new_vacancy = models.Vacancy(**vacancy.model_dump())  # Pydantic 2.0+ метод вместо .dict()
    db.add(new_vacancy)
    db.commit()
    db.refresh(new_vacancy)
    return new_vacancy

# ⁡⁢⁣⁣---------- ЗАЯВКИ ----------

@app.post("/api/v1/applications", response_model=schemas.ApplicationOut, status_code=201, tags=["Заявки"])
def apply(application: schemas.ApplicationCreate, db: Session = Depends(get_db)):
    new_app = models.Application(**application.model_dump())
    db.add(new_app)
    db.commit()
    db.refresh(new_app)
    return new_app

@app.get("/api/v1/applications", response_model=list[schemas.ApplicationOut], tags=["Заявки"])
def read_applications(db: Session = Depends(get_db)):
    return db.query(models.Application).all()
