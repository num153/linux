#!/bin/bash

if [ $# -ne 3 ]; then
	echo "Loi doi so!"
	exit 1
fi

tong=$(($1+$2+$3))

echo "Tong: $tong"
