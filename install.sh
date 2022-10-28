#!/usr/bin/env bash

# Installation steps for flask server
cd server
sudo apt install -y software-properties-common
sudo add-apt-repository -y ppa:deadsnakes/ppa
sudo apt -y update
sudo apt -y upgrade
sudo apt install -y python3
sudo pip3 install -r requirements.txt

# Installation steps for react
cd ../web
sudo apt install -y npm
sudo npm install -g n
sudo npm install -g yarn
sudo n 18.6.0
hash -r
yarn install
yarn build

# Installation steps for nginx
sudo apt install -y nginx
sudo cp nginx/nginx-vm.conf /etc/nginx/sites-available/default
sudo cp -r build/* /usr/share/nginx/html
