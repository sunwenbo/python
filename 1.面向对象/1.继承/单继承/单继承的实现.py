#__author:  Administrator
#date:  2019/12/22
from student import Student
from work import Work

stu = Student("Tom",18,99999,1000)
print(stu.name,stu.age,stu.stuId)
stu.setMoney("250")
# stu.stuFunc()
print(stu.getMoney())#通过继承过来的公有方法来调用私有属性
print(stu.name,stu.age,stu.getMoney)
stu.setMoney(10100101)
print(stu.getMoney())

wor = Work("sunwenbo",24,10000,"music")
print(wor.name,wor.age,wor.like)
print(wor.eat(" Apple"))
print(wor.getMoney())
wor.setMoney(123)
print(wor.getMoney())

from random import randint

class Die(object):
    def __init__(self,sides):
        self.sides = sides

    def roll_die(self):
        list1 = []
        for i in range(1,6):
            x = randint(1, self.sides)
            list1.append(x)
        return list1
a = Die(100)
print(a.roll_die())

