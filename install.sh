#!/bin/bash

red='\e[0;31m'
green='\e[0;32m'
default='\e[0;m'

if [ $USER != "root" ]; then
	echo -e "${red}Need root privileges ${default}"
	exit 1 
fi

# Installation dependances
if [ -f requirements.txt ]; then 
	pip3 install -r requirements.txt 
fi

# Add executable permission in script
chmod +x main.py
 
if [ -f /usr/bin/pomoff ]; then 
       echo  -e "${red}pomoff already exist ${default}"
       exit 1
fi

# Add symbolic links
ln -sf `pwd`/main.py /usr/bin/pomoff

echo -e "${green}Success 👌🏾 ${default}"
