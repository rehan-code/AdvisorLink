PYTHON = python3

help:
	@echo "> test ............ Run the tests"
	@echo "> course_config ... Run the course parser to create the course configuration files"
	@echo "> search_cli ...... Run the course search CLI"

test:
	${PYTHON} -m unittest discover src/tests -v

course_config:
	${PYTHON} src/scripts/course_parser

search_cli:
	${PYTHON} src/scripts/course_search
