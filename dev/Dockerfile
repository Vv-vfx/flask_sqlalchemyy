FROM python:3

COPY ./ ./

COPY ./dev/dev_requirements.txt dev_requirements.txt

RUN pip install -r dev_requirements.txt

ENV STATIC_PATH /app/static