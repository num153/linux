#!/bin/bash

user=$(whoami)
host=$(hostname)
time=$(date +%H:%M:%S)
gio=$(date +%H)
buoi=""

if [ $gio -ge 0 -a $gio -lt 11 ]
then
	buoi="sang"
elif [ $gio -gt 11 -a $gio -lt 14 ]
then
	buoi="trua"
elif [ $gio -gt 14 -a $gio -lt 16 ]
then
	buoi="chieu"
else 	
	buoi="toi"
fi

echo "Xin chao ban $user"
echo "May tinh: $host"
echo "Hien tai: $time"
echo "Xin chao buoi $buoi"
