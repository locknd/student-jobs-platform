import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';

function VacancyList() {
  const [vacancies, setVacancies] = useState([]);

  useEffect(() => {
    fetch('http://localhost:8000/api/v1/vacancies')
      .then(res => res.json())
      .then(data => setVacancies(data));
  }, []);

  return (
    <div>
      <h2>Доступные вакансии</h2>
      <ul>
        {vacancies.map(vacancy => (
          <li key={vacancy.id}>
            <Link to={`/vacancies/${vacancy.id}`}>{vacancy.title}</Link>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default VacancyList;