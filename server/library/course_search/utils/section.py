class Section():
    # Creates a section instance with the given attributes
    def __init__(self, course, term, number, location, instructor, capacity, enrolled, meetings=[]):
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
        rep = 'Code:           {0}*{1}*{2}\n'.format(self.course.faculty, self.course.course_code, self.number) +\
            'Name:           {0}\n'.format(self.course.name) +\
            'Weight:         {0}\n'.format(str(self.course.credits)) +\
            'Level:          {0}\n'.format(str(self.course.level)) +\
            'Instructor:     {0}\n'.format(self.instructor) +\
            'Term:           {0}, {1}\n'.format(self.term, self.location) +\
            'Meetings: \n\n'

        for meeting in self.meetings:
            rep += '\t' + str(meeting) + '\n' if meeting else '\n'

        return rep

    def toJson(self):
        meetingsJson = []
        for meeting in self.meetings:
            meetingsJson.append(meeting.toJson())

        return {
            'name': self.course.name,
            'faculty': self.course.faculty,
            'code': self.course.course_code,
            'number': self.number,
            'weight': self.course.credits,
            'level': self.course.level,
            'instructor': self.instructor,
            'term': self.term,
            'location': self.location,
            'capacity': self.capacity,
            'enrolled': self.enrolled,
            'meetings': meetingsJson
        }
