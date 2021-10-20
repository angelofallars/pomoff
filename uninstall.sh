#!/bin/bash

green='\e[0;32m'
default='\e[0;m'

echo -e "Uninstalling ${green}Pomoff${default}..."

# Delete symbolic link
sudo rm /usr/bin/pomoff && \
echo -e "${green}Pomoff${default} successfully uninstalled."

