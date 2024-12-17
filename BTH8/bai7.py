#!/usr/bin/env python3

n=int(input("Nhap so luong n: "))

arr = []

for i in range (n):
	print("Nhap so thu ",i+1)
	num=int(input())
	if num%2==0:
		arr.append(num)

for i in arr:
	print(i)
	
