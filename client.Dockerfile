# syntax=docker/dockerfile:1
FROM python:3.7-alpine
WORKDIR /clientdata
ENV FLASK_APP=runclient.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=80
COPY client.requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 80
COPY . .
CMD ["flask", "run"]
