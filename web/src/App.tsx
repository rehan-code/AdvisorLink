import './App.css';
import './index.css'

import Navbar from "./components/Navbar";
import Footer from "./components/Footer";
import Main from "./components/Main";
import { useEffect, useState } from 'react';

function App() {
  const [data, setData] = useState<any>(null);
  
  useEffect(() => {
    fetch('/api').then(async (response) => {
      // console.log(response.json());
      setData(await response.json());
    });
  }, []);

  return (
    <div className="App">
      <Navbar />
      <Main />
      <Footer />
    </div>
  );
}

export default App;
