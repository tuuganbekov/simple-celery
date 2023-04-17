# simple-celery
django-server: python manage.py runserver
celery worker: celery -A config worker -l INFO
celery beat: celery -A config beat -l INFO