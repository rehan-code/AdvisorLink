import React from 'react';
import { Routes, Route } from 'react-router-dom';

import Home from '../pages/Home';
import Calendar from '../pages/Calendar';
import About from '../pages/About';

function Main() {
  return (
    <Routes>
      {' '}
      {/* The Switch decides which component to show based on the current URL. */}
      <Route path="/" element={<Home />} />
      <Route path="/calendar" element={<Calendar />} />
      <Route path="/about" element={<About />} />
    </Routes>
  );
}

export default Main;
