#!/usr/bin/env python3
import csv
#Read csv file
with open('sinhvien.csv') as f:
	r = csv.reader(f)
	next(r) #bo di dong dau tien
	for line in r:
		print(line[1])

#Write csv file
with open('new_sinhvien.csv','a') as f:
	w = csv.writer(f)
	w.writerow(['An','30','IT','HCM'])
	w.writerow(['Thanh','25','Dev','Binh Duong'])
	#khong can tao, no tu tao, dung bo quen 'w' hoac 'a'

#Create .csv from pre-exist data
header=['Ho ten','Dia chi','Thanh pho','Sdt']
data=[
	['Tran Van A','123 so 12','Dong nai','345345'], #chu y dau phay
	['Le Thi B','1 so 12','Binh Duong','345345'],
	['Dang Thi C','123 so 12','Dong nai','345345']
]
with open('country.csv','w',encoding='UTF8',newline='') as f:
	w = csv.writer(f)
	w.writerow(header)
	w.writerows(data)

#Create .csv from .txt
txt_file=open('sinhvien.txt','r')
noidung=csv.reader(txt_file,delimiter=',')

csv_file=open('new_sinhvien2.csv','w',newline='')
file_csv_moi=csv.writer(csv_file)
file_csv_moi.writerows(noidung)

txt_file.close()
csv_file.close()

#BAI_TAP_6

#tao file nhansu.txt
data_ns=[
	['MaNV','HoTen','NamSinh','DiaChi'],
	['NV01','Tran Van Qua','2003','Da Nang'],
	['NV02','Le Thi But','2003','Da Nang'],
	['NV03','Nguyen La La','2003','Da Nang']
]
with open('nhansu.txt','w',encoding='UTF8',newline='') as f:
	ns=csv.writer(f,delimiter='\t')
	ns.writerows(data_ns)
#tao nhansu.csv tu .txt
with open('nhansu.txt','r') as f_txt:
	noidung_ns=csv.reader(f_txt,delimiter='\t')
	with open('nhansu.csv','w',newline='') as f:
		w=csv.writer(f,delimiter='\t')
		w.writerows(noidung_ns)
#in ra tieu de cua cac cot trong nhansu.csv
with open('nhansu.csv','r') as f:
	r=csv.reader(f,delimiter='\t')
	head=next(r)
	print(head)
	print("\t".join(head)) #noi thanh chuoi cach nhau boi tab
#doc va in NOI DUNG cua nhansu.txt
with open('nhansu.txt','r') as f:
	r=csv.reader(f,delimiter='\t')
	next(r)
	print("=======Noi dung cua nhansu.txt======")
	for line in r:
		print("\t".join(line))
