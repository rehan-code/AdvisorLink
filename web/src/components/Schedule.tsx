/* eslint-disable react/jsx-no-bind */
/* eslint-disable react/jsx-boolean-value */
/* eslint-disable @typescript-eslint/no-unused-vars */
/* eslint-disable func-names */
/* eslint-disable @typescript-eslint/no-empty-function */
/* eslint-disable jsx-a11y/label-has-associated-control */

import React, { useState, createRef, useEffect } from 'react';
import FullCalendar from '@fullcalendar/react';
import timeGridPlugin from '@fullcalendar/timegrid';
import dayGridPlugin from '@fullcalendar/daygrid';
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
  BORDER: '#171717',
};

interface Events {
  week: WeeklyEvent[];
  exam: ExamEvent[];
}

interface WeeklyEvent {
  title: string;
  allDay: boolean;
  daysOfWeek: number[];
  startTime: string;
  endTime: string;
  color: string;
  borderColor: string;
}

interface ExamEvent {
  title: string;
  allDay: boolean;
  start: string;
  end: string;
  color: string;
  borderColor: string;
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
  const events: Events = { week: [], exam: [] };
  sections.forEach((section) => {
    section.meetings
      .filter((m) => m.start_time && m.end_time && m.days)
      .forEach((meeting) => {
        const meetingDays = getDaysOfWeekInteger(meeting.days);
        if (meeting.type.substring(12) !== 'EXAM')
          events.week.push({
            title: `${section.faculty}*${section.code}*${
              section.number
            }\n${meeting.type.substring(12)}`,
            allDay: false,
            daysOfWeek: meetingDays,
            startTime: meeting.start_time,
            endTime: meeting.end_time,
            color: checkConflict(
              events.week,
              meeting.start_time,
              meeting.end_time,
              meetingDays,
            )
              ? colors.ERROR
              : getColor(meeting.type.substring(12)),
            borderColor: colors.BORDER,
          });
        else
          events.exam.push({
            title: `${section.faculty}*${
              section.code
            }*\n${meeting.type.substring(12)}`,
            allDay: false,
            start: `${meeting.date}T${meeting.start_time}`,
            end: `${meeting.date}T${meeting.end_time}`,
            color: colors.EXAM,
            borderColor: colors.EXAM,
          });
      });
  });
  return events;
}

function checkConflict(
  events: WeeklyEvent[],
  startTime: string,
  endTime: string,
  meetingDays: number[],
) {
  return (
    events.filter(
      (event) =>
        event.startTime <= endTime &&
        event.endTime >= startTime &&
        event.daysOfWeek.filter((x) => meetingDays.indexOf(x) !== -1).length >
          0,
    ).length > 0
  );
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

function getMinDate(events: ExamEvent[]) {
  return (
    events.length > 1
      ? events.reduce((a, b) => (a.start < b.start ? a : b))
      : events[0]
  ).start;
}

export default function Schedule(props: any) {
  const [scheduleType, setScheduleType] = useState<string>('Weekly');
  const events = createCalendarEvents(props.events);
  const weekScheduleRef = createRef<FullCalendar>();
  const examScheduleRef = createRef<FullCalendar>();

  // Set View to the first exam week
  useEffect(() => {
    if (events.exam.length > 0) {
      const examCalendarApi = examScheduleRef.current?.getApi();
      examCalendarApi?.gotoDate(getMinDate(events.exam));
    }
  }, [events]);

  return (
    <div className="bg-white p-5">
      <div id="sc">
        <div className={scheduleType === 'Weekly' ? 'block' : 'hidden'}>
          <div>
            <h1 className="text-2xl font-bold pb-8">Weekly Schedule</h1>
            <FullCalendar
              ref={weekScheduleRef}
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
              events={events.week}
              slotMinTime="07:00:00"
              slotMaxTime="23:00:00"
              allDaySlot={false}
              contentHeight="auto"
              slotEventOverlap={false}
            />
          </div>
        </div>
        <div className={scheduleType === 'Weekly' ? 'hidden' : 'block'}>
          <h1 className="text-2xl font-bold pb-8">Exam Schedule</h1>
          <FullCalendar
            ref={examScheduleRef}
            plugins={[dayGridPlugin, timeGridPlugin]}
            headerToolbar={{
              left: 'prev',
              center: 'title',
              right: 'dayGridMonth timeGridWeek next',
            }}
            initialView="dayGridMonth"
            events={events.exam}
            eventDisplay="block"
            displayEventEnd={true}
            weekends
            slotMinTime="07:00:00"
            slotMaxTime="23:00:00"
            contentHeight="auto"
            slotEventOverlap={false}
          />
        </div>
      </div>
      <div className="flex justify-evenly items-center p-4">
        <button
          type="submit"
          className="bg-blue-500 hover:bg-blue-700 text-white p-5 rounded-md"
          onClick={(e) =>
            scheduleType === 'Weekly'
              ? setScheduleType('Exam')
              : setScheduleType('Weekly')
          }
        >
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
    </div>
  );
}
