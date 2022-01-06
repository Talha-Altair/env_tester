FROM docker.io/python:3.9.7-slim-buster

ADD . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD [ "python3" , "app.py" ]