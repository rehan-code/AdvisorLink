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
