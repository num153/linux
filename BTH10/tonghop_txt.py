#!/usr/bin/env python3

#Read txt
with open('file.txt','r',encoding='UTF8') as f:
	r=f.read()
	print(r)

with open('file.txt','r') as f:
	print(f.read(10))

#Write txt
with open('file2.txt','w') as f:
	f.write("Xin chao\n")
	f.write("Xin chao lan nua")

with open('file.txt','r') as f:
	data=f.readlines()
	for line in data:
		print(line)
	
