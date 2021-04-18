#__author:  Administrator
#date:  2019/12/22
#创建一个空类
from types import MethodType

class Person(object):
    __slots__ = ("name","age",'speak')  #动态加入属性，属于类属性
per = Person()
#动态添加属性，这体现出了动态语言的特点（灵活）
per.name = "tom"
#动态添加方法
def say(self):
    print("my name is " + self.name)
per.speak = MethodType(say,per)
per.speak()
#思考：如果我们想要限制实例的属性怎么办？
#比如，只允许给对象添加name,age,height,weight
#解决：定义类的时候，定义一个特殊的属性（__slots__）,可以
#动态的添加

#限制添加指定的属性
per.speak = 100
print(per.speak)