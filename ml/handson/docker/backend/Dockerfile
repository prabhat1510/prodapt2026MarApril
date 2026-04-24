FROM ubuntu:jammy

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository -y ppa:deadsnakes/ppa && \
    apt-get update && \
    apt-get install -y python3.11 python3.11-dev python3-pip

WORKDIR /app
COPY requirements.txt .
RUN rm -f /usr/bin/python && ln -s /usr/bin/python3.11 /usr/bin/python
RUN rm -f /usr/bin/python3 && ln -s /usr/bin/python3.11 /usr/bin/python3

RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn

ADD ./backend /app/backend
ADD ./docker /app/docker
ADD ./research /app/research

#RUN mkdir -p /app/backend/server/staticfiles
RUN mkdir -p /app/backend/server/static