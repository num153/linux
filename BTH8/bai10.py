#!/usr/bin/env python3

chuoi=input("Nhap mot chuoi: ")
chu=0;
for i in range(len(chuoi)):
	if chuoi[i].isalpha():
		chu=chu+1
print("Chu trong chuoi: ",chu)
print("Tong ky tu trong chuoi: ",len(chuoi))
