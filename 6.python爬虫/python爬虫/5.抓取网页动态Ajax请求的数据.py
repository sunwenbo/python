#__author:  Administrator
#date:  2019/9/1
import urllib.request
import ssl
import json
def ajaxCrawler(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
    }
    req = urllib.request.Request(url,headers=headers)
    #使用ssl创建未验证的上下文
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(req,context=context)
    jsonStr = response.read().decode("utf-8")
    jsonData = json.loads(jsonStr)
    return jsonData

# url = "https://movie.douban.com/j/chart/top_list?type=17&interval_id=100%3A90&action=&start=40&limit=20"
# info = ajaxCrawler(url)
# print(info)
for i in range(1,8):
    url = "https://movie.douban.com/j/chart/top_list?type=17&interval_id=100%3A90&action=&start="+ str(i * 20)+"&limit=20"
    info = ajaxCrawler(url)
    with open(r'E:\python笔记\python爬虫\python爬虫\file\test.txt',"a") as f:
        json.dump(info, f)