/* eslint-disable react/jsx-no-bind */
/* eslint-disable @typescript-eslint/no-unused-vars */
/* eslint-disable func-names */
/* eslint-disable @typescript-eslint/no-empty-function */
/* eslint-disable jsx-a11y/label-has-associated-control */

import React, { useState } from 'react';
import FullCalendar, { EventSourceInput } from '@fullcalendar/react';
import timeGridPlugin from '@fullcalendar/timegrid';
import jsPDF from 'jspdf';
import { Section } from './CalendarComponent';

const daysOfWeek = ['MON', 'TUES', 'WED', 'THUR', 'FRI', 'SAT', 'SUN'];
const colors = {
  LEC: '#BB5098',
  LAB: '#5344A9',
  EXAM: '#F5C63C',
  SEM: '#8BD29E',
  ERROR: '#F72A25',
  DEFAULT: '#444140',
  BORDER: '#171717'
}

interface Event {
  title: string;
  daysOfWeek: number[];
  startTime: string;
  endTime: string;
  color: string;
  borderColor: string;
  extendedProps: {
    eventType: string;
  };
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
    section.meetings
      .filter((m) => m.start_time && m.end_time && m.days)
      .forEach((meeting) => {
        const meetingDays = getDaysOfWeekInteger(meeting.days);
        const backgroundColor = checkConflict(events, meeting.start_time, meeting.end_time, meetingDays) ? colors.ERROR : getColor(meeting.type.substring(12));
        events.push({
          // FIX THIS - meeting type in 'MeetingType.TYPE' format
          title: `${section.faculty}*${section.code}*${section.number
            }\n${meeting.type.substring(12)}`,
          daysOfWeek: meetingDays,
          startTime: meeting.start_time,
          endTime: meeting.end_time,
          color: meeting.type.substring(12) === 'EXAM' ? colors.EXAM : backgroundColor,
          borderColor: colors.BORDER,
          extendedProps: {
            eventType: meeting.type.substring(12),
          },
        });
      });
  });
  return events;
}

function checkConflict(events: Event[], startTime: string, endTime: string, meetingDays: number[]) {
  return events.filter((event) => (
    (event.startTime <= endTime && event.endTime >= startTime)
    && event.daysOfWeek.filter(x => meetingDays.indexOf(x) !== -1).length > 0
    && event.extendedProps.eventType !== 'EXAM'
  )).length > 0;
}

function getColor(eventType: string) {
  switch (eventType) {
    case 'LEC':
      return colors.LEC;
    case 'LAB':
      return colors.LAB;
    case 'EXAM':
      return colors.EXAM;
    case 'SEM':
      return colors.SEM;
    default:
      return colors.DEFAULT;
  }
}

const handleExport = async () => {
  const htmlElement: HTMLElement = document.getElementById('sc') as HTMLElement;
  // eslint-disable-next-line new-cap
  const report = new jsPDF('landscape', 'mm', [
    htmlElement.scrollWidth + 1,
    htmlElement.scrollHeight + 1,
  ]);
  report.html(htmlElement).then(() => {
    report.save('schedule.pdf');
  });
};

export default function Schedule(props: any) {
  const [scheduleType, setScheduleType] = useState<string>('Weekly');
  const events = createCalendarEvents(props.events);
  const weeklyEvents = events.filter((event) => (event.extendedProps.eventType !== 'EXAM'));
  const examEvents = events.filter((event) => (event.extendedProps.eventType === 'EXAM'));
  return (
    <div className="bg-white">
      <div id="sc">
        <h1 className="text-2xl font-bold pb-8">{scheduleType === 'Weekly' ? 'Weekly' : 'Exam'} Schedule</h1>
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
          events={scheduleType === 'Weekly' ? weeklyEvents : examEvents}
          slotMinTime="07:00:00"
          slotMaxTime="23:00:00"
          allDaySlot={false}
          contentHeight="auto"
          slotEventOverlap={false}
        />
      </div>
      <div className="flex justify-evenly items-center p-4">
        <button
          type="submit"
          className="bg-blue-500 hover:bg-blue-700 text-white p-5 rounded-md"
          onClick={(e) => scheduleType === 'Weekly' ? setScheduleType('Exam') : setScheduleType('Weekly')}>
          Switch to {scheduleType === 'Weekly' ? 'Exam' : 'Weekly'} Schedule
        </button>
        <button
          className="py-4 px-8 bg-blue-500 rounded-md text-white hover:bg-blue-800 font-bold"
          type="submit"
          onClick={handleExport}
        >
          Export
        </button>
      </div>
    </div >
  );
}
