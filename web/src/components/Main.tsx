import React from 'react';
import { Routes, Route } from 'react-router-dom';

import Home from '../pages/Home';
import Calendar from '../pages/Calendar';
import About from '../pages/About';

const Main = () => {
  return (
    <Routes> {/* The Switch decides which component to show based on the current URL.*/}
        <Route path='/' element={<Home/>}></Route>
        <Route path='/calendar' element={<Calendar/>}></Route>
        <Route path='/about' element={<About/>}></Route>
    </Routes>
  );
}

export default Main;