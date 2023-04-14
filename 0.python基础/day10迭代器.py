from collections import Iterable
from collections import Iterator
"""
可迭代对象：可以直接作用于for循环的对象通称为可迭代对象
（Iterable），可以用isinstance()去判断一个对象是否是Iterable

可以直接作用for的数据类型一般分两种
1、集合类数据类型   如：list、tuple、dict、set、string
2、generator   包括生成器和带yield的generator function
"""
print(isinstance([],Iterable))
print(isinstance((),Iterable))
print(isinstance({},Iterable))
print(isinstance("",Iterable))
print(isinstance((x for x in range(10)), Iterator))
#迭代器：不但可以作用于for循环，还可以被next()函数不断的调用
#并返回下一个值，知道最后抛出一个StopIteration错误表示无法
#继续返回下一个值

#可以被next()函数调用并不断返回下一个值的对象称为迭代器 (Iterator对象)
#可以使用isinstance()函数判断一个对象是否是Iterator对象

print(isinstance([],Iterator))
print(isinstance((),Iterator))
print(isinstance({},Iterator))
print(isinstance("",Iterator))
print(isinstance((x for x in range(10)), Iterator))

l = (x for x in range(5))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
#print(next(l))  超出范围就会报错  StopIteration

list = (y for y in [12,212,434,66])
print(next(list))
print(next(list))
print(next(list))
print(next(list))

#转成Iterator对象
a = iter([1,2,3,4,5])
print(next(a))
print(next(a))
print(next(a))
endstr = "end"
str = ""
for line in iter(input, endstr):
    str += line + "\n"
print(str)