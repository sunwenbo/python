#__author:  Administrator
#date:  2019/9/1

import  urllib.request
import ssl
import re
import os
from collections import deque
def writeFilyByte(htmlBytes,toPath):
    with open(toPath,"wb") as f:
        f.write(htmlBytes)
def writeFileStr(htmlBytes,toPath):
    with open(toPath,"w") as f:
        f.write(str(htmlBytes))
def getHtmlBytes(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
    }
    req = urllib.request.Request(url, headers=headers)
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(req, context=context)
    return  response.read()
def qqCrawler(url, toPath):
    htmlBytes = getHtmlBytes(url)
    #writeFilyByte(htmlBytes,r"E:\py练习\python爬虫\file\qqFile1.html")
    #writeFileStr(htmlBytes,r"E:\py练习\python爬虫\file\qqFile2.html")
    htmlStr = str(htmlBytes)
    pat = r"[1-9]\d{5,9}"
    re_qq = re.compile(pat)
    qqsList = re_qq.findall(htmlStr)
    #去重
    qqsList = list(set(qqsList))
    print("@@@@@@@@@@@@@",qqsList)
    f=open(toPath,"a")
    for qqStr in qqsList:
        f.write(qqStr+"\n")
    f.close()

    pat = r'(((http|ftp|https)://)(([a-zA-Z0-9\._-]+\.[a-zA-Z]{2,6})|([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}))(:[0-9]{1,4})*(/[a-zA-Z0-9\&%_\./-~-]*)?)'
    re_url = re.compile(pat)
    urlsList = re_url.findall(htmlStr)
    urlsList = list(set(urlsList))
    return urlsList
# url = "https://www.douban.com/group/topic/110094603/"
# toPath = r"E:\py练习\python爬虫\file\qqFile.txt"
# qqCrawler(url,toPath)

def center(url,toPath):
    queue = deque()
    queue.append(url)
    while len(queue) != 0:
        targetUrl = queue.popleft()
        urlList = qqCrawler(targetUrl, toPath)
        for item in urlList:
            print(item)
            tempUrl = item[0]
            print(tempUrl)
            queue.append(tempUrl)

url = "https://www.douban.com/group/topic/110094603/"
toPath = r"E:\python\6.python爬虫\python爬虫\file\qqFile.txt"

center(url,toPath)