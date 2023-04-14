#__author:  Administrator
#date:  2019/12/22
class Person(object):
    def __init__(self,name,age,money):
        self.name = name
        self.age = age
        self.__money = money

    def setMoney(self,money):
        #数据的过滤
        money = int(money)
        if money < 0:
            money = 0
        self.__money = money

    def getMoney(self):
        return self.__money

    def run(self):
        return print("run")

    def eat(self, food):
        return "eat" + food