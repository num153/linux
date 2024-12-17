#!/usr/bin/env python3

n=int(input("Nhap so luong ds so: "))

arr=[]

for i in range(n):
	num=int(input("Nhap so: "))
	arr.append(num)
maxx=arr[0]

for i in range(1,n):
	if(arr[i]>maxx):
		maxx=arr[i]
print("So lon nhat la:",maxx)
print("So lon nhat theo max() la:",max(kq))



