from ..base import db
from sqlalchemy.dialects.postgresql import UUID
import uuid
from ..utils.uuid_from_string import uuid_from_str


class Term(db.Model):
    __tablename__ = 'term'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.VARCHAR(length=255))
    start_date = db.Column(db.Date())
    end_date = db.Column(db.Date())

    def __init__(self, name, start_date, end_date):
        self.id = uuid_from_str(name)
        self.name = name
        self.start_date = start_date
        self.end_date = end_date

    def toClientJson(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'start_date': str(self.start_date),
            'end_date': str(self.end_date)
        }
