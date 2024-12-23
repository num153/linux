#!/usr/bin/env python3

#hien thi 2 dong dau cua txt
with open('text1.txt','r') as f:
	r=f.readlines()
print("Hai dong dau cua van ban")
for i in range(2):
	print(r[i].strip())
print("====================")
with open('text1.txt','r') as f:
	mang1=f.read().lower().split()
with open('text2.txt','r') as f:
	mang2=f.read().lower().split()


arr1=set(mang1)
arr2=set(mang2)
arr3=arr1.intersection(arr2)

chuoi=" ".join(arr3)
print(chuoi)

so_tu_giong=len(arr3)
tong_tu=len(arr1)+len(arr2)

if tong_tu != 0:
	ty_le=(so_tu_giong*2/tong_tu)*100
else:
	ty_le=0
print("Ty le giong nhau: ",ty_le)



