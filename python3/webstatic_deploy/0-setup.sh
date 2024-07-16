#!/usr/bin/env bash
# script to set up the environment for codebase
sudo apt-get update 
sudo apt-get install nginx -y

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "Holberton School" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
 chown -R ubuntu:ubuntu /data/
 chgrp -R ubuntu /data/

 #code to the nginx config file to congigure the server

printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-served-By $HOSTNAME;
    root /var/www/html;
    index index.html index.htm;
    location /hbnb_static {
	    alias /data/web_static/current/;
	    index index.html index.htm;
    }
    location /redirect_me {
	    return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }
    error_page 404 /404.html;
    location /404 {
	    root /var/www/html;
	    internal;
    }" > /etc/nginx/sites-available/default:w

    
  
