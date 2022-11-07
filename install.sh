#!/usr/bin/env bash

# Installation steps for flask server
cd server
sudo apt install -y software-properties-common
sudo add-apt-repository -y ppa:deadsnakes/ppa
sudo apt -y update
sudo apt -y upgrade
sudo apt install -y python3
sudo apt install -y python3-pip
sudo pip3 install -r requirements.txt

# Installation steps for react
cd ../web
sudo apt install -y npm
sudo npm install -g n
sudo npm install -g yarn
sudo n 18.6.0
hash -r

# Installation steps for nginx
sudo apt install -y nginx

# Installation steps for Docker => Postgres
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common
sudo mkdir /etc/ssl/certs || true
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -sudo apt-key fingerprint 0EBFCD88sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
sudo apt-get install docker-ce docker-ce-cli containerd.io
sudo docker pull postgres
