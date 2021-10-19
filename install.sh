#!/bin/bash

if [ $USER != "root" ]; then
	echo 'need root privileges'
	exit 1 
fi

# Installation dependances
if [ -f requirements.txt ]; then 
	pip3 install -r requirements.txt 
fi

# Add header script
sed -i '1 i #!/usr/bin/python3' main.py

# Add executable permission in script
chmod +x main.py

# Add symbolic links 
ln -sf `pwd`/main.py /usr/bin/pomoff


