#!/usr/bin/python3

import json
import re
import os

# If importing from main, it is not run as part of the package, use absolute imports.
# If not, then its a part of the package, so import relatively,
if __name__ == "__main__":
    from utils import HTMLNodeParser, courses_to_csv
else:
    from .utils import HTMLNodeParser, courses_to_csv

# Helper function to make paths relative to this script instead of the directory
# from which it was run.
script_directory = os.path.dirname(os.path.abspath(__file__))
def rel_path(path):
    return os.path.join(script_directory, path)

# An array of valid days for class meetings
VALID_DAYS = ['Mon', 'Tues', 'Wed', 'Thur', 'Fri', 'Sat']

# A dictionary of values to find and replace to sanitize meeting data
REPLACEMENT_TABLE = {
    'Distance Education': 'DE',
    'Independent Study': 'IS',
    'Days TBA Days TBA': 'NoDays',
    'Times TBA Times TBA': 'NoTimes, ',
    'Room TBA Room TBA': 'NoRoom',
    'NoTimes,,': 'NoTimes, ',
    'NoTimes, ,': 'NoTimes,'
}

def parse_html(file_name):
    parser = HTMLNodeParser()
    with open(file_name, encoding='utf-8') as file:
        parser.feed(file.read())
    return parser.get_root()

def main():
    print('Parsing HTML...', end='')
    root = parse_html(rel_path('../../config/courses.html'))
    print('done')


    table_body = root.find_element('table', 'summary', 'Sections').child(0)

    course_table = {}

    print('Extracting course information...', end='')
    for row in table_body.children:
        # Only extract information from rows that actually contain course data.
        if row.child(0) and row.child(0).child(0) and row.child(0).child(0) != 'Sections':
            row_id = row.child(0).child(0)
            term = row.find_element('p', 'id', f'WSS_COURSE_SECTIONS_{row_id}').child(0)
            status = row.find_element('p', 'id', f'LIST_VAR1_{row_id}').child(0)
            title_raw = row.find_element('a', 'id', f'SEC_SHORT_TITLE_{row_id}').child(0)
            location = row.find_element('p', 'id', f'SEC_LOCATION_{row_id}').child(0)
            instructor = row.find_element('p', 'id', f'SEC_FACULTY_INFO_{row_id}').child(0)
            capacity_raw = row.find_element('p', 'id', f'LIST_VAR5_{row_id}').child(0)
            course_credits = row.find_element('p', 'id', f'SEC_MIN_CRED_{row_id}').child(0)
            level = row.find_element('p', 'id', f'SEC_ACAD_LEVEL_{row_id}').child(0)

            meeting_input = row.find_element('td', 'class', 'SEC_MEETING_INFO').find_element('input')
            meeting_string = meeting_input.attributes["value"]

            # format meeting string
            for key, value in REPLACEMENT_TABLE.items():
                meeting_string = meeting_string.replace(key, value)

            # additional course title parsing
            title_tokens = title_raw.split()

            # handle invalid course entries
            if len(title_tokens) <= 1:
                continue

            name = " ".join(title_tokens[2:])
            course_code = "*".join(title_tokens[0].split('*')[:2])

            # additional course section parsing
            total_capacity = 0
            enrolled = 0
            if capacity_raw:
                capacity_tokens = capacity_raw.split('/')
                total_capacity = capacity_tokens[1].replace(' ', '')
                enrolled = capacity_tokens[0].replace(' ', '')

            # additional section meeting parsing
            meetings = []
            meeting_string_tokens = meeting_string.split('\n')

            # create list of meetings for each section
            for meeting in meeting_string_tokens:
                meeting_info_tokens = meeting.split()

                # handle invalid meeting entries
                if len(meeting_info_tokens) <= 1:
                    continue

                section_meeting = {}
                section_meeting['type'] = meeting_info_tokens[1]
                section_meeting['date'] = None
                section_meeting['start_date'] = meeting_info_tokens[0].split('-')[0]
                section_meeting['end_date'] = meeting_info_tokens[0].split('-')[1]

                if meeting_info_tokens[1] == 'EXAM':
                    section_meeting['date'] = meeting_info_tokens[0].split('-')[0]
                    section_meeting['start_date'] = None
                    section_meeting['end_date'] = None
                elif meeting_info_tokens[1] == 'IS':
                    section_meeting['type'] = 'Independent Study'
                elif meeting_info_tokens[1] == 'DE':
                    section_meeting['type'] = "Distance Education"
                    section_meeting['start_time'] = None
                    section_meeting['end_time'] = None
                    section_meeting['building'] = None
                    section_meeting['room'] = None
                    section_meeting['days'] = []
                    meetings.append(section_meeting)
                    continue

                # retrieve meeting days
                days = []
                for item in meeting_info_tokens:
                    day = item.replace(',','')
                    if day in VALID_DAYS:
                        days.append(day)
                section_meeting['days'] = days

                if 'NoTimes,' in meeting_info_tokens:
                    section_meeting['start_time'] = None
                    section_meeting['end_time'] = None
                else:
                    time_regex = re.compile('([0-9]|0[0-9]|1[0-9]|2[0-3]):([0-5][0-9])\s*([AaPp][Mm])')
                    meeting_times = [item for item in meeting_info_tokens if time_regex.match(item)]
                    section_meeting['start_time'] = meeting_times[0]
                    section_meeting['end_time'] = meeting_times[1].replace(',','')

                if 'NoRoom' in meeting_info_tokens:
                    section_meeting['building'] = None
                    section_meeting['room'] = None
                else:
                    section_meeting['building'] = meeting_info_tokens[-3].replace(',','')
                    section_meeting['room'] = meeting_info_tokens[-1]

                meetings.append(section_meeting)

            section = {}
            section['term'] = term
            section['number'] = title_tokens[0].split('*')[2]
            section['location'] = location
            section['instructor'] = instructor
            section['capacity'] = total_capacity
            section['enrolled'] = enrolled
            section['status'] = status
            section['meetings'] = meetings

            # insert section in existing course entry
            if course_code in course_table:
                existing_course = course_table.get(course_code)
                existing_course['sections'].append(section)
                continue

            course = {}
            course['name'] = name
            course['faculty'] = title_tokens[0].split('*')[0]
            course['course_code'] = course_code.split('*')[1]
            course['credits'] = course_credits
            course['level'] = level
            course['sections'] = [section]
            course_table[course_code] = course

    print('done')
    output = {'courses': list(course_table.values())}

    print('Saving course information to courses.json...', end='')
    with open(rel_path('../../config/courses.json'), 'w', encoding='utf-8') as file:
        json.dump(output, file, ensure_ascii=False, indent=2)
    print('done')

    print('Saving course information to courses.csv...', end='')
    with open(rel_path('../../config/courses.csv'), 'w', encoding='utf-8') as file:
        courses_csv = courses_to_csv(course_table.values())
        file.write(courses_csv)
    print('done')

if __name__ == "__main__":
    main()
