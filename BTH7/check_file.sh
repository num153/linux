#!/bin/bash

if [ $# -ne 1 ]
then
	echo "Chua co ten file de check"
	exit 1
fi

dir=$1

if [ -f $dir ]
then
	echo "File $dir co ton tai"
else
	echo "File $dir khong ton tai"
fi
