"""
一、递归
递归调用：一个函数，调用了自身，陈伟递归调用
递归函数：一个会调用自身的函数称为递归函数


凡是循环能干的事儿，递归都能干

方式：
1、写出临界条件
2、找这一次和上一次的关系
3、假设当前函数已经能用，调用自身计算上一次的结果，再求出本次的结果

#输入一个数（大于等于），求1+2+3+……+n的和

def sum1(n):
    sum = 0
    for x in range(1,n+1):
        sum += x
    return sum

def sum2(n):
    if n == 1:
        return 1
    else:
        return n + sum2(n - 1)
res = sum2(2)
print(res)

#二、模拟栈结构           先进后出
stack = []
#压栈（向栈里存数据）
stack.append("A")
stack.append("B")
stack.append("C")
print(stack)
#出栈（在栈里取数据）
resl = stack.pop()
print("resl=",resl)
print(stack)
res2 = stack.pop()
print("resl=",res2)
print(stack)
res3 = stack.pop()
print("resl=",res3)
print(stack)

#三、队列   （先进先出 ）
import collections
queue = collections.deque()
print(queue)

#进队（存数据）
queue.append("A")
print(queue)
queue.append("B")
print(queue)
queue.append("C")
print(queue)
#出队（取数据）

res1 = queue.popleft()
print("res1="  ,res1)
res2 = queue.popleft()
print("res2="  ,res2)
res3 = queue.popleft()
print("res3="  ,res3)
print(queue)


#三、递归遍历目录
import os

def getAllDir(path,sp = " "):
    #得到当前目录下的所有文件
    fileList = os.listdir(path)
    print(fileList)
    #处理每一个文件
    sp += "   "
    for fileName in fileList:
        #判断是否是路径(要用绝对路径)
        fileAbsPath=os.path.join(path, fileName)
        if os.path.isdir(fileAbsPath):
            print(sp + "目录: ", fileName)
            #递归调用
            getAllDir(fileAbsPath, sp)
        else:
            print(sp + "普通文件: ", fileName)

getAllDir(r"F:\密管系统-发行系统\app\kms-service\deloy")

import os
#栈深度遍历目录
def getALLdirDE(path):
    stack=[]
    stack.append(path)
    print(stack)
    #处理栈，当栈为空的时候结束循环
    while len(stack) !=0:
        #从栈里取出数据(现在指最顶层的目录)
        dirPath = stack.pop()
        #目录下所有的所有文件
        filesList = os.listdir(dirPath)
        #处理每一个目录，如果是普通文件则打印出来，如果是目录则将该目录的地址压栈
        for fileName in filesList:
            fileAbsPath = os.path.join(dirPath,fileName)
            if os.path.isdir(fileAbsPath):
                #是目录就压栈
                print("目录：" + fileName)
                #将是目录的文件添加到stack列表，下次循环
                stack.append(fileAbsPath)
            else:
                #打印普通文件
                print("普通文件：" + fileName)
getALLdirDE(r"F:\密管系统-发行系统\app\kms-crypto-service")
"""
#四、列队广度遍历目录
import os
import collections
# def getAllDirQU(path):
#     queue = collections.deque()
#     #进队
#     queue.append(path)
#     while len(queue) != 0 :
#         #出队数据
#         dirPath = queue.popleft()
#         #找出所有的文件
#         filesList = os.listdir(dirPath)
#         for  fileName in filesList:
#             #绝对路径
#             fileAbsPath = os.path.join(dirPath,fileName)
#             print(fileAbsPath,"****")
#             #判断是否是目录，是目录就进队，不是就打印
#             if os.path.isdir(fileAbsPath):
#                 print("目录：" + fileName)
#                 queue.append(fileAbsPath)
#             else:
#                 print("普通文件" + fileName)
# getAllDirQU(r"F:\密管系统-发行系统\app\kms-crypto-service")

# shoping_list=[('iphone',5000),('mac',9000),('python_book',80),('coffee',35),('bike',2000)]
# gwc = []
# GZ = input("请输入您要存钱的数目:")
# if GZ.isdigit():
#     GZ = int(GZ)
# else:
#     exit("请输入数字！！")
# while True:
#     for i , v in enumerate(shoping_list,1):
#         print(i ,'>>>',v)
#     tx = input("请选序号进行购物,按[q]退出:")
#     if tx.isdigit():
#         tx = int(tx)
#         if tx >= 0 and tx <= len(shoping_list):
#             tx_item = shoping_list[tx-1]
#             if tx_item[1] < GZ:
#                 GZ -= tx_item[1]
#                 gwc.append(tx_item)
#             else:
#                 print("余额不足，请充值")
#         else:
#             print("输入错误")
#     elif tx == 'q':
#         print('------------您已经购买如下商品----------------')
#         for i in gwc:
#             print(i)
#         print("您还剩余%s元钱" % GZ)
#         break
#     else:
#         print('invalid input')

list=[('iphone',5000),('mac',9000),('python_book',80),('coffee',35),('bike',2000)]
GWC = []
GZ = input("请输入您要存钱的数目用于购物:")
if GZ.isdigit():
    GZ = int(GZ)
else:
    exit("错误的输入！")
while True:
    for i, v in enumerate(list, 1):
        print(i, '>>>>', v)
    tx = input("输入您要购买商品的序号按[q]退出:")
    if tx.isdigit():
        tx = int(tx)
        if tx >= 0 and tx <= len(list):
            tx_item = list[tx-1]
            if tx_item[1] < GZ:
                GZ  -= tx_item[1]
                GWC.append(tx_item)
                print("已购买商品",GWC)
            else:
                print("余额不足，还剩%s" % (GZ))
        else:
            print("错误的编码!")
    elif tx == 'q':
        print('------------您已经购买如下商品----------------')
        for i in GWC:
            print(i)
        print("您的余额为%s元钱" % (GZ))
        break
    else:
        print("=========================")











