PYTHON = python
DOCKER = docker

help:
	@echo "> test ............ Run the tests"
	@echo "> lint ............ Lint all python files in src/"
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

db:
	${DOCKER} -v
	-${DOCKER} stop schedulerDb
	-${DOCKER} rm schedulerDb
	${DOCKER} pull postgres
	${DOCKER} run \
    --name schedulerDb \
    -p 5455:5432 \
    -e POSTGRES_USER=admin \
    -e POSTGRES_PASSWORD=team106 \
    -e POSTGRES_DB=postgres \
    -d \
    postgres
