import React, { ChangeEvent, useCallback, useState } from 'react';
import Schedule from './Schedule';

const queryRegex = /(name|code|faculty|credits|level|term|location|building|instructor|year):\s*([A-Za-z0-9]+)/g; // Save for future reference 

export interface Section {
	name: string,
	code: string,
	number: string,
	faculty: string,
	weight: number,
	instructor: string,
	term: string,
	location: string,
	capacity: number,
	enrolled: number,
	meetings: [
		{
			building: string,
			date: string,
			days: string[],
			start_time: string,
			end_time: string,
			room: string,
			type: string
		}
	]
}


export default function CalendarComponent() {
	const [filters, setFilters] = useState<string[] | undefined>([]); // Save for future reference
	const [query, setQuery] = useState<string | string[][]>("");
	const [courseSections, setSections] = useState<Section[]>([]);

	// Stores the schedule to use with FullCalendar
	const [scheduleSections, setScheduleSections] = useState<Section[]>([]);

	// Break search field into queryable strings
	const updateFilters = (event: ChangeEvent<HTMLInputElement>) => {
		event.preventDefault();

		let target = event.target as HTMLInputElement;
		let queryString = target.value;

		let queries = queryString.match(queryRegex);

		let matches = queries?.map((element) => {
			return element;
		});
		setFilters(matches);
	}

	const updateQuery = (event: ChangeEvent<HTMLInputElement>) => {
		event.preventDefault();

		let target = event.target as HTMLInputElement;
		setQuery(target.value);
	}

	const searchSections = async (event: React.MouseEvent<HTMLButtonElement> | React.FormEvent<HTMLFormElement>) => {
		event.preventDefault();

		let searchResults = await fetch("/api/sections?" + new URLSearchParams(`query=${query}`));
		let { sections } = await searchResults.json();
		setSections(sections);
	}

	// Memoize previous results
	const renderSearchTable = useCallback(() => {

		const addToSchedule = (event: React.MouseEvent<HTMLButtonElement>, index: number) => {
			event.preventDefault();
			let section = courseSections[index];

			let tempSchedule = [...scheduleSections];
			tempSchedule.push(section);

			setScheduleSections(tempSchedule);
		}

		return (
			<table className="w-full table-auto" id="coursetable" >
				<thead className="text-center sticky top-0 bg-white">
					<tr>
						<th>Name</th>
						<th>Section</th>
						<th>Code</th>
						<th>Weight</th>
						<th>Add</th>
					</tr>
				</thead>
				<tbody>
					{courseSections.map((section, index) => {
						return <tr className="text-center" id={String(index)}>
							<td>{section.name}</td>
							<td>{section.number}</td>
							<td>{section.faculty + section.code}</td>
							<td>{section.weight}</td>
							<td><button className="px-2 hover:bg-blue-500 hover:text-white rounded-sm text-xl" onClick={(event) => addToSchedule(event, index)}>+</button></td>
						</tr>
					})}
				</tbody>
			</table>
		)
	}, [courseSections, scheduleSections])

	const renderCourseTable = useCallback(() => {

		const removeFromSchedule = (event: React.MouseEvent<HTMLButtonElement>, index: number) => {
			event.preventDefault();

			let tempSchedule = [...scheduleSections];
			tempSchedule.splice(index, 1);

			setScheduleSections(tempSchedule);
		}

		return (
			<table className="w-full table-auto">
				<thead className="text-center sticky top-0 bg-white">
					<tr>
						<th>Name</th>
						<th>Section</th>
						<th>Code</th>
						<th>Weight</th>
						<th>Remove</th>
					</tr>
				</thead>
				<tbody>
					{scheduleSections.map((section, index) => {
						return <tr className="text-center" id={String(index)}>
							<td>{section.name}</td>
							<td>{section.number}</td>
							<td>{section.faculty + section.code}</td>
							<td>{section.weight}</td>
							<td><button className="px-2 hover:bg-blue-500 hover:text-white rounded-sm text-xl" onClick={(event) => removeFromSchedule(event, index)}>-</button></td>
						</tr>
					})}
				</tbody>
			</table>
		)
	}, [scheduleSections])

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
										onChange={(event: ChangeEvent<HTMLInputElement>) => updateQuery(event)}
									/>
									<div className="flex justify-evenly items-center p-4">
										<button className="py-4 px-8 bg-blue-500 rounded-md text-white hover:bg-blue-800 font-bold" onClick={searchSections}>
											Search
										</button>
									</div>
								</form>
							</div>
						</div>
					</div>
				</div>
				<div className="flex items-center justify-start w-full rounded-md px-10 py-10 bg-gray-300 col-start-2 col-end-4">
					<div className="w-full">
						{/* COURSE SEARCH RESULTS*/}
						<h1 className="text-2xl font-bold pb-8">Search Results</h1>
						<div className="w-full bg-white rounded-md h-64 overflow-auto">
							{renderSearchTable()}
						</div>
					</div>
				</div>
			</div>
			<div className="flex items-center justify-start w-8/12 rounded-md px-10 py-10 bg-gray-300">
				<div className="w-full">
					<h1 className="text-2xl font-bold pb-8">My Courses</h1>
					<div className="w-full bg-white rounded-md h-64 overflow-auto">
						{renderCourseTable()}
					</div>
				</div>
			</div>
			<div className="p-40">
				<Schedule events={scheduleSections} />
			</div>
		</div>
	);
}
