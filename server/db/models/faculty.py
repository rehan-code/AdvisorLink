from ..base import db
from sqlalchemy.dialects.postgresql import UUID
import uuid
from ..utils.uuid_from_string import uuid_from_str


class Faculty(db.Model):
    __tablename__ = 'faculty'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    code = db.Column(db.VARCHAR(length=255))

    def __init__(self, code):
        self.id = uuid_from_str(code)
        self.code = code
