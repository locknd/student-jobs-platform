import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';

// ⁡⁢⁣⁣Компонент отображения деталей вакансии и управления подачей заявки⁡
function VacancyDetail() {
  // ⁡⁢⁣⁣Получаем параметр id из URL (React Router)⁡
  const { id } = useParams();
  
  // ⁡⁢⁣⁣Состояния для хранения данных вакансии, статусов загрузки, ошибки и отправки заявки⁡
  const [vacancy, setVacancy] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [submitted, setSubmitted] = useState(false);

  // ⁡⁢⁣⁣Загружаем данные вакансии при монтировании или изменении id⁡
  useEffect(() => {
    setLoading(true);           // ⁡⁢⁣⁣Отмечаем начало загрузки⁡
    setError(null);             // ⁡⁢⁣⁣Сбрасываем предыдущую ошибку⁡
    fetch(`/api/v1/vacancies/${id}`) // ⁡⁢⁣⁣Запрос к API за детальной информацией⁡
      .then(res => {
        if (!res.ok) throw new Error('Вакансия не найдена');
        return res.json();      // ⁡⁢⁣⁣Преобразуем ответ в JSON⁡
      })
      .then(data => setVacancy(data))      // ⁡⁢⁣⁣Сохраняем данные вакансии⁡
      .catch(err => setError(err.message)) // ⁡⁢⁣⁣Записываем сообщение об ошибке⁡
      .finally(() => setLoading(false));   // ⁡⁢⁣⁣Завершаем загрузку⁡
  }, [id]);

  // ⁡⁢⁣⁣Обработчик подачи заявки⁡
  const handleApply = () => {
    setError(null);                                    // ⁡⁢⁣⁣Сбрасываем ошибку перед новым запросом⁡
    fetch('/api/v1/applications', {
      method: 'POST',                                  // ⁡⁢⁣⁣Метод POST для создания заявки⁡
      headers: { 'Content-Type': 'application/json' }, // ⁡⁢⁣⁣Указываем, что тело запроса JSON⁡
      body: JSON.stringify({                           // ⁡⁢⁣⁣Тело: user_id и vacancy_id⁡
        user_id: 1,
        vacancy_id: parseInt(id, 10)
      })
    })
      .then(res => {
        if (!res.ok) throw new Error('Ошибка при отправке заявки');
        setSubmitted(true);                            // ⁡⁢⁣⁣Помечаем успешную отправку⁡
      })
      .catch(err => {
        setError(err.message);                         // ⁡⁢⁣⁣Устанавливаем текст ошибки⁡
        // ⁡⁢⁣⁣Дополнительно показываем всплывающее сообщение пользователю⁡
        alert(`Произошла ошибка: ${err.message}`);
      });
  };

  // ⁡⁢⁣⁣Пока идёт загрузка — отображаем индикатор⁡
  if (loading) {
    return (
      <div className="container my-4">
        <p>Загрузка вакансии...</p>
      </div>
    );
  }

  // ⁡⁢⁣⁣Если при загрузке возникла ошибка — показываем её⁡
  if (error) {
    return (
      <div className="container my-4">
        <div className="alert alert-danger" role="alert">
          {error}
        </div>
      </div>
    );
  }

  // ⁡⁢⁣⁣Если вакансия не найдена (vacancy всё ещё null после загрузки без ошибки)⁡
  if (!vacancy) {
    return (
      <div className="container my-4">
        <p>Вакансия не найдена.</p>
      </div>
    );
  }

  return (
    <div className="container my-4">
      {/*⁡⁢⁣⁣ Заголовок вакансии⁡ */}
      <h2 className="mb-3">{vacancy.title}</h2>
      {/* ⁡⁢⁣⁣Описание вакансии⁡ */}
      <p className="mb-4">{vacancy.description}</p>
      {/* ⁡⁢⁣⁣Блок с кнопкой подачи заявки или сообщением об успешной отправке ⁡*/}
      {!submitted ? (
        <>
          <button className="btn btn-primary" onClick={handleApply}>
            Подать заявку
          </button>
        </>
      ) : (
        <div className="alert alert-success" role="alert">
          ✅ Заявка отправлена!
        </div>
      )}
    </div>
  );
}

export default VacancyDetail;