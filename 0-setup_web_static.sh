#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static

# Installing nginx
sudo apt-get -y update
sudo apt-get -y install nginx

#directories
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html

sudo echo '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>' | sudo tee /data/web_static/releases/test/index.html >/dev/null

# Creating a symbolic link
if [ -L "/data/web_static/current" ]; then
    sudo rm "/data/web_static/current"
fi
sudo ln -sf /data/web_static/releases/test /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '/listen 80 default_server/a location /hbnb_static {alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default
sudo service nginx restart
