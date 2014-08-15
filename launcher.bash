#!/bin/bash


for i in {9..27}; do 
	if [ -e  lecture$i.srt ]; then
		#~ python execute2.py lecture$i 
		python execute4.py lecture$i 0 
		#~ python execute5.py lecture$i 0
	fi
done 
