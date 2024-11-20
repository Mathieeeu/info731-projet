#!/bin/bash

INTERFACE="eth5"
OUTPUT_FILE="/shared/tcpdump.dmp"

# Lancer tcpdump pour capturer le trafic HTTP
tcpdump -l -i $INTERFACE -A -s 0 "tcp port 80" | while read -r line; do
    # Verifier si le paquet est une page HTML
    echo "$line" | grep -q "Content-Type: text/html"
    if [ $? -eq 0 ]; then
        # Verifier si le paquet contient le mot banni
        echo "$line" | grep -q "Move"
        if [ $? -eq 0 ]; then
            echo "heeeey"
        else
            echo "hey"
        fi
    fi
done
