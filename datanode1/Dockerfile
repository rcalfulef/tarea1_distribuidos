FROM ubuntu:latest

MAINTAINER Andres calfulef "rcalfulef@gmail.com"

RUN apt-get update && apt-get install -y \
	python3 \
	python3-pip

RUN mkdir /usr/bin/archivos

COPY datanode.py /usr/bin/archivos/datanode.py

CMD ["python3" ,"/usr/bin/archivos/datanode.py"]
