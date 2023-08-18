#!/bin/bash
python manage.py makemigrations selfappraisal --noinput 
python manage.py migrate

if [[ "$1" == "-i" ]]; then
    python manage.py createsuperuser --username vaibhav --email vaibhav@example.com
fi

if [[ "$1" == "-r" ]]; then
    pip freeze > requirements.txt
    pip install -r requirements.txt
fi