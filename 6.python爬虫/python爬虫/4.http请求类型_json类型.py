#__author:  Administrator
#date:  2019/8/30

"""
http请求
使用场景：进行客户端与服务端之前的消息传递时使用
GET：通过URL网址传递信息，可以直接在URL网址上添加要传递的信息  不安全
POST：可以向服务器提交数据，是一种比较流行的比较安全的数据传递方式  安全
PUT：请求服务器，存储一个资源，通常要指定存储的位置
DELETE：请求服务器，删除一个资源，通常要指定存储的位置
HEAD:请求获取对应的HTTP报头的信息
OPTIONS: 可以获取当前URL所支持的请求类型

GET请求
特点：把数据拼接到请求路径的后面传递给服务器
优点：速度快
缺点：承载的数据量少，而且不安全
"""
import  urllib.request
#网络传输json格式的数据类型
url = "http://39.105.169.214:8083/citytxnservice/"
response = urllib.request.urlopen(url)
data = response.read().decode("utf-8")
print(data)

"""
json数据解释
概念：一种保存数据的格式
作用：可以保存本地的json文件，也可以将json串进行传输，
通常将json称为轻量级的传输方式
json文件组成
{} :代表对象{字典} 
[] :代表列表  
,  :代表键值对  
:  :分割两个部分 

"""
import  json
jsonStr = '{"name":"sunck","age":18,"hobby":["money","power","english"],"parames":{"a":1,"b":2}}'
#转为字典类型
jsonData = json.loads(jsonStr)
print(jsonData)
print(type(jsonData))
print(jsonData["hobby"])
#将python数据类型的对象转为json格式的字符串
jsonData2 = '{"name":"sunck","age":18,"hobby":["money","power","english"],"parames":{"a":1,"b":2}}'
#转为字符串类型
jsonStr2 = json.dumps(jsonData2)
print(jsonStr2)
print(type(jsonStr2))
#读取本地json文件
path1 = r"E:\python笔记\python爬虫\python爬虫\file\json1.json"
with open(path1,"rb") as f:
    data = json.load(f)
    print(data)
    #转换为字典类型
    print(type(data))
#写本地json
path2 = r"E:\python笔记\python爬虫\python爬虫\file\test.json"
jsonData3 = '{"name":"sunck","age":18,"hobby":["money","power","english"],"parames":{"a":1,"b":2}}'
with open(path2,"w") as f:
    json.dump(jsonData3,f)

"""
特点： 把参数进行打包，单独传输
优点：数量大，安全（当对服务器进行修改数据时建议使用post）
缺点：速度慢
"""
import urllib.response
import  urllib.parse
#post 打包依赖lib
#将要发送的数据合成一个字典
#字典的键
url = "http://39.105.212.52/cityconsole/login_toLogin.do?systemid=2"
data = {
    "loginname":"dev",
    "password":"123"
}
#对要发送的数据进行打包，记住编码
postData = urllib.parse.urlencode(data).encode("utf-8")
#请求体
req = urllib.request.Request(url,postData)
#添加请求头
req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",)
#发起请求获取返回信息
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))