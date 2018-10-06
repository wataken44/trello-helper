FROM wataken44/ubuntu-latest-sshd
LABEL maintainer "wataken44"

ENV DOCKER "YES"
ENV LANG C.UTF-8

RUN set -xe \
    && apt update -y \
    && apt dist-upgrade -y \
    && apt install -y python3 python3-pip git-core

USER ubuntu

RUN set -xe \
    && cd /home/ubuntu/ \
    && git clone https://github.com/wataken44/trello-helper

USER root

RUN set -xe \
    && cd /home/ubuntu/trello-helper \
    && pip3 install -r requirements.txt

EXPOSE 22
