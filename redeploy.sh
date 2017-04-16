python manage.py supervisor stop all
kill -9 `ps -ef | grep supervisor | grep -v grep | awk '{print $2}'`
#sudo /etc/init.d/nginx stop
#sudo git pull origin master
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput --clear
#sudo service nginx start
python manage.py supervisor -d
