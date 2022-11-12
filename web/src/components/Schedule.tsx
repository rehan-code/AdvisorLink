/* eslint-disable react/jsx-no-bind */
/* eslint-disable @typescript-eslint/no-unused-vars */
/* eslint-disable func-names */
/* eslint-disable @typescript-eslint/no-empty-function */
import React from 'react';
import FullCalendar, { EventSourceInput } from '@fullcalendar/react';
import timeGridPlugin from '@fullcalendar/timegrid';
import jsPDF from 'jspdf';
import { Section } from './CalendarComponent';

const daysOfWeek = ['MON', 'TUES', 'WED', 'THUR', 'FRI', 'SAT', 'SUN'];
const randomColor = require('randomcolor');

interface Event {
  title: string;
  daysOfWeek: number[];
  startTime: string;
  endTime: string;
  color: string;
}

function getDaysOfWeekInteger(days: string[]) {
  const daysInt: number[] = [];
  days.forEach((day) => {
    // FIX THIS - days in 'DayOfWeek.DAY' format
    daysInt.push(daysOfWeek.indexOf(day.substring(10)) + 1);
  });

  return daysInt;
}

function createCalendarEvents(sections: Section[]) {
  const events: Event[] = [];
  sections.forEach((section) => {
    const color = randomColor({ luminosity: 'dark' });
    section.meetings
      .filter((m) => m.start_time && m.end_time && m.days)
      .forEach((meeting) => {
        events.push({
          // FIX THIS - meeting type in 'MeetingType.TYPE' format
          title: `${section.faculty}*${section.code}*${section.number
          }\n${meeting.type.substring(12)}`,
          daysOfWeek: getDaysOfWeekInteger(meeting.days),
          startTime: meeting.start_time,
          endTime: meeting.end_time,
          color,
        });
      });
  });

  return events;
}

const handleExport = async () => {
  const htmlElement: HTMLElement = document.getElementById('sc') as HTMLElement;
  // eslint-disable-next-line new-cap
  const report = new jsPDF('landscape', 'mm', [htmlElement.scrollWidth + 1, htmlElement.scrollHeight + 1]);
  report.html(htmlElement).then(() => {
    report.save('schedule.pdf');
  });
};

export default function Schedule(props: any) {
  return (
    <div className="bg-white">
      <div id="sc">
        <h1 className="text-2xl font-bold pb-8">Course Schedule</h1>
        <FullCalendar
          plugins={[timeGridPlugin]}
          headerToolbar={{
            left: '',
            center: '',
            right: '',
          }}
          dayHeaderFormat={{
            weekday: 'short',
          }}
          initialView="timeGridWeek"
          weekends
          eventDidMount={function (info) { }}
          events={createCalendarEvents(props.events)}
          slotMinTime="07:00:00"
          slotMaxTime="23:00:00"
          allDaySlot={false}
          contentHeight="auto"
          slotEventOverlap={false}
        />
      </div>
      <div className="flex justify-evenly items-center p-4">
        <button
          className="py-4 px-8 bg-blue-500 rounded-md text-white hover:bg-blue-800 font-bold"
          type="submit"
          onClick={handleExport}
        >
          Export
        </button>
      </div>
    </div>
  );
}
