#!/bin/bash

echo "Nhap ten thu muc sao luu"
read backup

backup_path="$HOME/Desktop/$backup"
time=$(date +%H:%M:%S)
if [ ! -d $backup ];then
	echo "Thu muc chua ton tai. Tien hanh tao thu muc"
	mkdir $backup
fi

source_path="$HOME/Videos/Data"
if [ -d $source_path ];then
	#cp -r $source_path/* $backup_path
	backup_filename="Backup_$time.tar"
	tar -cf "$backup_path/$backup_filename" -c $source_path
	echo "Sao luu du lieu thanh cong"
else
	echo "Khong tim thay thu muc nguon"
fi
