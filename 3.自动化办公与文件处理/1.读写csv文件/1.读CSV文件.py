#__author:  Administrator
#date:  2020/3/1
import csv
# class ReadCSV():
#     def readCsv(path):
#         with open(path,"r",encoding='utf-8') as f:
#             infoList = []
#             allFileInfo = csv.reader(f)
#             for row in allFileInfo:
#               infoList.append(row)
#             return infoList
#
# path = r'E:\python笔记\自动化办公\1.读写csv文件\00000000卡交易明细20200109143231.csv'
#
# info = ReadCSV.readCsv(path)
# print(info)



filepath = r'/Users/sunwenbo/Desktop/uat-stella-ks/stella-k8s/README.md'
tofilepath = r'/Users/sunwenbo/Desktop/uat-stella-ks/stella-k8s/README1.md'

files = ""

with open(filepath,"r",encoding='utf-8') as f :
    valuesline = f.readlines()
    for i in valuesline:
        files += i
    print(files)

with open(tofilepath,"w", encoding='utf-8') as f1:
    for i in valuesline:
        f1.write(i)
