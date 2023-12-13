FROM tiangolo/uwsgi-nginx-flask:python3.11

COPY ./prod/prod_requirements.txt /app/prod_requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/prod_requirements.txt

COPY ./ /app

ENV STATIC_PATH /app/app/static

#RUN adduser --disabled-password --gecos '' appuser
#USER appuser