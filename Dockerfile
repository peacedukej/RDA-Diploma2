FROM python:3.11

ADD ./RDA /app
WORKDIR /app

RUN pip install --upgrade pip && pip install -r requirements.txt