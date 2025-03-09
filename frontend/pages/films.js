// frontend/pages/films.js
import { useEffect, useState } from 'react';

export default function Films() {
  const [films, setFilms] = useState([]);

  useEffect(() => {
    fetch('http://localhost:8000/media/films')
      .then(res => res.json())
      .then(data => setFilms(data));
  }, []);

  return (
    <div className="min-h-screen bg-gray-900 text-white p-4">
      <h1 className="text-2xl font-bold mb-4">Films</h1>
      <ul>
        {films.map((film, index) => (
          <li key={index} className="p-2 bg-gray-800 rounded mb-2">{film.title}</li>
        ))}
      </ul>
    </div>
  );
}

