import unittest
import sys

sys.path.insert(0, '../src/scripts')

import course_parser

class TestInvalidHTMLFiles(unittest.TestCase):
    def test_empty_file(self):
        root = course_parser.parse_html('./HTML/empty.html')
        self.assertEqual(root.__str__(), '<root />')

    def test_empty_course_table(self):
        root = course_parser.parse_html('./HTML/empty_table.html')
        table_body = root.find_element('table', 'summary', 'Sections').child(0)

        # no children, table_body should be of NoneType
        self.assertEqual(table_body, None)

    def test_invalid_entries(self):
        with self.assertRaises(Exception):
            root = course_parser.parse_html('./HTML/invalid_entries.html')

if __name__ == '__main__':
    unittest.main()
