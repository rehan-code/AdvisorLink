PYTHON = python

help:
	@echo "> test ............ Run the tests"
	@echo "> course_config ... Run the course parser to create the course configuration files"
	@echo "> search_cli ...... Run the course search CLI"

test:
	${PYTHON} -m unittest discover src/tests -v

lint:
	pylint -d C0301,R0903,R0913,C0116,R1729,C0114,C0115,W0102,R0902,R0912,E0401,R0916,W1401 src

course_config:
	${PYTHON} src/scripts/course_parser

search_cli:
	${PYTHON} src/scripts/course_search
