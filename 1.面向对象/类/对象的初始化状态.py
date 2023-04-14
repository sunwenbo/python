#__author:  Administrator
#date:  2019/12/8
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
    def say(self):
        print("Hello! my name is %s,I am %d years old" % (self.name,self.age))
        print(self.__class__)
per1 = Person("sunwenbo",24,177,60)
print(per1.name,per1.age,per1.height,per1.weight)
per2 = Person("zhangsan",24,160,50)
print(per2.name,per2.age,per2.height,per2.weight)
'''
self代表类的实例，而非类
那个对象调用方法，那么该方法中的self就代表那个对象
self.__class__ 代表类名
'''
per3 = Person("Tom",25,100,50)
per3.say()