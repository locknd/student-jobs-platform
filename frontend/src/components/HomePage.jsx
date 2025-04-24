import React from 'react';
import { Link } from 'react-router-dom';

export default function Home() {
  return (
    <div className="container-fluid px-0">
      {/* ⁡⁢⁣⁣Hero во весь экран ⁡*/}
      <div
        className="bg-light d-flex align-items-center justify-content-center"
        style={{ minHeight: '100vh' }}
      >
        <div className="text-center px-3">
          <p className="display-4 fw-bold mb-3">
            Добро пожаловать на платформу Student Jobs
          </p>
          <p className="lead mb-4">
            Здесь вы сможете быстро найти временную работу или стажировку в кампусе,
            подать заявку и отслеживать её статус.
          </p>
          <Link
            to="/vacancies"
            className="btn btn-lg btn-outline-primary shadow-sm"
            style={{ borderWidth: 2 }}
          >
            Перейти к вакансиям
          </Link>
        </div>
      </div>
    </div>
  );
}