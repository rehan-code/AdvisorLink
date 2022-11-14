import React from 'react';

export interface MultibuttonProps {
  onClick?: any;
  children?: any;
  type?: any;
  setSelectValue?: any;
  selectValue?: any;
}

export function Multibutton(props: MultibuttonProps) {
  const { onClick, type, children } = props;
  const { setSelectValue, selectValue } = props;

  return (
    <>
      <select
        className="py-4 px-8 bg-blue-800 rounded-md text-white hover:bg-blue-900 font-bold"
        style={{
          color: 'white',
          fontWeight: 'bold',
          textAlign: 'center',
        }}
        onClick={(e: any) => {
          e.preventDefault();
          e.stopPropagation();
        }}
        onChange={(e) => setSelectValue(e.target.value)}
        value={selectValue}
      >
        <option value="all">Search</option>
        <option value="title">Search by Course Name</option>
        <option value="code">Search by Course Code</option>
        <option value="instructor">Search by Instructor</option>
      </select>

      <button
        className="py-4 px-8 bg-blue-500 rounded-md text-white hover:bg-blue-600 font-bold"
        type="submit"
        onClick={onClick}
      >
        {' →'}
      </button>
    </>
  );
}
