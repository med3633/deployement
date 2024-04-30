#!/bash/bin
# I will create the step of running django project
python manage.py migrate --no-input
# collect all static file needed for this
python manage collectstatic --no-input
#run django server
# gunicorn khedma.wsgi:application --bind 0.0.0.0:8000
python manage.py runserver