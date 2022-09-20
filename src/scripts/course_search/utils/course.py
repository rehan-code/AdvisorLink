class Course():
    # Creates a course instance with the given attributes
    def __init__(self, name, faculty, course_code, creds, level, sections = []):
        self.name = name
        self.faculty = faculty
        self.course_code = course_code,
        self.credits = creds,
        self.level = level,
        self.sections = sections
