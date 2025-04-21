import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';

function VacancyDetail() {
  const { id } = useParams();
  const [vacancy, setVacancy] = useState(null);
  const [submitted, setSubmitted] = useState(false);

  useEffect(() => {
    fetch(`http://localhost:8000/api/v1/vacancies/${id}`)
      .then(res => res.json())
      .then(data => setVacancy(data));
  }, [id]);

  const handleApply = () => {
    fetch('http://localhost:8000/api/v1/applications', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ user_id: 1, vacancy_id: parseInt(id) })
    })
    .then(res => {
      if (res.ok) setSubmitted(true);
      else alert("Ошибка при отправке заявки");
    });
  };

  if (!vacancy) return <p>Загрузка...</p>;

  return (
    <div>
      <h2>{vacancy.title}</h2>
      <p>{vacancy.description}</p>
      {!submitted ? (
        <button onClick={handleApply}>Подать заявку</button>
      ) : (
        <p>✅ Заявка отправлена!</p>
      )}
    </div>
  );
}

export default VacancyDetail;