from app import app
from flask import request
import json
from db import db, models
import re


# Test route
@app.route('/api')
def ding():
    return json.dumps({'message': 'Ding!'})


SECTIONS_SEARCH_QUERY_TYPES = {
    # format: <input>: [<table>, <column>, <sort by SIMILARITY>]
    'all': ['course_section', 'search_all_tags', True],
    'title': ['course', 'name', True],
    'code': ['course_section', 'search_course_code', True],
    'instructor': ['course_section', 'instructor', True]
}


def getSectionsSearchQuery(queryString=None, queryType=None, termId=None):
    # Query for the databases with appropriate joins/selects.
    query = models.CourseSection.query \
        .select_from(models.CourseSection).join(models.Course) \
        .join(models.Faculty) \
        .join(models.Term) \
        .join(models.Meeting) \
        .add_columns(models.Course, models.Faculty, models.Term, models.Meeting)

    # If a query was provided in the request, add the condition to the query.
    if queryString:
        [queryTable, queryColumn, sortBySimilarity] = SECTIONS_SEARCH_QUERY_TYPES[queryType or 'all']
        tsqueryArgs = ' | '.join(re.findall(r'\w+', queryString))
        query = query.where(db.text(f"{queryTable}.{queryColumn} @@ to_tsquery('english', '{tsqueryArgs}')"))

        # Add the order by condition based on the configuration.
        orderBy = [models.Faculty.code, models.Course.course_code, models.CourseSection.number]
        if (sortBySimilarity):
            orderBy.insert(0, db.text(f"SIMILARITY({queryTable}.{queryColumn}, '{tsqueryArgs}') DESC"))
        query = query.order_by(*orderBy)

    # If a term id was providede in the request, add the condition to the query.
    if termId:
        query = query.where(db.text(f"course_section.term_id = '{termId}'"))

    return query

# Get all the sections


@app.route('/api/sections', methods=['GET'])
def getSectionsHandler():
    # Execute the constructed query.
    query = getSectionsSearchQuery(
        request.args.get('query') if 'query' in request.args else None,
        request.args.get('queryType') if 'queryType' in request.args else None,
        request.args.get('termId') if 'termId' in request.args else None
    )
    queryResults = query.all()

    # Build out the sections with meetings grouped and entities attached.
    sectionMap = {}
    for rowSection, course, faculty, term, meeting in queryResults:
        if rowSection.id not in sectionMap:
            sectionMap[rowSection.id] = rowSection
            rowSection.meetings = []
        section = sectionMap[rowSection.id]
        section.course = course
        course.faculty = faculty
        section.meetings.append(meeting)
        section.term = term
    sections = sectionMap.values()

    return json.dumps({'sections': [s.toClientJson() for s in sections]})


@app.route('/api/terms', methods=['GET'])
def getTermsHandler():
    terms = models.Term.query.all()
    return json.dumps({'terms': [term.toClientJson() for term in terms]})
