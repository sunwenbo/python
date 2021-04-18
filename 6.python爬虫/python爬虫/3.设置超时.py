#__author:  Administrator
#date:  2019/8/30
import urllib.request
import re
#如果网页长时间未响应，系统判断超时，无法爬去

for i in range(1,100):
    try:
        response = urllib.request.urlopen("http://www.baidu.com",timeout=0.5)
        a = response.read().decode("utf-8")
        htmlStr = str(a)
        pat = r'(((http|ftp|https)://)(([a-zA-Z0-9\._-]+\.[a-zA-Z]{2,6})|([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}))(:[0-9]{1,4})*(/[a-zA-Z0-9\&%_\./-~-]*)?)'
        re_url = re.compile(pat)
        urlsList = re_url.findall(htmlStr,1)
        # 去重
        qqsList = list(set(urlsList))
        print(qqsList)

        #print(len(response.read().decode("utf-8")))
    except:
        print("请求失败，继续下一次爬取")
