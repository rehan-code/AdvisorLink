import os
import json

if __name__ == "__main__":
    from utils import Faculty, Term, Course, Section, Meeting
else:
    from .utils import Faculty, Term, Course, Section, Meeting

# Helper function to make paths relative to this script instead of the directory
# from which it was run.
script_directory = os.path.dirname(os.path.abspath(__file__))
def rel_path(path):
    return os.path.join(script_directory, path)


# Converts a string to CONSTANT_CASE.
def constant_case(string):
    return string.strip().upper().replace(' ', '_')

print('Opening courses.json ...')
with open(rel_path('../../config/courses.json'), 'r', encoding='utf-8') as file:
    courses_json = json.load(file)

faculties = {}
terms = {}
courses = []
sections = []
meetings = []

print('Parsing courses ...')
for courseJson in courses_json['courses']:
    # Pull out a new faculty if it has not been created yet.
    if courseJson['faculty'] not in faculties:
        faculties[courseJson['faculty']] = Faculty(courseJson['faculty'])
    faculty = faculties[courseJson['faculty']]

    # Create and append the course.
    course = Course(
        courseJson['name'],
        faculty.id,
        courseJson['course_code'],
        float(courseJson['credits']),
        courseJson['level'].upper()
    )
    courses.append(course)

    # Create the term, section, and meeting entities from the section level.
    for sectionJson in courseJson['sections']:
        # Pull out a new term if it has not been created yet.
        if sectionJson['term']:
            meeting_with_term_dates = next((m for m in sectionJson['meetings'] if m['start_date']), None)
            if meeting_with_term_dates:
                terms[sectionJson['term']] = Term(sectionJson['term'], meeting_with_term_dates['start_date'].replace('/', ','), meeting_with_term_dates['end_date'].replace('/', ','))
        term = terms[sectionJson['term']]

        # Create and append the section.
        section = Section(
            sectionJson['number'],
            course.id,
            term.id,
            sectionJson['location'],
            sectionJson['instructor'],
            int(sectionJson['capacity']),
            int(sectionJson['enrolled']),
            sectionJson['status'].upper()
        )
        sections.append(section)

        # Create the meeting entities.
        for index,meetingJson in enumerate(sectionJson['meetings']):
            if meetingJson['type'] != 'None':
                meeting = Meeting(
                    section.id,
                    constant_case(meetingJson['type']),
                    meetingJson['date'].replace('/', '-') if meetingJson['date'] else None,
                    [i.upper() for i in meetingJson['days']] if meetingJson['days'] else None,
                    meetingJson['start_time'].replace('AM', ' AM').replace('PM', ' PM') if meetingJson['start_time'] else None,
                    meetingJson['end_time'].replace('AM', ' AM').replace('PM', ' PM') if meetingJson['end_time'] else None,
                    meetingJson['building'],
                    meetingJson['room'],
                    index
                )
                meetings.append(meeting)

print('Generating script ...')
statements = []
statements.append('-- Faculties')
statements.extend([i.getInsert() for i in faculties.values()])
statements.append('\n-- Terms')
statements.extend([i.getInsert() for i in terms.values()])
statements.append('\n-- Courses')
statements.extend([i.getInsert() for i in courses])
statements.append('\n-- Course Sections')
statements.extend([i.getInsert() for i in sections])
statements.append('\n-- Meetings')
statements.extend([i.getInsert() for i in meetings])
seeding_script = '\n'.join(statements)

with open(rel_path('../seeding_script.sql'), 'w') as fp:
    fp.write(seeding_script)

print('Done !')
