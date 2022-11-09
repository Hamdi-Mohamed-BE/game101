FROM python:3.9

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get -y dist-upgrade
RUN apt install -y netcat

COPY ./requirements.txt /requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r /requirements.txt
RUN pip3 install spotipy --upgrade


RUN mkdir /app
WORKDIR /app

COPY entrypoint.sh /entrypoint.sh
#.sh problem
# this for windows users / wsl users
RUN sed -i 's/\r$//' $app/entrypoint.sh  && \  
        chmod +x $app/entrypoint.sh

COPY ./app /app
RUN mkdir /tmp/runtime-user

ENTRYPOINT ["/entrypoint.sh"]

