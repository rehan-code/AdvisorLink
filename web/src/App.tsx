import React, { useEffect, useState } from 'react';
import './App.css';

function App() {
  const [data, setData] = useState<any>(null);
  
  useEffect(() => {
    fetch('/ding').then(async (response) => {
      // console.log(response.json());
      setData(await response.json());
    });
  });

  return (
    <p>{data?.message ?? 'Loading...'}</p>
  );
}

export default App;
