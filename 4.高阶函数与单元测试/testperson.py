#__author:  Administrator
#date:  2020/3/14

class Person(object):
    def __init__(self,name ,age,**kwargs):
        self.name = name
        self.age = age
        super(Person, self).__init__(**kwargs)
        
    def getAge(self,):
        return self.age + 1