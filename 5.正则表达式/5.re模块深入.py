#__author:  Administrator
#date:  2020/3/19

import re
'''
字符串的切割
'''
str1 = "sunwenbo   is a good man"
#print(str1.split("#"))
print(re.split(r" +",str1))
'''
re.finditer函数
原型：re.finditer(pattern, string, flags=0)
参数：
patter  匹配的正则表达式
string  要匹配的字符串
flags   标志位，用于控制正则表达式的匹配方式
功能：与findall类似，扫描整个字符串，返回的是一个迭代器
'''

str3 = "sunwenbo is a good man! sunwenbo is a nice man!"
d = re.finditer(r"(sunwenbo)",str3)
while True:
    try:
        l = next(d)
        print(l)
    except StopIteration as e:
        break
"""
字符串的替换和修改
sub(pattern, repl, string, count=0, flags=0)
subn(pattern, repl, string, count=0, flags=0)
pattern:正则表达式(规则)
repl:指定的用来替换的字符串
string:目标字符串
count:最多替换次数
flags:
功能：在目标字符串以正则表达式的规则匹配字符串,再把它们替换成指定的字符串，可以指定替换的次数，如果不指定会替换所有的指定的字符串
区别：前者返回一个被替换的字符串，后者返回一个元组，第一个函数被替换的字符串，第二个函数表示被替换的次数
"""
str4 = "sunwenbo is a good man! sunwenbo is a good man!\nsunwenbo is a good man!"
print(re.sub(r"(good)","nice",str4,count=0))  #返回字符串，全部替换包括换行符
print(re.subn(r"(good)","nice",str4)) #返回元组类型

'''
分组：
概念：除了简单的判断是否匹配之外，正则表达式还有提取子串的功能，用()表示的就是提取的分组
'''

str5 = "010-532476545"

m = re.search(r"(?P<first>(?P<last>\d{3})-(\d{5})(\d{4}))",str5)
print(m.group(0))
print(m.group("last"))   #起名字
print(m.group(2))
print(m.group(3))
print(m.group(4))

#查看匹配的各组的元素，group(0) 代表的是原始字符串
print(m.groups())

'''
编译：当我们使用正则表达式时，re模块会干两件事
1、编译正则表达式，如果正则表达式本身不合法，会报错
2、用编译后的表达式去匹配对象
compile(pattern, flags=0)
pattern:要编译的正则表达式
'''
#编译成正则表达式
pat = r"^1[345678]\d{9}"
re_telephon = re.compile(pat)
print(re_telephon.match("13901010202"))
"""
re.match()
re.search()
re.findall()
re.finditer()
re.split()
re.sub()
re.subn()
re_telephon.match()   #使用编译后的方法，只传一个string
"""