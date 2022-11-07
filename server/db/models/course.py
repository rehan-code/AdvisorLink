from ..base import db
from sqlalchemy.dialects.postgresql import UUID
import uuid
import enum
from ..utils.uuid_from_string import uuid_from_str

class CourseLevel(enum.Enum):
    UNDERGRADUATE = 'UNDERGRADUATE'
    GRADUATE = 'GRADUATE'
    DIPLOMA = 'DIPLOMA'

class Course(db.Model):
    __tablename__ = 'course'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.VARCHAR(length=255))
    faculty_id = db.Column(UUID(as_uuid=True), db.ForeignKey('faculty.id'))
    course_code = db.Column(db.VARCHAR(length=255))
    credits = db.Column(db.Numeric(precision=4,scale=2))
    level = db.Column(db.Enum(CourseLevel))

    def __init__(self, name, faculty_id, course_code, credits, level):
        self.id = uuid_from_str(f'{faculty_id}*{course_code}: {name}')
        self.name = name
        self.faculty_id = faculty_id
        self.course_code = course_code
        self.credits = credits
        self.level = level
