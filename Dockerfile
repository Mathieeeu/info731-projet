#Commande pour créer l'image 
#docker build -t kathara-freedonia .

FROM kathara/base

ARG DEBIAN_FRONTEND="noninteractive"
RUN apt update
RUN apt upgrade -y

RUN apt install -y \
	openbsd-inetd \
	telnetd \
	python3-pip

RUN apt install python3-requests -y

RUN useradd -m -p $(perl -e 'print crypt($ARGV[0], "password")' 'telnet') telnet
