FROM kathara/base 

ARG DEBIAN_FRONTEND="noninteractive"
RUN apt update
RUN apt upgrade -y

RUN apt install -y \
	openbsd-inetd \
	telnetd \
	python3-pip

RUN python3 -m pip install --no-cache-dir --break-system-packages requests

RUN useradd -m -p $(perl -e 'print crypt($ARGV[0], "password")' 'telnet') telnet
