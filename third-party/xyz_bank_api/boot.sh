#!/bin/sh
source venv/bin/activate
# flask db upgrade
# flask translate compile
exec gunicorn -b :5002 --access-logfile - --error-logfile - xyz_bank_api:app