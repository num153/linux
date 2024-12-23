#!/usr/bin/env python3

ten=input("Nhap ten tep tin: ")
sodong=int(input("Nhap so dong muon doc: "))

with open(ten,'r',encoding='UTF8') as f:
	arr=[]
	for i in range(sodong):
		line=f.readline().strip()
		arr.append(line)
for i in arr:
	print(i)

so_dong=len(arr)
so_tu=0
so_ki_tu=0

for line in arr:
	so_tu+=len(line.split())
	so_ki_tu+=len(line)

with open('ketqua.txt','w',encoding='UTF8') as f:
	f.write(f"Thong tin tap tin {ten}\n")
	f.write(f"So luong dong: {so_dong} dong\n")
	f.write(f"So luong tu: {so_tu} tu\n")	
	f.write(f"So ki tu (k khoang trang): {so_ki_tu} ki tu\n")
	f.write("======================\n")
	f.write(f"{sodong} dong dau tien cua {ten} la:\n")
	for line in arr:
		f.write(line + '\n')
