FROM python:3.10
WORKDIR /usr/src/server

# Install dependencies
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["gunicorn", "-w2", "-b 0.0.0.0:5000", "wsgi:app"]
