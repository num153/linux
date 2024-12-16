#!/bin/bash


check_valid() {
	if [[ $1 -lt 10 || $1 -gt 99 ]]; then
		echo "Nam ngoai tu 10 den 99"
		exit 1
	fi
}

echo "Nhap so thu 1"
read a
check_valid $a
echo "Nhap so thu 2"
read b
check_valid $b
echo "Nhap so thu 3"
read c
check_valid $c

tong=$((a+b+c))

echo "Tong: $tong"


