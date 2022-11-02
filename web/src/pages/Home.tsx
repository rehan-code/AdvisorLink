import React, { useState } from "react";
import CourseList from "../components/CourseList";
import { Cookies, useCookies } from "react-cookie";
import { Console } from "console";

const Home = () => {
    const [cookies, setCookie] = useCookies(['courses']);
    //array of meeting information (containing temp information)
    let meetingList = [{ title: 'CIS3210', startRecurrence: '2022-09-07', endRecurrence: '2022-12-07', daysOfWeek: [2, 4], startTime: '08:30', endTime: '10:30' },
    { title: 'CIS2500', startRecurrence: '2022-09-07', endRecurrence: '2022-12-07', daysOfWeek: [1, 3, 5], startTime: '12:30', endTime: '14:30', color: 'purple' },] 

    // function should add course to the meeting list
    // function addCourseToMeeting({ course1 }) {
        
    //     let course = {"name": "Intro Financial Accounting",
    //         "faculty": "ACCT",
    //         "code": "1220",
    //         "number": "0108",
    //         "weight": "0.50",
    //         "level": "Undergraduate",
    //         "instructor": "P. Lassou",
    //         "term": "Fall 2022",
    //         "location": "Guelph",
    //         "capacity": "70",
    //         "enrolled": "2",
    //         "meetings": [
    //             {
    //                 "type": "LEC",
    //                 "days": [
    //                     "Fri"
    //                 ],
    //                 "start_time": "08:30AM",
    //                 "end_time": "10:20AM",
    //                 "date": null,
    //                 "building": "ROZH",
    //                 "room": "104"
    //             },
    //             {
    //                 "type": "SEM",
    //                 "days": [
    //                     "Wed"
    //                 ],
    //                 "start_time": "01:30PM",
    //                 "end_time": "02:20PM",
    //                 "date": null,
    //                 "building": "AD-S",
    //                 "room": "VIRTUAL"
    //             },
    //             {
    //                 "type": "EXAM",
    //                 "days": [
    //                     "Tues"
    //                 ],
    //                 "start_time": "08:30AM",
    //                 "end_time": "10:30AM",
    //                 "date": "2022/12/06",
    //                 "building": null,
    //                 "room": null
    //             }
    //         ]
    //     }

    //     let startDate = '';
    //     let endDate = '';
    //     let startTime = course.meetings[0].start_time;
    //     let endTime = course.meetings[0].end_time;

    //     // assign start and endDate based off of term
    //     if (course.term == "Fall 2022") {
    //         startDate = '2022-09-10';
    //         endDate = '2022-12-20';
    //     }
    //     //assign start and endtime for each meeting
    //     //assign days of the week for each meeting

    //     //add item in the json format required
    //     meetingList.push({title: course.faculty+course.code, startRecurrence: startDate, endRecurrence: endDate, daysOfWeek: [2, 4], startTime: startTime, endTime: endTime});
    // }

    const [clickedButton, setClickedButton] = useState(false);
    const buttonHandler = (event: React.MouseEvent<HTMLButtonElement>) => {
        event.preventDefault();

        const button: HTMLButtonElement = event.currentTarget;
        setClickedButton(true);

        // this would be in the add course button handler
        setCookie('courses', meetingList, { path: '/' });
        console.log(cookies.courses);
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