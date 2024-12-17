#!/bin/bash

echo "Nhap ten file can tim"
read name

if [ -z $name ]
then
	echo "Chua co ten file"
	exit 1
fi

if [ -f $name ]
then
	echo "Tep tin ton tai o $(realpath $name)"
else
	echo "Tep tin khong ton tai"
fi
