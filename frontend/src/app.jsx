import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import VacancyList from './components/VacancyList';
import VacancyDetail from './components/VacancyDetail';
import EmployerDashboard from './components/EmployerDashboard';

/**
⁡⁢⁣⁣ Используем export default для:
  - Упрощённого импорта без фигурных скобок
  - Совместимости с большинством сборщиков и шаблонов React
  - Возможности называть импортированный модуль произвольно при необходимости⁡
 **/
export default function App() {
  return (
    // ⁡⁢⁣⁣Router-обёртка для поддержки SPA-маршрутов⁡
    <Router>
      <Routes>
        {/* ⁡⁢⁣⁣Главная страница со списком вакансий⁡ */}
        <Route path="/" element={<VacancyList />} />

        {/* ⁡⁢⁣⁣Страница деталей вакансии по ID⁡ */}
        <Route path="/vacancies/:id" element={<VacancyDetail />} />

        {/* ⁡⁢⁣⁣Панель работодателя для управления заявками⁡ */}
        <Route path="/dashboard" element={<EmployerDashboard />} />
      </Routes>
    </Router>
  );
}