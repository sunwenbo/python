#__author:  Administrator
#date:  2019/8/29

import urllib.request

# 向指定的url地址发起请求，并返回服务器响应的数据（文件的对象）

response = urllib.request.urlopen("http://cityservice.cityunion.org.cn/jkconsole/")
#读取文件的全部内容,会把读取到的数据赋值给一个字符串变量

data = response.read()
print(data)
print(type(data))

# data = response.readline()
#
# for i in data:
#     print(i)

#读取文件的全部内容，会把读取到的内容赋值给一个列表变量
# data = response.readlines()
# print(data)
# print(len(data))
# print(type(data[100].decode("utf-8")))

# #将爬取到的网页写入文件

with open(r"E:\python笔记\6.python爬虫\python爬虫\file1","wb") as f:
    f.write(data)

#response 属性
#返回当前环境的有关信息
print(response.info())
#返回状态码
print(response.getcode())
if response.getcode() == 200 or response.getcode ==304:
    #处理网页的信息
    pass
#返回当前正在爬取的URL地址
print(response.geturl())

#解码
url = r'https://baike.baidu.com/item/%E7%99%BE%E5%BA%A6/6699?fromtitle=baidu&fromid=107002&fr=aladdin'
newUrl1 = urllib.request.unquote(url)
print(newUrl1)
#编码
newUr2 = urllib.request.quote(newUrl1)
print(newUr2)

urllib.request.urlretrieve("http://www.baidu.com" ,
filename = r"E:\python笔记\6.python爬虫\python爬虫\file\file2.html")

#urlretrieve 在执行的过程中，会产生一些缓存，占用内存
#清楚缓存
#urllib.request.urlcleanup()