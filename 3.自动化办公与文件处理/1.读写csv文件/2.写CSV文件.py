#__author:  Administrator
#date:  2020/3/1
import csv

def writeCsv(path,data):
    with open(filedata,"r",encoding="utf-8") as data:
        fileinfo = data.readlines()
        print(fileinfo)
        print(type(fileinfo))

    with open(path,"a",encoding="utf-8",newline="") as f:
        #write = f.write()
        # write.writerow(fileinfo)
        for rowData in fileinfo:
            f.write(rowData)

path = r'/Users/sunwenbo/Downloads/python/3.自动化办公与文件处理/1.读写csv文件/00000000卡交易明细20200109143233.csv'

filedata = r'/Users/sunwenbo/Downloads/python/3.自动化办公与文件处理/1.读写csv文件/1.读CSV文件.py'

writeCsv(path,filedata)