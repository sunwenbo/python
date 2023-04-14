#__author:  Administrator
#date:  2020/3/14
#排序：冒泡，选择  快速，插入，计算器

#普通排序
list1 = [2,5,6,1,3,6,8,4]   #默认升序排序
list2 = sorted(list1)
print(list2)

#按绝对值大小排序
list3 = [2,-5,6,1,-3,6,8,-4]
#key 接受函数来实现自定义排序规则
list4 = sorted(list3,key=abs)  #key= 函数
print(list4)

#倒序
list5 = [2,5,6,1,3,6,8,4]
list6 = sorted(list5,reverse=True)
print(list6)

#可以使用自定义函数
def myLen(str):
    return len(str)

list7 = ['a1111','b2222','c3333','aa']
list8 = sorted(list7,key=myLen)
print(list8)