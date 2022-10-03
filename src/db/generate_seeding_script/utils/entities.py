from abc import ABC, abstractmethod
import uuid
import hashlib
import random
import re

# Generates a random uuid based on the input string.
def uuid_from_str(string):
    rd = random.Random()
    rd.seed(int(hashlib.sha256(string.encode('utf-8')).hexdigest(), 16) % 10**8)
    return uuid.UUID(int=rd.getrandbits(128))

pascal_to_snake_pattern = re.compile(r'(?<!^)(?=[A-Z])')

class Entity(ABC):
    # Generates an insert statement to insert the entity into the database.
    def getInsert(self):
        # The table name is either explicitly set or derived from the class name.
        table_name = self.table_name if hasattr(self, 'table_name') else pascal_to_snake_pattern.sub('_', type(self).__name__).lower()
        defined_columns = [c for c in list(self.columns.keys()) if hasattr(self, c)]
        columns_sql = ','.join([f'"{c}"' for c in defined_columns])

        values_sql = []
        for col in defined_columns:
            col_type = self.columns[col]
            col_val = getattr(self, col)

            # Format each column value correctly to correspond with its type in the database.
            if (col_val == None):
                values_sql.append('NULL')
            elif col_type == 'str':
                sanitized_val = str(col_val).replace("'", "\\'")
                values_sql.append(f"E'{sanitized_val}'")
            elif col_type == 'float':
                values_sql.append(str(col_val))
            elif col_type == 'int':
                values_sql.append(str(col_val))
            elif col_type == 'str[]':
                values_sql.append("E'{" + ','.join([f'"{i}"' for i in col_val]) + "}'")
            else:
                raise Exception(f'Unknown column type "{col_type}"')
        values_sql = ','.join(values_sql)

        return f'INSERT INTO "public"."{table_name}"({columns_sql}) VALUES ({values_sql});'

class Faculty(Entity):
    columns = {
        'id': 'str',
        'code': 'str'
    }

    def __init__(self, code):
        self.id = uuid_from_str(code)
        self.code = code

class Term(Entity):
    columns = {
        'id': 'str',
        'name': 'str',
        'start_date': 'str',
        'end_date': 'str'
    }

    def __init__(self, name, start_date, end_date):
        self.id = uuid_from_str(name)
        self.name = name
        self.start_date = start_date
        self.end_date = end_date

class Course(Entity):
    columns = {
        'id': 'str',
        'name': 'str',
        'faculty_id': 'str',
        'course_code': 'str',
        'credits': 'float',
        'name': 'str',
        'level': 'str'
    }

    def __init__(self, name, faculty_id, course_code, credits, level):
        self.id = uuid_from_str(f'{faculty_id}*{course_code}: {name}')
        self.name = name
        self.faculty_id = faculty_id
        self.course_code = course_code
        self.credits = credits
        self.level = level

class Section(Entity):
    table_name = 'course_section'
    columns = {
        'id': 'str',
        'number': 'str',
        'course_id': 'str',
        'term_id': 'str',
        'location': 'str',
        'instructor': 'str',
        'capacity': 'int',
        'enrolled': 'int',
        'status': 'str'
    }
    def __init__(self, number, course_id, term_id, location, instructor, capacity, enrolled, status):
        self.id = uuid_from_str(f'{course_id}{number}')
        self.number = number
        self.course_id = course_id
        self.term_id = term_id
        self.location = location
        self.instructor = instructor
        self.capacity = capacity
        self.enrolled = enrolled
        self.status = status

class Meeting(Entity):
    columns = {
        'id': 'str',
        'course_section_id': 'str',
        'type': 'str',
        'date': 'str',
        'days': 'str[]',
        'start_time': 'str',
        'end_time': 'str',
        'building': 'str',
        'room': 'str'
    }

    def __init__(self, section_id, type, date, days, start_time, end_time, building, room, index = None):
        self.id = uuid.UUID(int=rd.getrandbits(128)) if index == None else uuid_from_str(f'{section_id}{str(index)}')
        self.course_section_id = section_id
        self.type = type
        self.date = date
        self.days = days
        self.start_time = start_time
        self.end_time = end_time
        self.building = building
        self.room = room
