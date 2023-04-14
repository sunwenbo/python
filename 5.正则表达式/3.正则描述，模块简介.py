#__author:  Administrator
#date:  2020/3/15
'''
Python自1.5以后增加了re的模块，提供了正则表达式模式，
re模块使python语言拥有了全部的正则表达式功能
'''
import re

'''
re.match 函数
原型：match(pattern,string,flags=0)
参数：
patter  匹配的正则表达式
string  要匹配的字符串
flags   标志位，用于控制正则表达式的匹配方式
re.I  忽略大小写
re.L  做本地化识别
re.M  多行匹配，会影响^和$
re.S  使.匹配包括换行符在内的所有字符
re.U  根据Unicode字符集解析字符，影响\w \W \b \B 元字符
re.X  使我们更灵活的格式理解正则表达式
功能：尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，也会返回None

'''

# www.baidu.com
print(re.match("www","ww.baidu.com"))
print(re.match("www","www.baidu.com").span())   #返回匹配的下标位
print(re.match("www","baidu.wwwcom"))   #从起始位置开始匹配，
print(re.match("www","wwW.baidu.com",flags=re.I))
#扫描整个字符串，返回从起始位置成功的匹配

print("--------------------------")
'''
re.search 
原型：search(pattern, string, flags=0)
参数：
patter  匹配的正则表达式
string  要匹配的字符串
flags   标志位，用于控制正则表达式的匹配方式
功能：扫描整个字符串，并返回第一个匹配成功的

'''
print(re.search("sunwenbo","good man is Sunwenbo!sunwenbo is nice",flags=re.I))

'''
re.findall
原型：search(pattern, string, flags=0)
参数：
patter  匹配的正则表达式
string  要匹配的字符串
flags   标志位，用于控制正则表达式的匹配方式
功能：  扫描整个字符串，并返回结果列表

'''
print(re.findall("sunwenbo","good man is Sunwenbo!sunwenbo is nice",flags=re.I))
