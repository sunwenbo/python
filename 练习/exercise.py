
# prices = [2,4,1,3,5]
# sum1 = 0
# sum2 = 0
# index = 0
#
# while  index < len(prices):
#     if index == 1 :
#         sum1 = prices[index] - prices[index-1]
#     if index == 3:
#         pass
#     if index == 4:
#         sum2  = prices[index] - prices[index-2]
#     index += 1
#
# print(sum1 + sum2)


def maxProfit(prices):
    if len(prices) <= 1:
        return 0
    min_num = prices[0]
    max_profit = 0
    for  i in prices[1::]:
        min_num = min(i,min_num)
        max_profit = max(max_profit,i - min_num)
    return max_profit

prices = [2,0,1,3,5]
sum = maxProfit(prices)
print(sum)


# str = input("输入一个数字：")
# index = 0
# sum = 0
#
# while index < len(str):
#     if str[index] >= "0" and str[index] <= "9" :
#         sum += int(str[index])
#     index += 1
# print("sum = %d" %(sum))

####################################################################
nums = [1,2,3,5,4,2,6]
print(nums[::-1])
nums.reverse()
print(nums)

####################################################################

list2 = [18, 19, 20, 21, 22]

print()
index = 0
sum = 0
while index < len(list2) :
    sum += list2[index]
    index += 1
    if index == len(list2) :
        print("总年龄：%d" % sum)
        print("平均年龄：%d" % (sum / len(list2)))

####################################################################

sum = 0
num = 1
for i in range(100+1):
    sum += i
    num += 1
print("sum = %d" % (sum))


str = input("请输入一个数字:")
index = 0
sum = 0
while index < len(str):
    if str[index] > "0" and str[index] < "9":
        sum += int(str[index])
        index += 1
    else:
        print("请输入合法的数字～～")
        break
print(sum)
####################################################################

num = 153
a = num % 10
b = num // 10 % 10
c = num // 100
print(a,b,c)

####################################################################
# 输入："abbccd" 输出："ab2c2d"
# 输入："aabcccccffaaa" 输出："a2b1c5f2a3"
'''
import re
str_in="abbccd"
str1=list(str_in)
res=[]
for i in str1:
    patten=re.compile(i)
    res.append(patten.findall(str_in))
print(res)
res1=[]
for i in res:
    if i not in res1:
        res1.append(i)
print(res1)
count0=[]
for i in res1:
    count0.append(str(len(i)))
print(count0)
result=[]
for i in range(len(res1)):
    result.append(res1[i][0])
    result.append(count0[i])
print(result)
print("".join(result))
'''

####################################################################

# h = int(input("请输入高:"))
# w = int(input("请输入宽:"))
# num_h = 1
# while num_h <= h:
#     num_w = 1
#     while num_w <= w:
#         print("#",end="")
#         num_w += 1
#     print()
#     num_h += 1

####################################################################
'''

product_list=[
    ('Mac',9000),
    ('kindle',800),
    ('tesla',900000),
    ('python book',105),
    ('bike',2000),

]
print(product_list)
saving=input('please input your money:')
shopping_car=[]
if saving.isdigit():
    saving=int(saving)
    while True:
        #打印商品内容
        for i,v in enumerate(product_list,1):
            print(i,'>>>>',v)
         #引导用户选择商品
        choice=input('选择购买商品编号[退出：q]：')
        print(choice)
        #验证输入是否合法
        if choice.isdigit():
            choice=int(choice)
            if choice>0 and choice<=len(product_list):
                #将用户选择商品通过choice取出来
                p_item=product_list[choice-1]
                print(type(p_item))
                #如果钱够，用本金saving减去该商品价格，并将该商品加入购物车
                if p_item[1]<saving:
                    saving-=p_item[1]
                    shopping_car.append(p_item)
                else:
                    print('余额不足，还剩%s'%saving)
                print(p_item)
            else:
                print('编码不存在')
        elif choice=='q':
            print('------------您已经购买如下商品----------------')
            #循环遍历购物车里的商品，购物车存放的是已买商品
            for i in shopping_car:
                print(i)
            print('您还剩%s元钱'%saving)
            break
        else:
            print('invalid input')
'''
####################################################################
class heavy(object):
    def countSum(self,list_str,target):
        index_list = []
        for i in range(len(list_str)):
            for j in range(i+1,len(list_str)):
                if list_str[i] + list_str[j] == target:
                    index_list.append(i)
                    index_list.append(j)
                    index_list = list(set(index_list))
        print(index_list)
        return index_list

a = [2, 7, 5, 15]
b = 12
aaa = heavy()
aaa.countSum(a,b)

####################################################################

Str = input("请输入一串字符:")
resoult = {}  # 定义一个空字典
for i in Str:  # 遍历输入的字符串，以键值对的方式存储在字典中
    resoult[i] = Str.count(i)
print(resoult)
for key in resoult:  # 遍历字典，格式化输出结果
    print(f'"{key}":{resoult[key]}次')




