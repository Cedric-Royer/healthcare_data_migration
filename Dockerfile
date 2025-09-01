FROM python:3.11-slim
WORKDIR /app

COPY import_to_mongodb.py ./
COPY requirements.txt ./

ADD data /data

RUN pip install -r requirements.txt
