#!/usr/bin/env python3

n=int(input("Nhap so luong ds:"))
arr=[]

for i in range(n):
	print("Nhap so thu",i+1)
	num=int(input())
	while(num<100 or num>999):
		num=int(input("Nhap lai (100-999): "))
	arr.append(num)

sum=0
for i in range (n):
	sum+=arr[i]
print("Tong:",sum)
