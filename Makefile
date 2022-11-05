PYTHON=python3

help:
	@echo "> make debug_flask ............ Run the flask web server in debug mode (hot refresh)"
	@echo "> make install ................ Install project dependencies (using apt)"
	@echo "> sudo make prod_nginx ........ Build/Copy nginx configuration files and restart the nginx service"
	@echo "> sudo make prod_flask ........ Kill previous instance of gunicorn flask web server and restart it"
	@echo "> sudo make production ........ Run the nginx + flask web server using gunicorn wsgi"

debug_flask:
	${PYTHON} ./server/app.py

install:
	sudo ./install.sh

prod_nginx:
	cd web/ && yarn install && yarn build
	sudo cp web/nginx/nginx.conf /etc/nginx/sites-available/default
	sudo cp -r web/build/* /usr/share/nginx/html
	sudo service nginx restart

prod_flask:
	sudo killall gunicorn || true
	gunicorn -w2 -b 0.0.0.0:5000 --certfile=/etc/ssl/cert.crt --keyfile=/etc/ssl/private.key --chdir server 'wsgi:app' --daemon

production: prod_nginx prod_flask
