import keyword,math
print(keyword.kwlist)
print(int(1.8))
print(float(1.6))
print(max(1,2,3,4,5,6,7,8,9))
print(min(1,2,3,4,5,6,7,8,9))
print(pow(2,4))
print(round(3.456))
print(round(3.456, 2))
print(math.sqrt(18))
import random
print(random.choice([1,3,5,7,9,"你好"]))

print(random.choice(range(1000))) #          生成1000以内随机数
print(random.choice("sunwenbo"))
r1 = random.choice(range(10+1))
print(r1)
list = [1,2,3,4,5,6]
random.shuffle(list)			#将列表的数字随机输出
print(list)
print(random.uniform(3,100))
# num1 = int(input("请输入一个数字："))
# if num1 % 2 == 0:
#     print("是偶数")
# else:
#     print("是奇数")
num = 153

a = num % 10
b = num // 10 % 10
c = num // 100
#c = b ** 3
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

str13 = "sunwenbo is a good man!"
str15 = str13[9:18]
print("str15", str15)
str16 = str13[:5]
print(str16)
str17 = str13[19:]
print("str17", str17)

num1 = "sunwenbo is a very good man!"
num2 = num1.split(" ")
count =0
for i in num2 :
    if len(i) > 0 :
        count += 1
print("一共有%s个单词" % count )


num1 = "sunwenbo is a very good man!"
num2 = num1.split(" ")
count1 = 0
for i in num2:
    if len(i) > 0:
        count1 += 1
print("单词数为%d" % (count1))


list41 = ['sunwenbo', 'is', 'a', 'good', 'man!']
str42 = "&^%$#.join(list41)"
print(list41)
str43 = "sunwenbo is a good man z"
print(max(str43))

str46 = str.maketrans("sunck",'kaige')
print(str46)
str47="sunwenbo is a good man"
str48 = str47.translate(str46)
print(str48)

sum = 0
num = 1
while num <= 100 :
    sum += num
    num += 1
print("sum = %d" % (sum))
sum = 0
num = 1

for i in range(100+1):
    sum += i
    num += 1
print(sum)

index = 0
str = "sunwenbo is a good man!"
while index < len(str) :
    print("str[%d] = %s" % (index, str[index]))
    index += 1

list2 = [18, 19, 20, 21, 22]
index = 0
sum = 0

while index < len(list2) :
    print(list2[index])
    sum += list2[index]
    index+= 1
    if index== 5 :
        print("总年龄：%d" % sum)
        print("平均年龄：%d" % (sum / len(list2)))

list2 = [18, 19, 20, 21, 22]

def foo(list):
    list2.append(33)
    return list2

print(foo(list2))


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

nums = [1,2,3,5,4,2,6]
print(nums[::-1])
nums.reverse()
print(nums)

#
# str = input("输入一个数字：")
# index = 0
# sum = 0
# while index < len(str):
#     if str[index] >= "0" and str[index] <= "9" :
#         sum += int(str[index])
#     index += 1
# print("sum = %d" %(sum))
#
# print("mazzzz" > "mazzz")


list2 = [18, 19, 20, 21, 22]
index = 0
sum = 0
while index < 5:
    sum += list2[index]
    index += 1
    if index == 5:
        print("平均年龄为",sum / 5)



list11 = [[1, 2, 3],[4, 5, 6],[7, 8 ,9]]
print(list11[2][2])

list31 = tuple((1, 2, 3, 4, 5))
print(list31)
print(type(list31))


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
list14.insert(2, 100)
print(len(list14))

for i  in list14:
    print(list14.index(i),i)

list23 = [1, 2, 3, 4, 5, 6, 3, 3, 3, 3,]
#print(list23.count(3))
num24 = 0
all = list23.count(3)
while num24 < all :
    list23.remove(3)
    num24 += 1
print(list23)

list23.reverse()
print(list23)