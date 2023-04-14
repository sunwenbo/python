#__author:  Administrator
#date:  2019/9/1
import re
import urllib.request
import ssl

def jokeCrawler(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
    }
	#创建请求体，使用自定义的请求头
    req = urllib.request.Request(url,headers=headers)
	#使用ssl创建未验证的上下文
    context = ssl._create_unverified_context()
	#发起请求使用未验证的上下文，打开请求的url
    response = urllib.request.urlopen(req, context=context)
    #response = urllib.request.urlopen(req)
	#将获取的内容赋值给HTML
    HTML = str(response.read().decode("utf-8"))
	#使用正则表达式定义一定的截取规则
    pat = r'<div class="author clearfix">(.*?)<span class="stats-vote"><i class="number">'
    # 编译
    re_joke = re.compile(pat, re.S)
    #按照正则表达式找出文件的内容
    divsList = re_joke.findall(HTML)
    # print(divsList)
    # print(len(divsList))
    dic = {}
    for div in divsList:
        #用户名
        re_u = re.compile(r"<h2>(.*?)</h2>",re.S)
        username = re_u.findall(div)
        username = username[0]
        #print(username)
        # 段子
        re_d = re.compile(r'<div class="content">\n<span>(.*?)</span>', re.S)
        duanzi = re_d.findall(div)
        duanzi = duanzi[0]
        #print(duanzi)
        dic[username] = duanzi
    return dic


url = "https://www.qiushibaike.com/text/page/4/"
info = jokeCrawler(url)
for k, v in info.items():
    print(k + "说\n" +v)
info = str(info)
print(info)
with open(r"E:\python笔记\python爬虫\python爬虫\file\csbk.html", "w") as f:
    f.write(info)
