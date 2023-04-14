#__author:  Administrator
#date:  2019/8/29
import urllib.request
import random
import re
url = "http://39.105.212.52/cityconsole/t_info_customer/listPages.do"
#模拟请求头 字典类型   浏览器的信息
#headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"}
headers = {
           #"Host": "http://39.105.212.52/cityconsole/t_info_customer/listPages.do",
           "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
           "Cookie": "JSESSIONID=DABA96F7D7CFC88CE86D727B60C88693; ace_skin=skin-1",
           "Referer": "http://39.105.212.52/cityconsole/"
          }
#设置一个请求体
req  = urllib.request.Request(url,headers=headers)
#发起请求
response = urllib.request.urlopen(req)
data = response.read().decode("utf-8")
print(data)
htmlStr = str(data)
pat = r'(((http|ftp|https)://)(([a-zA-Z0-9\._-]+\.[a-zA-Z]{2,6})|([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}))(:[0-9]{1,4})*(/[a-zA-Z0-9\&%_\./-~-]*)?)'
re_url = re.compile(pat)
urlsList = re_url.findall(htmlStr)
# 去重
qqsList = list(set(urlsList))
print(qqsList)


agentList =[
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; Tablet PC 2.0; .NET4.0E)"
]

#随机获取一个请求头
agentStr = random.choice(agentList)
#获取url的信息
req = urllib.request.Request(url)
#向请求体里添加了User-Agent
req.add_header("User-Agent", agentStr)
#req = <urllib.request.Request object at 0x00000000026E7C50>
response = urllib.request.urlopen(req)
data1 = response.read().decode("utf-8")
#print(data1)
print("#############################################")