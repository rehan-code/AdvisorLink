CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

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

  FOREIGN KEY (course_id) REFERENCES course (id),
  FOREIGN KEY (term_id) REFERENCES term (id)
);

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
