FROM jenkins/inbound-agent:latest

USER root

RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv && \
    apt-get clean

RUN python3 -m venv /home/jenkins/venv

RUN /home/jenkins/venv/bin/pip install --upgrade pip 

ENV PATH="/home/jenkins/venv/bin:${PATH}"

USER jenkins