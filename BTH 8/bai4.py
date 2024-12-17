#!/usr/bin/env python3

a=int(input("Nhap so thu 1: "))
b=int(input("Nhap so thu 2: "))
c=int(input("Nhap so thu 3: "))

max=a
if b > max:
	max=b
if c > max:
	max=c
print("So lon nhat la: ",max)
