FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
	python3 \
	python3-pip 

ADD headnode.py /
CMD [ "python3", "./headnode.py" ]

