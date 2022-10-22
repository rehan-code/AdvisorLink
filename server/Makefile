PYTHON=python3

help:
	@echo "> debug ............ Run the flask web server in debug mode (hot refresh)"
	@echo "> production ...... Run the flask web server using gunicorn wsgi"

debug:
	${PYTHON} app.py

production:
	gunicorn -w2 -b 0.0.0.0:5000 'wsgi:app'
