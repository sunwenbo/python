#__author:  Administrator
#date:  2019/12/22
from types import MethodType

class Person(object,):
    # 这里的属性实际上属于类属性（用类名来调用）
    name = "person" #类属性
    def __init__(self,name,age):
        self.name = name #对象属性
        self.age = age

#类名属性
print(Person.name)
#对象属性
per = Person("tom",20)
per.age = 20
print(per.age)
abc = Person("jeery",18)
#对象属性的优先级高于类属性
print(per.name)
print(abc.name)
#动态的给对象添加对象属性
per.age = 18  #只针对于当前对象生效，对于类创建的其他对象没有作用
per.like = "music"
print(per.age,per.like)
print(Person.name)
#删除对象中的某个属性,再调用会使用到同名的类属性
print(per.name)
del per.name
print(per.name)
#注意：以后千万不要将对象属性与类属性重名，因为对象属性会屏蔽掉类属性。
#但是当删除对象属性后，再使用又能使用类属性了。
