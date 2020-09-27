#!/bin/sh
source venv/bin/activate
# flask db upgrade
# flask translate compile
exec gunicorn --certfile fullchain.pem --keyfile privkey.pem -b :5000 --access-logfile - --error-logfile - app:app
