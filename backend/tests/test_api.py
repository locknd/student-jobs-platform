from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# ⁡⁢⁣⁣1. Проверка пустого списка вакансий⁡
def test_get_vacancies_empty():
    response = client.get("/api/v1/vacancies")
    assert response.status_code == 200
    assert response.json() == []

# ⁡⁢⁣⁣2. Создание вакансии⁡
def test_create_vacancy():
    data = {
        "title": "Python-разработчик",
        "description": "Работа с FastAPI",
        "created_by": 1
    }
    response = client.post("/api/v1/vacancies", json=data)
    assert response.status_code == 201
    assert response.json()["title"] == data["title"]
    assert "id" in response.json()

# ⁡⁢⁣⁣3. Получение списка вакансий (теперь не пустой)⁡
def test_get_vacancies_non_empty():
    response = client.get("/api/v1/vacancies")
    assert response.status_code == 200
    assert len(response.json()) >= 1

# ⁡⁢⁣⁣4. Получение существующей вакансии по id⁡
def test_get_vacancy_by_id():
    response = client.get("/api/v1/vacancies/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

# ⁡⁢⁣⁣5. Получение несуществующей вакансии⁡
def test_get_nonexistent_vacancy():
    response = client.get("/api/v1/vacancies/9999")
    assert response.status_code == 404

# ⁡⁢⁣⁣6. Подача заявки на вакансию⁡
def test_apply_to_vacancy():
    data = {
        "user_id": 1,
        "vacancy_id": 1
    }
    response = client.post("/api/v1/applications", json=data)
    assert response.status_code == 201
    assert response.json()["status"] == "pending"

# ⁡⁢⁣⁣7. Ошибка валидации заявки (не хватает vacancy_id)⁡
def test_apply_missing_data():
    data = {
        "user_id": 1
    }
    response = client.post("/api/v1/applications", json=data)
    assert response.status_code == 422