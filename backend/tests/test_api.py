from fastapi.testclient import TestClient  # ⁡⁢⁣⁣импорт клиента для тестирования FastAPI⁡
from app.main import app
# from app import models # модели для подготовки данных
# from app.database import SessionLocal  

client = TestClient(app)  # ⁡⁢⁣⁣создаём клиент для отправки HTTP-запросов к API⁡

# def setup_function():
#     """
#     Перед каждым тестом очищаем таблицы, 
#     используемые в ключевом сценарии:
#       - Application
#       - Vacancy
#     """
#     db = SessionLocal()
#     db.query(models.Application).delete()
#     db.query(models.Vacancy).delete()
#     db.commit()
#     db.close()


# ⁡⁢⁣⁣1. Проверка пустого списка вакансий — ожидаем [], статус 200⁡

def test_get_vacancies_empty():
    response = client.get("/api/v1/vacancies")
    assert response.status_code == 200  # ⁡⁢⁣⁣проверяем код ответа⁡ы
    assert response.json() == []  # ⁡⁢⁣⁣список вакансий должен быть пустым⁡

# ⁡⁢⁣⁣2. Создание вакансии — передаём title и description, получаем 201 и ID⁡

def test_create_vacancy():
    data = {
        "title": "Python-разработчик",
        "description": "Работа с FastAPI",
        "created_by": 1  # ⁡⁢⁣⁣ключевой параметр сценария⁡
    }
    response = client.post("/api/v1/vacancies", json=data)
    assert response.status_code == 201  # ⁡⁢⁣⁣вакансия успешно создана⁡
    json_data = response.json()
    assert json_data["title"] == data["title"]  # ⁡⁢⁣⁣title совпадает⁡
    assert "id" in json_data  # ⁡⁢⁣⁣проверяем, что есть поле id⁡

# ⁡⁢⁣⁣3. Получение списка вакансий — после создания список не должен быть пустым⁡

def test_get_vacancies_non_empty():
    response = client.get("/api/v1/vacancies")
    assert response.status_code == 200  # ⁡⁢⁣⁣успешно⁡
    assert len(response.json()) >= 1  # ⁡⁢⁣⁣должна быть хотя бы одна вакансия⁡

# ⁡⁢⁣⁣4. Получение существующей вакансии по id=1 — ожидаем данные вакансии⁡

def test_get_vacancy_by_id():
    response = client.get("/api/v1/vacancies/1")
    assert response.status_code == 200  # ⁡⁢⁣⁣вакансия найдена⁡
    assert response.json()["id"] == 1  # ⁡⁢⁣⁣проверяем ID в ответе⁡

# ⁡⁢⁣⁣5. Запрос несуществующей вакансии — должны получить 404⁡

def test_get_nonexistent_vacancy():
    response = client.get("/api/v1/vacancies/9999")
    assert response.status_code == 404  # ⁡⁢⁣⁣вакансия с таким ID не найдена⁡

# ⁡⁢⁣⁣6. Подача заявки на вакансию — ожидаем создание со статусом pending⁡

def test_apply_to_vacancy():
    data = {
        "user_id": 1,  # ⁡⁢⁣⁣студент-аппликант⁡
        "vacancy_id": 1  # ⁡⁢⁣⁣на ранее созданную вакансию⁡
    }
    response = client.post("/api/v1/applications", json=data)
    assert response.status_code == 201  # ⁡⁢⁣⁣заявка создана⁡
    assert response.json()["status"] == "pending"  # ⁡⁢⁣⁣проверяем статус заявки⁡

# ⁡⁢⁣⁣7. Негативный тест: неполные данные для заявки — ожидаем ошибку валидации 422⁡

def test_apply_missing_data():
    data = {
        "user_id": 1  # ⁡⁢⁣⁣не передали vacancy_id⁡
    }
    response = client.post("/api/v1/applications", json=data)
    assert response.status_code == 422  # ⁡⁢⁣⁣ошибка валидации⁡
    errors = response.json()["detail"]
    assert any(err["loc"][-1] == "vacancy_id" for err in errors)  # ⁡⁢⁣⁣проверяем, что ошибка по vacancy_id⁡