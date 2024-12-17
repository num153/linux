#!/usr/bin/env python3

chuoi1="Tri tue nhan tao mot ngay nao do co the thay the con nguoi trong mot so cong viec nhat dinh"
chuoi2="con nguoi ngay nay"

loai=chuoi2.split()

chuoinew=""

for word in chuoi1.split():
	if word not in loai:
		chuoinew+=word+" "
print(chuoinew)
