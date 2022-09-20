import unittest

import src.scripts.search as search

def load_section_map(section_json_path='./src/scripts/courses.json'):
    parser = search.CourseJsonParser()
    section_map = parser.parse_json(section_json_path)
    return section_map

class ParserTests(unittest.TestCase):
    def test_json_parsing(self):
        section_map = load_section_map()
        searchables = [
            'CODE',
            'FACULTY',
            'CREDITS',
            'INSTRUCTOR',
            'BUILDING',
            'NAME',
            'TERM',
            'SECTION',
            'LEVEL',
            'LOCATION',
            'YEAR'
        ]

        # Ensure that the section map has the search parameters we are expecting.
        for term in searchables:
            self.assertIsInstance(section_map.searchMap[term], dict, f'Expected field {term} in section_map.searchMap to be dict')

    def test_search_by_code(self):
        section_map = load_section_map()

        # Test searching the exact course code.
        found_sections = section_map.search(search.SearchOptionEnum.CODE, 'ACCT1220')
        self.assertTrue(len(found_sections) > 0 and all([section.course.faculty == 'ACCT' and section.course.course_code[0] == '1220' for section in found_sections]))

        # Course code searching should be case-insensitive.
        # found_sections = section_map.search(search.SearchOptionEnum.CODE, 'AcCt1220')
        # self.assertTrue(len(found_sections) > 0 and all([section.course.faculty == 'ACCT' and section.course.course_code[0] == '1220' for section in found_sections]))

    def test_search_by_name(self):
        section_map = load_section_map()

        # Test searching by the name of the course.
        found_sections = section_map.search(search.SearchOptionEnum.NAME, 'Intro Financial Accounting')
        self.assertTrue(len(found_sections) > 0 and all([section.course.name == 'Intro Financial Accounting' for section in found_sections]))

    def test_search_by_faculty(self):
        section_map = load_section_map()

        # Test searching by the faculty of the course.
        found_sections = section_map.search(search.SearchOptionEnum.FACULTY, 'CIS')
        self.assertTrue(len(found_sections) > 0 and all([section.course.faculty == 'CIS' for section in found_sections]))

    def test_search_by_credits(self):
        section_map = load_section_map()

        # Test searching by the credits of the course.
        found_sections = section_map.search(search.SearchOptionEnum.CREDITS, '0.75')
        self.assertTrue(len(found_sections) > 0 and all([section.course.credits[0] == '0.75' for section in found_sections]))

    def test_search_by_instructor(self):
        section_map = load_section_map()

        # Test searching by the instructor of the course.
        found_sections = section_map.search(search.SearchOptionEnum.INSTRUCTOR, 'G. Klotz')
        self.assertTrue(len(found_sections) > 0 and all([section.instructor == 'G. Klotz' for section in found_sections]))

    def test_search_by_building(self):
        section_map = load_section_map()

        # Test searching by the course's meeting's building.
        found_sections = section_map.search(search.SearchOptionEnum.BUILDING, 'ROZH')
        self.assertTrue(len(found_sections) > 0 and all([any([meeting.building == 'ROZH' for meeting in section.meetings]) for section in found_sections]))

    def test_search_by_term(self):
        section_map = load_section_map()

        # Test searching by the term of the course.
        found_sections = section_map.search(search.SearchOptionEnum.TERM, 'Fall 2022')
        self.assertTrue(len(found_sections) > 0 and all([section.term == 'Fall 2022' for section in found_sections]))

    def test_search_by_section(self):
        section_map = load_section_map()

        # Test searching by the section number of the course.
        found_sections = section_map.search(search.SearchOptionEnum.SECTION, '0109')
        self.assertTrue(len(found_sections) > 0 and all([section.number == '0109' for section in found_sections]))

    def test_search_by_level(self):
        section_map = load_section_map()

        # Test searching by the level (graduate, undergraduate) of the course.
        found_sections = section_map.search(search.SearchOptionEnum.LEVEL, 'Graduate')
        self.assertTrue(len(found_sections) > 0 and all([section.course.level[0] == 'Graduate' for section in found_sections]))

    def test_search_by_location(self):
        section_map = load_section_map()

        # Test searching by the location of the course.
        found_sections = section_map.search(search.SearchOptionEnum.LOCATION, 'Guelph')
        self.assertTrue(len(found_sections) > 0 and all([section.location == 'Guelph' for section in found_sections]))

    def test_search_by_year(self):
        section_map = load_section_map()

        # Test searching by the year of the course is offered.
        found_sections = section_map.search(search.SearchOptionEnum.YEAR, '2022')
        self.assertTrue(len(found_sections) > 0 and all([section.term.split()[1] == '2022' for section in found_sections]))

if __name__ == '__main__':
    unittest.main()
