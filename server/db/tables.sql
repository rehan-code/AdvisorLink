CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pg_trgm";

DROP TABLE IF EXISTS MEETING;
DROP TABLE IF EXISTS COURSE_SECTION;
DROP TABLE IF EXISTS COURSE;
DROP TABLE IF EXISTS FACULTY;
DROP TABLE IF EXISTS TERM;
DROP TYPE IF EXISTS course_level;
DROP TYPE IF EXISTS day_of_week;
DROP TYPE IF EXISTS course_section_status;
DROP TYPE IF EXISTS meeting_type;

-- Types
CREATE TYPE course_level AS ENUM('UNDERGRADUATE', 'GRADUATE', 'DIPLOMA');
CREATE TYPE day_of_week AS ENUM('SUN', 'MON', 'TUES', 'WED', 'THUR', 'FRI', 'SAT');
CREATE TYPE course_section_status as ENUM('OPEN', 'CLOSED');
CREATE TYPE meeting_type as ENUM('LEC', 'LAB', 'SEM', 'EXAM', 'DISTANCE_EDUCATION', 'ELECTRONIC', 'READING', 'TUTORIAL', 'PRACTICUM', 'INDEPENDENT_STUDY');

CREATE TABLE faculty (
  id uuid DEFAULT uuid_generate_v4() PRIMARY KEY,
  code VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE term (
  id uuid DEFAULT uuid_generate_v4() PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  start_date DATE,
  end_date DATE
);

CREATE TABLE course (
  id uuid DEFAULT uuid_generate_v4() PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  faculty_id uuid NOT NULL,
  course_code VARCHAR(255) NOT NULL,
  credits NUMERIC(4, 2) DEFAULT 0 NOT NULL,
  level course_level,

  FOREIGN KEY (faculty_id) REFERENCES faculty (id)
);

CREATE TABLE course_section (
  id uuid DEFAULT uuid_generate_v4() PRIMARY KEY,
  course_id uuid NOT NULL,
  term_id uuid NOT NULL,
  number VARCHAR(255) NOT NULL,
  capacity BIGINT DEFAULT 0,
  status course_section_status NOT NULL,

  -- In a more complex system, these should probably be broken up into their own tables
  enrolled BIGINT DEFAULT 0,
  instructor VARCHAR(255),
  location VARCHAR(255),

  -- These columns should only ever be used in search
  search_course_code VARCHAR(255),
  search_all_tags VARCHAR(4095),

  FOREIGN KEY (course_id) REFERENCES course (id),
  FOREIGN KEY (term_id) REFERENCES term (id)
);
CREATE INDEX course_section_course_id_index ON course_section(course_id);

CREATE TABLE meeting (
  id uuid DEFAULT uuid_generate_v4() PRIMARY KEY,
  course_section_id uuid NOT NULL,
  type meeting_type NOT NULL,
  days day_of_week[],
  start_time TIME WITHOUT TIME ZONE,
  end_time TIME WITHOUT TIME ZONE,
  date DATE,

  -- In a more complex system, these should probably be broken up into their own tables
  building VARCHAR(255),
  room VARCHAR(255),

  FOREIGN KEY (course_section_id) REFERENCES course_section (id)
);
CREATE INDEX meeting_course_section_id_index ON meeting(course_section_id);
CREATE INDEX meeting_start_time ON meeting(start_time);
CREATE INDEX meeting_end_time ON meeting(end_time);
CREATE INDEX meeting_days ON meeting(days);

-- Add searching capability by course name
ALTER TABLE course ADD COLUMN ts_name tsvector
    GENERATED ALWAYS AS (to_tsvector('english', name)) STORED;
CREATE INDEX ts_name_idx ON course USING GIN (ts_name);

-- Add searching capability by section instructor
ALTER TABLE course_section ADD COLUMN ts_instructor tsvector
    GENERATED ALWAYS AS (to_tsvector('english', instructor)) STORED;
CREATE INDEX ts_instructor_idx ON course_section USING GIN (ts_instructor);

-- Add searching capability by section code generated for search
ALTER TABLE course_section ADD COLUMN ts_search_course_code tsvector
    GENERATED ALWAYS AS (to_tsvector('english', search_course_code)) STORED;
CREATE INDEX ts_search_course_code_idx ON course_section USING GIN (ts_search_course_code);

-- Add searching capability by section code generated for search
ALTER TABLE course_section ADD COLUMN ts_search_all_tags tsvector
    GENERATED ALWAYS AS (to_tsvector('english', search_all_tags)) STORED;
CREATE INDEX ts_search_all_tags_idx ON course_section USING GIN (ts_search_all_tags);
