import React, { useState } from "react";
import SectionList from "../components/SectionList";

const Home = () => {
  const [query, setQuery] = useState<string>("");
  const [hasSearched, setHasSearched] = useState(false);
  const [sections, setSections] = React.useState<any[]>([]);
  const [sectionsLoading, setSectionsLoading] = React.useState(false);

  const buttonHandler = async (event: React.MouseEvent<HTMLButtonElement>) => {
    event.preventDefault();
    setSectionsLoading(true);
    const res = await fetch("/api/sections");
    setSections((await res.json()).sections);
    setHasSearched(true);
    setSectionsLoading(false);
  };

  const formSubmitHandler = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    if (!query) return;
    setSectionsLoading(true);
    const res = await fetch("/api/sections?" + new URLSearchParams({ query }));
    setSections((await res.json()).sections);
    setHasSearched(true);
    setSectionsLoading(false);
  };

  return (
    <div className="hero">
      <div className="grid gap-6 mb-6 md:grid-cols-1 bg-black w-full justify-items-center">
        <div className="p-12 text-white">
          <h1 className="text-6xl font-bold">Search for Sections</h1>
          <form onSubmit={formSubmitHandler}>
            <div className="h-8">
              <input
                type="text"
                id="searchQuery"
                className="p-5 bg-gray-50 h-full border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 flex"
                placeholder="Search"
                value={query}
                onChange={(e) => setQuery(e.target.value)}
              ></input>
            </div>
            <div className="p-3"></div>
            <div className="grid md:grid-cols-2 w-full gap-6 h-10">
              <button
                type="submit"
                className="text-black bg-white hover:bg-gray-300 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
              >
                Find Sections
              </button>
              <button
                type="submit"
                onClick={buttonHandler}
                className="text-black bg-white hover:bg-gray-300 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
              >
                List All Courses
              </button>
            </div>
          </form>
        </div>
        <div className="p-12 w-full h-full">
          {hasSearched && (
            <SectionList sections={sections} loading={sectionsLoading} />
          )}
        </div>
      </div>
    </div>
  );
};

export default Home;
