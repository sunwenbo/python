#__author:  Administrator
#date:  2019/9/1
import urllib.request
import ssl
import re
import os

def imagesCrawler(url,toPath):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
    }
    req = urllib.request.Request(url,headers=headers)
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(req,context=context)
    HtmlStr = response.read().decode("utf-8")
    # with open(r"E:\py练习\python爬虫\images\yhd.html","wb") as f:
    #     f.write(HtmlStr)
    pat = r'<img (src)="//(.*?)"/>'
    re_image = re.compile(pat,re.S)
    imagesList = re_image.findall(HtmlStr)
    print(imagesList)
    print(len(imagesList))
    print(imagesList[0])
    num = 1
    for imageUrl in imagesList:
        path = os.path.join(toPath, str(num)+".jpg")
        num += 1
        #把图片下载到本地存储
        urllib.request.urlretrieve("https://"+imageUrl,filename=path)
url = "https://search.yhd.com/c1343-0-0"
toPath = r'E:\py练习\python爬虫\images'
imagesCrawler(url, toPath)
