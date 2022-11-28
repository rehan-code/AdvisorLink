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


def getSectionsSearchQuery(queryString=None, queryType=None, termId=None, ids=None):
    # Query for the databases with appropriate joins/selects.
    query = models.CourseSection.query \
        .select_from(models.CourseSection).join(models.Course) \
        .join(models.Faculty) \
        .join(models.Term) \
        .join(models.Meeting, isouter=True) \
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

    # If section IDs were specified, add the condition to the query.
    if ids:
        query = query.where(models.CourseSection.id.in_(ids))

    return query


def attachSectionSearchQueryResults(results):
    sectionMap = {}
    for rowSection, course, faculty, term, meeting in results:
        if rowSection.id not in sectionMap:
            sectionMap[rowSection.id] = rowSection
            rowSection.meetings = []
        section = sectionMap[rowSection.id]
        section.course = course
        course.faculty = faculty
        if (meeting):
            section.meetings.append(meeting)
        section.term = term
    sections = sectionMap.values()

    return list(sections)


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
    sections = attachSectionSearchQueryResults(queryResults)

    return json.dumps({'sections': [s.toClientJson() for s in sections]})


@app.route('/api/terms', methods=['GET'])
def getTermsHandler():
    terms = models.Term.query.all()
    return json.dumps({'terms': [term.toClientJson() for term in terms]})


def uniqueByField(lan, field):
    d = {}
    for e in lan:
        if getattr(e, field) not in d:
            d[getattr(e, field)] = e
    return list(d.values())


@app.route('/api/suggest-sections', methods=['GET'])
def getSuggestSectionsHandler():
    # Get the courses and meetings currently being taken.
    courseSectionIds = request.args.getlist('courseSectionIds') if 'courseSectionIds' in request.args else []
    currentSectionsAndMeetings = models.CourseSection.query \
        .select_from(models.CourseSection) \
        .join(models.Meeting, isouter=True) \
        .add_columns(models.Meeting) \
        .where(models.CourseSection.id.in_(courseSectionIds), models.Meeting.type != 'EXAM') \
        .all()
    currentSections = uniqueByField([r[0] for r in currentSectionsAndMeetings], 'id')
    currentMeetings = [r[1] for r in currentSectionsAndMeetings]
    currentCourseIds = [section.course_id for section in currentSections]

    # Get all the blocks of time that meetings cannot be within.
    timeBlocks = []
    for m in currentMeetings:
        if m.days:
            for d in m.days:
                timeBlocks.append((str(d).split('.')[1], str(m.start_time), str(m.end_time)))

    explicitBlockedTimes = request.args.getlist('blockedTimes') if 'blockedTimes' in request.args else []
    for i in explicitBlockedTimes:
        day, startTime, endTime = i.split('-')
        timeBlocks.append((day, startTime, endTime))

    # Variables for looping,
    nDesiredCourses = len(courseSectionIds) + 1 if len(courseSectionIds) >= 5 else 5
    noResults = False
    newSections = []
    termId = request.args.get('termId')

    while len(courseSectionIds) < nDesiredCourses and not noResults:
        # Query the database for courses with no conflicting times.
        queryString = \
            "SELECT course_section.id FROM course_section LEFT JOIN meeting ON (meeting.course_section_id = course_section.id AND meeting.type <> 'EXAM' AND " + \
            ("(" + " OR ".join([f"('{tb[0]}' = ANY(meeting.days) AND start_time < '{tb[2]}' AND end_time  > '{tb[1]}')" for tb in timeBlocks]) + ")" if len(timeBlocks) > 0 else "FALSE") + \
            f") WHERE meeting.id IS NULL AND course_section.term_id='{termId}' " + \
            (f""" AND course_section.course_id NOT IN ({','.join([f"'{id}'" for id in currentCourseIds])})""" if len(currentCourseIds) else '') + \
            " ORDER BY RANDOM() LIMIT 1;"
        results = db.engine.execute(queryString).mappings().all()

        if len(results) == 0:
            noResults = True
        else:
            # Fetch all the course data for the course being recommended.
            newCourseId = str(results[0]['id'])
            newCourseQueryResults = getSectionsSearchQuery(None, None, None, [newCourseId]).all()
            newCourse = attachSectionSearchQueryResults(newCourseQueryResults)[0]

            # Update the list of new courses, the list of current section IDs, and the blocked times.
            newSections.append(newCourse)
            courseSectionIds.append(newCourse.id)
            currentCourseIds.append(newCourse.course_id)
            for m in newCourse.meetings:
                if m.days:
                    for d in m.days:
                        timeBlocks.append((str(d).split('.')[1], str(m.start_time), str(m.end_time)))

    return json.dumps({'sections': [s.toClientJson() for s in newSections]})
