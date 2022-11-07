import React, { useState } from "react";
import CourseList from "../components/CourseList";
import { Cookies, useCookies } from "react-cookie";
import { Console } from "console";

const Home = () => {
    const [cookies, setCookie] = useCookies(['courses']);
    //array of meeting information (containing temp information)
    let meetingList: { title: string, startRecurrence: string, endRecurrence: string, daysOfWeek: number[], startTime: string, endTime: string, color: string } [] = [] ; 

    //let meetingList = [{ title: 'CIS3210', startRecurrence: '2022-09-07', endRecurrence: '2022-12-07', daysOfWeek: [2, 4], startTime: '08:30', endTime: '10:30' },
    //{ title: 'CIS2500', startRecurrence: '2022-09-07', endRecurrence: '2022-12-07', daysOfWeek: [1, 3, 5], startTime: '12:30', endTime: '14:30', color: 'purple' }] 

    // function should add course to the meeting list
    function addCourseToMeeting( course: { name: string, faculty: string, code: string, term: string, meetings: {type: string, days: string[], start_time: string | null, end_time: string | null, date: string | null}[] } ) {

        let startDate = '';
        let endDate = '';
        let startTime = '';
        let endTime = '';
        let meetingDays = [];

        // assign start and endDate based off of term
        if (course.term == "Fall 2022") {
            startDate = '2022-09-08';
            endDate = '2022-12-02';
        }if (course.term == "Winter 2022") {
            startDate = '2022-01-01';
            endDate = '2022-04-10';
        }if (course.term == "Summer 2022") {
            startDate = '2022-05-12';
            endDate = '2022-08-08';
        }

        if (course.meetings != null) {
            //Loop for meetings
            for (let i = 0; i < course.meetings.length; i++) {
                if (course.meetings[i].start_time != null && course.meetings[i].start_time != null) {
                    //assign start and endtime for each meeting
                    startTime = course.meetings[i].start_time!;
                    endTime = course.meetings[i].end_time!;
                    
                    //assign days of the week for each meeting
                    for ( let dayIndex = 0; dayIndex < course.meetings[i].days.length; dayIndex++ ) {
                        if ( course.meetings[i].days[dayIndex] == 'Mon' ) {
                            meetingDays.push(1);
                        } else if ( course.meetings[i].days[dayIndex] == 'Tues' ) {
                            meetingDays.push(2);
                        } else if ( course.meetings[i].days[dayIndex] == 'Wed' ) {
                            meetingDays.push(3);
                        } else if ( course.meetings[i].days[dayIndex] == 'Thurs' ) {
                            meetingDays.push(4);
                        } else if ( course.meetings[i].days[dayIndex] == 'Fri' ) {
                            meetingDays.push(5);
                        } else if ( course.meetings[i].days[dayIndex] == 'Sat' ) {
                            meetingDays.push(6);
                        } else if ( course.meetings[i].days[dayIndex] == 'Sun' ) {
                            meetingDays.push(7);
                        }
                    }

                    //add item in the json format required
                    meetingList.push({title: course.faculty+course.code, startRecurrence: startDate, endRecurrence: endDate, daysOfWeek: meetingDays, startTime: startTime, endTime: endTime, color: 'null'});
    
                }
            }
            
}
    }

    const [clickedButton, setClickedButton] = useState(false);
    const buttonHandler = (event: React.MouseEvent<HTMLButtonElement>) => {
        event.preventDefault();

        const button: HTMLButtonElement = event.currentTarget;
        setClickedButton(true);
    }

    // const [addCourseButton, setClickedCourseButton] = useState(false);
    const addCourseButtonHandler = (event: React.MouseEvent<HTMLButtonElement>) => {
        event.preventDefault();

        const button: HTMLButtonElement = event.currentTarget;
        // setClickedCourseButton(true);

        let course = {"name": "Intro Financial Accounting",
            "faculty": "ACCT",
            "code": "1220",
            "number": "0108",
            "weight": "0.50",
            "level": "Undergraduate",
            "instructor": "P. Lassou",
            "term": "Fall 2022",
            "location": "Guelph",
            "capacity": "70",
            "enrolled": "2",
            "meetings": [
                {
                    "type": "LEC",
                    "days": [
                        "Fri"
                    ],
                    "start_time": "08:30AM",
                    "end_time": "10:20AM",
                    "date": null,
                    "building": "ROZH",
                    "room": "104"
                },
                {
                    "type": "SEM",
                    "days": [
                        "Wed"
                    ],
                    "start_time": "01:30PM",
                    "end_time": "02:20PM",
                    "date": null,
                    "building": "AD-S",
                    "room": "VIRTUAL"
                },
                {
                    "type": "EXAM",
                    "days": [
                        "Tues"
                    ],
                    "start_time": "08:30AM",
                    "end_time": "10:30AM",
                    "date": "2022/12/06",
                    "building": null,
                    "room": null
                }
            ]
        }
        
        addCourseToMeeting(course);

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