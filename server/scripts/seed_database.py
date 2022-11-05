from flask import Flask, request
import os
import sys
import json

# Helper function to make paths relative to this script instead of the directory
# from which it was run.
script_directory = os.path.dirname(os.path.abspath(__file__))
def rel_path(path):
    return os.path.join(script_directory, path)
sys.path.insert(0, rel_path('..'))
from db import db,models

# Converts a string to CONSTANT_CASE.
def constant_case(string):
    return string.strip().upper().replace(' ', '_')

# Create a dummy app to communicate with the database.
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:Fall2022CIS3760@localhost:5432/advisorlink'
db.init_app(app)

# Load the database schema
schemaFile = open(rel_path("../db/tables.sql"), "r")
schemaSQL = schemaFile.read()
schemaFile.close()

with app.app_context():
    print('Opening courses.json ...')
    with open(rel_path('../library/config/courses.json'), 'r', encoding='utf-8') as file:
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
            faculties[courseJson['faculty']] = models.Faculty(courseJson['faculty'])
        faculty = faculties[courseJson['faculty']]

        # Create and append the course.
        course = models.Course(
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
                    terms[sectionJson['term']] = models.Term(sectionJson['term'], meeting_with_term_dates['start_date'].replace('/', ','), meeting_with_term_dates['end_date'].replace('/', ','))
            term = terms[sectionJson['term']]

            # Create and append the section.
            section = models.CourseSection(
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
                    meeting = models.Meeting(
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

    print('Clearing DB and syncing schema ...')
    db.session.execute(schemaSQL)

    print('Saving entities ...')
    db.session.add_all(faculties.values())
    db.session.commit()
    db.session.add_all(terms.values())
    db.session.commit()
    db.session.add_all(courses)
    db.session.commit()
    db.session.add_all(sections)
    db.session.commit()
    db.session.add_all(meetings)
    db.session.commit()

    print('Done !')
