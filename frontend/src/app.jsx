import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import VacancyList from './components/VacancyList';
import VacancyDetail from './components/VacancyDetail';
import EmployerDashboard from './components/EmployerDashboard';
import CreateVacancyForm from './components/CreateVacancyForm';
import Home from './components/HomePage';
/**
 * ⁡⁢⁣⁣ Используем export default для:
 *  - Упрощённого импорта без фигурных скобок
 *  - Совместимости с большинством сборщиков и шаблонов React
 *  - Возможности именовать импортируемый компонент произвольно
 **/
export default function App() {
  return (
    // ⁡⁢⁣⁣Router-обёртка для поддержки SPA-маршрутов⁡
    <Router>
      {/* ⁡⁢⁣⁣Навигационная панель приложения⁡ */}
      <nav className="navbar navbar-expand-lg navbar-light bg-light">
        <div className="container-fluid">
          {/* ⁡⁢⁣⁣Логотип, возвращающий на главную⁡ */}
          <Link className="navbar-brand" to="/">Student Jobs</Link>
          {/* ⁡⁢⁣⁣Кнопка-тогглер для мобильного меню⁡ */}
          <button
            className="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarNav"
            aria-controls="navbarNav"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span className="navbar-toggler-icon"></span>
          </button>
          {/* ⁡⁢⁣⁣Ссылки меню⁡ */}
          <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav me-auto">
              <li className="nav-item"><Link to="/vacancies" className="nav-link">Вакансии</Link></li>
              <li className="nav-item"><Link to="/vacancies/employer/dashboard" className="nav-link">Работодатель</Link></li>
            </ul>
          </div>
        </div>
      </nav>

      {/* ⁡⁢⁣⁣Определение маршрутов⁡ */}
      <Routes>
        {/* ⁡⁢⁣⁣Главная страница: описание сервиса⁡ */}
        <Route path="/" element={<Home />} />
        {/* ⁡⁢⁣⁣Список вакансий⁡ */}
        <Route path="/vacancies" element={<VacancyList />} />
        {/* ⁡⁢⁣⁣Детали вакансии по ID⁡ */}
        <Route path="/vacancies/:id" element={<VacancyDetail />} />
        {/* ⁡⁢⁣⁣Форма создания новой вакансии (для работодателя)⁡ */}
        <Route path="/vacancies/employer/create_new" element={<CreateVacancyForm />} />
        {/* ⁡⁢⁣⁣Панель работодателя: просмотр и управление заявками⁡ */}
        <Route path="/vacancies/employer/dashboard" element={<EmployerDashboard />} />
      </Routes>
    </Router>
  );
}