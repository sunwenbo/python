#__author:  Administrator
#date:  2020/3/1
import csv

def writeCsv(path,data):
    with open(path,"w",encoding="utf-8",newline="") as f:
        write = csv.writer(f)
        for rowData in data:
            write.writerow(rowData)

path = r'E:\python笔记\自动化办公\1.读写csv文件\00000000卡交易明细20200109143232.csv'

writeCsv(path,[[1,2,3],[4,5,6],[7,8,9]])