from app import app, searchUtil
from flask import request
import json
from db import db,models
import re

# Example
@app.route('/api')
def ding():
    return json.dumps({'message': 'Ding!'})

# Get all the sections
@app.route('/api/sections', methods = ['GET'])
def getSectionsHandler():
    # Query for the databases with appropriate joins/selects.
    query = models.CourseSection.query \
        .select_from(models.CourseSection).join(models.Course) \
        .join(models.Faculty) \
        .join(models.Term) \
        .join(models.Meeting) \
        .add_columns(models.Course, models.Faculty, models.Term, models.Meeting)

    # If a query was provided in the request, add the condition to the query.
    if 'query' in request.args:
        tsqueryArgs = ' & '.join(re.findall(r'\w+', request.args.get('query')))
        query = query.where(db.text(f"ts @@ to_tsquery('english', '{tsqueryArgs}')"))

    # Execute the constructed query.
    queryResults = query.all()

    # Build out the sections with meetings grouped and entities attached.
    sectionMap = {}
    for rowSection,course,faculty,term,meeting in queryResults:
        if rowSection.id not in sectionMap:
            sectionMap[rowSection.id] = rowSection
            rowSection.meetings = []
        section = sectionMap[rowSection.id]
        section.course = course
        course.faculty = faculty
        section.meetings.append(meeting)
        section.term = term
    sections = sectionMap.values()

    print(sections)

    return json.dumps({'sections' : [s.toClientJson() for s in sections]})
