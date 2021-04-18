#__author:  Administrator
#date:  2020/3/11
import csv
from dealFile import DealFile

path0 = r'E:\python笔记\3.自动化办公\1.读写csv文件\00000000卡交易明细20200109143231.csv'
d = DealFile()   #实例化对象
info = d.readCsv(path0)
#print(info)
path1 = r'E:\python笔记\3.自动化办公\3.读取word文件\2.docx'
#doc = d.readWordFile(path1)
#print(doc)

for i in range(2,4):
    path = r"E:\python笔记\3.自动化办公\1.读写csv文件\00000000卡交易明细20200109143231.csv"
    listInfo = d.readCsv(path)
    toPath = r"E:\python笔记\3.自动化办公\1.读写csv文件\00000000卡交易明细2020010914323"+str(i)+".csv"
    d.writeCsv(toPath,listInfo)

allInfo = d.readCsv(toPath)