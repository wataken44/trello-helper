FROM wataken44/ubuntu-latest-sshd
LABEL maintainer "wataken44"

ENV DOCKER "YES"
ENV LANG C.UTF-8

RUN set -xe \
    && apt update -y \
    && apt dist-upgrade -y \
    && apt install -y python3 python3-pip git-core cron

USER ubuntu

RUN set -xe \
    && cd /home/ubuntu/ \
    && git clone https://github.com/wataken44/trello-helper

RUN set -xe \
    && mkdir /home/ubuntu/bin \
    && cd /home/ubuntu/bin \
    && echo '#!/bin/sh' > run.sh \
    && echo 'cd /home/ubuntu/trello-helper/trello_helper' >> run.sh \
    && echo 'python3 add_periodical_task.py' >> run.sh \
    && echo 'python3 fill_due.py' >> run.sh \
    && chmod 755 run.sh

RUN set -xe \
    && mkdir /home/ubuntu/tmp/ \
    && cd /home/ubuntu/tmp/ \
    && echo '5  0  *  *  *  /home/ubuntu/bin/run.sh' > crontab.txt
    
USER root

RUN set -xe \
    && cd /home/ubuntu/trello-helper \
    && pip3 install -r requirements.txt

EXPOSE 22
CMD service cron start && service ssh start && tail -f /dev/null
