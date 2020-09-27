#!/bin/sh
source venv/bin/activate
# flask db upgrade
# flask translate compile
exec gunicorn -b :5001 --access-logfile - --error-logfile - abc_bank_api:app