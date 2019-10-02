FROM ubuntu:latest

MAINTAINER Andres calfulef "rcalfulef@gmail.com"

RUN apt-get update && apt-get install -y \
	python3 \
	python3-pip 

RUN mkdir /usr/bin/archivos

COPY headnode.py /usr/bin/archivos/headnode.py

CMD ["python3" ,"/usr/bin/archivos/headnode.py"] 
