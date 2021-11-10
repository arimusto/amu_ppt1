# syntax=docker/dockerfile:1
FROM python:3.7-alpine
WORKDIR /serverdata
ENV FLASK_APP=runserver.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000
COPY server.requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]
