"""
def myPrint():
    print("sunwenbo is a good man")
    print("sunwenbo is a nice man")
    print("sunwenbo is a very good man")
myPrint()

def myprint1(str,age):
    print(str, age)
myprint1("sunwenbo is a good man " , 18)

def mySum(num1, num2):
    return num1 + num2
res = mySum(2, 1)
print(res)

值传递：传递的不可变类型
strint、tuple、number不可变的

引用传递：传递的可变类型
list、dict、set是可变的

def func1(num):
    num = 10
temp = 20           #值传递
func1(temp)
print(temp)

def func2(list):
    list[0] = 100   #引用传递
li = [1,2,3,4,5]
func2(li)
print(li)

c = 20
d = 30
print(id(c),id(d))
c = d
print(id(c),id(d))
print(c,d)

关键字参数：
概念：允许函数调用时参数的顺序与定义时不一致。


def myPrint2(str,age):
    print(str,age)
#使用关键字参数
myPrint2(age = 18,str = "sunwenbo is a good man!")

装饰器
概念：是一个闭包，把一个函数当做参数返回一个替代版的函数，本质上
就是一个返回函数的函数


#简单的装饰器
def func1():
    print("sunwenbo is a good man!")
def outer(abc):
    def inner():
        print("***********************")
        abc()
    return inner

f = outer(func1)
f()

def outer(func):
    def inner(age):
        if age < 0:
            age = 0
        func(age)
    return inner
@outer
def say(age):
    print("sunwenbo is %d year old" % age)
@outer
def say1(age):
    print("sunwenbo is %d year old" % age)
say(-20)
say1(-10)

def outer1(func10):
    def inner1(age1):
        if age1 < 0 :
            age1 = 0
        func10(age1)
    return inner1
@outer1
def say1(age1):
    print("sunwenbo is %d old" % (age1) )
say1(-10)
"""

'''
#通用装饰器
def outer(func):
    def inner(*args,**kwargs):
        print("############")
        func(*args, **kwargs)
    return inner
@outer
def say(name,age,color):   #函数的参数理论上是无限制的，但实际上最好不要超过6,7个。
    print("myname is %s,I am %d years old, I like cacloer is %s" % (name,age,color))

say("sunwenbo",20,"blue")

for i in range(1,10):
    for j in range(i,10):
        print("%d * %d = %d" % (i,j,j*i),end="")
    print("")
    
for i in range(1,10):
    for j in range(1,i + 1):
        print("%d * %d = %d " %(i,j,i * j),end=" ")
    print( )


默认参数
概念：调用函数时，如果没有传递参数，则使用默认参数
以后要用默认参数，最好将默认参数放到最后

def myPrint(str = "sunwenbo is a good man" , age = 18):
    print(str,age)
myPrint()
myPrint("kaige is a good man!",15)

def myPrint(str , age = 18):    #默认参数，只写str，age会使用默认参数
    print(str,age)
myPrint("kaige is a good man!")


不定长参数
概念：能处理比定义时更多的参数
#加了星号（*）的变量存放所有未命名的变量参数，
#如果在函数调用时没有指定参数，她就是一个空元组。
'''
def func(*abc):
    print(type(abc))
    print(abc)
    for x in abc:
        print(x)
func("sunwenbo","is","a","good","man!")

def mySum(*arr):
    sum = 0
    for i in arr:    #计算多个数字的和，不定长参数。
        sum += i
    return sum
print(mySum(1,2,3,4,5,2,))

#**代表键值对的参数字典，和*所代表的意义类似
def func2(**kwargs):
    print(kwargs)
    print(type(kwargs))
func2(x=1,y=2,z=3)          #传关键字参数，变成字典类型

'''

def func3(*args, **kwargs):
    print(*args, **kwargs)
    # pass  #代表一个空语句
    
func3(1, 2, 4, 5, 5)

def mySum(num1, num2):
    return num1 + num2

res = mySum(22121, 13232)
print(type(res))
print(res)

'''

def func1(func):
    #开始创建装饰器
    def func2():
        print("准备执行add函数")
        func()
        print("执行add函数结束")
    return func2

@func1
def add():
    print("add函数正在执行")

