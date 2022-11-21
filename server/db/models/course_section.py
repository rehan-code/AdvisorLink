from ..base import db
from sqlalchemy.dialects.postgresql import UUID
import uuid
import enum
from ..utils.uuid_from_string import uuid_from_str


class CourseSectionStatus(enum.Enum):
    OPEN = 'OPEN'
    CLOSED = 'CLOSED'


class CourseSection(db.Model):
    __tablename__ = 'course_section'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    course_id = db.Column(UUID(as_uuid=True), db.ForeignKey('course.id'))
    term_id = db.Column(UUID(as_uuid=True), db.ForeignKey('term.id'))
    number = db.Column(db.VARCHAR(length=255))
    capacity = db.Column(db.BigInteger())
    status = db.Column(db.Enum(CourseSectionStatus))
    enrolled = db.Column(db.BigInteger())
    instructor = db.Column(db.VARCHAR(length=255))
    location = db.Column(db.VARCHAR(length=255))

    def __init__(self, number, course_id, term_id, location, instructor, capacity, enrolled, status):
        self.id = uuid_from_str(f'{term_id}{course_id}{number}')
        self.number = number
        self.course_id = course_id
        self.term_id = term_id
        self.location = location
        self.instructor = instructor
        self.capacity = capacity
        self.enrolled = enrolled
        self.status = status

    def toClientJson(self):
        return {
            'id': str(self.id),
            'name': self.course.name,
            'faculty': self.course.faculty.code,
            'code': self.course.course_code,
            'number': self.number,
            'weight': float(self.course.credits),
            'level': str(self.course.level),
            'instructor': self.instructor,
            'term': self.term.name,
            'location': self.location,
            'capacity': int(self.capacity),
            'enrolled': int(self.enrolled),
            'meetings': [m.toClientJson() for m in self.meetings],
            'courseId': str(self.course_id),
            'termId': str(self.term_id)
        }
