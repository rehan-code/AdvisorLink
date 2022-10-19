import json
import jsonschema
import os

script_directory = os.path.dirname(os.path.abspath(__file__))
def rel_path(path):
    return os.path.join(script_directory, path)
class JSONValidator:
    def __init__(self, course_schema, section_schema, meeting_schema):
        self.course_schema = course_schema
        self.section_schema = section_schema
        self.meeting_schema = meeting_schema
    
    # Method for validating all courses in a json file
    def validateCourses(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            course_data = json.load(file)

        # Validate each course against an expected course schema
        for course in course_data['courses']:
            try:
                jsonschema.validate(course, self.course_schema)

                # Validate each section against an expected section schema
                for section in course['sections']:
                    jsonschema.validate(section, self.section_schema)

                    # Validate each meeting against an expected meeting schema
                    for meeting in section['meetings']:
                        jsonschema.validate(meeting, self.meeting_schema)

            except jsonschema.exceptions.ValidationError:
                return False

        return True