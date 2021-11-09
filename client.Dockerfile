# syntax=docker/dockerfile:1
FROM python:3.7-alpine
WORKDIR /clientdata
COPY . .
