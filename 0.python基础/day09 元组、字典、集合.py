"""
1。与列表非常相似     元组比较安全  无法修改
2。一旦初始化就不能修改
3。使用小括号
元组：元组的元素不可以替换，修改，但是元组的元素的值如果是可变的就可以修改。
#元组元素的访问
#格式：元组名[]  打印下标
#下标从0开始

tuple4 = (1,2,3,4,5)
print(type(tuple4))
print(tuple4[0])
print(tuple4[1])
print(tuple4[2])
print(tuple4[3])
print(tuple4[0])
#print(tuple4[5])   #下标超过范围（越界）
#获取最后一个元素
print(tuple4[-1])
#修改元组
tuple5 = (1,2,3,4,[5,6,7])
#tuple5[0] = 100 报错，元组不能变
tuple5[-1][0] = 100
tuple5[-1][1] = 200
print(tuple5)
tuple6 = (1,2,3)
del tuple6
#print(tuple6)      #删除一组变量
tuple7 = (1,2,3)
tuple8 = (4,5,6)
#print(tuple7 , tuple8)
t9 = tuple7 + tuple8
print(t9)
#元组重复
t10 = (1,2,3)
print(t10 * 3)
t11 = (1,2,3)
print(4 in t11)   #返回False
#元组的截取
#格式：元组名[开始下标:结束下标]
#从开始下标开始截取，截取到下标之前
t12 = (1,2,3,4,5,6,7,8,9)
print(t12[3:7])
print(t12[3:])
print(t12[:7])
#二维元组：
t13 = ((1,2,3),(4,5,6),(7,8,9))
print(t13[1][1])
#元组的方法
t14 = (1,2,3,4,5)
#len()    返回元组中元素的个数
print(len(t14))
#max()    返回元组中的最大值
print(max((t13)))
#min      返回元组中最小的值

#将列表转为元组
list = [1,2,3]
t15 = tuple(list)
print(type(t15))

#元组的循环
for i in t15 :
    print(i)

#字典


概述：
使用键值（key - value）存储，具有几块的查找速度
注意：字典是无序的

key 的特性
1、字典中的key必须唯一
2、key必须是不可变的对象
3、字符串、整数等都是不可变的，可以作为key
4、list是可变的，不能作为key

思考：保存多为学生的姓名与成绩
使用字典，学生姓名作为key，学生成绩作为值

#元素的访问
#获取：自点名[key]
dict1 = {"tom":60, "lilei":70}
print(dict1["lilei"])
print(dict1.get("sunwenbo"))    #如果有返回对应的值，没有返回None

#添加
dict1["hanmeimei"] = 90
#修改
#因为一个key对应一个value，所以，多次对一个key的value赋值，其实就是修改值。
dict1["lilei"] = 80
print(dict1)
#删除
dict1.pop("tom")
print(dict1)
dict1["tom"] = 60

dict10 = {"limi":10,"zhangsan":20,"lisi":30}
print(dict10["limi"])
dict10["limi"] = 100
print(dict10)
dict10.pop("zhangsan")
print(dict10)
dict10["zhangsan"] = 200
print(dict10["zhangsan"])
#遍历
for key in dict1:
    print(key)
print(dict1)
for value in dict1.values():   # 80   90  60 将字典中的值打印出来
    print(value)
print(dict1.items())
for k, v in dict1.items():
    print(k, v)

print(dict1)
for i, v2 in enumerate(dict1):
    print(i,v2)
#在大多数的程序语言，字典都是无序的
#和list比较
#1、查找和插入的速度极快,不会随着key-value的增加而变慢
#2、list需要占用大量的内存，内存浪费多
#list
#1、查找和插入的速度回随着数据量的增多而减慢
#2、占用空间小，浪费内存少

w  = input("输入关键字:")
d ={} #word:次数
str = "sunwenbo is a good man! sunwenbo is a nice man!" \
      " sunwenbo is a hands man! sunwenbo is a good man!" \
      " sunwenbo is a nice man! sunwenbo is a great man!" \
      " sunwenbo is a noble man! sunwenbo is a cool man!"
l = str.split(" ")
for v in l:
    c = d.get(v)
    if c == None:
        d[v] = 1
    else:
        d[v] += 1
print(d)
print(d[w])
"""
'''
1、以空格切割字符串
2、循环处理列表中的每个元素
3、以元素当key去一个字典中提取数据
4、如果没有提取到，就以元素作为key，1作为value 存进字典
5、如果提取到，将对应的key的value修改，值加1
6、根据输入的字符串当做key再去字典里取值


str1 = "sunwenbo is a good man! sunwenbo is a nice man!" \
      " sunwenbo is a hands man! sunwenbo is a good man!" \
      " sunwenbo is a nice man! sunwenbo is a great man!" \
      " sunwenbo is a noble man! sunwenbo is a cool man!"
w = input("请输入一个关键字:")
l = str1.split(" ")
d = {}
for v in l :
   c = d.get(v)
   if c == None :
       d[v] = 1
   else:
       d[v] += 1
print(d[w])




set:类似dict，是一组key的集合，不存储value
本质：无序和无重复元素的集合
'''

str1 = "sunwenbo is a good man! sunwenbo is a nice man!" \
       " sunwenbo is a hands man! sunwenbo is a good man!" \
       " sunwenbo is a nice man! sunwenbo is a great man!" \
       " sunwenbo is a noble man! sunwenbo is a cool man!"

w = input("请输入关键字：")
d = {}
l = str1.split(" ")
for i in l:
    c = d.get(i)
    if c == None:
        d[i] = 1
    else:
        d[i] += 1
print(d[w])
'''
#创建
#创建set需要一个list或者tuple或者dict作为输入集合
#重复元素在set中自动会被过滤
s1 = set([1,2,3,4,5,2,3,1,5])
print(s1)
s2 = set((1,2,3,4,5,2,3,1,5))
print(s2)
s3 = set({1:"good",2:"nice"})   #只取key  不取value
print(s3)
#添加
s4 = set([1,2,3,4,5])
s4.add(6)
s4.add(3)
s4.add((7,8,9))    #set的元素不能是列表，因为列表是可变的
#s4.add({1:"a"})    #set的元素也不能是字典，字典是可变的
print(s4)
#插入整个list，tuple、字符串、打碎插入
s5 = set([1,2,3,4,5])
s5.update([6,7,8])
s5.update((9,10,11))
s5.update("hello")
print(s5)

#删除
s6 = set([1,2,3,4,5,6])
s6.remove(3)
print(s6)
#遍历
s7 = set([1,2,3,4,5,])
for i in s7:
    print(i)
#set没有索引
for index, data in enumerate(s7):
    print(index,data)
s8 = set([1,2,3])
s9 = set([2,3,4])
#交集
a1 = s8  & s9
print(a1)
print(type(a1))
#并集
a2 = s8 | s9
print(a2)
print(type(a2))

#转换
list1 = [1,2,3,4,1,2,3,4,]
s1 = set(list1)
print(s1)
t2 = (1,2,3,4,4)
s2 =set(t2)
print(s2)
d1 = {1:"good",2:"nice",3:"very"}
s3 = {1,2,3,4}
s3 =list(s3)
print(type(s3))

#set-->tuple
s4 = {1,2,3,4}
t4 = tuple(s4)
print(type(t4))
'''