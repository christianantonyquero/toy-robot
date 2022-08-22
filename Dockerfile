# syntax=docker/dockerfile:1
# FROM python:3.8-slim-buster

###################################
# Using the Ubuntu image. You can change this to the ubuntu version image you want to use
FROM ubuntu:latest

# Update package manager (apt-get)
# and install (with the yes flag `-y`)
# Python3 and Pip
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .
