# 爬虫使用cookie
from urllib import request
if __name__ == '__main__':
    url = "http://47.93.49.242:8080/cityconsole/t_info_customer/listPages.do"
    headers = {
        # Cookie值从登录后的浏览器，拷贝，方法文章上面有介绍
        "Cookie": "JSESSIONID=B1A6DF553E220A8A0D81C34631F1C9A6; ace_skin=skin-3",
        "Referer": "JSESSIONID=B1A6DF553E220A8A0D81C34631F1C9A6; ace_skin=skin-3"
    }
    req = request.Request(url=url,headers=headers)
    rsp = request.urlopen(req)
    html = rsp.read().decode()

    with open(r"E:\python笔记\python爬虫\python爬虫\file\test.html","w",encoding="utf-8")as f:
        # 将爬取的页面
        print(html)
        f.write(html)

import requests
headers = {
    'Referer': 'http://www.sse.com.cn/assortment/stock/list/share/'
}
url = 'http://query.sse.com.cn/security/stock/getStockListData2.do?&jsonCallBack=jsonpCallback96332&isPagination=true&stockCode=&csrcCode=&areaName=&stockType=1&pageHelp.cacheSize=1&pageHelp.beginPage=1&pageHelp.pageSize=25&pageHelp.pageNo=2&pageHelp.endPage=21&_=1522509003629'
response = requests.get(url, headers=headers)
print(response.text)

