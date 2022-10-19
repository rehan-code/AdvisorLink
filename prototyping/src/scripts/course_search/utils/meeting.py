class Meeting():
     # Creates a meeting instance with the given attributes
    def __init__(self, meeting_type, days, start_time, end_time, date, building, room):
        self.type = meeting_type
        self.days = days
        self.start_time = start_time
        self.end_time = end_time
        self.date = date
        self.building = building
        self.room = room

    # Returns a string representation of the meeting
    def __str__(self):
        rep = self.type + '\n\t' + ','.join(self.days) + '\n' + '\t' + self.start_time if self.start_time else '' + ' - ' + self.end_time if self.end_time else '' + '\n'
        if self.building and self.room:
            rep += f' {self.building}*{self.room}\n'

        return rep
