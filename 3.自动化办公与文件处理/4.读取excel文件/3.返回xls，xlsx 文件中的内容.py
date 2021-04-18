#__author:  Administrator
#date:  2020/3/8
#需要安装 pyexcel pyexcel-xls ordereddict(有序的字典) pyexcel-io xlwt-future future xlrd openpyxl
#导入有序字典
from collections import OrderedDict
from pyexcel_xls import get_data

def readXlsAndXlsxFile(path):
    dic = OrderedDict()
    #抓取数据,获取excel表中所有的数据
    xdata = get_data(path)
    for sheet in xdata:
        dic[sheet] = xdata[sheet]
        return dic
path = r'E:\python笔记\3.自动化办公\4.读取excel文件\加密机_密钥接口分析.xls'
dic = readXlsAndXlsxFile(path)
print(dic)
print(len(dic))