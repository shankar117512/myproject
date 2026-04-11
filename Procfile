web: sh -c "python manage.py collectstatic --noinput &&  config.wsgi:application --bind 0.0.0.0:$PORT"
release: python manage.py migrate --noinput
