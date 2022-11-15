import React, { ChangeEvent, useState, useEffect } from 'react';
import { useCookies } from 'react-cookie';
import Schedule from './Schedule';
import { Multibutton } from './Multibutton';
import { TermSelector } from './TermSelector';

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

  // Memoize previous results
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
      <div className="grid grid-cols-3 gap-12 w-full px-16 py-20">
        <div className="flex items-center justify-start w-full rounded-md px-10 py-10 bg-gray-300 col-start-1 col-end-1">
          <div className="w-full">
            {/* COURSE SEARCHING */}
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
                  <TermSelector setValue={setTermId} />
                  <div className="flex justify-evenly items-center p-4">
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
        <div className="flex items-center justify-start w-full rounded-md px-10 py-10 bg-gray-300 col-start-2 col-end-4">
          <div className="w-full">
            {/* COURSE SEARCH RESULTS */}
            <h1 className="text-2xl font-bold pb-8">Search Results</h1>
            <div className="w-full bg-white rounded-md h-64 overflow-auto">
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
      </div>
      <div className="flex items-center justify-start w-8/12 rounded-md px-10 py-10 bg-gray-300">
        <div className="w-full">
          <h1 className="text-2xl font-bold pb-8">My Courses</h1>
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
      <div className="m-20 p-10 rounded-md bg-gray-300">
        <Schedule events={scheduleSectionsInTerm} />
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
          <th>Code</th>
          <th>Weight</th>
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

  const onAddCourse = (e: any) => {
    e.stopPropagation();
    addToSchedule(e, index);
  };

  const courseAdded = !!selectedSections?.find(
    (s: Section) => s.id === section.id,
  );

  return (
    <>
      <tr
        className="text-center"
        id={String(index)}
        onClick={() => setExpanded(!expanded)}
      >
        <td>{section.name}</td>
        <td>{section.number}</td>
        <td>{section.faculty + section.code}</td>
        <td>{section.weight}</td>
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
