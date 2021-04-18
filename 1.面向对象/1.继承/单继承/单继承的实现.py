#__author:  Administrator
#date:  2019/12/22
from student import Student
from work import Work
# stu = Student("Tom",18,99999,1000)
# print(stu.name,stu.age,stu.stuId)
# stu.setMoney("250")
# print(stu.getMoney())
# #stu.stuFunc()
# stu.run()
# print(stu.getMoney())#通过继承过来的公有方法来调用私有属性
# print(stu.name,stu.age,stu.getMoney)
# stu.setMoney(10100101)
# print(stu.getMoney())

wor = Work("sunwenbo",24,10000,"music")
print(wor.name,wor.age,wor.like)
print(wor.eat(" Apple"))
wor.getMoney()
wor.setMoney(123)
wor.getMoney()
