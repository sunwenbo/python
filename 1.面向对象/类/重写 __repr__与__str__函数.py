#__author:  Administrator
#date:  2019/12/8
'''
重写：将函数重新定义写一遍
__str__():在调用print打印对象是自动调用，是给用户用的，是一个描述对象的方法
__repr__()：是给机器用的，在python解释器里面直接敲对象名在回车后调用的方法
注意：在没有str时，且有repr时， str=repr
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
    def __str__(self):
        return "%s-%d-%d-%d" % (self.name,self.age,self.height,self.weight)
    # def __repr__(self):
    #     return "%s-%d-%d-%d" % (self.name,self.age,self.height,self.weight)
per = Person("sunwenbo",24,177,60)
print(per)
#优点：当一个对象的属性值很多，并且都需要打印，重写了__str__方法后，简化了代码