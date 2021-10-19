#!/bin/bash

if [ $USER != 'root' ]; then 
	echo 'Need root privileges'
	exit 1
fi

# delete symbolic links
rm /usr/bin/pomoff

