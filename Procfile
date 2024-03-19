python manage.py migrate
python manage.py collectstatic --noinput
web: gunicorn juitform.wsgi:application --log-file - --log-level debug