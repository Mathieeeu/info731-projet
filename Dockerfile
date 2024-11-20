FROM kathara/base 

ARG DEBIAN_FRONTEND="noninteractive"
RUN apt update
RUN apt upgrade -y

RUN apt install -y \
	openbsd-inetd \
	telnetd

RUN apt-get install python3-pip -y

RUN useradd -m -p $(perl -e 'print crypt($ARGV[0], "password")' 'telnet') telnet
