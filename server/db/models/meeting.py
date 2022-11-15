from ..base import db
from sqlalchemy.dialects.postgresql import UUID, ARRAY
import random
import uuid
import enum
from ..utils.uuid_from_string import uuid_from_str

class MeetingType(enum.Enum):
    LEC = 'LEC'
    LAB = 'LAB'
    SEM = 'SEM'
    EXAM = 'EXAM'
    DISTANCE_EDUCATION = 'DISTANCE_EDUCATION'
    ELECTRONIC = 'ELECTRONIC'
    READING = 'READING'
    TUTORIAL = 'TUTORIAL'
    PRACTICUM = 'PRACTICUM'
    INDEPENDENT_STUDY = 'INDEPENDENT_STUDY'

class DayOfWeek(enum.Enum):
    SUN = 'SUN'
    MON = 'MON'
    TUES = 'TUES'
    WED = 'WED'
    THUR = 'THUR'
    FRI = 'FRI'
    SAT = 'SAT'

class Meeting(db.Model):
    __tablename__ = 'meeting'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    course_section_id = db.Column(UUID(as_uuid=True), db.ForeignKey('course_section.id'))
    type = db.Column(db.Enum(MeetingType))
    days = db.Column(ARRAY(db.Enum(DayOfWeek, native_enum=True, create_constraint=True, name='day_of_week')))
    start_time = db.Column(db.DateTime(timezone=False))
    end_time = db.Column(db.DateTime(timezone=False))
    date = db.Column(db.Date())
    building = db.Column(db.VARCHAR(length=255))
    room = db.Column(db.VARCHAR(length=255))

    def __init__(self, section_id, type, date, days, start_time, end_time, building, room, index=None):
        rd = random.Random()
        self.id = uuid.UUID(int=rd.getrandbits(128)) if index is None else uuid_from_str(f'{section_id}{str(index)}')
        self.course_section_id = section_id
        self.type = type
        self.date = date
        self.days = days
        self.start_time = start_time
        self.end_time = end_time
        self.building = building
        self.room = room

    def toClientJson(self):
        return {
            'id': str(self.id),
            'type': str(self.type),
            'days': [str(d) for d in self.days] if self.days else None,
            'start_time': str(self.start_time),
            'end_time':  str(self.end_time),
            'date': str(self.date),
            'building': self.building,
            'room': self.room
        }
