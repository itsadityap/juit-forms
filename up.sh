#!/bin/bash
python manage.py makemigrations selfappraisal --noinput 
python manage.py migrate

if [[ "$1" == "-i" ]]; then
    python manage.py createsuperuser --username vaibhav --email vaibhav@example.com
fi