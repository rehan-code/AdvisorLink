/* eslint-disable no-restricted-syntax */

import React from 'react';

export interface SuggestionEngineMenuProps {
  currentSectionIds?: string[];
  termId: string;
  onGetSections?: Function;
}

export function SuggestionEngineMenu(props: SuggestionEngineMenuProps) {
  const { termId, onGetSections } = props;
  const currentSectionIds = props.currentSectionIds ?? [];
  const [blockedTimes, setBlockedTimes] = React.useState<string[]>([]);
  const [customBlockedTimes, setCustomBlockedTimes] = React.useState<string[]>(
    [],
  );
  const customMode = blockedTimes[0] === 'CUSTOM';

  const onSuggestSections = async () => {
    const params = new URLSearchParams();
    for (const id of currentSectionIds) params.append('courseSectionIds', id);
    const activeBlockedTimes = customMode ? customBlockedTimes : blockedTimes;
    for (const bt of activeBlockedTimes) params.append('blockedTimes', bt);
    params.append('termId', termId);

    const searchResults = await fetch(`/api/suggest-sections?${params}`);
    const resultJson = await searchResults.json();

    if (resultJson.sections) onGetSections?.(resultJson.sections);
  };

  return (
    <>
      <button
        className="py-4 px-8 bg-blue-500 rounded-md text-white hover:bg-blue-600 font-bold"
        type="button"
        onClick={onSuggestSections}
      >
        Suggest Sections →
      </button>

      <h2 className="text-xl font-bold mt-6">Filters</h2>

      <div className="grid grid-cols-2 auto-rows-min gap-0 w-full">
        <PresetSelector
          label="Any"
          timestrings={[]}
          state={[blockedTimes, setBlockedTimes]}
        />
        <PresetSelector
          label="Tuesdays/Thursdays Off"
          timestrings={['TUES-00:00:00-23:59:59', 'THUR-00:00:00-23:59:59']}
          state={[blockedTimes, setBlockedTimes]}
        />
        <PresetSelector
          label="No Mornings"
          timestrings={[
            'MON-00:00:00-12:00:00',
            'TUES-00:00:00-12:00:00',
            'WED-00:00:00-12:00:00',
            'THUR-00:00:00-12:00:00',
            'FRI-00:00:00-12:00:00',
          ]}
          state={[blockedTimes, setBlockedTimes]}
        />
        <PresetSelector
          label="Custom"
          timestrings={['CUSTOM']}
          state={[blockedTimes, setBlockedTimes]}
        />
      </div>

      {customMode && (
        <div className="grid grid-cols-4 auto-rows-min gap-y-1 w-full mt-2 px-5">
          {[
            ['MON', 'Monday'],
            ['TUES', 'Tuesday'],
            ['WED', 'Wednesday'],
            ['THUR', 'Thursday'],
            ['FRI', 'Friday'],
          ].map(([day, label]) => (
            <DaySelectorRow
              day={day}
              label={label}
              state={[customBlockedTimes, setCustomBlockedTimes]}
            />
          ))}
        </div>
      )}
    </>
  );
}

function DaySelectorRow(props: { day: string; label: string; state: any }) {
  const { day, label, state } = props;
  return (
    <>
      <p className="font-bold mt-2">{label}</p>
      <TimeOfDaySelector
        day={day}
        label="Morning"
        timestring="00:00:00-12:00:00"
        state={state}
        style={{ borderRadius: '0.375rem 0 0 0.375rem' }}
      />
      <TimeOfDaySelector
        day={day}
        label="Afternoon"
        timestring="12:00:00-18:00:00"
        state={state}
      />
      <TimeOfDaySelector
        day={day}
        label="Evening"
        timestring="18:00:00-23:59:59"
        state={state}
        style={{ borderRadius: '0 0.375rem 0.375rem 0' }}
      />
    </>
  );
}

function PresetSelector(props: {
  label: string;
  timestrings: string[];
  state: any;
}) {
  const { label, timestrings, state } = props;
  const [blockedTimes, setBlockedTimes] = state;
  const selected = blockedTimes.join(',') === timestrings.join(',');

  const select = () => {
    setBlockedTimes([...timestrings]);
  };

  const className = `text-white p-2 rounded-md m-1 ${
    selected ? 'bg-blue-500' : 'bg-blue-800 hover:bg-blue-900'
  }`;

  return (
    <button type="button" className={className} onClick={select}>
      {label}
    </button>
  );
}

function TimeOfDaySelector(props: {
  day: string;
  label: string;
  timestring: string;
  state: any;
  style?: any;
}) {
  const { day, label, timestring, state, style } = props;
  const [blockedTimes, setBlockedTimes] = state;
  const key = `${day}-${timestring}`;
  const blocked = !!blockedTimes.find((bt: string) => bt === key);

  const toggle = () => {
    if (blocked)
      setBlockedTimes(blockedTimes.filter((bt: string) => bt !== key));
    else setBlockedTimes([...blockedTimes, key]);
  };

  return (
    <button
      type="button"
      className="text-white p-2 text-large"
      style={{
        backgroundColor: blocked
          ? 'rgba(40, 129, 202, 1)'
          : 'rgba(66, 153, 225, 1)',
        ...(style ?? {}),
      }}
      onClick={toggle}
    >
      {label}
    </button>
  );
}
