PYTHON=python3

help:
	@echo "> make debug_flask ............ Run the flask web server in debug mode (hot refresh)"
	@echo "> sudo make production ...... Run the nginx + flask web server using gunicorn wsgi"

debug_flask:
	${PYTHON} ./server/app.py

production:
	sudo ./install.sh
	sudo service nginx restart
	sudo killall gunicorn || true
	gunicorn -w2 -b 0.0.0.0:5000 --chdir server 'wsgi:app' --daemon
