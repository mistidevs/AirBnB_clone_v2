#!/usr/bin/env bash
# Configuring an Ubuntu Machine for Production
sudo apt-get -y update
sudo apt-get -y install nginx
ufw allow 'Nginx HTTP'
mkdir -p /data/
mkdir -p /data/web_static
mkdir -p /data/web_static/releases
mkdir -p /data/web_static/shared
mkdir -p /data/web_static/releases/test/
echo "Hello, Nginx here" > /data/web_static/releases/test/index.html
sudo ln -fs /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo nginx -t -c "/data/web_static/current/ /hbnb_static"
sudo service nginx restart
