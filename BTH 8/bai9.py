#!/usr/bin/env python3

n=int(input("Nhap so n (10-99): "))
while n<10 or n>99:
	n=int(input("Nhap lai so n (10-99): "))

for i in range(10):
	print(n+i*3)

