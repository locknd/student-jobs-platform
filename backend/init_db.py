# ⁡⁢⁣⁣Этот скрипт предназначен для инициализации базы данных.⁡
# ⁡⁢⁣⁣Он автоматически создаёт все таблицы, определённые в SQLAlchemy-моделях.⁡
# ⁡⁢⁣⁣Это особенно важно при первом запуске проекта, когда БД ещё пустая.⁡

from app.database import engine, SessionLocal, Base
from app.models import Student, Department, Location, Employer
# ⁡⁢⁣⁣Создание всех таблиц на основе моделей⁡
# ⁡⁢⁣⁣SQLAlchemy проверит, какие таблицы уже есть, и создаст только недостающие⁡

def seed_initial_data():
    db = SessionLocal()
    # ⁡⁢⁣⁣Создаём «заглушечные» записи с id=1⁡
    db.merge(Student(id=1, name="Default Student"))
    db.merge(Department(id=1, name="Default Department"))
    db.merge(Location(id=1, city="Default City", state="Default State"))
    db.merge(Employer(id=1, name="Default Employer"))
    db.commit()
    db.close()

if __name__ == "__main__":
    print("Инициализация базы данных: создание таблиц...")
    Base.metadata.create_all(bind=engine)
    print("Таблицы успешно созданы.")
    print("Сидирование начальных данных...")
    seed_initial_data()  # ⁡⁢⁣⁣вызываем заполнение данными⁡
    print("Начальные данные успешно добавлены.")