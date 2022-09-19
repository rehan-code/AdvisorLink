import json
from enum import Enum
import argparse
from argparse import Action

class Course():
    # Creates a course instance with the given attributes
    def __init__(self, name, faculty, course_code, creds, level, sections = []):
        self.name = name
        self.faculty = faculty
        self.course_code = course_code,
        self.credits = creds,
        self.level = level,
        self.sections = sections

class Section():
    # Creates a section instance with the given attributes
    def __init__(self, course, term, number, location, instructor, capacity, enrolled, meetings = []):
        self.course = course
        self.term = term
        self.number = number
        self.location = location
        self.instructor = instructor
        self.capacity = capacity
        self.enrolled = enrolled
        self.meetings = meetings

    # Returns a string representation of the section
    def __str__(self):
        #FIX self.course.course_code -> string instead of tuple
        #FIX self.course.credit -> string instead of tuple
        rep = self.course.faculty + '*' + self.course.course_code[0] + '*' + self.number + '\n' +\
            self.course.name + ' ' + str(self.course.credits[0]) + '\n' +\
            str(self.course.level[0]) + '\n' +\
            self.instructor + '\n' +\
            self.term + ', ' + self.location + '\n\tMeetings: \n'

        for meeting in self.meetings:
            rep += str(meeting) + '\n' if meeting else '\n'

        return (rep)

class Meeting():
     # Creates a meeting instance with the given attributes
    def __init__(self, meetingType, days, start_time, end_time, date, building, room):
        self.type = meetingType
        self.days = days
        self.start_time = start_time
        self.end_time = end_time
        self.date = date
        self.building = building
        self.room = room

    # Returns a string representation of the meeting
    def __str__(self):
        rep = self.type + '\n' + ','.join(self.days) + '\n'+ self.start_time if self.start_time else '' + ' - ' + self.end_time if self.end_time else '' + '\n'
        if self.building and self.room:
            rep += self.building + '*' + self.room + '\n'

        return (rep)

# A class to parse the course JSON file
class CourseJsonParser():
    def __init__(self):
        pass

    # This method parses the JSON file and returns a hashmap later used to search for sections
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

# An enum with all the search options
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

# A Section search map class with a dictionary to store section data
class SectionSearchMap():
    def __init__(self):
        self.searchMap = {}

    # This function retrieves a list of sections using the search criteria and the searched item. O(1) to retrieve data
    def search(self, searchBy, item):
        if (searchBy not in self.searchMap):
            return set()

        stored_items = self.searchMap[searchBy]

        return (self.searchMap[searchBy][item] if item in stored_items else set())

    # This function adds a section to the hashmap using the search criteria to store by, the key to use and the item to store
    def add_section(self, storeBy, key, section):
        if storeBy not in self.searchMap: self.searchMap[storeBy] = {}

        if key in self.searchMap[storeBy]:
            self.searchMap[storeBy][key].add(section)
        else:
            self.searchMap[storeBy][key] = set()
            self.searchMap[storeBy][key].add(section)


def get_arg_parser():
    parser = argparse.ArgumentParser(description='Search program that searches through the courses offered at the University of Guelph.', add_help=False)
    parser.add_argument('-name', default=None, type=str, help='course name eg. "Intro Financial Accounting"', nargs='+')
    parser.add_argument('-code', default=None, type=str, help='course code eg. ACCT1220')
    parser.add_argument('-faculty', default=None, type=str, help='faculty eg. ACCT')
    parser.add_argument('-credits', default=None, type=float, help='number of credits eg. 0.5')
    parser.add_argument('-level', default=None, type=str, help='eg. undergraduate, graduate')
    parser.add_argument('-term', default=None, type=str, help='eg. \'Fall 2022\'')
    parser.add_argument('-location', default=None, type=str, help='location of the course eg. Guelph')
    parser.add_argument('-building', default=None, type=str, help='building code eg. ROZH')
    parser.add_argument('-instructor', default=None, type=str, help='instructor name eg. P. Lassou', nargs='+')
    parser.add_argument('-year', default=None, type=str, help='year offered eg. 2022')
    parser.add_argument('-q', default=False, nargs='?', action=quitAction)
    parser.add_argument('-h', default=False, nargs='?', action=helpAction)
    return parser

# The action that is carried out when the user wants to quit the program
class quitAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        print('Exiting App')
        exit(0)

# The action that is carried out when the user wants help with the program
class helpAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        print('usage: Add filters by adding the following flags to your query:\n\n'
            '-h: help\n'
            '-q: quit\n'
            '-name: course name eg. "Introduction to Accounting"\n'
            '-code: course code eg. ACCT1220\n'
            '-faculty: faculty eg. ACCT\n'
            '-credits: number of credits eg. 0.5\n'
            '-level: course level eg. undergraduate, graduate\n'
            '-term: term offered eg. \'Fall 2022\'\n'
            '-location: location of the course eg. Guelph\n'
            '-building: building code eg. ROZH\n'
            '-instructor: instructor name eg. P. Lassou\n'
            '-year: year offered eg. 2022\n'
        )

def search_tool():
    parser = CourseJsonParser()
    sectionMap = parser.parse_json('./courses.json')
    print(
            'Welcome to the offline search tool for courses.\n\n'
            'usage: Add filters by adding the following flags to your query:\n\n'
            '-h: help\n'
            '-q: quit\n'
            '-name: course name eg. Introduction to Accounting\n'
            '-code: course code eg. ACCT1220\n'
            '-faculty: faculty eg. ACCT\n'
            '-credits: number of credits eg. 0.5\n'
            '-level: course level eg. undergraduate, graduate\n'
            '-term: term offered eg. Fall 2022\n'
            '-location: location of the course eg. Guelph\n'
            '-building: building code eg. ROZH\n'
            '-instructor: instructor name eg. P. Lassou\n'
            '-year: year offered eg. 2022\n'
    )
    sections = []
    arg_parser = get_arg_parser()
    while (True):
        try:
            args = arg_parser.parse_args(input('\nQuery: \n').split())

            # Get all the section lists requested in the user query
            if args.name: sections.append(sectionMap.search(SearchOptionEnum.NAME, ' '.join(args.name)))
            if args.code: sections.append(sectionMap.search(SearchOptionEnum.CODE, args.code))
            if args.faculty: sections.append(sectionMap.search(SearchOptionEnum.FACULTY, args.faculty))
            if args.credits: sections.append(sectionMap.search(SearchOptionEnum.CREDITS, args.credits))
            if args.level: sections.append(sectionMap.search(SearchOptionEnum.LEVEL, args.level))
            if args.term: sections.append(sectionMap.search(SearchOptionEnum.TERM, args.term))
            if args.location: sections.append(sectionMap.search(SearchOptionEnum.LOCATION, args.location))
            if args.building: sections.append(sectionMap.search(SearchOptionEnum.BUILDING, args.building))
            if args.instructor: sections.append(sectionMap.search(SearchOptionEnum.INSTRUCTOR, ' '.join(args.instructor)))
            if args.year: sections.append(sectionMap.search(SearchOptionEnum.YEAR, args.year))

            print('')
            if len(sections) == 0: continue

            # Find the common set. O(min(n, m, o, ..)) where n, m , o are the lenghts of the different sections in the query
            filteredList = set.intersection(*sections)
            if len(filteredList) > 0:
                print('Sections Found: \n\n')
                for section in filteredList:
                    print(section)
                    print('---------------------------------')
            else:
                print('No Sections met your criterias.')

            sections = []

        except argparse.ArgumentError:
            print('Argument error caught')


def main():
    search_tool()

if __name__ == "__main__":
    main()
