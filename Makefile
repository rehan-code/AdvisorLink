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

build_images:
	echo glpat-2Fy4r4qfydMx59tAqVEj | docker login -u hnantais registry.socs.uoguelph.ca --password-stdin
	docker build -t registry.socs.uoguelph.ca/hnantais/f22_cis3760_team106online/web web/
	docker build -t registry.socs.uoguelph.ca/hnantais/f22_cis3760_team106online/server server/
	docker push registry.socs.uoguelph.ca/hnantais/f22_cis3760_team106online/web
	docker push registry.socs.uoguelph.ca/hnantais/f22_cis3760_team106online/server

deploy_images:
	curl -X POST https://\$AdvisorLink:kqk5nPXutJsibLHJTej75wcjyJovbxkwyLvLY7aznccvz8sKBHanPXZYNpwd@advisorlink.scm.azurewebsites.net/api/registry/webhook -d -H
