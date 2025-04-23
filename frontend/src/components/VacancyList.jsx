import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';

// ⁡⁢⁣⁣Компонент для отображения списка ваканс⁡⁢⁣⁣ий⁡
function VacancyList() {
  // ⁡⁢⁣⁣Состояние для хранения массива вакансий⁡
  const [vacancies, setVacancies] = useState([]);

  // ⁡⁢⁣⁣Хук эффект: загрузка вакансий при монтировании компонента⁡
  useEffect(() => {
    fetch('/api/v1/vacancies')  // ⁡⁢⁣⁣Запрос к API бэкенда⁡
      .then(res => res.json())                       // ⁡⁢⁣⁣Парсинг JSON⁡
      .then(data => setVacancies(data));             // ⁡⁢⁣⁣Сохранение данных в состояние⁡
  }, []);

  return (
    // ⁡⁢⁣⁣Bootstrap контейнер для адаптивного центра контента⁡
    <div className="container my-4">
      {/* ⁡⁢⁣⁣Заголовок страницы⁡ */}
      <h2 className="mb-4">Доступные вакансии</h2>
      {/* ⁡⁢⁣⁣Bootstrap сетка: row для строки карточек⁡ */}
      <div className="row">
        {vacancies.map(vacancy => (
          // ⁡⁢⁣⁣Колонка: на md — 6, на lg — 4 ширина⁡
          <div key={vacancy.id} className="col-12 col-md-6 col-lg-4 mb-3">
            {/* ⁡⁢⁣⁣Ссылка-обёртка, стилизованная как Bootstrap-карта⁡ */}
            <Link to={`/vacancies/${vacancy.id}`} className="card h-100 text-decoration-none text-dark">
              <div className="card-body">
                {/* ⁡⁢⁣⁣Название вакансии⁡ */}
                <h5 className="card-title">{vacancy.title}</h5>
                {/* ⁡⁢⁣⁣Описание вакансии (обрезанное)⁡ */}
                <p className="card-text text-truncate">{vacancy.description}</p>
              </div>
            </Link>
          </div>
        ))}
      </div>
    </div>
  );
}

export default VacancyList;
