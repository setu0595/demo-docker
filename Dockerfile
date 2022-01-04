FROM ubuntu:latest

RUN apt-get update
RUN apt-get install vim -y
RUN apt-get install python3 -y
COPY src/server1.py /tmp/

EXPOSE 8181

CMD ["python3","/tmp/server1.py"]
