FROM python:3.6-alpine

RUN apk update
RUN apk add python3-dev
#RUN apk add libpq
#RUN apk add --virtual .build-deps gcc python3-dev musl-dev postgresql-dev

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
COPY app.py ./
COPY boot.sh ./

# ssl keys
COPY fullchain.pem .
COPY privkey.pem .

RUN chmod +x boot.sh

ENV FLASK_APP app.py

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
