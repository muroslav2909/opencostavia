#!/bin/bash

sudo kill -9 `ps -ef | grep supervisor | grep -v grep | awk '{print $2}'`
sudo kill -9 `ps -ef | grep gunicorn | grep -v grep | awk '{print $2}'`
sudo kill -9 `ps -ef | grep celery | grep -v grep | awk '{print $2}'`


if [ "$RUN_ENV" == PROD ]; then
    sudo kill -9 `ps -ef | grep nginx | grep -v grep | awk '{print $2}'`
    sudo git pull origin master
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py collectstatic --noinput --clear
    sudo service nginx restart
fi


python manage.py supervisor -d





