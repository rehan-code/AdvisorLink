import json

from .section_search_map import SectionSearchMap, SearchOptionEnum
from .course import Course
from .section import Section
from .meeting import Meeting

# A class to parse the course JSON file
class CourseJsonParser():
    def __init__(self):
        pass

    # This method parses the JSON file and returns a hashmap later used to search for sections
    def parse_json(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)

        section_map = SectionSearchMap()
        for course_data in data['courses']:
            course = self.__parse_course_data(course_data)

            for section_data in course_data['sections']:
                section = self.__parse_section_data(section_data)
                section.course = course

                section_map.add_section(SearchOptionEnum.CODE, course_data['faculty'] + course_data['course_code'], section)
                section_map.add_section(SearchOptionEnum.FACULTY, course_data['faculty'], section)
                section_map.add_section(SearchOptionEnum.CREDITS, course_data['credits'], section)
                section_map.add_section(SearchOptionEnum.INSTRUCTOR, section_data['instructor'], section)
                section_map.add_section(SearchOptionEnum.NAME, course_data['name'], section)
                section_map.add_section(SearchOptionEnum.TERM, section_data['term'], section)
                section_map.add_section(SearchOptionEnum.SECTION, section_data['number'], section)
                section_map.add_section(SearchOptionEnum.LEVEL, course_data['level'], section)
                section_map.add_section(SearchOptionEnum.LOCATION, section_data['location'], section)
                section_map.add_section(SearchOptionEnum.YEAR, course_data['course_code'][0], section)

                for meeting_data in section_data['meetings']:
                    meeting = self.__parse_meeting_data(meeting_data)

                    section_map.add_section(SearchOptionEnum.BUILDING, meeting_data['building'], section)

                    if meeting_data['type'] == 'EXAM':
                        section_map.add_section(SearchOptionEnum.EXAM, meeting_data['date'], section)

                    section.meetings.append(meeting)

                course.sections.append(section)

        return section_map

    # Helper function to create a course object from json data
    def __parse_course_data(self, course_data):
        return Course(
            course_data['name'],
            course_data['faculty'],
            course_data['course_code'],
            course_data['credits'],
            course_data['level'],
            []
        )

    # Helper function to create a section object from json data
    def __parse_section_data(self, section_data):
        return Section(
            None,
            section_data['term'],
            section_data['number'],
            section_data['location'],
            section_data['instructor'],
            section_data['capacity'],
            section_data['enrolled'],
            []
        )

    # Helper function to create a meeting object from json data
    def __parse_meeting_data(self, meeting_data):
        return Meeting(
            meeting_data['type'],
            meeting_data['days'] if 'days' in meeting_data else [],
            meeting_data['start_time'],
            meeting_data['end_time'],
            meeting_data['date'],
            meeting_data['building'],
            meeting_data['room']
        )
