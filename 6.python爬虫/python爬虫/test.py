import requests
#url = "https://www.douban.com/group/topic/110094603/"
url = 'http://query.sse.com.cn/security/stock/getStockListData2.do?&jsonCallBack=jsonpCallback96332&isPagination=true&stockCode=&csrcCode=&areaName=&stockType=1&pageHelp.cacheSize=1&pageHelp.beginPage=1&pageHelp.pageSize=25&pageHelp.pageNo=2&pageHelp.endPage=21&_=1522509003629'

response = requests.get(url)
with open(r"E:\python笔记\python爬虫\python爬虫\file\test.txt" ,"w",encoding="utf-8") as f:
    f.write(response.text)
print(response.text)

headers = {
    'Referer': 'http://www.sse.com.cn/assortment/stock/list/share/'
}
url = 'http://query.sse.com.cn/security/stock/getStockListData2.do?&jsonCallBack=jsonpCallback96332&isPagination=true&stockCode=&csrcCode=&areaName=&stockType=1&pageHelp.cacheSize=1&pageHelp.beginPage=1&pageHelp.pageSize=25&pageHelp.pageNo=2&pageHelp.endPage=21&_=1522509003629'
response = requests.get(url, headers=headers)
print(response.text)

import time

a = time.time()
print(a)
b = time.ctime(a)
print(b)
c = time.gmtime(a)
print(c)
d = time.asctime(c)
print(d)
e = time.localtime()
print(e)
f = time.asctime(e)
print(f)
g = time.strftime(b)
print(g)
print(time.strftime('%Y-%m-%d %X',e))
h = time.clock()
print(h)