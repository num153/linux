#!/bin/bash

if [ $# -ne 1 ]; then
	echo "Chua co ten folder can check"
	exit 1
fi

dir=$1
# -d tra ve bool cho folder
if [ -d $dir ]; then
	echo "Thu muc $dir co ton tai"
	exit 0
else
	echo "Thu muc $dir khong ton tai"
	exit 0
fi


