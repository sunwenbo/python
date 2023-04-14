#__author:  Administrator
#date:  2020/2/7
class Person(object):
    def __init__(self,age):
        #属性直接对外暴露
        #self.age = age
        #限制访问
        self.__age = age
    def getAge(self):
        return self.__age
    def setAge(self,age):
        if age < 0:
            age = 0
        self.__age = age
    #方法名为受限制的变量去掉双下划线
    @property
    def age(self):
        return self.__age
    @age.setter #去掉下划线 加   .setter
    def age(self,age):
        if age < 0:
            age = 0
        self.__age = age
per = Person(11)
#属性直接对外暴露，不安全，没有数据的过滤
# print(per.age)
# per.age = -10    #新添加的对象属性，优先访问的是对象属性，
# print(per.age)
#使用限制访问，需要自己写get和set方法才能访问
per.setAge(15)
print(per.getAge())

per.age = 110
print(per.age)
#总结：property:可以让你对受限制访问的属性使用.语法 以及当程序调用方法多的情况下，使用这种方式访问受限制的方法，可减少程序的代码量，以及避免多个调用方法的set get。







