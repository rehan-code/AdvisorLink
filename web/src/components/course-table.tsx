import React from "react";

interface CourseTableProps {
  sections: any[];
  loading?: boolean;
}

export const CourseTable = (props: CourseTableProps) => {
  const { sections, loading } = props;

  return (
    <div style={{ color: "white", maxHeight: "20vh", overflowY: "scroll" }}>
      <h2>Results</h2>
      {loading
        ? "Searching ..."
        : sections.length === 0
        ? "No Results Found"
        : sections.map((s) => <CourseTableRow section={s} key={s.id} />)}
    </div>
  );
};

interface CourseTableRowProps {
  section: any;
}

const CourseTableRow = (props: { section: any }) => {
  return <div>{props.section.name}</div>;
};
