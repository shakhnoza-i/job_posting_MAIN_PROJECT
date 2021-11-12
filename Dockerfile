FROM python:3.10.0-slim-buster
# if not set it - python create the PYC based files for all our python files
ENV PYTHONDONTWRITEBYTECODE 1
# to see the output of your application (e.g.logs) in real time without buffering
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./requirements.txt /requirements.txt

RUN pip3 install -r /requirements.txt

COPY . /app/
