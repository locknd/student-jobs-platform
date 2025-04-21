import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import VacancyList from './components/VacancyList';
import VacancyDetail from './components/VacancyDetail';

function App() {
  return (
    <Router>
      <div className="container">
        <Routes>
          <Route path="/" element={<VacancyList />} />
          <Route path="/vacancies/:id" element={<VacancyDetail />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;