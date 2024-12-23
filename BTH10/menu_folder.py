#!/bin/bash

while true; do
echo "====CHUONG TRINH TAO-XOA THU MUC===="
echo "1. Tao thu muc"
echo "2. Xoa thu muc"
echo "3. Thoat"
echo "Lua chon cua ban: "
read choice

case $choice in
1)
	echo "Nhap ten thu muc: "
	read tenthumuc
	if [ -d $tenthumuc ];then 
		echo "Thu muc da ton tai"
	else
		echo "Tao thu muc thanh cong!!"
		mkdir $tenthumuc
	fi
;;
2)
	echo "Nhap ten thu muc: "
	read tenthumuc
	if [ ! -d $tenthumuc ];then 
		echo "Thu muc khong ton tai"
	else
		rm -r $tenthumuc
		echo "Xoa thu muc thanh cong!!"
		
	fi
;;
3)
	exit 0
;;
*)
	echo "Lua chon khong hop le"
;;
esac
done

