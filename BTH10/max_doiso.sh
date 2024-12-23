#!/bin/bash

if [ $# -lt 1 ]
then
	echo "Khong co doi so nao!"
fi

max=$1

for num in "$@";do
	if [ "$num" -gt "$max" ];then
		max=$num
	fi
done

echo "So lon nhat: $max"
echo "Chuong trinh tim so max " > max.txt
echo "============= " >> max.txt
echo "So luong doi so: $# so" >> max.txt
echo "So max la: $max" >> max.txt
