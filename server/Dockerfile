FROM python:3.10
WORKDIR /usr/src/server

# Install dependencies
COPY ["requirements.txt", "install.sh", "./"]
RUN ./install.sh

COPY . .

EXPOSE 5000

CMD ["make", "production"]
