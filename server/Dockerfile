FROM python:3.6-jessie
ADD . /app
WORKDIR /app
RUN pip install --upgrade pip \
    && pip install pipenv gunicorn\
    && pipenv install --system --deploy
