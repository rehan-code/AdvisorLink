import unittest

import src.scripts.course_parser as parser
from src.scripts.course_parser.utils.courses_to_csv import courses_to_csv

class TestInvalidHTMLFiles(unittest.TestCase):
    def test_empty_file(self):
        root = parser.parse_html('./src/tests/html/empty.html')
        self.assertEqual(str(root), '<root />')

    def test_empty_course_table(self):
        root = parser.parse_html('./src/tests/html/empty_table.html')
        table_body = root.find_element('table', 'summary', 'Sections').child(0)

        # no children, table_body should be of NoneType
        self.assertEqual(table_body, None)

    def test_invalid_entries(self):
        with self.assertRaises(Exception):
            parser.parse_html('./src/tests/html/invalid_entries.html')

class TestCSVParsing(unittest.TestCase):

    # Ensure headers are generated even when no courses are available to parse
    def test_headers(self):
        courses = []
        csvstring = courses_to_csv(courses)
        self.assertEqual(csvstring, '"Course Code (long)","faculty","course_code","name","credits","level","term","section_number","location","instructor","capacity","enrolled","status","meeting_type","meeting_date","meeting_start_date","meeting_end_date","meeting_days","meeting_start_time","meeting_end_time","meeting_building","meeting_room"')

    def test_valid_courses(self):
        valid_courses = []
        courseone = {}
        courseone["name"] = "test course"
        courseone["faculty"] = "fac"
        courseone["course_code"] = "1222"
        courseone["credits"] = "1.0"
        courseone["level"] = "Undergraduate"

        coursesecone = {}
        coursesecone["term"] = "Fall 2023"
        coursesecone["number"] = "01"
        coursesecone["location"] = "Guelph"
        coursesecone["instructor"] = "test instructor"
        coursesecone["capacity"] = "68"
        coursesecone["enrolled"] = "2"
        coursesecone["status"] = "Open"
        coursesecone["meetings"] = []
        courseone["sections"] = [coursesecone]

        coursetwo = {}
        coursetwo["name"] = 'another test course'
        coursetwo["faculty"] = "fac"
        coursetwo["course_code"] = "1222"
        coursetwo["credits"] = "1.0"
        coursetwo["level"] = "Undergraduate"

        coursesectwo = {}
        coursesectwo["term"] = "Fall 2023"
        coursesectwo["number"] = "01"
        coursesectwo["location"] = "Guelph"
        coursesectwo["instructor"] = "test instructor"
        coursesectwo["capacity"] = "68"
        coursesectwo["enrolled"] = "2"
        coursesectwo["status"] = "Open"

        coursemeeting = {}
        coursemeeting["type"] = "LEC"
        coursemeeting["date"] = None
        coursemeeting["start_date"] = "2022/09/08"
        coursemeeting["end_date"] = "2022/12/16"
        coursemeeting["days"] = []
        coursemeeting["start_time"] = "01:00PM"
        coursemeeting["end_time"] = "02:20PM"
        coursemeeting["building"] = "CRSC"
        coursemeeting["room"] = "122"

        coursesectwo["meetings"] = [coursemeeting]

        coursetwo["sections"] = [coursesectwo]

        valid_courses.append(courseone)
        valid_courses.append(coursetwo)

        error = 0        
        try:
            courses_to_csv(valid_courses)
        except:
            error = 1

        self.assertEqual(error, 0)
        
if __name__ == '__main__':
    unittest.main()
