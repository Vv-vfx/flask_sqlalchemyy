FROM python:3

COPY ./ ./

COPY ./gunicorn/gunicorn_requirements.txt gunicorn_requirements.txt

RUN pip install -r gunicorn_requirements.txt

ENV STATIC_PATH /app/static
