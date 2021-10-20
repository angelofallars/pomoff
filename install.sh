#!/bin/bash

red='\e[0;31m'
green='\e[0;32m'
default='\e[0;m'

echo -e "Installing ${green}Pomoff${default}..."

# Install dependencies
if [ -f requirements.txt ]; then
    pip3 install -r requirements.txt
fi

# Warning if MPV not installed
which mpv > /dev/null 2>&1 || echo "${red}Warning:${default} mpv is not installed. Audio will not play."

# Add executable permission in script
chmod +x main.py

if [ -f /usr/bin/pomoff ]; then
    echo -e "${red}ERROR:${default} Pomoff already exists in /usr/bin/pomoff."
    exit 1
fi

# Add symbolic links
sudo ln -sf "$(pwd)/main.py" "/usr/bin/pomoff" && \
echo -e "Pomoff installed successfully. To run, type ${green}pomoff.${default}" || \
echo -e "${red}ERROR:${default} It seems like Pomoff failed to install."
