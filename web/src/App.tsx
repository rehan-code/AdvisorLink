import './App.css';
import './index.css'

import Navbar from "./components/Navbar";
import Footer from "./components/Footer";
import Main from "./components/Main";
import { useEffect, useState } from 'react';

function App() {
  return (
    <div className="App">
      <Navbar />
      <Main />
      <Footer />
    </div>
  );
}

export default App;
