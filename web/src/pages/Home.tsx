import React from 'react';
import { useNavigate } from 'react-router-dom';

function Home() {
  const navigate = useNavigate();

  const navigateToCalendar = () => {
    navigate('/calendar');
  };

  return (
    <div className="flex justify-center items-center w-full">
      <div className="flex flex-col gap-6 justify-center items-center p-6 bg-white w-7/12 text-xl rounded-md">
        <h1 className="text-4xl font-bold">Welcome to AdvisorLink</h1>
        <p>
          A course scheduling software designed to make your course selection
          process easy and simple
        </p>
        <button
          onClick={navigateToCalendar}
          type="submit"
          className="bg-blue-500 hover:bg-blue-700 text-white p-5 rounded-md"
        >
          Schedule Courses
        </button>
      </div>
    </div>
  );
}

export default Home;
