import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';

// ⁡⁢⁣⁣Компонент панели работодателя: просмотр и обновление статуса заявок⁡
function EmployerDashboard() {
  // ⁡⁢⁣⁣Состояние для списка заявок⁡
  const [applications, setApplications] = useState([]);
  // ⁡⁢⁣⁣Состояние для ошибок⁡
  const [error, setError] = useState(null);

  // ⁡⁢⁣⁣Загрузка всех заявок при монтировании компонента⁡
  useEffect(() => {
    fetch('/api/v1/applications') // ⁡⁢⁣⁣Запрос к API для получения заявок⁡
      .then(res => {
        if (!res.ok) throw new Error('Не удалось загрузить заявки');
        return res.json();
      })
      .then(data => setApplications(data))  // ⁡⁢⁣⁣Сохраняем список заявок⁡
      .catch(err => setError(err.message)); // ⁡⁢⁣⁣Сохраняем сообщение об ошибке⁡
  }, []);

  // ⁡⁢⁣⁣Функция для обновления статуса конкретной заявки⁡
  const updateStatus = (appId, newStatus) => {
    setError(null); // ⁡⁢⁣⁣Сбрасываем предыдущую ошибку⁡
    fetch(`/api/v1/applications/${appId}/status`, {
      method: 'PATCH',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ status: newStatus }) // ⁡⁢⁣⁣Передаем новый статус⁡
    })
      .then(res => {
        if (!res.ok) throw new Error('Не удалось обновить статус');
        return res.json();
      })
      .then(updatedApp => {
        // ⁡⁢⁣⁣Обновляем локальный список заявок⁡
        setApplications(apps =>
          apps.map(a => (a.id === updatedApp.id ? updatedApp : a))
        );
      })
      .catch(err => setError(err.message)); // ⁡⁢⁣⁣Устанавливаем текст ошибки⁡
  };

  return (
    <div className="container my-4">

      <h2 className="mb-4">Панель работодателя</h2>
      {/* ⁡⁢⁣⁣Отображение ошибки, если она есть⁡ */}
      {error && (
        <div className="alert alert-danger" role="alert">
          {error}
        </div>
      )}

      {/* ⁡⁢⁣⁣Кнопка для создания новой вакансии⁡ */}
      <Link to="/vacancies/employer/create_new" className="btn btn-primary mb-3">+ Создать вакансию</Link>

      {/* ⁡⁢⁣⁣Таблица заявок⁡ */}
      <table className="table table-bordered table-striped">
        <thead className="table-light">
          <tr>
            <th>Номер заявки</th>
            <th>Студент</th>
            <th>Вакансия</th>
            <th>Статус</th>
            <th>Действия</th>
          </tr>
        </thead>
        <tbody>
          {applications.map(app => (
            <tr key={app.id}>
              <td>{app.id}</td>
              <td>{app.user_id}</td>
              <td>{app.vacancy_id}</td>
              <td>
                <span className={`badge ${
                  app.status === 'approved' ? 'bg-success' :
                  app.status === 'rejected' ? 'bg-danger' :
                  'bg-secondary'
                }`}>
                  {app.status}
                </span>
              </td>
              <td>
                {/* ⁡⁢⁣⁣Кнопки для смены статуса⁡ */}
                <button
                  className="btn btn-sm btn-success me-2"
                  onClick={() => updateStatus(app.id, 'approved')}
                >✔️ Принять</button>
                <button
                  className="btn btn-sm btn-danger"
                  onClick={() => updateStatus(app.id, 'rejected')}
                >✖️ Отклонить</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default EmployerDashboard;