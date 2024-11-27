#Commande pour créer l'image (il faut se placer dans le repertoire)
#docker build -t kathara-freedonia .

# Pour l'instant, on met xtrm0 en plus mais c'est pas opti, beaucoup trop lourd et pas foufou => meilleure solution à trouver.....
FROM kathara/base
FROM xtrm0/quagga 

ARG DEBIAN_FRONTEND="noninteractive"
RUN apt update
RUN apt upgrade -y

RUN apt install -y \
	openbsd-inetd \
	telnetd \
	python3-pip \
	python3-mysqldb

RUN useradd -m -p $(perl -e 'print crypt($ARGV[0], "password")' 'telnet') telnet
