import React from 'react'
import FullCalendar from '@fullcalendar/react'
import timeGridPlugin from '@fullcalendar/timegrid'

const Calendar = () => {
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
                    events={[
                        { title: 'CIS3210', startRecurrence: '2022-09-07', endRecurrence: '2022-12-07', daysOfWeek: [2, 4], startTime: '08:30', endTime: '10:30' },
                        { title: 'CIS1500', startRecurrence: '2022-09-07', endRecurrence: '2022-12-07', daysOfWeek: [1, 3, 5], startTime: '12:30', endTime: '14:30', color: 'purple' },
                    ]}
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