#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static

# Installing nginx
# sudo -i
sudo apt-get -y update
sudo apt-get -y install nginx
sudo service nginx start

#directories
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html

echo '
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
' | sudo tee /data/web_static/releases/test/index.html >/dev/null

# Creating a symbolic link
if [ -L "/data/web_static/current" ]; then
    sudo rm "/data/web_static/current"
fi
sudo ln -sf /data/web_static/releases/test /data/web_static/current

sudo chown -hR ubuntu:ubuntu /data/
sudo sed -i '15 i \\n\tlocation /hbnb_static/ {\n\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default
sudo service nginx restart
