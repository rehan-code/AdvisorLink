import unittest

import src.scripts.course_parser as parser

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

if __name__ == '__main__':
    unittest.main()
