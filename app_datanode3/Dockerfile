FROM ubuntu:latest

MAINTAINER Andres calfulef "rcalfulef@gmail.com"

RUN apt-get update && apt-get install -y \
	python3 \
	python3-pip

COPY datanode.py /usr/bin/datanode.py

CMD ["python3" ,"/usr/bin/datanode.py"]
