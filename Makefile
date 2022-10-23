PYTHON=python3

help:
	@echo "> make debug ............ Run the flask web server in debug mode (hot refresh)"
	@echo "> sudo make production ...... Run the nginx + flask web server using gunicorn wsgi"

debug_flask:
	${PYTHON} app.py

production:
	sudo ./install.sh
	sudo systemctl restart nginx
	pkill gunicorn
	gunicorn -w2 -b 0.0.0.0:5000 --chdir server 'wsgi:app' --daemon
