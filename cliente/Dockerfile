FROM ubuntu:latest

MAINTAINER Andres calfulef "rcalfulef@gmail.com"

RUN apt-get update && apt-get install -y \
	python3 \
	python3-pip 

COPY client.py /usr/bin/client.py

CMD ["python3" ,"/usr/bin/client.py"]