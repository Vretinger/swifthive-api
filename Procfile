release: python manage.py makemigrations && python manage.py migrate
 web: pip install --no-cache-dir -r requirements.txt && gunicorn swifthive_api.wsgi