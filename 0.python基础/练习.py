import keyword,math
print(keyword.kwlist)
print(int(1.8))
print(float(1.6))
print(max(1,2,3,4,5,6,7,8,9))
print(min(1,2,3,4,5,6,7,8,9))
print(pow(2,4))
print(round(3.456))
print(round(3.456, 3))
print(math.sqrt(18))
import random
print(random.choice([1,3,5,7,9,"你好"]))

print(random.choice(range(1000))) #          生成1000以内随机数

list = [1,2,3,4,5,6]
random.shuffle(list)			#将列表的数字随机输出
print(list)
print(random.uniform(3,100))
print("############################################################")
# num1 = int(input("请输入一个数字："))
# if num1 % 2 == 0:
#     print("是偶数")
# else:
#     print("是奇数")
num = 153

a = num % 10
b = num // 10 % 10
c = num // 100
print(a,b,c)
a = a ** 3
b = b ** 3
c = c ** 3
print(a,b,c)
num1 = 10
num2 = 20
if num1 and num2:
    print("**********")

if not 0 > 1:
    print("******************")


print(~-10+1)

num1 = "sunwenbo is a very good man!"
num2 = num1.split(" ")
count =0
for i in num2 :
    if len(i) > 0 :
        count += 1
print("一共有%s个单词" % count )


str46 = str.maketrans("sunck",'kaige')
print(str46)
str47="sunwenbo is a good man"
str48 = str47.translate(str46)
print(str48)

index = 0
str = "sunwenbo"
while index < len(str) :
    print("str[%d] = %s" % (index, str[index]))
    index += 1


class Foo(object):
    def __init__(self):
        pass
    def __new__(cls, *args, **kwargs):
        pass
    def _sunwenbo(self):
        pass

obj = Foo()

print(type(obj))
print(type(Foo))

list2 = [18, 19, 20, 21, 22]
index = 0
sum = 0
while index < 5:
    sum += list2[index]
    index += 1
    if index == 5:
        print("平均年龄为",sum / 5)


# listnum = []
# num = 0
# while num < 5 :
#     va1 = int(input())
#     listnum.append(va1)
#     num += 1
# print(listnum)

# num = int(input())
# i = 2
# while num != 1:
#     if num % i == 0:
#         print(i)
#         num //= i
#     else :
#         i += 1
list12 = [1, 2, 3, 4, 5]
list12.append(6)
list12.append([7, 8 ,9])
print(list12[::-1])
print(list12[6][1])
list13 = [1, 2, 3, 4, 5]
list13.extend([6, 7, 8])
print(list13)

print(type(list13))
print(id(list13) )
list14 = [1, 2, 3, 4, 5]
list14.insert(3, 100)
print(len(list14))

for i  in list14:
    print(list14.index(i),i)

list23 = [1, 2, 3, 4, 5, 6, 3, 3, 3, 3,]
num24 = 0
num = 3
print(list23.count(num))
all = list23.count(num)
while num24 < all :
    list23.remove(num)
    num24 += 1
print(list23)

print(list23[::-1])
