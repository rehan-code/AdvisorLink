FROM python:3.10
WORKDIR /usr/src/server

# Install dependencies
COPY requirements.txt ./
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["gunicorn", "-w2", "-b 0.0.0.0:5000", "--chdir", "server", "'wsgi:app'", "--daemon", "production"]
