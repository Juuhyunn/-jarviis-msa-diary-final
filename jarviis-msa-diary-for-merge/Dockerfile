#FROM python:3.8
FROM pytorch/pytorch

WORKDIR /app


COPY . .
COPY requirements.txt requirements.txt
COPY machine machine


ENV TZ=Asia/Seoul

RUN python3 -m pip install --upgrade pip

# jvm 설치
RUN apt-get update && \
    apt-get install -y openjdk-8-jdk
ENV JAVA_HOME="/usr/lib/jvm/java-1.8-openjdk"

RUN pip install JPype1
RUN pip install -U "jpype1<1.1"
RUN pip install --user konlpy
RUN python -m pip install tweepy==3.10.0
RUN pip install -r requirements.txt
ENV conda /opt/conda/bin
RUN conda install mysqlclient


