sudo rm /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
#sudo ln -sf /home/box/etc/gunicorn.config   /etc/gunicorn.d/django
#sudo /etc/init.d/gunicorn restart
