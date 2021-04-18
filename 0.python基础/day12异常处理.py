
#需求：当程序遇到问题时不让程序结束，而越过错误继续向下执行
"""
def print99():
    for i in range(1,10):
        for j in range(1,i+1):
            print("%d*%d=%d" % (i,j,i*j),end=" ")
        print("")
print99()

try……except……else
格式：
try:
    语句t
except 错误码 as e：
    语句1
except 错误码 as e：
    语句2
except 错误码 as e：
    语句n
else:
    语句e
注意：else语句可有可无
作用：用来检测try语句块中的错误，从而让except语句铺货错误信息并处理
逻辑：当程序执行到try……except……else语句时
1、如果当try语句t出现错误，会匹配第一个错误码，如果匹配上就执行对应的"语句"
2、如果当try“语句t”执行没有错误，没有匹配到错误异常，错误将会被提交到上一层
的try语句，或者到程序的最上层
3、如果当try"语句t"执行没有出现错误，执行else下的"语句e"前提得存在。

num = 1
try:
    print(num)
    #print(3/0)
except ZeroDivisionError as e:
    print("除数不能为0")
except NameError as e :
    print("没有num变量")
else:
    print("代码没有问题")

#使用except而不使用任务错误类型
num = 1
try:
    print(4/0)
    #print(num)
except:
    print("程序出现了异常")

#使用except带着多种异常
try:
    print(5/0)
except(NameError,ZeroDivisionError):
    print("出现了ZeroDivisionError或NameError错误")

#特殊
#1、错误其实clas（类），所有的错误都继承自BasException，所有在
#捕获的时候，它捕获了该类型的错误，还把子类一网打尽
try:
    print(6/0)
except BaseException as e :
    print("异常1")
except ZeroDivisionError as e :
    print("异常2")
#2、跨用多层调用，main调用了func2，func2调用func1，func1出现了错误，
#只要main捕获到错误就可以
def func1(num):
    print(1 / num)
def func2(num):
    func1(num)
def main():
    func2(0)
try:
    main()
except ZeroDivisionError as e :
    print("参数不能为0")
"""
#try……except……finally 语句
"""
try……except……else
格式：
try:
    语句t
except 错误码 as e：
    语句1
except 错误码 as e：
    语句2
except 错误码 as e：
    语句n
finally:
    语句f

作用：语句t无论是否有错误都执行最后的句子
"""
try:
    print(1/0)
except ZeroDivisionError as e :
    print("被除数不能为0")
finally:
    print("**********")

#断言 提前猜测智能提示
def func(num,div):
    assert (div != 0 ), "div不能为0,请注意"
    return num / div
print(func(10,10))