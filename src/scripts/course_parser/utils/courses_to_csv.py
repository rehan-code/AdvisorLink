def course_to_csv(course):
    lines = []
    for section in course["sections"]:
        lines.append(section_to_csv(section, course))

    return '\n'.join(lines)

def section_to_csv(section, course):
    section_level_values = [
        f'{course["faculty"]}*{course["course_code"]}*{section["number"]}',
        course["faculty"],
        "'" + course["course_code"],
        course["name"],
        "'" + course["credits"],
        course["level"],
        section["term"],
        "'" + section["number"],
        section["location"],
        section["instructor"],
        section["capacity"],
        section["enrolled"],
        section["status"]
    ]

    meeting_csvs = [meeting_to_csv(meeting) for meeting in section['meetings']]

    for i in range(1, len(meeting_csvs)):
        meeting_csvs[i] = ','*len(section_level_values) + meeting_csvs[i]

    lines = [
        ','.join([f'"{v}"' for v in section_level_values]),
    ]

    if len(meeting_csvs):
        lines[0] += ',' + meeting_csvs[0]

    if len(meeting_csvs) > 1:
        lines += meeting_csvs[1:]

    return '\n'.join(lines)

def meeting_to_csv(meeting):
    values = [
        meeting['type'],
        meeting['date'],
        meeting['start_date'],
        meeting['end_date'],
        ' '.join(meeting['days']),
        meeting['start_time'],
        meeting['end_time'],
        meeting['building'],
        "'" + meeting['room'] if meeting['room'] else None
    ]

    return ','.join([f'"{value}"' if value else '' for value in values])

def courses_to_csv(courses):
    # header stuff
    headers = ["Course Code (long)", "faculty", "course_code", "name", "credits", "level", "term", "section_number", "location", "instructor", "capacity", "enrolled", "status", "meeting_type", "meeting_date", "meeting_start_date", "meeting_end_date", "meeting_days", "meeting_start_time", "meeting_end_time", "meeting_building", "meeting_room"]

    lines = [','.join([f'"{header}"' for header in headers])]

    for course in courses:
        lines.append(course_to_csv(course))

    return '\n'.join(lines)
