#!/usr/bin/env bash
# this is a bashscript to set up webservers for the deployment of web_static

# install nginx
sudo apt-get -y update
sudo apt-get -y install nginx
sudo service nginx start

# creating folders if it's doesn't already exists
sudo mkdir -p /data/web_static/{releases/test,shared}

# creating fake HTML file
echo "Hello i'm Mahmoud Malek" > /data/web_static/releases/test/index.html

# creating new simbolic link to test folder
symbolic_link="/data/web_static/current"

if [ -L "$symbolic_link" ]; then
	rm "$symbolic_link"
fi

ln -sfT /data/web_static/releases/test/ "$symbolic_link"

# change ownership of folder /data/
chown -R ubuntu:ubuntu /data/


# Update the Nginx configuration to serve the content
configs="server {
listen 80 default_server;
listen [::]:80 default_server;

server_name yes-ok.tech
root /data/web_static;
index index.html index.htm index.nginx-debian.html;

location /hbnb_static {
	alias /data/web_static/current/hbnb_static/;
}

}"

echo "$configs" > /etc/nginx/sites-available/default

# restarting nginx
service nginx restart
