import React, { ChangeEvent, useState, useEffect } from 'react';
import { useCookies } from 'react-cookie';
import Schedule from './Schedule';
import { Multibutton } from './Multibutton';
import { TermSelector } from './TermSelector';
import { SuggestionEngineMenu } from './SuggestionEngineMenu';

const queryRegex =
  /(name|code|faculty|credits|level|term|location|building|instructor|year):\s*([A-Za-z0-9]+)/g; // Save for future reference

export interface Section {
  id: string;
  name: string;
  termId: string;
  courseId: string;
  code: string;
  number: string;
  faculty: string;
  weight: number;
  instructor: string;
  term: string;
  location: string;
  capacity: number;
  enrolled: number;
  meetings: [
    {
      building: string;
      date: string;
      days: string[];
      start_time: string;
      end_time: string;
      room: string;
      type: string;
    },
  ];
}

export default function CalendarComponent() {
  const [cookies, setCookie] = useCookies(['schedule']);

  const [filters, setFilters] = useState<string[] | undefined>([]); // Save for future reference
  const [query, setQuery] = useState<string | string[][]>('');
  const [queryType, setQueryType] = useState('all');
  const [courseSections, setSections] = useState<Section[]>([]);
  const [termId, setTermId] = useState('');

  // Stores the schedule to use with FullCalendar
  const [scheduleSections, setScheduleSections] = useState<Section[]>(
    cookies.schedule ? cookies.schedule : [],
  );
  const scheduleSectionsInTerm = scheduleSections.filter(
    (c) => c.termId === termId,
  );

  useEffect(() => {
    setCookie('schedule', scheduleSections, { path: '/' });
  }, [scheduleSections]);

  /* Whenever the term ID changes, clear the table to avoid confusion. */
  useEffect(() => {
    setSections([]);
  }, [termId]);

  // Break search field into queryable strings
  const updateFilters = (event: ChangeEvent<HTMLInputElement>) => {
    event.preventDefault();

    const target = event.target as HTMLInputElement;
    const queryString = target.value;

    const queries = queryString.match(queryRegex);

    const matches = queries?.map((element) => element);
    setFilters(matches);
  };

  const updateQuery = (event: ChangeEvent<HTMLInputElement>) => {
    event.preventDefault();

    const target = event.target as HTMLInputElement;
    setQuery(target.value);
  };

  const searchSections = async (
    event:
      | React.MouseEvent<HTMLButtonElement>
      | React.FormEvent<HTMLFormElement>,
  ) => {
    event.preventDefault();

    const searchResults = await fetch(
      `/api/sections?${new URLSearchParams(
        `query=${query}&queryType=${queryType}&termId=${termId}`,
      )}`,
    );
    const { sections } = await searchResults.json();
    setSections(sections);
  };

  // Memorize previous results
  const addToSchedule = (
    event: React.MouseEvent<HTMLButtonElement>,
    index: number,
  ) => {
    event.preventDefault();
    const section = courseSections[index];

    const tempSchedule = [...scheduleSections];
    tempSchedule.push(section);

    setScheduleSections(tempSchedule);
  };

  const removeFromSchedule = (
    event: React.MouseEvent<HTMLButtonElement>,
    index: number,
  ) => {
    event.preventDefault();

    const tempSchedule = [...scheduleSections];
    tempSchedule.splice(index, 1);

    setScheduleSections(tempSchedule);
  };

  return (
    <div className="w-full flex flex-col justify-center items-center">
      <div
        className="grid auto-rows-min gap-12 px-16 pt-20 pb-0 w-full"
        style={{ paddingBottom: '3rem' }}
      >
        <div className="flex items-center justify-start w-full rounded-md p-10 bg-gray-300 align-middle">
          <h1 className="text-2xl font-bold pr-10">Term</h1>
          <TermSelector setValue={setTermId} />
        </div>
      </div>
      <div className="grid grid-cols-3 auto-rows-min gap-12 px-16 pb-20 w-full">
        <div className="flex items-center justify-start w-full rounded-md p-10 bg-gray-300 col-start-1 col-end-1">
          {/* COURSE SEARCHING */}
          <div className="w-full">
            <h1 className="text-2xl font-bold pb-8">Course Search</h1>
            <div className="flex gap-3 w-full items-center">
              <div className="flex flex-col items-center justify-center w-full">
                <form className="w-full" onSubmit={(event) => searchSections}>
                  <input
                    type="text"
                    className="text-lg p-4 w-full rounded-md"
                    placeholder="Accounting"
                    onChange={(event: ChangeEvent<HTMLInputElement>) =>
                      updateQuery(event)
                    }
                  />
                  <div className="flex justify-evenly items-center p-4 w-full">
                    <Multibutton
                      onClick={searchSections}
                      selectValue={queryType}
                      setSelectValue={setQueryType}
                    >
                      Search
                    </Multibutton>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>

        <div className="flex items-center justify-start w-full rounded-md p-10 bg-gray-300 col-start-1 col-end-1">
          {/* Suggestions. */}
          <div className="w-full">
            <h1 className="text-2xl font-bold pb-8">Course Suggestions</h1>
            <SuggestionEngineMenu
              termId={termId}
              currentSectionIds={scheduleSectionsInTerm.map((s) => s.id)}
              onGetSections={setSections}
            />
          </div>
        </div>

        <div className="flex items-center justify-start w-full row-start-1 row-end-3 rounded-md px-10 py-10 bg-gray-300 col-start-2 col-end-4">
          <div className="w-full">
            {/* COURSE SEARCH RESULTS */}
            <h1 className="text-2xl font-bold pb-8">Search Results</h1>
            <div
              className="w-full bg-white rounded-md overflow-auto"
              style={{ height: '32rem' }}
            >
              <SectionTable
                sections={courseSections}
                onCourseSelect={addToSchedule}
                selectedSections={scheduleSections}
                actionColTitle="Add"
                actionColText="+"
              />
            </div>
          </div>
        </div>

        <div className="w-full col-start-1 col-end-4 row-start-3 bg-gray-300 rounded-md flex items-center justify-center p-10">
          <div className="w-10/12">
            <h1 className="text-2xl font-bold pb-8">
              My Courses{' '}
              <sup className="text-gray-600">
                {scheduleSectionsInTerm.length}
              </sup>
            </h1>
            <div className="w-full bg-white rounded-md h-64 overflow-auto">
              <SectionTable
                sections={scheduleSectionsInTerm}
                onCourseSelect={removeFromSchedule}
                actionColTitle="Remove"
                actionColText="-"
              />
            </div>
          </div>
        </div>

        <div className="rounded-md bg-gray-300 row-start-4 col-start-1 col-end-4 p-10">
          <Schedule events={scheduleSectionsInTerm} />
        </div>
      </div>
    </div>
  );
}

interface TableSectionRowProps {
  sections: Section[];
  selectedSections?: Section[];
  onCourseSelect: Function;
  actionColTitle: string;
  actionColText: string;
}

function SectionTable(props: TableSectionRowProps) {
  const {
    sections,
    onCourseSelect,
    selectedSections,
    actionColTitle,
    actionColText,
  } = props;

  return (
    <table className="w-full table-auto" id="coursetable">
      <thead className="text-center sticky top-0 bg-white">
        <tr>
          <th>Name</th>
          <th>Section</th>
          <th>Course Code</th>
          <th>Weight</th>
          <th>Meetings</th>
          <th>{actionColTitle}</th>
        </tr>
      </thead>
      <tbody>
        {sections.map((section, index) => (
          <TableSectionRow
            section={section}
            index={index}
            addToSchedule={onCourseSelect}
            selectedSections={selectedSections}
            buttonText={actionColText}
            key={section.id}
          />
        ))}
      </tbody>
    </table>
  );
}

function TableSectionRow(props: any) {
  const { section, index, addToSchedule, selectedSections, buttonText } = props;

  const [expanded, setExpanded] = React.useState(false);

  const meetingsStrings = [];
  const nonExamMeetingCount = section.meetings
    .filter((m: any) => m.type !== 'MeetingType.EXAM')
    .reduce((acc: number, curr: any) => acc + (curr.days?.length || 0), 0);
  if (nonExamMeetingCount > 0)
    meetingsStrings.push(`${nonExamMeetingCount} Weekly`);

  const examMeetingCount = section.meetings
    .filter((m: any) => m.type === 'MeetingType.EXAM')
    .reduce((acc: number, curr: any) => acc + (curr.days?.length || 0), 0);
  if (examMeetingCount > 0)
    meetingsStrings.push(
      `${examMeetingCount} Exam${examMeetingCount > 1 ? 's' : ''}`,
    );

  const meetingsString = meetingsStrings.length
    ? meetingsStrings.join(', ')
    : 'None';

  const onAddCourse = (e: any) => {
    e.stopPropagation();
    addToSchedule(e, index);
  };

  const hasMeetings = examMeetingCount + nonExamMeetingCount > 0;

  const courseAdded = !!selectedSections?.find(
    (s: Section) => s.id === section.id,
  );

  const className = `text-center hover:bg-gray-200 ${
    hasMeetings ? 'cursor-pointer' : ''
  }`;

  return (
    <>
      <tr
        className={className}
        id={String(index)}
        onClick={() => setExpanded(hasMeetings && !expanded)}
      >
        <td>{section.name}</td>
        <td>{section.number}</td>
        <td>{section.faculty + section.code}</td>
        <td>{section.weight}</td>
        <td>
          {meetingsString}{' '}
          {hasMeetings && (
            <button
              type="button"
              className="bg-blue-500 text-white hover:bg-blue-600 font-bold min-height-1 min-width-1 ml-1"
              style={{
                borderRadius: '1000em',
                height: '16px',
                width: '16px',
                fontSize: '10px',
              }}
            >
              {expanded ? '-' : 'i'}
            </button>
          )}
        </td>
        <td>
          <button
            className="px-2 hover:bg-blue-500 hover:text-white rounded-sm text-xl"
            type="submit"
            onClick={onAddCourse}
            disabled={courseAdded}
          >
            {courseAdded ? '' : buttonText}
          </button>
        </td>
      </tr>
      {expanded && (
        <tr className="text-center" id={`${index}-times`}>
          <td colSpan={5}>
            {section.meetings.find((m: any) => m.days)
              ? section.meetings.map((m: any) => (
                  <MeetingRow meeting={m} key={m.id} />
                ))
              : 'No Meetings'}
          </td>
        </tr>
      )}
    </>
  );
}

function MeetingRow(props: any) {
  const { meeting } = props;

  if (
    !meeting.days &&
    !(meeting.start_time !== 'None' && meeting.end_time !== 'None')
  )
    return null;

  return (
    <div>
      {meeting.type.split('.')[1]}
      {!!meeting.days &&
        ` on ${meeting.days
          ?.map((d: string) => d.split('.')[1])
          .join(', ')}`}{' '}
      {!!(meeting.start_time !== 'None' && meeting.end_time !== 'None') &&
        `at ${meeting.start_time}-${meeting.end_time}`}
    </div>
  );
}
