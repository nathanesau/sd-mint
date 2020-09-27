#!/bin/sh
source venv/bin/activate
# flask db upgrade
# flask translate compile
exec gunicorn -b :5003 --access-logfile - --error-logfile - xyz_trade_api:app