import json
from enum import Enum

class Course():
    def __init__(self, name, faculty, course_code, creds, level, sections = []):
        self.name = name
        self.faculty = faculty
        self.course_code = course_code,
        self.credits = creds,
        self.level = level,
        self.sections = sections

class Section():
    def __init__(self, course, term, number, location, building, room, instructor, capacity, enrolled, meetings = []):
        self.course = course
        self.term = term
        self.number = number
        self.location = location
        self.building = building
        self.room = room
        self.instructor = instructor
        self.capacity = capacity
        self.enrolled = enrolled
        self.meetings = meetings
    
    def __str__(self):
        #FIX self.course.course_code -> string instead of tuple
        #FIX self.course.credit -> string instead of tuple
        print(self.course.level)
        return (
            self.course.faculty + '*' + self.course.course_code[0] + '*' + self.number + '\n' +
            self.course.name + ' ' + str(self.course.credits[0]) + '\n' +
            str(self.course.level[0]) + '\n' +
            self.instructor + '\n' +
            self.term + ', ' + self.location
        )

class Meeting():
    def __init__(self, type, days, start_time, end_time, date, building, room):
        self.type = type
        self.days = days
        self.start_time = start_time
        self.end_time = end_time
        self.date = date
        self.building = building
        self.room = room


class CourseJsonParser():
    def __init__(self):
        pass

    def parse_json(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
        
        sectionMap = SectionSearchMap()
        for course_data in data['courses']:
            course = self.__parse_course_data(course_data)

            for section_data in course_data['sections']:
                section = self.__parse_section_data(section_data)
                section.course = course

                sectionMap.add_section(SearchOptionEnum.CODE, course_data['faculty'] + course_data['course_code'], section)
                sectionMap.add_section(SearchOptionEnum.FACULTY, course_data['faculty'], section)
                sectionMap.add_section(SearchOptionEnum.CREDITS, course_data['credits'], section)
                sectionMap.add_section(SearchOptionEnum.INSTRUCTOR, section_data['instructor'], section)
                sectionMap.add_section(SearchOptionEnum.NAME, course_data['name'], section)
                sectionMap.add_section(SearchOptionEnum.TERM, section_data['term'], section)
                sectionMap.add_section(SearchOptionEnum.SECTION, section_data['number'], section)
                sectionMap.add_section(SearchOptionEnum.LEVEL, course_data['level'], section)
                sectionMap.add_section(SearchOptionEnum.LOCATION, section_data['location'], section)
                sectionMap.add_section(SearchOptionEnum.YEAR, section_data['term'].split()[1], section)

                for meeting_data in section_data['meetings']:
                    meeting = self.__parse_meeting_data(meeting_data)

                    sectionMap.add_section(SearchOptionEnum.BUILDING, meeting_data['building'], section)

                    section.meetings.append(meeting)

                course.sections.append(section)

        return sectionMap

    def __parse_course_data(self, course_data):
        return Course(
            course_data['name'],
            course_data['faculty'],
            course_data['course_code'],
            course_data['credits'],
            course_data['level']
        )

    def __parse_section_data(self, section_data):
        return Section(
            None,
            section_data['term'],
            section_data['number'],
            section_data['location'],
            section_data['building'],
            section_data['room'],
            section_data['instructor'],
            section_data['capacity'],
            section_data['enrolled']
        )
    
    def __parse_meeting_data(self, meeting_data):
        return Meeting(
            meeting_data['type'],
            meeting_data['days'],
            meeting_data['start_time'],
            meeting_data['end_time'],
            meeting_data['date'],
            meeting_data['building'],
            meeting_data['room']
        )


class SearchOptionEnum(str, Enum):
    CODE = 'CODE'
    FACULTY = 'FACULTY'
    CREDITS = 'CREDITS'
    INSTRUCTOR = 'INSTRUCTOR'
    BUILDING = 'BUILDING'
    NAME = 'NAME'
    TERM = 'TERM'
    SECTION = 'SECTION'
    LEVEL = 'LEVEL'
    LOCATION = 'LOCATION'
    YEAR = 'YEAR'

class SectionSearchMap():
    def __init__(self):
        self.searchMap = {}

    def search(self, searchBy, item):
        return (self.searchMap[searchBy][item] if searchBy in self.searchMap and item in self.searchMap[searchBy] else [])
    
    def add_section(self, storeBy, key, section):
        if storeBy not in self.searchMap: self.searchMap[storeBy] = {}

        if key in self.searchMap[storeBy]:
            if section not in self.searchMap[storeBy][key]: self.searchMap[storeBy][key].append(section)
        else:
            self.searchMap[storeBy][key] = [section]

def search_tool():
    parser = CourseJsonParser()
    sectionMap = parser.parse_json('../example-courses.json')
    print('Welcome to the offline search tool for courses.')
    while (True):
        print(
            '\nSearch by:\n'\
            '(type "q" to exit)\n'\
            '1) Course Code \n'\
            '2) Faculty\n'\
            '3) Instructor\n'\
            '4) Location (Building)\n'\
            '5) Credits\n'\
            '6) Course Name\n'\
            '7) Term\n'\
            '8) Section\n'\
            '9) Location/Campus\n'\
            '10) Year'
        )
        userInput = input()

        sections = []
        filteredsections = []
        if (userInput == '1'):
            print('Enter the course code (e.g. ACCT1220): ')
            sections = sectionMap.search(SearchOptionEnum.CODE, input())
        elif (userInput == '2'):
            print('Enter the faculty (e.g. CIS): ')
            sections = sectionMap.search(SearchOptionEnum.FACULTY, input())
        elif (userInput == '3'): # should be in filter
            print('Enter the course instructor (e.g. P. Lassou): ')
            sections = sectionMap.search(SearchOptionEnum.INSTRUCTOR, input())
        elif (userInput == '4'):# should be in filter
            print('Enter the course location (e.g. ROZH): ')
            sections = sectionMap.search(SearchOptionEnum.BUILDING, input())
        elif (userInput == '5'):
            print('Enter the course credit (e.g. 0.75): ')
            sections = sectionMap.search(SearchOptionEnum.CREDITS, float(input()))
        elif (userInput == '6'):
            print('Enter the course name (e.g. ROZH): ')
            sections = sectionMap.search(SearchOptionEnum.NAME, input())
        elif (userInput == '7'):# should be in filter
            print('Enter the term (e.g. Fall 2022): ')
            sections = sectionMap.search(SearchOptionEnum.TERM, input()) 
        elif (userInput == '8'):
            print('Enter the section number (e.g. 0101): ')
            sections = sectionMap.search(SearchOptionEnum.SECTION, input())
        elif (userInput == '9'):
            print('Enter the location/campus (e.g. Guelph): ')
            sections = sectionMap.search(SearchOptionEnum.LOCATION, input())
        elif (userInput == '10'):
            print('Enter the year (e.g. 2023): ')
            sections = sectionMap.search(SearchOptionEnum.YEAR, input()) 
        elif (userInput == 'q'):
            break
        
        if len(sections) > 0:
            print('Sections found: \n')
            for section in sections:
                print(section)
                print('------------------------------')
        else:
            print('No sections available')

def main():
    search_tool()

if __name__ == "__main__":
    main()
