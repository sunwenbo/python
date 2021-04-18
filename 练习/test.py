# '''
# h = int(input("请输入高:"))
# w = int(input("请输入宽:"))
#
# num_h = 1
# while num_h <= h:
#     num_w = 1
#     while num_w <= w:
#         print("#",end="")
#         num_w += 1
#     print()
#     num_h += 1
# '''
#
# class Car():
#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 23
#     def get_descriptive_name(self):
#         long_name = str(self.year) + ' ' + self.make + ' '+ self.model
#         return long_name.title()
#     def read_odmoter(self):
#         print("this car has " + str(self.odometer_reading) + " miles on it.")
#     def update_odometer(self,mileage):
#         self.odometer_reading = mileage
# my_new_car = Car('audi','a4', 2016)
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odmoter()
# my_new_car.update_odometer(44)
# my_new_car.read_odmoter()
#
# class Restaurant():
#     def __init__(self,restaurant_name,cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#     def describe_restaurant(self):
#         a = self.restaurant_name + self.cuisine_type
#         return a
#     def open_restaurant(self):
#         print("正在营业")
# restaurant = Restaurant('sunwenbo',' love')
# print(restaurant.describe_restaurant())
# print(restaurant.open_restaurant())
# #restaurant = Restaurant(123,456)
# #print(restaurant.describe_restaurant())
#
#
# # abc = input("abc:")
# # if abc.isdigit():
# #     abc = int(abc)
# #     print(abc)
# # # else:
# # #     exit("输入错误,请输入数字")
#
#
# product_list=[
#     ('Mac',9000),
#     ('kindle',800),
#     ('tesla',900000),
#     ('python book',105),
#     ('bike',2000),
#
# ]
# print(product_list)
# saving=input('please input your money:')
# shopping_car=[]
# if saving.isdigit():
#     saving=int(saving)
#     while True:
#         #打印商品内容
#         for i,v in enumerate(product_list,1):
#             print(i,'>>>>',v)
#
#          #引导用户选择商品
#         choice=input('选择购买商品编号[退出：q]：')
#         print(choice)
#
#         #验证输入是否合法
#         if choice.isdigit():
#             choice=int(choice)
#             if choice>0 and choice<=len(product_list):
#                 #将用户选择商品通过choice取出来
#                 p_item=product_list[choice-1]
#                 print(type(p_item))
#
#                 #如果钱够，用本金saving减去该商品价格，并将该商品加入购物车
#                 if p_item[1]<saving:
#                     saving-=p_item[1]
#
#                     shopping_car.append(p_item)
#
#                 else:
#                     print('余额不足，还剩%s'%saving)
#                 print(p_item)
#             else:
#                 print('编码不存在')
#         elif choice=='q':
#             print('------------您已经购买如下商品----------------')
#             #循环遍历购物车里的商品，购物车存放的是已买商品
#             for i in shopping_car:
#                 print(i)
#             print('您还剩%s元钱'%saving)
#             break
#         else:
#             print('invalid input')

#
# a = "你好"
# print(a)
# b = a.encode("gbk")
# print(b)
# b = b.decode("gbk")
# print(b)
# c = b.encode("utf-8")
# print(c)
# d = c.decode("utf-8")
# print(d)
#
# f = open('小重山.txt','r',encoding='utf-8')
# print(f.readline().strip())
# print(f.readline().strip())
# print("########################")
# data=f.readlines()#注意及时关闭文件
# f.seek(0)
# print(f.read(3))
# print(f.tell())
# f.seek(6)
# print(f.read(2))
# print(f.tell())
# f.close()
# num = 1
# for i in data:
#     num += 1
#     if num == 3:
#         i = ''.join([i.strip(),'aaaaaa'])
#     print(i.strip())

# import  sys,time
# for i in range(30):
#     sys.stdout.write("*")
#     sys.stdout.flush
#     time.sleep(0.3)

# f_read = open("小重山.txt","r",encoding="utf-8")
# f_wirte = open("小重山2","w",encoding="utf-8")
# number = 0
# for i in f_read:
#     number+=1
#     if number == 5:
#         i = "".join([i.strip(),"hello word\n"])
#     f_wirte.write(i)
# f_read.close()
# f_wirte.close()
# h = int(input("请输入高:"))
# w = int(input("请输入宽:"))
#
# num_h = 1
# while num_h <= h:
#     num_w = 1
#     while num_w <= w:
#         print("#",end="")
#         num_w += 1
#     print()
#     num_h += 1
# count = 10
# def f():
#     global count
#     print(count)
#     count = 11
#     print(count)
# f()
#
# class Danjia():
#     def __init__(self,count):
#         self.Zidancount = count
# class Gun():
#     def __init__(self,GunZidan):
#         self.GunZidan = GunZidan
#     def shoot(self):
#         if self.GunZidan.Zidancount == 0:
#             print("没有子弹了")
#         else:
#             self.GunZidan.Zidancount -= 1
#             print("剩余子弹数量: %d发" % (self.GunZidan.Zidancount))
#             if self.GunZidan.Zidancount == 1:
#                 return  print("请扩充子弹数量，")
# class Person():
#     def __init__(self,gun):
#         self.gun = gun
#     def fire(self):
#         self.gun.shoot()
#     def kuochong(self,count):
#         self.gun.GunZidan.Zidancount = count
#         print("已扩充弹夹子弹%d" % (self.gun.GunZidan.Zidancount))
# danjia = Danjia(2)
# gun = Gun(danjia)
# per = Person(gun)
# per.fire()
# per.fire()
# per.kuochong(4)
# per.fire()
# per.fire()

'''
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


class Solution:
    def lengthOfLongestSubstring(self, s):
        length = len(s)
        if length <= 0:
            return 0
        if length == 1:
            return 1
        head = 0
        max_length = 0
        myHashMap = {}
        for index in range(length):
            if s[index] in myHashMap and head <= myHashMap[s[index]]:
                head = myHashMap[s[index]] + 1
            else:
                max_length = max(max_length, index - head + 1)
            myHashMap[s[index]] = index
        print(max_length)
        return max_length
str1 = Solution()
str1.lengthOfLongestSubstring("bacabc")


class Solution(object):
    def reverse(self, x):
        chars = list(str(x))
        if x < 0 :
            chars.remove('-')
            chars.reverse()
            nums = ''.join(chars)
            nums = -int(nums)
            if not -pow(2, 31) <= nums <= pow(2, 31) - 1:
                r = 0
                print("输入的数值超出范围")
                return 0
            print(nums)
        else:
            chars.reverse()
            nums = ''.join(chars)
            nums = int(nums)
            if not -pow(2, 31) <= nums <= pow(2, 31) - 1:
                r = 0
                print("输入的数值超出范围")
                return 0
            print(nums)
abc = Solution()
abc.reverse(-123)
class Solution:
    def lengthOfLongestSubstring(self, s):
        length = len(s)
        if length <= 0:
            return 0
        if length == 1:
            return 1
        head = 0
        max_length = 0
        myHashMap = {}
        for index in range(length):
            if s[index] in myHashMap and head <= myHashMap[s[index]]:
                head = myHashMap[s[index]] + 1
            else:
                max_length = max(max_length, index - head + 1)
                print(max_length)
            myHashMap[s[index]] = index
        print(max_length)
        return max_length
str1 = Solution()
str1.lengthOfLongestSubstring("bbabc")





class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        chars = list(str(x))
        x = int(x)
        if x < 0:
            return False
        else:
            chars.reverse()
            list_str = ''.join(chars)
            list_str = int(list_str)
            if x == list_str:
                return True
            else:
                return False
test = Solution()
test.isPalindrome(121)

class Solution:
    def isPalindrome(self, x):
        chars = list(str(x))
        if x < 0:
            return False
        else:
            chars.reverse()
            list_str = int(''.join(chars))
            if x == list_str:
                return True
            else:
                return False

test = Solution()
test.isPalindrome(1212)

class Solution(object):
    def longestPalindrome(self, s):
        self.start = 0
        self.max_len = 0
        n = len(s)
        if n < 2:
            return s

        def results(i, j):
            while i >= 0 and j < n and s[i] == s[j]:
                i -= 1
                j += 1

            if self.max_len < j - i - 1:
                # print(i,j)
                self.max_len = j - i - 1
                self.start = i + 1

        for k in range(n):
            results(k, k)
            results(k, k + 1)
            print(s[self.start:self.start + self.max_len ])
        return s[self.start:self.start + self.max_len ]
qqq = Solution()
qqq.longestPalindrome("babad")

class Solution(object):
    def romanToInt(self, s):
        dict1 = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        results = 0
        n = len(s)
        for i in range(len(s)):
            if i < len(s) - 1 and dict1[s[i]] < dict1[s[i+1]]:
                print(dict1[s[i]])
                results -= dict1[s[i]]
            else:
                print(dict1[s[i]])
                results += dict1[s[i]]
        print(results)
        return results

www = Solution()
www.romanToInt("MLDXCII")


class maxSum(object):
    def maxCount(self, list_str, target):
        list_index = []
        for i in range(len(list_str)):
            for j in range(i + 1, len(list_str)):
                if list_str[i] + list_str[j] == target:
                    list_index.append(i)
                    list_index.append(j)
                    list_index = list(set(list_index))
        print(list_index)
        return list_index


bbb = maxSum()
list1 = [2, 1, 4, 5, 9]
target = 14
bbb.maxCount(list1, target)


class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        ss = list(map(set, zip(*strs)))
        print(ss)
        res = ""
        for i, x in enumerate(ss):
            x = list(x)
            if len(x) > 1:
                break
            res = res + x[0]
        return res


aaa = Solution()
list2 = ["flower", "flow", "flight"]
aaa.longestCommonPrefix(list2)


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))

        print(nums)
        return nums


l2 = [0, 1, 1, 2, 4, 5, 4, 3]
zzz = Solution()
zzz.removeDuplicates(l2)

print(0o654)
def read_file():
    # 在windows环境中的编码问题，指定utf-8
    with open('a', 'r', encoding='utf-8') as f:
        word = []  # 空列表用来存储文本中的单词
        # readlins为分行读取文本，且返回的是一个列表，每行的数据作为列表中的一个元素：
        for word_str in f.readlines():  # 如：["In this article, you will learn about Python closures, understand ",...]
            # 因为原文中每个单词都是用空格 或者逗号加空格分开的，去除原文中的逗号
            word_str = word_str.replace(',', '')
            # strip去除每行字符串数据两边的空白字符
            word_str = word_str.strip()
            # 对单行字符串通过空格进行分割，返回一个列表
            word_list = word_str.split(' ')
            # 将分割后的列表内容，添加到word空列表中
            word.extend(word_list)
        return word

def clear_account(lists):
    # 定义空字典，用来存放单词和对应的出现次数
    count_dict = {}
    # count_dict是这种形式{'': None, 'LEARN': None, 'CODING': None, 'FROM': None......}
    count_dict = count_dict.fromkeys(lists)  # 现在的lists是一个没有去重，包含所有单词的列表
    # 取出字典中的key，放到word_list1（去重后的列表中）
    word_list1 = list(count_dict.keys())

    # 然后统计单词出现的次数,并将它存入count_dict字典中
    for i in word_list1:
        # lists为没有去重的那个列表，即包含所有重复单词的列表，使用count得到单词出现次数，作为value
        count_dict[i] = lists.count(i)
    return count_dict


def sort_dict(count_dict):
    # 删除字典中''单词
    del [count_dict['']]
    # 排序,按values进行排序，如果是按key进行排序用sorted(wokey.items(),key=lambda d:d[0],reverse=True)

    # 使用lambda匿名函数用value排序,返回列表[('the', 45), ('function', 38)...这种形式]
    my_dict = sorted(count_dict.items(), key=lambda d: d[1], reverse=True)  # 临时参数d[1]是用value排序
    # 将列表转成字典<class 'dict'>
    my_dict = dict(my_dict)

    return my_dict


def main(my_dict):
    # 输出前10个
    i = 0
    # .items返回一个包含所有（键，值）元祖的列表
    for x, y in my_dict.items():
        if i < 10:
            # print('the word is "', '{}'.format(x), '"', ' and its amount is "', '{}'.format(y), '"')
            print('单词"%s",出现次数为 %s' % (x, y))
            i += 1
            continue
        else:
            break


# 执行函数
main(sort_dict(clear_account(read_file())))
'''
class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance

if __name__ == '__main__':
    # 构建3个实例
    instance1 = Singleton()
    instance2 = Singleton()
    instance3 = Singleton()

    # 打印出实例的内存地址，判断是否是同一个实例
    print(id(instance1))
    print(id(instance2))
    print(id(instance3))

