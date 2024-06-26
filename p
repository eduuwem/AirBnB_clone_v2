#!/usr/bin/env bash

# script that sets up web servers for the deployment of web_static
sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
sudo chown -R ubuntu:ubuntu /data/
sudo tee /data/web_static/current/index.html <<EOF
<html>
  <head>
  </head>
  <body>
    Holberton School is a learning hub
  </body>
</html>
EOF
sudo rm -rf /data/web_static/current
sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

echo "server {
   listen 80 default_server;
   listen [::]:80 default_server;
   server_name _;
   add_header X-Served-By \"\$hostname\";
   root /var/www/html;
   index index.html;

   location /redirect_me {
      return 301 https://youtube.com/;
   }
   location /hbnb_static {
      alias /data/web_static/current/;
      index index.html index.htm;
   }

   error_page 404 /404.html;
   location /404 {
      root /var/www/html;
      internal;
   }
}" | sudo tee /etc/nginx/sites-enabled/default

sudo nginx -t
sudo service nginx restart
