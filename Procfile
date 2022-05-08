release: python3 manage.py migrate
web: daphne housieme.asgi:application -p $PORT --bind 0.0.0.0 -v2
