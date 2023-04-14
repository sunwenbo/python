#__author:  Administrator
#date:  2020/3/12
#在分布式中最常见
#python 内置了map()  和 reduce()函数
#map   分散到各个储存中
# reduce  将分散出的数据整合并重新计算
from functools import reduce
#map()
#原型   map(fn，lsd)
#参数1是函数
#参数2是序列
#功能：将传入的函数依次作用在序列中的每一个元素，并把结果作为新的Iterator返回

#将单个字符转成对应的字面量整数
def cha2int(chr):
    return {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6}[chr]
    # return chr ** 2
list1 = ["2","1","6","5"]
# list1 = [2,3,1,5]
res = map(cha2int, list1)
print(res)
print(list(res))

#将整数元素的序列，转为字符串类型
l = map(str,[1,2,3,4])
print(list(l))

#reduce(fn.lsd)
#参数1位函数
#参数2位列表
#功能：一个函数作用在序列上，这个函授必须接受两个参数，reduce把结果继续和序列的下个元素累计运算

#reduce(f,[a,b,c,d])
#f(f(f(a,b),c),d)
#求一个序列的和
list2 = [1,2,3,4,5]
def mySum(x,y):
    return x + y

r = reduce(mySum,list2)
print(r)

def str2int(str):
    def fc(x,y):
        return x * 10 + y
    def fs(chr):
        return {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, }[chr]
    return reduce(fc,map(fs,list(str)))
a = str2int("12367")
print(a)
print(type(a))