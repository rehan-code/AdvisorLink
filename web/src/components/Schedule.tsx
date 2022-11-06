import React from 'react';
import FullCalendar, { EventSourceInput } from '@fullcalendar/react';
import timeGridPlugin from '@fullcalendar/timegrid';
import { Section } from './CalendarComponent';

const daysOfWeek = ['MON', 'TUES', 'WED', 'THUR', 'FRI', 'SAT', 'SUN'];
var randomColor = require('randomcolor');

interface Event {
    title: string,
    daysOfWeek: number[],
    startTime: string,
    endTime: string,
    color: string
}

function getDaysOfWeekInteger(days: string[]) {
    let daysInt: number[] = [];
    days.forEach((day) => {
        // FIX THIS - why am I getting days in 'DayOfWeek.DAY' format
        daysInt.push(daysOfWeek.indexOf(day.substring(10)) + 1)
    })

    return daysInt;
}

function createCalendarEvents(sections: Section[]) {
    let events: Event[] = [];
    sections.forEach((section) => {
        if (!section.number.includes("DE")) {
            var color = randomColor();
            section.meetings.forEach((meeting) => {
                events.push({
                    // FIX THIS - meeting type in 'MeetingType.TYPE' format
                    title: section.faculty + '*' + section.code + '*' + section.number + '\n' + meeting.type.substring(12),
                    daysOfWeek: getDaysOfWeekInteger(meeting.days),
                    startTime: meeting.start_time,
                    endTime: meeting.end_time,
                    color: color
                })
            })
        }
    })

    return events;
}

export default function Schedule(props: any) {
    return (
        <>
            <h1 className="text-2xl font-bold pb-8">Course Schedule</h1>
            <FullCalendar
                plugins={[timeGridPlugin]}
                headerToolbar={{
                    left: '',
                    center: '',
                    right: ''
                }}
                dayHeaderFormat={{
                    weekday: 'short'
                }}
                initialView="timeGridWeek"
                weekends={true}
                events={createCalendarEvents(props.events)}
                slotMinTime="07:00:00"
                slotMaxTime="23:00:00"
                allDaySlot={false}
                contentHeight="auto"
                slotEventOverlap={false}
            />
        </>
    )
}
