import { ChangeEvent, useState } from 'react';
import FullCalendar from '@fullcalendar/react';
import timeGridPlugin from '@fullcalendar/timegrid';

const queryRegex = /(name|code|faculty|credits|level|term|location|building|instructor|year):([A-Za-z0-9]+)/g;

export default function CalendarComponent() {
    const [filters, setFilters] = useState<string[] | undefined>([]);

    // Break search field into queryable strings
    const updateFilters = (event: ChangeEvent<HTMLInputElement>) => {
        let target = event.target as HTMLInputElement;
        let queryString = target.value;

        let queries = queryString.match(queryRegex);

        let matches = queries?.map((element) => {
            return element;
        });
        setFilters(matches);
    }

    const searchSections = async () => {
        let query : {[key: string]: any} = {}

        // Generate a request body
        if (filters) {
            for(let filter of filters) {
                let tokens = filter.split(":");
                query[`${tokens[0]}`] = tokens[1];
            }
        }

        let results = await fetch("http://localhost:5000/api/sections/search", {
            method: "POST",
            body: JSON.stringify({query})
        });

        console.log(results);
    }

	return (
		<div className="w-full flex flex-col justify-center items-center">
			<div className="grid grid-cols-2 gap-12 w-full p-40">
				<div className="flex items-center justify-start w-full rounded-md px-20 py-10 bg-gray-300">
					<div className="w-full">    
                        {/* COURSE SEARCHING */}
						<h1 className="text-2xl font-bold pb-8">Course Search</h1>
						<div className="flex gap-3 w-full items-center">
							<div className="flex flex-col items-center justify-center w-full">
								<input
									type="text"
									className="text-lg p-4 w-full rounded-md"
									placeholder="faculty:ACCT code:1220 ..."
									onChange={(e: ChangeEvent<HTMLInputElement>) => updateFilters(e)}
								/>
								<div className="flex justify-evenly items-center p-2">
									<button className="py-4 px-8 bg-blue-500 rounded-md text-white hover:bg-blue-800 font-bold" onClick={searchSections}>
										Search
									</button>
								</div>
							</div>
						</div>
					</div>
				</div>
				<div className="flex items-center justify-start w-full rounded-md px-20 py-10 bg-gray-300">
					<div className="w-full">
                        {/* COURSE SEARCH RESULTS*/}
						<h1 className="text-2xl font-bold pb-8">Search Results</h1>
                        <div className='w-full bg-white rounded-md'>
                            <table className='w-full'>
                                <tr>
                                    <th colSpan={2}>Name</th>
                                    <th>Time</th>
                                    <th>Code</th>
                                    <th>Weight</th>
                                </tr>
                            </table>
                        </div>
					</div>
				</div>
			</div>
			<div className="p-40">
				<FullCalendar
					plugins={[ timeGridPlugin ]}
					headerToolbar={{
						left: 'today',
						center: 'title',
						right: 'prev,next'
					}}
					initialView="timeGridWeek"
					weekends={true}
					events={[
						{
							title: 'CIS3210',
							startRecurrence: '2022-09-07',
							endRecurrence: '2022-12-07',
							daysOfWeek: [ 2, 4 ],
							startTime: '08:30',
							endTime: '10:30'
						},
						{
							title: 'CIS1500',
							startRecurrence: '2022-09-07',
							endRecurrence: '2022-12-07',
							daysOfWeek: [ 1, 3, 5 ],
							startTime: '12:30',
							endTime: '14:30',
							color: '#000'
						}
					]}
					slotMinTime="07:00:00"
					slotMaxTime="23:00:00"
					allDaySlot={false}
					contentHeight="auto"
				/>
			</div>
		</div>
	);
}
