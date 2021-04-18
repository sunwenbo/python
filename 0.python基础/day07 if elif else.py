

"""
if - elif -else 语句
格式：
if 表达式1：
    语句1
else 表达式2：
    语句2
elif 表达式3：
    语句3

elif 表达式n：
    语句n
else                    #可有可无
    语句
逻辑：当程序执行到if-elif-else语句时，首先计算表达式1的值，如果“表达式1”的值为假，
那么跳过整个if-elif-else语句，如果表达式1的值为真时，执行语句1.执行完语句1，则跳过整个
if-elif-else语句。如果“表达式2”的值为假时，则跳过语句2。表达式2值为真时，执行语句2.
计算表达式3.如果表达式值为真，则执行语句3.跳出整个if-elif-else。如果为假，继续执行下列条件。
直到执行到为真。停止。如果没有为真的值，执行else语句。

# -*- coding: utf-8 -*-
age= int(input("请输入一个年龄："))
if age < 0:
    print("娘胎里")
elif age <= 3:
    print("婴儿")
elif age <=6:
    print("幼儿")
elif age >= 7 and age <= 18:
    print("少年")
elif age >=19 and age <= 40:
    print("成年")
elif age >= 41 and age <= 70:
    print("中年")
elif age >=71 and age <= 100:
    print("老年")
else :
    print("老妖怪")

while  表达式:
    语句1
else:
    语句2
逻辑：在条件语句1为False时，会执行else中的“语句2”。

a = 1
while a <= 3:
    print("sunwenbo is a good man ")
    a += 1
else :
    print("very very good")

for 语句
格式
for  变量名  in  集合：
    语句

逻辑：按顺序取“集合”中的每个元素赋值给“变量”，再去执行语句，
如此循环往复，直到取完“集合”中的元素截止。
for i in [1,2,3,4,5] :
    print(i)

range([start,]end[,step])函数    列表生成器
功能：生出数列

for x in range(10+1) :
    print(x)
for y in range(2,20,3) :   #2为开始值，20结束值，3步长
    print(y)

for index, m in enumerate([1,2,3,4,5]): #index,m = 下标，元素
    print(index,m)

sum = 0
for  n  in  range(1,101):
    sum += n
print(sum)

break语句：
作用：跳出for和while循环
注意：只能跳出距离他最近的那一层循环

for i in range(10):
    print(i)
    if i == 5 :
        break
num = 1
while num <= 10 :
    print(num)
    if num == 3:
        break
    num += 1
#注意：循环语句可以有else语句，break导致循环截止，不会执行else下的语句
else :
    print("sunwenbo is a good man!")
continue 语句
作用：跳出当前循环中的剩余语句，然后继续下一次循环


for i in range(5):
    if i == 3 :
        continue
    print(i)
    #print("*")
    #print("&")

for i in range(1,10):
    for j in range(1,i+1):
         print("%d*%d=%2d" % (i,j,i*j),end=" ")
    print (" ")

"""