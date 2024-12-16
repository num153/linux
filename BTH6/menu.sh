#!/bin/bash

cong() {
	echo "Cong: $(($1+$2))"
}

chia() {
	if [ $2 -eq 0 ]; then
		echo "Khong the chia cho 0"
	else
		echo "Chia: $(($1/$2))"
	fi
}

while true; do
	echo "1. Phep cong"
	echo "2. Phep chia"
	echo "Lua chon"
	read choice

echo "Nhap so thu 1"
read a
echo "Nhap so thu 2"
read b

case $choice in
1)
	cong $a $b;;
2)
	chia $a $b;;
*)
	echo "Lua chon khong hop le";;
esac
done

