UPDATE course_section c
SET
	search_course_code = faculty.code || ' ' || course.course_code || ' ' || c.number,
	search_all_tags = course.name || ' ' || c.instructor || ' ' || faculty.code || ' ' || course.course_code || ' ' || c.number
FROM
	course_section c2
	LEFT JOIN course ON course.id = c2.course_id
	LEFT JOIN faculty ON faculty.id = course.faculty_id
	LEFT JOIN term ON term.id = c2.term_id
WHERE c.id = c2.id;
