/* eslint-disable react/require-default-props */
import React from 'react';

// eslint-disable-next-line react/no-unused-prop-types
function SectionRow(props: { data: any; key: string }) {
  return (
    <li className="p-4 m-4 border-slate-50 border rounded-md">
      <div className="flex flex-row">
        <div className="flex-1">
          {`${props.data.faculty}*${props.data.code}*${props.data.number}`}
        </div>
        <div className="flex-1">
          <p>{props.data.name}</p>
          <p>{props.data.term}</p>
        </div>
        <div className="flex-1">{props.data.instructor}</div>
      </div>
    </li>
  );
}

export default function SectionList(props: {
  sections: any[];
  loading?: boolean;
}) {
  return (
    <div className="text-white">
      <h1 className="text-6xl font-bold">Results</h1>
      <div
        className="container overflow-y-scroll mx-auto"
        style={{ maxHeight: '30vh' }}
      >
        {props.loading ? (
          'Searching...'
        ) : props.sections.length === 0 ? (
          'No Results Found'
        ) : (
          <ul>
            {props.sections.map((section) => (
              <SectionRow
                data={section}
                key={section.faculty + section.code + section.number}
              />
            ))}
          </ul>
        )}
      </div>
    </div>
  );
}
