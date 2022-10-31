import React, { useState } from "react";
import CourseList from "../components/CourseList";

const Home = () => {
    const [clickedButton, setClickedButton] = useState(false);
    const buttonHandler = (event: React.MouseEvent<HTMLButtonElement>) => {
        event.preventDefault();

        const button: HTMLButtonElement = event.currentTarget;
        setClickedButton(true);
    }

    return (
        <div className='hero'>
            <div className='grid gap-6 mb-6 md:grid-cols-1 bg-black w-full justify-items-center'>
                <div className='p-12 text-white'>
                    <h1 className='text-6xl font-bold'>Search for Sections</h1>
                    <form>
                        <div className="h-8">
                            <input type="text" id="searchQuery" className="p-5 bg-gray-50 h-full border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 flex" placeholder="Search"></input>
                        </div>
                        <div className='p-3'></div>
                        <div className='grid md:grid-cols-3 w-full gap-6 h-10'>
                            <button type="submit" className="text-black bg-white hover:bg-gray-300 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Find Sections</button>
                            <button type="submit" className="text-black bg-white hover:bg-gray-300 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Suggest Sections</button>
                            <button type="submit" onClick={buttonHandler} className="text-black bg-white hover:bg-gray-300 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">List All Courses</button>
                        </div>
                    </form>
                </div>
                <div className='p-6 w-full h-full'>
                    {clickedButton ?
                        <CourseList /> : <div className='p-10 bg-white rounded-lg'>Results appear here...</div>
                    }
                </div>
            </div>
        </div>
    )
}

export default Home;