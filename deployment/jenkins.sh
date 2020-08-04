ssh ubuntu@3.128.42.45 << EOF
cd /home/ubuntu/project_viralnews
git pull
cd ui
npm run build
sudo cp -r build /var/www/html
sudo systemctl restart nginx.service
sudo systemctl restart projectviralnews.service
