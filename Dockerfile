FROM python:3.10.4-slim
LABEL maintainer="edlrian814@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR app/

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git

COPY requirements.txt requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install git+https://github.com/liqpay/sdk-python#egg=liqpay-python
RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /vol/web/media

RUN adduser \
    --disabled-password \
    --no-create-home \
    django-user

RUN chown -R django-user:django-user /vol/
RUN chmod -R 755 /vol/web/
RUN chgrp -R www-data /vol/web/
RUN chmod -R g+w  /vol/web/

USER django-user
