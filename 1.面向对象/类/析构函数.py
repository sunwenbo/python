#__author:  Administrator
#date:  2019/12/8
'''
析构函数：__del__() 释放对象时自动调用
'''
class Person(object):
    def __init__(self, name, age, height, weight):
        #print(name, age, height, weight)
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    def run(self):
        print("run")
    def eat(self, food: object) -> object:
        print("eat " + food)
    def __del__(self):
        print("这里是析构函数")
per = Person("sunwenbo",24,177,60)
#释放对象
print(per.age)
#对象释放后就不能再调用了
del per
# print(per.age)
#再函数里定义的对象，会在函数结束时自动释放，这样可以用来监视内存空间的浪费
def func():
    per2 = Person("zhangsan",24,160,50)
    print(per2.name,per2.age,per2.height,per2.weight)
func()
while True:
    pass