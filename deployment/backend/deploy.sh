# configure system service
sudo mv project_viralnews.service /etc/systemd/system/
sudo systemctl start myproject
sudo systemctl enable myproject

# configure nginx
sudo mv project_viralnews /etc/nginx/sites-available/
sudo ln -s /etc/nginx/sites-available/project_viralnews /etc/nginx/sites-enabled
sudo systemctl restart nginx