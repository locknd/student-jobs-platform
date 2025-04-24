import { useState } from 'react';
import { useNavigate } from 'react-router-dom';

// ⁡⁢⁣⁣Форма создания новой вакансии⁡
export default function CreateVacancyForm() {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();

    const payload = { title, description, created_by: 1 /* временный user_id */ };

    const res = await fetch('/api/v1/vacancies', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
    });

    if (res.ok) {
      const vacancy = await res.json();
      // После успешного создания — переходим на страницу списка или деталей
      navigate(`/vacancies/${vacancy.id}`);
    } else {
      alert('Ошибка при создании вакансии');
    }
  };

  return (
    <div className="container my-4">
      <h1 className="mb-4">Создать новую вакансию</h1>
      <form onSubmit={handleSubmit}>
        <div className="mb-3">
          <label className="form-label">Заголовок</label>
          <input
            type="text"
            className="form-control"
            value={title}
            onChange={e => setTitle(e.target.value)}
            required
          />
        </div>

        <div className="mb-3">
          <label className="form-label">Описание</label>
          <textarea
            className="form-control"
            rows="4"
            value={description}
            onChange={e => setDescription(e.target.value)}
            required
          />
        </div>

        <button type="submit" className="btn btn-success">Сохранить</button>
        <button type="button" className="btn btn-secondary ms-2"onClick={() => navigate(-1)}
        >
          Отменить
        </button>
      </form>
    </div>
  );
}