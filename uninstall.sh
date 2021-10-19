#!/bin/bash

red='\e[0;31m'
green='\e[0;32m'
default='\e[0;m'

if [ $USER != 'root' ]; then 
	echo -e "${red}Need root privileges ${default}"
	exit 1
fi

# delete symbolic links
rm /usr/bin/pomoff

echo -e "${green}Success 👌🏾 ${default}"

