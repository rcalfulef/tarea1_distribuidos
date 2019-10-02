FROM ubuntu:latest

MAINTAINER Andres calfulef "rcalfulef@gmail.com"

RUN apt-get update && apt-get install -y \
	python3 \
	python3-pip

RUN mkdir archivos

COPY datanode.py /

CMD ["python3" ,"./datanode.py"]
