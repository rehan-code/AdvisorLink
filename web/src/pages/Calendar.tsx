import React from 'react'
import FullCalendar from '@fullcalendar/react'
import timeGridPlugin from '@fullcalendar/timegrid'
import { useCookies } from 'react-cookie';

const Calendar = () => {
    const [cookies, setCookie] = useCookies(['courses']);
    return (
        <div className='section'>
            <div className='container w-full'>
                <FullCalendar
                    plugins={[timeGridPlugin]}
                    headerToolbar={{
                        left: 'today',
                        center: 'title',
                        right: 'prev,next'
                    }}
                    initialView='timeGridWeek'
                    weekends={true}
                    events={cookies.courses}
                    slotMinTime='08:00:00'
                    slotMaxTime='24:00:00'
                    allDaySlot={false}
                    contentHeight='auto'
                />
            </div>
        </div>
    )
}

export default Calendar;