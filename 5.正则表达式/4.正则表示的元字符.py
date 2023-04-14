#__author:  Administrator
#date:  2020/3/15
import re
print("---------匹配单个字符与数字---------")
'''
.       匹配除换行符以外的任意字符
[0123456789]    []是字符集合，表示匹配方括号中所包含的任意一个字符
[sunwenbo]      匹配's''u''n''w''e''n''b''o' 中任意一个字符
[a-z]           匹配任意小写字母
[A-Z]           匹配任意大写字母
[0-9]           匹配任意数字，类似[0123456789]
[0-9a-zA-Z]     匹配任意的数字和字母
[0-9a-zA-Z_]    匹配任意的数字和字母和下划线
[^sunwenbo]     匹配除了sunwenbo这几个字母以外的所有字符，中括号里面的^称为脱字符，表示不匹配集合中的字符
[^0-9]          匹配所有的非数字字符
\d              匹配所有的数字，效果同[0-9]
\D              匹配非数字字符效果同[^0-9]
\w              匹配数字，字母和下划线效果同[0-9a-zA-Z_]
\W              匹配非数字，字母和下划线效果同[^0-9a-zA-Z_]
\s              匹配任意的空白符(空格，换行，回车，换页，制表),效果同[ \f\n\r\t]
\S              匹配任意的非空白符[^ \f\n\r\t]
'''
#匹配任意一个字符，第一个字符
print(re.search(".","sunwenbo is a good man 6"))
print(re.search("[0-9]","sunwenbo is a good man 6"))
print(re.findall("[^sunwenbo]","sunwenbo is a good man 6"))
print(re.findall("\d","sunwenbo is 5 a good man 6"))
print(re.findall("\D","sunwenbo is 5 a good man 6"))
print(re.findall("\w","sunwenbo 孙文波is 5 a good man 6_-"))
print(re.findall("\W","sunwenbo 孙文波is 5 a good man 6_-"))


print("-----------锚字符(边界字符)------------")
'''
^          行首匹配，在和[]里面的^不是一个意思,匹配每一行的行首
$          行尾匹配
\A         匹配字符串开始，它和^的区别是，\A只匹配整个字符串的开头，即使在re.M模式下，也不会匹配其它行的行首
\Z         匹配字符串开始，它和$的区别是，\Z只匹配整个字符串的开头，即使在re.M模式下，也不会匹配其它行的行尾
\b         匹配一个单词的边界，也就是值单词和空格间的位置
           er\b","never,不能匹配nerve
\B         匹配非单词的边界
'''
print(re.search("^sunwenbo","sunwenbo is 5 a good man 6"))
print(re.search("sunwenbo$","sunwenbo is 5 a good man 6"))
print(re.findall("^sunwenbo","sunwenbo is 5 a good man 6\nsunwenbo is nice man",flags=re.M))
print(re.findall("\Asunwenbo","sunwenbo is 5 a good man 6\nsunwenbo is nice man",flags=re.M))
print(re.findall("man$","sunwenbo is 5 a good man\nsunwenbo is nice man",flags=re.M))
print(re.findall("man\Z","sunwenbo is 5 a good man\nsunwenbo is nice man",flags=re.M))
print(re.search(r"er\b","never "))
print(re.search(r"er\b","nerve "))
print(re.search(r"er\B","nerve "))
print(re.search(r"er\B","never "))


print("----------------匹配多个字符---------------")
'''
说明：下方的x,y,z均为假设的普通字符，不是正则表达式的元字符
(xyz)  匹配小括号内的xyz，作为一个整体去匹配
x?     匹配0个或者1个x
x*     匹配0个或者任意多个x（.* 表示匹配0个或者任意多个字符(换行符除外)）
x+     匹配至少一个x
x{n}   匹配确定的n个x（n是一个非负整数）
x{n,}  匹配至少n个x
x{n,m} 匹配至少n个最多m个x。注意：n<=m
x|y    匹配或，匹配的是x或者是y
'''

print(re.findall(r"(sunwenbo)","sunwenbo is a good man,sunwenbois a nice man"))
print(re.findall(r"(a?)","aaabaa"))  #尽可能少的匹配
print(re.findall(r"(a*)","aaabaa"))  #贪婪匹配
print(re.findall(r"(.*)","aaabaa"))  #贪婪匹配
print(re.findall(r"(a+)","aaabaa,aaa m  "))  #贪婪匹配
print(re.findall(r"(a{3})","aaabaaaaa"))
print(re.findall(r"(a{3,})","aaaabaaa"))
print(re.findall(r"(a{4,5})","aaaabaaa"))
print(re.findall(r"((s|S)unwenbo)","sunwenbo---Sunwenbo"))

#需求，提取sunwenbo……man.

str1 = "sunwenbo is a good man! sunwenbo is a nice man!sunwenbo is a very handsome man"

print(re.findall(r"sunwenbo.*?man$",str1))


print("---------------特殊-----------------")
"""
*?    +？  x？最小匹配，通常都是尽可能多的匹配，可以使用非贪婪
(?:x)     类似(xyz),但不表示一个组
"""
#注释： /* part1  */    /*  part2  */
print(re.findall(r"/\*.*?/*/",r"/* part1  */    /*  part2  */"))


pat1 = r".*\d+/(.+?)/.*"
pat = r"\S+/(\w+.+)/"
str0 = 'docker2.yidian.com:5000/publish/'
str1 = 'harbor.int.yidian-inc.com/sre-project/'
str2 = ''.join(re.findall(pat,str0))
print(str2)
