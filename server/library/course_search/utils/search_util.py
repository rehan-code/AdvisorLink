from .course_json_parser import CourseJsonParser
from .section_search_map import SectionSearchMap, SearchOptionEnum
import os
# Helper function to make paths relative to this script instead of the directory
# from which it was run.
script_directory = os.path.dirname(os.path.abspath(__file__))
def rel_path(path):
    return os.path.join(script_directory, path)

class SearchUtil():
    def __init__(self):
        parser = CourseJsonParser()
        self.section_map = parser.parse_json(rel_path('../../config/courses.json'))

    def all(self):
        return self.section_map.get_all()

    def search(self, name = None, code = None, faculty = None, credits = None, level = None, term = None, location = None, building = None, instructor = None, year = None, exam = None):
        sections = []
        if name: sections.append(self.section_map.search(SearchOptionEnum.NAME, name))
        if code: sections.append(self.section_map.search(SearchOptionEnum.CODE, code))
        if faculty: sections.append(self.section_map.search(SearchOptionEnum.FACULTY, faculty))
        if credits: sections.append(self.section_map.search(SearchOptionEnum.CREDITS, str(format(float(credits), ".2f"))))
        if level: sections.append(self.section_map.search(SearchOptionEnum.LEVEL, level))
        if term: sections.append(self.section_map.search(SearchOptionEnum.TERM, term))
        if location: sections.append(self.section_map.search(SearchOptionEnum.LOCATION, location))
        if building: sections.append(self.section_map.search(SearchOptionEnum.BUILDING, building))
        if instructor: sections.append(self.section_map.search(SearchOptionEnum.INSTRUCTOR, instructor))
        if year: sections.append(self.section_map.search(SearchOptionEnum.YEAR, year))
        if exam: sections.append(self.section_map.search(SearchOptionEnum.EXAM, exam))

        if len(sections) > 0:
            filtered_list = set.intersection(*sections)
            return filtered_list
        else:
            return sections

    
    def suggest(self):
        # Add code that suggests sections
        pass

