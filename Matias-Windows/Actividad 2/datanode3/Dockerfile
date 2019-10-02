FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
	python3 \
	python3-pip 

ADD datanode.py /
CMD [ "python3", "./datanode.py" ]

