#__author:  Administrator
#date:  2019/12/22
class Animal(object):
    def __init__(self,name):
        self.name = name
    def eat(self):
        print(self.name + "吃")

